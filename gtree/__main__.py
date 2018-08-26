"""
Parse out .gitignore files and feed them into GNU tree
"""

import os
import sys
import subprocess


def parse_ignore(ignore: str) -> list:
    """
    Turn a .gitignore file into a pattern for tree.

    Arguments:
        ignore: A string representation of a .gitignore file
    Returns:
        result: A list of arguments for tree
    """
    split = ignore.split("\n")
    # List Comprehension to remove all comments
    split = [x for x in split if x and x[0] != "#"]
    # Combine to create one pattern for tree
    result = '|'.join(split)
    return result


def tree_ignore(ignore_args: list) -> None:
    """
    Put the results of parse_ignore into tree.

    Arguments:
        ignore: .gitignore file
    """
    base = ["tree", "-I"]
    base.append("{}".format(ignore_args))
    subprocess.run(base)


def open_ignore(name: str) -> str:
    """Open the requested file"""
    with open(name, "r") as file:
        result = file.read()
    return result


def main():
    """Main Command"""
    if not len(sys.argv) > 1:
        ignore_file = open_ignore(".gitignore")
    else:
        ignore_file = open_ignore(sys.argv[1])
    arguments = parse_ignore(ignore_file)
    tree_ignore(arguments)
