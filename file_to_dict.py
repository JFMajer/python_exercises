from pathlib import Path


def etcpasswd_to_dict() -> dict:
    filename = "/etc/passwd"
    path = Path(filename)

    users_ids = {}

    try:
        with path.open(mode="r", encoding="utf-8") as file:
            for line in file:
                if not line.strip() or line.startswith("#"):
                    continue
                splitted = line.split(":")
                if len(splitted) > 2:
                    users_ids[splitted[0]] = splitted[2]
    except FileNotFoundError:
        print("Provided filename could not be found")

    return users_ids


new_dict = etcpasswd_to_dict()
print(new_dict)
