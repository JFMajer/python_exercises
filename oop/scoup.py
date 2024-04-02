class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():
    chocolate = Scoop("chocolate")
    vanilla = Scoop("vanilla")
    coffee = Scoop("coffee")
    flavours = [chocolate, vanilla, coffee]
    for flavor in flavours:
        print(flavor.flavor)


create_scoops()
