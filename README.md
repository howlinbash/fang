

Fang
====

Fang maintains the seaworthiness of the individuals in the Howlin Fleet. He tracks the packages installed and manages the dotfiles of each vessel and the fleet at large. 

Don't be put off by his cranky ways; He's a good lad and a he does a fine job.


## Usage

Fleet branches are managed from an unconnected dotfiles repo. The updates are
then pulled from each respective host as and when they want the latest updates.

Updates are generally not commited from the individual hosts, rather they are commited
from the unconnect dotfiles repo at the appropriate location in the tree.

If they *are* committed from the individual host, that change must only be relevant
to that host and it must be pushed to remote immediately.


### Initialising

New unconnected dotfile repos are initialised with 

    fang -i

This checksout each branch locally and tracks it with origin so it is ready to
accept any changes to come.


### Default

By default 

    fang

will pull any recent changes from remote and then add all unignored files to
staging and commit them. He will then checkout all downstream branches merge the
commit and push the updated branch to origin. Before this command 


### Selective commiting

If you for whatever reason a host has some untracked changes that are not to be commited by fang on this occasion, he can be instructed to only commit files that are currently staged. 

    fang -s

Outside of this nuance, the command works exactly like the default path.


### Pulling downstream changes

If an unconnected dotfiles repo gets out of sync with origin, run

    fang -p

and he will pull all the latest changes from each branch.


## Fanglists

Fang is also the proud guardian of the fanglists. Each list details which top
level pakaages are installed on which host so that they can be recreated on
command.

Just like with the Howlin Dotfiles the lists are mapped with a tree heirarchy
with the exception of `_aur` lists, which are extracted from their parent so
that howlos can compile them from the aur without passing makepkg root
privilages.

The current structure is
- base [installs from endeavourOS]
  - main
    - server
      - host leaves
    - worker
      - host leaves


## RoadMap

- Output all untracked installed packages on `source .bashrc`.
  - use pacman -Qqtt
  - use a concat of all packages in pac lists
