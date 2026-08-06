Repo edits are under notes/beauveria-bassiana/. Push them to the vault (reverse of the pull in _mabb beauveria bassiana.md):

```
rsync -av --delete \
  "/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana/" \
  "/Users/md/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana/"
```
Warning: --delete removes vault files that are not in the repo copy. Dry-run first:

```
rsync -avn --delete \
  "/Users/md/Developer/beauveria-bassiana/notes/beauveria-bassiana/" \
  "/Users/md/Library/Mobile Documents/iCloud~md~obsidian/Documents/notes/400 computer vision/beauveria-bassiana/"
```
