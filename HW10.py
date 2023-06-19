# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від
# "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    type = 'Vehicle'
    description = 'to carry'

    def definition_of_a_vehicle(self):
        return f'The definition of a vehicle is it designed {self.description}'


my_vehicle = Vehicle()
print(Vehicle)
print(my_vehicle.definition_of_a_vehicle())


class Car(Vehicle):
    further_desc = 'land'

    def further_description(self):
        return f'The {self.__class__.__name__} is designed for {self.further_desc} transport'


my_car = Car()
print(Car)
print(my_car.definition_of_a_vehicle())
print(my_car.further_description())


class Plane(Car, Vehicle):
    further_desc = 'air'


my_plane = Plane()
print(Plane)
print(my_plane.definition_of_a_vehicle())
print(my_plane.further_description())

class Ship(Plane):
    further_desc = 'water'

    def add_description(self):
        addition = 'the most romantic of vehicles'
        return f'We want to add that {self.__class__.__name__} is {addition}'

my_ship = Ship()
print(Ship)
print(my_ship.definition_of_a_vehicle())
print(my_ship.further_description())
print(my_ship.add_description())