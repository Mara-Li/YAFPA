import argparse
import os
import sys

try:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


from . import file_checking as check
from . import convert_one as one
from . import convert_all as all
from . import setup_config as setup

def mobile_shortcuts(file = "0"):
    delopt = False
    git = True
    if file == "--c":
        setup.create_env()
    elif file != "0":
        if os.path.exists(file):
            one.convert_one(file, delopt, git)
        else:
            all.convert_all(git=False)
    else:
        all.convert_all(git=False)


def main():
    parser = argparse.ArgumentParser(
        description="Create file in _notes, move image in assets, convert to relative path, add share support, and push to git"
    )
    group_f = parser.add_mutually_exclusive_group()
    group_f.add_argument(
        "--preserve",
        "--p",
        "--P",
        help="Don't delete file if already exist",
        action="store_true",
    )
    group_f.add_argument(
        "--update",
        "--u",
        "--U",
        help="force update : delete all file and reform.",
        action="store_true",
    )
    parser.add_argument(
        "--filepath",
        "--f",
        "--F",
        help="Filepath of the file you want to convert",
        action="store",
        required=False,
    )
    parser.add_argument(
        "--git", "--g", "--G", help="No commit and no push to git", action="store_true"
    )
    parser.add_argument(
        "--keep",
        "--k",
        help="Keep deleted file from vault and removed shared file",
        action="store_true",
    )
    parser.add_argument(
        "--config", "--c", help="Edit the config file", action="store_true"
    )
    args = parser.parse_args()
    ori = args.filepath
    delopt = False
    if args.preserve:
        delopt = True
    force = args.update
    ng = args.git
    if args.config:
        setup.create_env()
        return
    if not args.keep:
        check.delete_not_exist()
        stop_share = 1
    else:
        stop_share = 0
    if ori:
        if os.path.exists(ori):  # Share ONE
            one.convert_one(ori, delopt, ng)
        else:
            print(f"Error : {ori} doesn't exist.")
            return
    else:
        all.convert_all(delopt, ng, force, stop_share)
