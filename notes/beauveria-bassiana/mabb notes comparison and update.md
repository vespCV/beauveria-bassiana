on first run
```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"
```

```
rsync -avun "$VAULT/" "$REPO/"
```

```
rsync -avu "$VAULT/" "$REPO/"
```

```
diff -rq "$REPO" "$VAULT"
```

```
git add notes/
git commit -m "Sync notes from Obsidian vault"
```


push to obsidian
```
REPO="/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana"

rsync -avu "$VAULT/" "$REPO/"
rsync -avu "$REPO/" "$VAULT/"
diff -rq "$REPO" "$VAULT"
```