from dataclasses import dataclass


@dataclass
class Scoop:
    flavor: str


def create_scoops():
    scoops = [Scoop(flavor) for flavor in ('chocolate', 'coffee', 'vanilla')]
    for flavor in scoops:
        print(flavor.flavor)


create_scoops()
