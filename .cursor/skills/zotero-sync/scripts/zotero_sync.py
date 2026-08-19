#!/usr/bin/env python3
"""Zotero -> repo sync (read-only against live Zotero DB).

Copies zotero.sqlite (and Better BibTeX citationkey DB) when locked, then:
  - places PDF copies under `pdfs/` (includes) or `pdfs/excluded/` from Zotero storage
  - syncs excluded into input-phase2/excluded/ and strips include CSV
  - writes annotation markdown under temp/zotero-annotations/ when Obsidian notes absent
  - updates temp/overview/literature-overview.md exclusion stubs

Never writes to the live Zotero database or removes files from Zotero storage.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sqlite3
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

EXCLUDED_COLLECTION = "excluded"
LEGACY_EXCLUDED_COLLECTION = "99-excluded"

COLLECTION_TO_PDF_DIR = {
    "00-key-papers": ".",
    "01-existing-products": ".",
    "02-efficacy-mechanics-delivery": ".",
    "02a-efficacy": ".",
    "02b-strains-traits": ".",
    "02c-formulation-delivery": ".",
    "03-autodissemination-social": ".",
    "04-nontarget-ecotox": ".",
    "05-regulatory-policy": ".",
    "06-background-proxies": ".",
    "07-vespideae-biocontrol": ".",
    EXCLUDED_COLLECTION: EXCLUDED_COLLECTION,
}

# Prefer child collections over parent when both present.
COLLECTION_DEPTH = {
    "02-efficacy-mechanics-delivery": 0,
    "02a-efficacy": 1,
    "02b-strains-traits": 1,
    "02c-formulation-delivery": 1,
    "00-key-papers": 1,
    "01-existing-products": 1,
    "03-autodissemination-social": 1,
    "04-nontarget-ecotox": 1,
    "05-regulatory-policy": 1,
    "06-background-proxies": 1,
    "07-vespideae-biocontrol": 1,
    EXCLUDED_COLLECTION: 2,  # exclusion always wins for placement
}

DEFAULT_ZOTERO_DIR = Path.home() / "Zotero"
DEFAULT_BIB_CANDIDATES = [
    Path("temp/zotero/excluded.bib"),
    Path.home() / "Downloads" / "Mijn Bibliotheek.bib",
]


@dataclass
class ZItem:
    item_id: int
    key: str
    title: str = ""
    doi: str = ""
    year: str = ""
    surname: str = ""
    citekey: str = ""
    collections: list[str] = field(default_factory=list)
    pdf_storage_path: Path | None = None
    annotations: list[dict] = field(default_factory=list)


def normalize_doi(doi: str | None) -> str:
    if not doi:
        return ""
    d = doi.strip()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d, flags=re.I)
    return d.lower().rstrip(".")


def normalize_title(title: str) -> str:
    t = unicodedata.normalize("NFKD", title or "")
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def safe_surname(surname: str) -> str:
    s = (surname or "Unknown").strip()
    s = re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)
    return s or "Unknown"


def copy_db(src: Path, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return dest


def open_readonly_copy(src: Path, dest: Path) -> sqlite3.Connection:
    copy_db(src, dest)
    return sqlite3.connect(f"file:{dest}?mode=ro", uri=True)


def field_map(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute("SELECT fieldID, fieldName FROM fields").fetchall()
    return {name: fid for fid, name in rows}


def get_item_value(conn: sqlite3.Connection, item_id: int, field_id: int) -> str:
    row = conn.execute(
        """
        SELECT v.value FROM itemData id
        JOIN itemDataValues v ON v.valueID = id.valueID
        WHERE id.itemID = ? AND id.fieldID = ?
        """,
        (item_id, field_id),
    ).fetchone()
    return row[0] if row else ""


def load_citekeys(bbt_path: Path, dest: Path) -> dict:
    """Return maps keyed by itemID (int) and itemKey (str) -> citationKey."""
    out: dict = {}
    if not bbt_path.exists():
        return out
    try:
        conn = open_readonly_copy(bbt_path, dest)
    except OSError:
        return out
    try:
        rows = conn.execute(
            "SELECT itemID, itemKey, citationKey FROM citationkey"
        ).fetchall()
        for item_id, item_key, ck in rows:
            if not ck:
                continue
            out[int(item_id)] = ck
            if item_key:
                out[str(item_key)] = ck
        return out
    except sqlite3.Error:
        return out
    finally:
        conn.close()


def load_collections(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute("SELECT collectionID, collectionName FROM collections").fetchall()
    wanted = set(COLLECTION_TO_PDF_DIR) | {LEGACY_EXCLUDED_COLLECTION}
    out: dict[str, int] = {}
    for cid, name in rows:
        if name not in wanted:
            continue
        canonical = EXCLUDED_COLLECTION if name == LEGACY_EXCLUDED_COLLECTION else name
        if canonical in COLLECTION_TO_PDF_DIR:
            out[canonical] = cid
    return out


def pick_placement_collection(names: list[str]) -> str | None:
    if not names:
        return None
    if EXCLUDED_COLLECTION in names or LEGACY_EXCLUDED_COLLECTION in names:
        return EXCLUDED_COLLECTION
    ranked = sorted(
        names,
        key=lambda n: (COLLECTION_DEPTH.get(n, 0), n),
        reverse=True,
    )
    return ranked[0]


def parse_bib_dois(bib_path: Path) -> list[dict]:
    text = bib_path.read_text(encoding="utf-8", errors="replace")
    entries: list[dict] = []
    for block in re.split(r"\n(?=@)", text):
        if not block.strip().startswith("@"):
            continue
        mkey = re.match(r"@\w+\{([^,]+)", block)
        citekey = mkey.group(1).strip() if mkey else ""
        doi_m = re.search(r"\bdoi\s*=\s*\{([^}]+)\}", block, re.I)
        title_m = re.search(r"\btitle\s*=\s*\{([^}]+)\}", block, re.I | re.S)
        year_m = re.search(r"\byear\s*=\s*\{?(\d{4})\}?", block, re.I)
        author_m = re.search(r"\bauthor\s*=\s*\{([^}]+)\}", block, re.I | re.S)
        surname = ""
        if author_m:
            first = author_m.group(1).split(" and ")[0].strip()
            if "," in first:
                surname = first.split(",")[0].strip()
            else:
                surname = first.split()[-1]
        entries.append(
            {
                "citekey": citekey,
                "doi": normalize_doi(doi_m.group(1) if doi_m else ""),
                "title": re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else "",
                "year": year_m.group(1) if year_m else "",
                "surname": surname,
            }
        )
    return entries


def bib_is_excluded_only(bib_path: Path, excluded_count: int) -> bool:
    """Reject full-library exports; accept small exports near collection size."""
    entries = parse_bib_dois(bib_path)
    n = len(entries)
    if n == 0:
        return False
    if excluded_count > 0 and n <= max(excluded_count + 5, excluded_count * 2):
        return True
    if n <= 40:
        return True
    return False


def load_zotero_items(
    zotero_dir: Path,
    work_dir: Path,
) -> tuple[dict[int, ZItem], dict[str, list[int]]]:
    zdb = zotero_dir / "zotero.sqlite"
    if not zdb.exists():
        raise FileNotFoundError(f"Missing Zotero DB: {zdb}")

    conn = open_readonly_copy(zdb, work_dir / "zotero.sqlite")
    citekeys = load_citekeys(
        zotero_dir / "better-bibtex.migrated",
        work_dir / "better-bibtex.migrated",
    )
    fields = field_map(conn)
    collections = load_collections(conn)
    items: dict[int, ZItem] = {}
    by_collection: dict[str, list[int]] = defaultdict(list)

    for cname, cid in collections.items():
        rows = conn.execute(
            """
            SELECT i.itemID, i.key
            FROM collectionItems ci
            JOIN items i ON i.itemID = ci.itemID
            WHERE ci.collectionID = ?
              AND i.itemTypeID NOT IN (
                  SELECT itemTypeID FROM itemTypes WHERE typeName IN ('attachment', 'note', 'annotation')
              )
            """,
            (cid,),
        ).fetchall()
        for item_id, key in rows:
            if item_id not in items:
                title = get_item_value(conn, item_id, fields.get("title", -1)) if "title" in fields else ""
                doi = get_item_value(conn, item_id, fields.get("DOI", -1)) if "DOI" in fields else ""
                date_s = get_item_value(conn, item_id, fields.get("date", -1)) if "date" in fields else ""
                year_m = re.search(r"(19|20)\d{2}", date_s or "")
                year = year_m.group(0) if year_m else ""
                crow = conn.execute(
                    """
                    SELECT c.lastName FROM itemCreators ic
                    JOIN creators c ON c.creatorID = ic.creatorID
                    JOIN creatorTypes ct ON ct.creatorTypeID = ic.creatorTypeID
                    WHERE ic.itemID = ?
                      AND ct.creatorType IN ('author', 'artist', 'creator', 'contributor')
                    ORDER BY CASE ct.creatorType WHEN 'author' THEN 0 ELSE 1 END,
                             ic.orderIndex
                    LIMIT 1
                    """,
                    (item_id,),
                ).fetchone()
                if not crow:
                    crow = conn.execute(
                        """
                        SELECT c.lastName FROM itemCreators ic
                        JOIN creators c ON c.creatorID = ic.creatorID
                        WHERE ic.itemID = ?
                        ORDER BY ic.orderIndex LIMIT 1
                        """,
                        (item_id,),
                    ).fetchone()
                surname = crow[0] if crow else ""
                citekey = citekeys.get(item_id) or citekeys.get(key) or ""
                if not citekey and surname and year:
                    citekey = f"{safe_surname(surname).lower()}{year}"
                items[item_id] = ZItem(
                    item_id=item_id,
                    key=key,
                    title=title,
                    doi=normalize_doi(doi),
                    year=year,
                    surname=surname,
                    citekey=citekey,
                )
            items[item_id].collections.append(cname)
            by_collection[cname].append(item_id)

    # PDF attachments
    for item in items.values():
        row = conn.execute(
            """
            SELECT att.key, ia.path
            FROM itemAttachments ia
            JOIN items att ON att.itemID = ia.itemID
            WHERE ia.parentItemID = ?
              AND ia.contentType LIKE '%pdf%'
            ORDER BY ia.itemID
            LIMIT 1
            """,
            (item.item_id,),
        ).fetchone()
        if not row:
            continue
        att_key, path = row
        storage_dir = zotero_dir / "storage" / att_key
        pdf = None
        if path and path.startswith("storage:"):
            candidate = storage_dir / path[len("storage:") :]
            if candidate.exists():
                pdf = candidate
        if pdf is None and storage_dir.is_dir():
            pdfs = sorted(storage_dir.glob("*.pdf"))
            if pdfs:
                pdf = pdfs[0]
        item.pdf_storage_path = pdf
        if pdf is not None and not item.year:
            ym = re.search(r"(19|20)\d{2}", pdf.name)
            if ym:
                item.year = ym.group(0)
                if not item.citekey and item.surname:
                    item.citekey = f"{safe_surname(item.surname).lower()}{item.year}"

    # Annotations (type 1 highlight text; include comments)
    for item in items.values():
        ann_rows = conn.execute(
            """
            SELECT a.type, a.text, a.comment, a.pageLabel, a.color, ann.key
            FROM itemAnnotations a
            JOIN items ann ON ann.itemID = a.itemID
            WHERE a.parentItemID IN (
                SELECT ia.itemID FROM itemAttachments ia WHERE ia.parentItemID = ?
            )
            ORDER BY a.sortIndex
            """,
            (item.item_id,),
        ).fetchall()
        for typ, text, comment, page, color, ann_key in ann_rows:
            item.annotations.append(
                {
                    "type": typ,
                    "text": (text or "").strip(),
                    "comment": (comment or "").strip(),
                    "page": page or "",
                    "color": color or "",
                    "key": ann_key,
                }
            )

    conn.close()
    return items, by_collection


def load_include_csv(path: Path) -> tuple[list[dict], list[str]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    return rows, fieldnames


def match_include_row(rows: list[dict], item: ZItem) -> dict | None:
    doi = item.doi
    if doi:
        for r in rows:
            if normalize_doi(r.get("doi", "")) == doi:
                return r
    nt = normalize_title(item.title)
    if not nt:
        return None
    for r in rows:
        if normalize_title(r.get("title", "")) == nt:
            if not item.year or str(r.get("publication_year", "")) == item.year:
                return r
    return None


def pdf_dest_name(item: ZItem) -> str:
    return f"{safe_surname(item.surname)}_{item.year or '0000'}.pdf"


def ensure_unique_dest(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    for i in range(1, 26):
        letter = chr(ord("a") + i)
        cand = dest.with_name(f"{stem}-{letter}{suffix}")
        if not cand.exists():
            return cand
    return dest.with_name(f"{stem}-dup{suffix}")


def find_existing_pdf(pdfs_root: Path, item: ZItem) -> Path | None:
    """Find an already-filed repo PDF by surname+year naming variants."""
    surname = safe_surname(item.surname)
    year = item.year or ""
    if not surname or not year:
        return None
    name = pdf_dest_name(item)
    sn_lower = surname.lower()
    hits: list[Path] = []
    for p in pdfs_root.rglob("*.pdf"):
        stem = p.stem
        low = stem.lower()
        if p.name == name:
            return p
        if low.startswith(f"{sn_lower}_{year}") or low.startswith(f"{sn_lower}-{year}"):
            hits.append(p)
            continue
        if low.startswith(f"{sn_lower}-{year}-") or low.startswith(f"{sn_lower}_{year}_"):
            hits.append(p)
            continue
        if year in stem and sn_lower in low.replace(" ", ""):
            hits.append(p)
    if not hits:
        return None
    for h in hits:
        if h.name == name:
            return h
    return hits[0]


def write_annotation_md(path: Path, item: ZItem) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"## {item.title or item.citekey or item.key}",
        "",
        f"- citekey: {item.citekey or ''}",
        f"- doi: {item.doi or ''}",
        f"- year: {item.year or ''}",
        f"- collections: {', '.join(item.collections)}",
        f"- evidence: zotero-annotation",
        "",
        "### Annotations",
        "",
    ]
    for a in item.annotations:
        if not a["text"] and not a["comment"]:
            continue
        page = a["page"] or "?"
        lines.append(f"- p.{page}: {a['text']}")
        if a["comment"]:
            lines.append(f"  - note: {a['comment']}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def update_overview_exclusions(
    overview_path: Path,
    excluded_items: list[ZItem],
    apply: bool,
) -> None:
    overview_path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"# Literature overview draft\n\n"
        f"_Generated/updated by zotero_sync on {date.today().isoformat()}. "
        f"User promotes keepers to README.md._\n\n"
    )
    section = ["## Screened out (excluded)\n"]
    for item in excluded_items:
        label = item.citekey or f"{item.surname}{item.year}"
        doi = f" ({item.doi})" if item.doi else ""
        section.append(f"- screened-out: {label}{doi} — {item.title[:120]}")
    section.append("")
    body = "\n".join(section)

    if overview_path.exists():
        text = overview_path.read_text(encoding="utf-8")
        if re.search(r"## Screened out \((?:99-)?excluded\)", text):
            text = re.sub(
                r"## Screened out \((?:99-)?excluded\).*?(?=\n## |\Z)",
                body,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.rstrip() + "\n\n" + body
    else:
        text = header + body

    if apply:
        overview_path.write_text(text, encoding="utf-8")


def sync(
    repo: Path,
    zotero_dir: Path,
    apply: bool,
    bib_path: Path | None,
) -> int:
    work_dir = repo / "temp" / "zotero"
    work_dir.mkdir(parents=True, exist_ok=True)

    items, by_collection = load_zotero_items(zotero_dir, work_dir)
    excluded_ids = list(dict.fromkeys(by_collection.get(EXCLUDED_COLLECTION, [])))
    excluded_items = [items[i] for i in excluded_ids]

    # Exclusion source preference
    excl_source = f"sqlite:{EXCLUDED_COLLECTION}"
    bib_entries: list[dict] = []
    candidates = []
    if bib_path:
        candidates.append(bib_path)
    candidates.extend([(repo / p if not p.is_absolute() else p) for p in DEFAULT_BIB_CANDIDATES])
    seen = set()
    for cand in candidates:
        cand = cand.resolve() if cand.exists() else cand
        key = str(cand)
        if key in seen:
            continue
        seen.add(key)
        if not cand.exists():
            continue
        if bib_is_excluded_only(cand, len(excluded_items)):
            bib_entries = parse_bib_dois(cand)
            excl_source = f"bib:{cand}"
            break
        else:
            print(f"note: ignoring full-library or oversized bib at {cand}")

    include_csv = repo / "input-phase2" / "relevant_articles_categorized.csv"
    include_rows, fieldnames = load_include_csv(include_csv) if include_csv.exists() else ([], [])
    notes_zotero = repo / "notes" / "beauveria-bassiana" / "zotero"
    pdfs_root = repo / "pdfs"
    excl_dir = repo / "input-phase2" / EXCLUDED_COLLECTION
    excl_dir.mkdir(parents=True, exist_ok=True)
    (pdfs_root / EXCLUDED_COLLECTION).mkdir(parents=True, exist_ok=True)
    ann_dir = repo / "temp" / "zotero-annotations"
    ann_dir.mkdir(parents=True, exist_ok=True)

    report = {
        "excl_source": excl_source,
        "moved": [],
        "copied": [],
        "conflicts": [],
        "excluded_synced": [],
        "annotations_written": [],
        "annotations_reused": [],
        "missing_pdf": [],
        "multi_collection": [],
    }

    # --- Placement pass ---
    for item in items.values():
        placement = pick_placement_collection(item.collections)
        if not placement:
            continue
        if len(set(item.collections)) > 1:
            report["multi_collection"].append(
                {
                    "citekey": item.citekey,
                    "collections": item.collections,
                    "placement": placement,
                }
            )
        rel = COLLECTION_TO_PDF_DIR[placement]
        dest_dir = pdfs_root / rel
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_name = pdf_dest_name(item)
        dest = dest_dir / dest_name

        # Conflict: CSV primary vs Zotero placement (non-excluded)
        matched = match_include_row(include_rows, item) if include_rows else None
        if matched and placement != EXCLUDED_COLLECTION:
            csv_cat = matched.get("screening_category", "")
            # Map CSV ids (underscores) to collection-ish names for compare
            csv_norm = csv_cat.replace("_", "-")
            place_norm = placement.replace("_", "-")
            if csv_norm and csv_norm not in place_norm and place_norm not in csv_norm:
                # 02a special: csv 02a_efficacy vs 02a-efficacy
                if not (
                    csv_cat.startswith("02")
                    and placement.startswith("02")
                ):
                    report["conflicts"].append(
                        {
                            "citekey": item.citekey,
                            "doi": item.doi,
                            "csv_category": csv_cat,
                            "zotero_placement": placement,
                            "action": "pdf_follows_zotero",
                        }
                    )

        existing = find_existing_pdf(pdfs_root, item)
        if existing and existing.parent.resolve() == dest_dir.resolve():
            # Already in the correct category folder (any naming scheme).
            pass
        elif existing and existing.resolve() != dest.resolve():
            final = (
                ensure_unique_dest(dest)
                if dest.exists() and dest.resolve() != existing.resolve()
                else dest
            )
            report["moved"].append(
                f"{existing.relative_to(repo)} -> {final.relative_to(repo)}"
            )
            if apply:
                final.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(existing), str(final))
        elif item.pdf_storage_path and item.pdf_storage_path.exists():
            if not dest.exists():
                report["copied"].append(
                    f"{item.pdf_storage_path.name} -> {dest.relative_to(repo)}"
                )
                if apply:
                    shutil.copy2(item.pdf_storage_path, dest)
        elif not existing:
            report["missing_pdf"].append(item.citekey or item.title[:60])

    # --- Exclusion pass ---
    excl_records: list[dict] = []
    if bib_entries and excl_source.startswith("bib:"):
        for e in bib_entries:
            excl_records.append(
                {
                    "citekey": e["citekey"],
                    "doi": e["doi"],
                    "title": e["title"],
                    "year": e["year"],
                    "surname": e["surname"],
                    "source": excl_source,
                }
            )
        # Build pseudo items for overview from bib when not in sqlite list
        # Prefer sqlite items when DOI matches
        by_doi = {i.doi: i for i in excluded_items if i.doi}
        overview_items = []
        for e in bib_entries:
            if e["doi"] and e["doi"] in by_doi:
                overview_items.append(by_doi[e["doi"]])
            else:
                overview_items.append(
                    ZItem(
                        item_id=0,
                        key="",
                        title=e["title"],
                        doi=e["doi"],
                        year=e["year"],
                        surname=e["surname"],
                        citekey=e["citekey"],
                        collections=[EXCLUDED_COLLECTION],
                    )
                )
        excluded_items = overview_items
    else:
        for item in excluded_items:
            excl_records.append(
                {
                    "citekey": item.citekey,
                    "doi": item.doi,
                    "title": item.title,
                    "year": item.year,
                    "surname": item.surname,
                    "source": excl_source,
                }
            )

    excl_csv = excl_dir / "records.csv"
    excl_fields = ["citekey", "doi", "title", "year", "surname", "source"]
    if apply:
        with excl_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=excl_fields)
            w.writeheader()
            for r in excl_records:
                w.writerow(r)

    # Remove excluded from include CSV
    remove_dois = {normalize_doi(r["doi"]) for r in excl_records if r.get("doi")}
    remove_titles = {normalize_title(r["title"]) for r in excl_records if r.get("title")}
    kept = []
    removed = []
    for row in include_rows:
        doi = normalize_doi(row.get("doi", ""))
        title_n = normalize_title(row.get("title", ""))
        if (doi and doi in remove_dois) or (title_n and title_n in remove_titles):
            removed.append(row)
            report["excluded_synced"].append(row.get("title", "")[:80])
        else:
            kept.append(row)

    if apply and include_csv.exists() and removed:
        with include_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(kept)

    # --- Annotation pass ---
    for item in items.values():
        if not item.annotations:
            continue
        cite = item.citekey or f"item{item.item_id}"
        # Prefer Obsidian note (do not overwrite)
        note_hits = []
        if notes_zotero.is_dir():
            cite_l = (item.citekey or "").lower()
            sn_l = safe_surname(item.surname).lower()
            for p in notes_zotero.glob("*.md"):
                stem_l = p.stem.lower().replace(" ", "")
                if cite_l and (cite_l == stem_l or cite_l in stem_l or stem_l in cite_l):
                    note_hits.append(p)
                elif sn_l and item.year and sn_l in stem_l and item.year in p.stem:
                    note_hits.append(p)
        if note_hits:
            report["annotations_reused"].append(str(note_hits[0].relative_to(repo)))
            continue
        out = ann_dir / f"{cite}.md"
        report["annotations_written"].append(str(out.relative_to(repo)))
        if apply:
            write_annotation_md(out, item)

    # --- Overview touch ---
    overview = repo / "temp" / "overview" / "literature-overview.md"
    update_overview_exclusions(overview, excluded_items, apply=apply)
    if apply:
        print(f"updated {overview.relative_to(repo)}")

    # Report JSON + human summary
    summary = {
        **report,
        "n_items_in_collections": len(items),
        "n_excluded": len(excl_records),
        "n_include_removed": len(removed),
        "n_include_remaining": len(kept) if include_rows else None,
        "apply": apply,
    }
    out_json = work_dir / "last-sync-report.json"
    if apply or True:
        out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"excl_source={excl_source}")
    print(f"items_in_collections={len(items)} excluded={len(excl_records)}")
    print(f"copied={len(report['copied'])} moved={len(report['moved'])} missing_pdf={len(report['missing_pdf'])}")
    print(f"conflicts={len(report['conflicts'])} multi_collection={len(report['multi_collection'])}")
    print(f"include_removed={len(removed)} annotations_written={len(report['annotations_written'])} reused={len(report['annotations_reused'])}")
    print(f"report={out_json}")
    if not apply:
        print("dry-run only; re-run with --apply to write changes")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--repo",
        type=Path,
        default=Path(__file__).resolve().parents[4],
        help="Repository root",
    )
    p.add_argument(
        "--zotero-dir",
        type=Path,
        default=DEFAULT_ZOTERO_DIR,
        help="Zotero data directory",
    )
    p.add_argument(
        "--bib",
        type=Path,
        default=None,
        help="Optional excluded-collection-only BibTeX path",
    )
    p.add_argument(
        "--apply",
        action="store_true",
        help="Write PDF copies/moves, CSVs, annotation files, overview",
    )
    args = p.parse_args(argv)
    repo = args.repo.resolve()
    return sync(repo, args.zotero_dir.resolve(), apply=args.apply, bib_path=args.bib)


if __name__ == "__main__":
    sys.exit(main())
