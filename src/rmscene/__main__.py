"""Experimental cli helpers."""

import sys
import argparse
from . import read_blocks, build_tree, SceneTree
from rmscene import scene_items as si

def parse_args(args):
    parser = argparse.ArgumentParser(prog="rmscene")
    parser.add_argument("file", type=argparse.FileType("rb"), help="filename to read")
    return parser.parse_args(args)


def recursive(item: si.Group):
    for child_id in item.children:
        child = item.children[child_id]
        if isinstance(child, si.Group):
            recursive(child)
        elif isinstance(child, si.Line):
            pass

def pprint_file(args) -> None:
    import pprint

    result = read_blocks(args.file)
    tree = SceneTree()
    build_tree(tree, result)


    recursive(tree.root)

    for el in result:
        print()
        pprint.pprint(el)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    pprint_file(args)
