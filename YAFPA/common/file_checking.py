import glob
import os
from pathlib import Path

import frontmatter
from unidecode import unidecode

from YAFPA.common import convert_all as exclude
from YAFPA.common import global_value as settings
from YAFPA.common import metadata as mt

BASEDIR = settings.BASEDIR
post = settings.post
vault = settings.vault


def check_folder(folder_key):
    folder_key = folder_key.replace("_", "")
    path = Path(f"{BASEDIR}/_{folder_key}")
    if os.path.isdir(path):
        return path
    else:
        return post


def retro(filepath, opt=0):
    notes = []
    if opt == 0:
        metadata = frontmatter.load(filepath)
    else:
        metadata = frontmatter.loads("".join(filepath))
    file = metadata.content.split("\n")
    for n in file:
        notes.append(n)
    return notes


# PATH WORKING #
def delete_file(filepath, folder):
    path = Path(folder)
    for file in os.listdir(path):
        filename = unidecode(os.path.basename(filepath))
        filecheck = unidecode(os.path.basename(file))
        if filecheck == filename:
            os.remove(Path(f"{path}/{file}"))
            mt.update_frontmatter(filepath, folder, 0, 0)
            return True
    return False


def delete_not_exist():
    vault_file = []
    excluded = []
    info = []
    important_folder = ["_includes", "_layout", "_site", "assets", "script"]
    for i, j, k in os.walk(vault):
        for ki in k:
            vault_file.append(os.path.basename(ki))
            if exclude.exclude_folder(i + os.sep + ki):
                excluded.append(os.path.basename(ki))
    for file in glob.iglob(f"{BASEDIR}/_*/**"):
        if not (any(i in file for i in important_folder)):
            # Delete the file from the database if moved in the excluded folder
            if os.path.basename(file) != "404.md" and (
                os.path.basename(file) not in vault_file
                or os.path.basename(file) in excluded
            ):  # or if file in file_excluded
                os.remove(file)
                info.append(os.path.basename(file))
    return info


def all_file():
    all_file = {}
    post = []
    folder = "_notes"
    important_folder = ["_includes", "_layout", "_site"]
    contents = glob.glob(f"{BASEDIR}/_*/**")
    contents.extend(glob.glob(f"{BASEDIR}/_*/.*"))
    contents = sorted(contents)
    for file in contents:
        if not (any(i in file for i in important_folder)):
            if folder == os.path.basename(Path(file).parent.absolute()):
                post.append(file)
            else:
                post = [file]
                folder = os.path.basename(Path(file).parent.absolute())
            all_file[folder] = post
    return all_file


def check_file(filepath, folder, all_file):
    post_file = all_file[os.path.basename(Path(folder))]
    post_file = [os.path.basename(i) for i in post_file]
    if filepath in post_file:
        return "EXIST"
    else:
        return "NE"


def dest(filepath, folder):
    file_name = os.path.basename(filepath)
    dest = Path(f"{folder}/{file_name}")
    return str(dest)
