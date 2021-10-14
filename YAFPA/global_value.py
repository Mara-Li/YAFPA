import os
from datetime import datetime
from pathlib import Path

from dotenv import dotenv_values

from . import setup_config as settup

base = Path.home()

if not os.access(base, os.W_OK):
    base= os.getcwd()
env_path = Path(f"{base}/.YAFPA-env")

if not os.path.isfile(env_path):
    settup.create_env()
else:
    with open(env_path) as f:
        components = f.read().splitlines()
        if len(components) == 0:
            settup.create_env()
        else:
            for data in components:
                vault = data.split("=")
                if len(data) == 0 or len(vault[1]) == 0 :
                    settup.create_env()


env = dotenv_values(env_path)

# Seems to have problem with dotenv with pyto on IOS 15
try:
    BASEDIR = Path(env["blog_path"])
    vault = Path(env["vault"])
    web = env["blog"]
except KeyError:
    with open(env_path) as f:
        vault = "".join(f.readlines(1)).replace("vault=", "")
        BASEDIR = "".join(f.readlines(2)).replace("blog_path=", "")
        web = "".join(f.readlines(3)).replace("blog=", "")
    if len(vault) == 0 or len(web) == 0 or len(web) == 0:
        print("Please provide the good path for all folder")
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
