from dataclasses import dataclass, field
from typing import List

from scoup import Scoop


@dataclass
class Bowl:
    scoops: List[Scoop] = field(default_factory=list)

    def add_scoops(self, *scoops: Scoop):
        self.scoops.extend(scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)
