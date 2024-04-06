from dataclasses import dataclass, field
from typing import List

from scoup import Scoop


@dataclass
class Bowl:
    scoops: List[Scoop] = field(default_factory=list)
    bowl_limit: int = 3

    def add_scoops(self, *scoops: Scoop):
        for s in scoops:
            if len(self.scoops) < self.bowl_limit:
                self.scoops.append(s)


@dataclass
class BigBowl(Bowl):
    bowl_limit: int = 5


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop("carrot")
s5 = Scoop('flavor 5')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)
b.add_scoops(s4)
print(b)
bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)
print(bb)
