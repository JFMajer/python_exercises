import json
from pathlib import Path

numbers = [1, 2, 3, 5, 6, 8, 45, 23]

path = Path("files/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

simple_dict = {
    "name": "John Doe",
    "age": 30,
    "is_student": False
}

simple_dict_json = json.dumps(simple_dict)
Path("files/simple_dict.json").write_text(simple_dict_json)

list_of_dicts = [
    {"name": "Alice", "age": 25, "interests": ["reading", "gardening"]},
    {"name": "Bob", "age": 22, "interests": ["coding", "chess"]}
]

Path("files/list_of_dicts.json").write_text(json.dumps(list_of_dicts, indent=4))

nested_structure = {
    "team": "Data Science",
    "members": [
        {"name": "Eve", "role": "Data Analyst", "skills": ["Python", "SQL", "Tableau"]},
        {"name": "Adam", "role": "Data Engineer", "skills": ["Python", "Spark", "Hadoop"]}
    ],
    "project": {
        "name": "Market Analysis",
        "deadline": "2023-12-31",
        "status": "In Progress"
    }
}

path_to_json_data = Path("files/random_data.json")
if path_to_json_data.exists():
    contents = path_to_json_data.read_text()
    from_json = json.loads(contents)
    print(f"Data from json was loaded into {type(from_json)}")
    print(contents)
else:
    print(f"There is no file {path_to_json_data}")

