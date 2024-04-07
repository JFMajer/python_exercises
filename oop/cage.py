from typing import List

from animals import Animal


class Cage:
    _id_counter = 0

    def __init__(self):
        self.id = Cage._get_next_id()
        self.animals: List[Animal] = []

    @classmethod
    def _get_next_id(cls):
        cls._id_counter += 1
        return cls._id_counter

    def add_animals(self, *args):
        self.animals.extend(args)

    def __repr__(self):
        animals_repr = ', '.join(repr(animal) for animal in self.animals)
        return f"Cage number {self.id} contains [{animals_repr}]"


