
stores definitive pacman lists for
- base
- server
- worker
- leafs
Can diff HEAD against tree (what is tracked verse what is currently installed)
- because currentlyInstalled is dynamic don't cache it anywhere. just use pacman
    command when the info is needed
If I decide i like a package and always want to be installed with config, i can
save it. Wherever I decide to put it (base/server/worker/leaf) pac will make the
commit to the correct branch and merge update all the other branches so all the
upstreams that need it, get it and we leave the command on the branch we started
on
It is from this repo that config gets it's package download list.
It lives @ mnt/share/src/pac
it is symlinked to each machine on install
it needs to pull the correct branches before any commits

The correct command is pacman -Qqtt

The take inventory command needs to take top level packages into account

store pkglist in .notes so backups can recreate packages installed
- later handle this with pac
- rl: could spit out diff of untracked packages

use the /mnt/shared/src/dotfiles repo to commit changes from a local fs.
- add a file on bass

howl
drop
bud
todo

- main
  - server
    - the
  - worker
    - howlin
    - bass

## main

## server

## the
.local/share/ranger/bookmarks
.local/bin/pac 

## worker
.local/share/ranger/bookmarks
.local/bin/songs-loc.csv
.local/bin/howl 
.local/bin/drop 
.local/bin/bud 
.local/bin/pac 

## howlin
.config/terminator/config
.local/config/gtk-3.0/bookmarks
.local/share/ranger/bookmarks
.local/bin/todo 

## bass
.local/config/gtk-3.0/bookmarks
.local/share/ranger/bookmarks
.local/bin/todo 

## next
track firefox bookmars
