import json
import pathlib


def scores(directory_name: str):
    files = pathlib.Path(directory_name).rglob('*.json')
    for f in files:
        print(f"Analyzed file is: {f}")
        science_stats = {"min": 23748347000, "max": 0, "cum": 0}
        literature_stats = {"min": 23748347000, "max": 0, "cum": 0}
        math_stats = {"min": 23748347000, "max": 0, "cum": 0}
        path = pathlib.Path(f)
        with path.open(mode='r') as file:
            content = json.load(file)
            for s in content:
                math_stats["cum"] += s["math"]
                if s["math"] > math_stats["max"]:
                    math_stats["max"] = s["math"]
                if s["math"] < math_stats["min"]:
                    math_stats["min"] = s["math"]

                literature_stats["cum"] += s["literature"]
                if s["literature"] > literature_stats["max"]:
                    literature_stats["max"] = s["literature"]
                if s["literature"] < literature_stats["min"]:
                    literature_stats["min"] = s["literature"]

                science_stats["cum"] += s["science"]
                if s["science"] > science_stats["max"]:
                    science_stats["max"] = s["science"]
                if s["science"] < science_stats["min"]:
                    science_stats["min"] = s["science"]

            print(f"science: min {science_stats['min']}, max {science_stats['max']}, average {science_stats['cum'] / len(content)}")
            print(
                f"literature: min {literature_stats['min']}, max {literature_stats['max']}, average {literature_stats['cum'] / len(content)}")
            print(
                f"math: min {math_stats['min']}, max {math_stats['max']}, average {math_stats['cum'] / len(content)}")
            print("\n")


scores("files/scores")
