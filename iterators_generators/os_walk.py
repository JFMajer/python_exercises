import os
from pathlib import Path


def walk_the_dir(dir_name: str):
    for (root, _, files) in os.walk(dir_name, topdown=True):
        for f in files:
            path = Path(root) / f
            with path.open(mode="r", encoding="utf-8") as file:
                for line in file:
                    yield line


for line in walk_the_dir("/home/kuba/coding/python_exercises/files"):
    print(line)
