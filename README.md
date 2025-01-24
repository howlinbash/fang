
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
