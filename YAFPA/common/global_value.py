import os
from datetime import datetime
from pathlib import Path

from dotenv import dotenv_values

import YAFPA
from YAFPA.common import setup_config as settup

BASEDIR = YAFPA.__path__[0]
env_path = Path(f"{BASEDIR}/.YAFPA-env")

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
                if len(data) == 0 or len(vault[1]) == 0:
                    settup.create_env()


env = dotenv_values(env_path)

# Seems to have problem with dotenv with pyto on IOS 15
try:
    BASEDIR = Path(env["blog_path"]).expanduser()
    vault = Path(env["vault"]).expanduser()
    web = env["blog"]
except KeyError:
    with open(env_path) as f:
        vault_str = "".join(f.readlines(1)).replace("vault=", "")
        basedir_str = "".join(f.readlines(2)).replace("blog_path=", "")

        vault = Path(vault_str)
        BASEDIR = Path(basedir_str)
        web = "".join(f.readlines(3)).replace("blog=", "")
    if len(vault_str) == 0 or len(basedir_str) == 0 or len(web) == 0:
        print("Please provide a valid path for all config items")
        exit(1)

vault = vault.expanduser()
BASEDIR = BASEDIR.expanduser()
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
