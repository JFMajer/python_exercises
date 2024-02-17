from collections import Counter
from pathlib import Path


def count_shells():
    path = Path("/etc/passwd")

    if not path.is_file():
        raise FileNotFoundError(f"No such file: '{path}'")

    with path.open() as f:
        shells = [line.strip().split(":")[-1] for line in f if line.strip()]

    shell_popularity = Counter(shells).most_common()
    for s in shell_popularity:
        print(f"shell {s[0]} appears {s[1]} times")


count_shells()
