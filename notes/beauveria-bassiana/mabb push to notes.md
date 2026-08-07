
```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"
```

Bidirectional sync uses **two passes**. `-u` skips a file when the destination is already newer, so one direction alone leaves the other side's edits behind.

**Typical flow:** pull Obsidian edits into the repo, then push repo edits to Obsidian. Run both every sync.

## Check

```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"

diff -rq "$REPO" "$VAULT"
```

Expected leftover: `Only in $REPO: mabb push to notes.md` (repo-only helper; not in the vault).

## 1. Pull (Obsidian → repo)

Vault wins when the vault file is newer.

Dry-run:

```
rsync -avun "$VAULT/" "$REPO/"
```

Apply:

```
rsync -avu "$VAULT/" "$REPO/"
```

## 2. Push (repo → Obsidian)

Repo wins when the repo file is newer.

Dry-run:

```
rsync -avun "$REPO/" "$VAULT/"
```

Apply:

```
rsync -avu "$REPO/" "$VAULT/"
```

## Full sync (copy-paste)

```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"

rsync -avu "$VAULT/" "$REPO/"
rsync -avu "$REPO/" "$VAULT/"
diff -rq "$REPO" "$VAULT"
```

Do **not** use `--delete` unless you intend to remove files from the destination.
