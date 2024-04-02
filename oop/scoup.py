class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():
    scoops = [Scoop(flavor) for flavor in ('chocolate', 'coffee', 'vanilla')]
    for flavor in scoops:
        print(flavor.flavor)


create_scoops()
