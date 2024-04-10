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
    pass


def simple_generator():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")


# Create the generator
gen = simple_generator()

# Advance to the first yield
next(gen)

# Advance to the second yield
next(gen)

# Try to advance past the end
next(gen)
