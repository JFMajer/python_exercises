class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

    def __str__(self):
        return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'

    def __repr__(self):
        return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'

class Sheep(Animal):
    def __init__(self, color):
        super().__init__("sheep", 4, color)


class Wolf(Animal):
    def __init__(self, color):
        super().__init__("wolf", 4, color)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__("parrot", 2, color)


class Snake(Animal):
    def __init__(self, color):
        super().__init__("snake", 0, color)


