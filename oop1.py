class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog("Reksio", 6)
print(f"My dog's name is {my_dog.name}")
my_dog.sit()
my_dog.roll_over()


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Our name is {self.restaurant_name} and we serve {self.cuisine_type} food')


rest1 = Restaurant("Big Burgers", "american")
rest1.describe_restaurant()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())