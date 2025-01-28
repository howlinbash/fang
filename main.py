#! /usr/bin/python3

from subprocess import run, check_output
import os
import sys

git_branches = {
    "main": {
        "server": {
            "the": {},
        },
        "worker": {
            "bass": {},
            "howlin": {}
        }
    }
}

def print_error(msg):
    print("== ERROR:", msg, "==")

def print_help(exit=0):
    print("NAME")
    print("       pac - Manage dotfile branches")
    print("")
    print("SYNOPSIS")
    print("       pac [OPTION]... [COMMIT MESSAGE]...")
    print("")
    print("DESCRIPTION")
    print("       commit changes then push & merge for all downstream branches")
    print("       If no option is provided, all changes will be commited.")
    print("")
    print("       -h")
    print("              list this menu")
    print("")
    print("       -s")
    print("              Only commit staged files")
    sys.exit(exit)

def too_many_args():
    print_error("Too many args")
    sys.exit(1)

def no_commit_msg():
    print_error("We need a commit message")
    sys.exit(1)

def parse_args(args ):
    if not args[1]:
        no_commit_msg()

    if args[1][0] == "-":
        if args[1][1] == "h":
            print_help()
        elif args[1][1] == "s":
            if len(args) < 3:
                no_commit_msg()
            if len(args) > 3:
                too_many_args()

            ## Only commit staged files
            return [args[2], True]
        else: 
            print_error("Invalid argument")
            print("")
            print_help(1)
    else:
        if len(args) > 2:
            too_many_args()

        ## Simple commit message without options
        return [args[1]]

def approve_staged(branch):
    run(['git', 'log', '--graph', '--oneline', '--all', '-10'])
    print("")
    run(['git', 'status', '-s'])
    print("")
    print(branch)
    print("")
    user_input = input("Are you happy with staging? [Y/n]: ")
    if user_input == "n" or user_input == "q":
        print("bye then")
        sys.exit(0)
    if user_input != "":
        print_error("Invalid option")
        sys.exit(1)

def merge_downstreams(tree, parent, commit_msg):
    for node, children in tree.items():
        print("")
        run(['git', 'checkout', node])
        print("--MERGE--")
        run(['git', 'merge', parent, '-m', commit_msg])
        print("--PUSH--")
        run(['git', 'push'])
        merge_downstreams(children, node, commit_msg)

def commit(tree, branch, args):
    for node, children in tree.items():
        if node == branch:
            if len(args) == 1:
                run(['git', 'add', '.'])
            approve_staged(branch)
            print("--COMMIT--")
            run(['git', 'commit', '-m', args[0]])
            print("--PUSH--")
            run(['git', 'push'])
            merge_downstreams(children, node, args[0])
        else:
            commit(children, branch, args)

def main():
    args = parse_args(sys.argv)
    branch = check_output(['git', 'branch', '--show-current'], text=True).strip()
    commit(git_branches, branch, args)
    run(['git', 'checkout', branch])
    
main()
