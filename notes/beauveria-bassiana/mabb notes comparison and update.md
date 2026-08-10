Pull only (Obsidian → repo / Cursor):
```sh
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"
rsync -avun "$VAULT/" "$REPO/"   # dry-run
rsync -avu "$VAULT/" "$REPO/"    # apply
```

Usual full sync (pull first, then push repo edits back):
```sh
rsync -avu "$VAULT/" "$REPO/"
rsync -avu "$REPO/" "$VAULT/"
diff -rq "$REPO" "$VAULT"
```
