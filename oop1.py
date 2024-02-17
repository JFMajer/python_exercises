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
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it")

    def update_odometer(self, new_value):
        if new_value < self.odometer_reading:
            print("You can't roll odometer back")
        self.odometer_reading = new_value


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWh battery.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(1000)
my_new_car.read_odometer()
my_new_car.update_odometer(999)

my_leaf = ElectricCar('nissan', 'leaf', 2022)
print(my_leaf.get_descriptive_name())
my_leaf.read_odometer()
my_leaf.describe_battery()