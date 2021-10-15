from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="YAFPA",
    version="1.50.8",
    description="A script to share your obsidian vault (in partial way)",
    author="Mara-Li",
    author_email="mara-li@icloud.com",
    packages=["YAFPA"],
    install_requires=[
        "python-dotenv",
        "gitpython",
        "python-frontmatter",
        "pyYAML",
        "pyperclip",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mara-Li/YAFPA-python",
    entry_points={
        "console_scripts": ["yafpa=YAFPA.blog:main"],
    },
)
