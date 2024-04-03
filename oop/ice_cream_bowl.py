from scoup import Scoop


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoops):
        self.scoops.extend(scoops)

    def __str__(self):
        return f"My bowl contains {[s.flavor for s in self.scoops]}"


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)