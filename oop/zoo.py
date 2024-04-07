from typing import List

from cage import Cage
from animals import Animal, Sheep, Wolf


class Zoo:
    def __init__(self):
        self.cages: List[Cage] = []

    def add_cages(self, *cages):
        self.cages.extend(cages)

    def animals_by_color(self, color: str):
        return [animal for cage in self.cages for animal in cage.animals if animal.color == color]

    def animals_by_legs(self, num_of_legs: int):
        return [animal for cage in self.cages for animal in cage.animals if animal.number_of_legs == num_of_legs]

    def sum_of_all_legs(self):
        return sum(animal.number_of_legs for cage in self.cages for animal in cage.animals)

    def __str__(self):
        zoo_details = "Zoo contains the following cages:\n"
        for cage in self.cages:
            zoo_details += f"{cage}\n"
        return zoo_details


s = Sheep('white')
w = Wolf('brown')
print(s.species)
print(s.color)
print(s.number_of_legs)
print(s)

c1 = Cage()
c1.add_animals(s, w)
print(c1)
c2 = Cage()
print(c2)

z = Zoo()
z.add_cages(c1, c2)
print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.sum_of_all_legs())
