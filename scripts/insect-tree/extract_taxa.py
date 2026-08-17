#!/usr/bin/env python3
"""Match curated insect taxa against Zotero notes and render an ASCII tree.

Usage (from repo root):
  python3 scripts/insect-tree/extract_taxa.py

Edit taxonomy.json to add taxa, then re-run. Output:
  temp/overview/insect-tree.md
  temp/overview/insect-tree.json
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TAXONOMY_PATH = Path(__file__).with_name("taxonomy.json")
OUT_DIR = ROOT / "temp" / "overview"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)


def citekey_from_note(path: Path) -> str:
    stem = path.stem
    if stem.endswith(" 2"):
        stem = stem[:-2]
    return stem


def doi_from_text(text: str) -> str | None:
    m = DOI_RE.search(text[:5000])
    if not m:
        return None
    return m.group(0).rstrip(").,").lower()


def title_key(text: str) -> str | None:
    for line in text.splitlines()[:20]:
        line = line.strip()
        if not line.startswith("#"):
            continue
        line = re.sub(r"^#+\s*", "", line)
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"[_*]", "", line)
        line = re.sub(r"\s+", " ", line).strip().lower()
        return line[:90] or None
    return None


def is_excluded(text: str) -> bool:
    head = text[:1500]
    return bool(re.search(r"collections:\s*.*99-excluded", head, re.I))


def pub_id(path: Path, text: str) -> str:
    doi = doi_from_text(text)
    if doi:
        return f"doi:{doi}"
    title = title_key(text)
    if title:
        return f"title:{title}"
    return f"file:{citekey_from_note(path).lower()}"


def compile_patterns(patterns: list[str]) -> list[re.Pattern[str]]:
    compiled = []
    for raw in patterns:
        compiled.append(re.compile(r"(?<![A-Za-z])" + re.escape(raw) + r"(?![A-Za-z])"))
    return compiled


def collect_taxa(node: dict, acc: list[dict]) -> None:
    if node.get("kind") == "taxon":
        acc.append(node)
    for child in node.get("children") or []:
        collect_taxa(child, acc)


def node_has_hits(node: dict, hits: dict[str, list[str]]) -> bool:
    if node.get("kind") == "taxon":
        return bool(hits.get(node["id"]))
    return any(node_has_hits(child, hits) for child in node.get("children") or [])


def note_dirs(spec: dict) -> list[Path]:
    dirs = [ROOT / spec["notes_dir"]]
    for extra in spec.get("extra_notes_dirs") or []:
        path = ROOT / extra
        if path.is_dir():
            dirs.append(path)
    return dirs


def scan_notes(dirs: list[Path], taxa: list[dict]) -> tuple[dict[str, list[str]], int]:
    compiled = {
        taxon["id"]: compile_patterns(taxon["patterns"]) for taxon in taxa
    }
    hits: dict[str, set[str]] = defaultdict(set)
    canonical: dict[str, str] = {}
    n_files = 0
    for notes_dir in dirs:
        for path in sorted(p for p in notes_dir.glob("*.md") if p.is_file()):
            n_files += 1
            text = path.read_text(encoding="utf-8", errors="replace")
            if is_excluded(text):
                continue
            key = citekey_from_note(path)
            pid = pub_id(path, text)
            if pid in canonical:
                key = canonical[pid]
            else:
                canonical[pid] = key
            for taxon_id, patterns in compiled.items():
                if any(p.search(text) for p in patterns):
                    hits[taxon_id].add(key)
    return {k: sorted(v) for k, v in hits.items()}, n_files


def render_tree(node: dict, hits: dict[str, list[str]], prefix: str = "", is_last: bool = True, is_root: bool = True) -> list[str]:
    lines: list[str] = []
    if not node_has_hits(node, hits) and not is_root:
        return lines

    if is_root:
        connector = ""
        child_prefix = ""
        label_prefix = ""
    else:
        connector = "└── " if is_last else "├── "
        child_prefix = prefix + ("    " if is_last else "│   ")
        label_prefix = prefix

    if node.get("kind") == "taxon":
        n = len(hits.get(node["id"], []))
        common = node.get("common") or ""
        extra = f"  {common}" if common else ""
        lines.append(f"{label_prefix}{connector}{node['scientific']} ({n}){extra}")
        return lines

    label = node["label"]
    if is_root:
        lines.append(f"── {label}")
    else:
        lines.append(f"{label_prefix}{connector}{label}")

    visible = [c for c in (node.get("children") or []) if node_has_hits(c, hits)]
    for i, child in enumerate(visible):
        last = i == len(visible) - 1
        if is_root:
            child_is_last = last
            # Root children hang from a blank stem.
            stem = "   "
            lines.extend(render_tree(child, hits, stem, child_is_last, is_root=False))
        else:
            lines.extend(render_tree(child, hits, child_prefix, last, is_root=False))
    return lines


def count_by_role(taxa: list[dict], hits: dict[str, list[str]]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for taxon in taxa:
        if hits.get(taxon["id"]):
            counts[taxon["role"]] += 1
    return dict(counts)


def write_markdown(tree_lines: list[str], taxa: list[dict], hits: dict[str, list[str]], n_notes: int) -> str:
    present = [t for t in taxa if hits.get(t["id"])]
    missing = [t for t in taxa if not hits.get(t["id"])]
    roles = count_by_role(taxa, hits)
    today = date.today().isoformat()
    rows = []
    for taxon in sorted(present, key=lambda t: (-len(hits[t["id"]]), t["scientific"])):
        notes = ", ".join(hits[taxon["id"]])
        rows.append(
            f"| {taxon['scientific']} ({len(hits[taxon['id']])}) | {taxon.get('common', '')} | {taxon['role']} | {notes} |"
        )
    missing_lines = "\n".join(f"- {t['scientific']}" for t in missing) or "_none_"
    return f"""# Insect taxa in notes (PDF-backed)

Generated {today} by `scripts/insect-tree/extract_taxa.py` from `notes/beauveria-bassiana/zotero/` and `temp/zotero-annotations/` (DOI/title-deduped; `99-excluded` skipped).
Curated map: `scripts/insect-tree/taxonomy.json`. Re-run the script after editing the map.

Notes scanned: {n_notes}. Taxa with at least one note: {len(present)} of {len(taxa)}.

Role counts: motivation {roles.get('motivation', 0)}; vespidae {roles.get('vespidae', 0)}; nontarget {roles.get('nontarget', 0)}; social_proxy {roles.get('social_proxy', 0)}; distant_proxy {roles.get('distant_proxy', 0)}.

Spray or contact results on distant proxies do not stand in for _Vespa velutina_.

```
{chr(10).join(tree_lines)}
```

## Taxa with notes

| Taxon | Common name | Role | Citekeys |
|---|---|---|---|
{chr(10).join(rows)}

## In the map, not found in notes this run

{missing_lines}
"""


def main() -> None:
    spec = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))
    dirs = note_dirs(spec)
    tree = spec["tree"]
    taxa: list[dict] = []
    collect_taxa(tree, taxa)

    hits, n_notes = scan_notes(dirs, taxa)
    tree_lines = render_tree(tree, hits)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    snapshot = {
        "generated": date.today().isoformat(),
        "notes_scanned": n_notes,
        "taxa_in_map": len(taxa),
        "taxa_with_notes": sum(1 for t in taxa if hits.get(t["id"])),
        "role_counts": count_by_role(taxa, hits),
        "tree_ascii": "\n".join(tree_lines),
        "hits": {
            t["id"]: {
                "scientific": t["scientific"],
                "common": t.get("common", ""),
                "role": t["role"],
                "notes": hits.get(t["id"], []),
            }
            for t in taxa
        },
    }
    (OUT_DIR / "insect-tree.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "insect-tree.md").write_text(
        write_markdown(tree_lines, taxa, hits, n_notes), encoding="utf-8"
    )
    print("\n".join(tree_lines))
    print()
    print(f"Wrote {OUT_DIR / 'insect-tree.md'}")
    print(f"Wrote {OUT_DIR / 'insect-tree.json'}")


if __name__ == "__main__":
    main()
