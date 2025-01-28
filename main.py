#! /usr/bin/python3

from subprocess import run, check_output
import os
from sys import argv

def merge_downstreams(tree, parent):
    for node, children in tree.items():
        print("")
        run(['git', 'checkout', node])
        run(['git', 'merge', parent, '--no-edit'])
        # git push
        merge_downstreams(children, node)

def commit(tree, branch, arg):
    for node, children in tree.items():
        if node == branch:
            run(['git', 'add', '.'])
            # halt and ask for approval on staged files before commit
            run(['git', 'commit', '-m', arg])
            # git push
            merge_downstreams(children, node)
        else:
            commit(children, branch, arg)

branches = {
    "main": {
        "server": {
            "the": {},
            "worker": {
                "bass": {},
                "howlin": {}
            }
        }
    }
}

def main():
    branch = check_output(['git', 'branch', '--show-current'], text=True).strip()
    commit(branches, branch, argv[1])

    
main()
