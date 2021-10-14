import os
from datetime import datetime
from pathlib import Path
import sys

from dotenv import dotenv_values
from . import setup_config as settup, blog

base = Path.home()


if not os.path.isfile(Path(f"{base}/.YAFPA-env")):
    settup.create_env()
else:
    with open(Path(f"{base}/.YAFPA-env")) as f:
        components = f.read().splitlines()
        for data in components:
            vault = data.split("=")
            if len(vault[1]) == 0:
                settup.create_env()

env = dotenv_values(Path(f"{base}/.YAFPA-env"))

# Seems to have problem with dotenv with pyto on IOS 15
try:
    BASEDIR = Path(env["blog_path"])
    vault = Path(env["vault"])
    web = env["blog"]
except KeyError:
    with open(Path(f"{base}/.env")) as f:
        vault = "".join(f.readlines(1)).replace("vault=", "")
        BASEDIR = "".join(f.readlines(2)).replace("blog_path=", "")
        web = "".join(f.readlines(3)).replace("blog=", "")
    if len(vault ) == 0 or len(web) == 0 or len(web)==0:
        print('Please provide the good path for all folder')
        exit(1)
path = Path(f"{BASEDIR}/.git")  # GIT SHARED
post = Path(f"{BASEDIR}/_notes")
img = Path(f"{BASEDIR}/assets/img/")


def git_push(COMMIT):
    try:
        import git

        repo = git.Repo(Path(f"{BASEDIR}/.git"))
        repo.git.add(".")
        repo.git.commit("-m", f"{COMMIT}")
        origin = repo.remote("origin")
        origin.push()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {COMMIT} successfully 🎉")
    except ImportError:
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] Please, use another way to push your change 😶"
        )
