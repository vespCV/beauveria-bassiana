
```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"
```


check
```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"

diff -rq "$REPO" "$VAULT"
```

Pull Obsidian edits into repo (vault wins when newer):
```
rsync -avun \
  "$VAULT/" \
  "$REPO/"
```

Push repo edits to Obsidian (repo wins when newer):
```
rsync -avun \
  "$REPO/" \
  "$VAULT/"
```
