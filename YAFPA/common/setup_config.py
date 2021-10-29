from pathlib import Path

import YAFPA

BASEDIR = YAFPA.__path__[0]
env_path = Path(f"{BASEDIR}/.YAFPA-env")


def create_env():
    print(f"Creating environnement in {env_path}")
    env = open(env_path, "w", encoding="utf-8")
    vault = ""
    blog = ""
    blog_link = ""
    while vault == "":
        vault = str(input("Please provide your obsidian vault path : "))
    while blog == "":
        blog = str(input("Please provide the blog repository path : "))
    while blog_link == "":
        blog_link = str(
            input("Please provide the blog link (as https://yourblog.netlify.app) : ")
        )
    env.write(f"vault={vault}\n")
    env.write(f"blog_path={blog}\n")
    env.write(f"blog={blog_link}\n")
    env.close()
