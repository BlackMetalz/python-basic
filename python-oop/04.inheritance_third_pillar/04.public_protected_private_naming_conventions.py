class Car:
    number_of_wheels = 4 # Public attribute
    _color = "red"  # Protected attribute
    __year_of_manufacture = 2025  # Private attribute
    # if you still want to access this attribute, you can use the name mangling technique
    # _Car__year_of_manufacture

class Bmw(Car):
    def __init__(self):
        print("Protected attributes color: ", self._color)  # Accessing protected attribute

car = Car()
print("Public attributes number_of_wheels: ", car.number_of_wheels)

bmw = Bmw()

# This will raise an AttributeError
# AttributeError: 'Car' object has no attribute '__year_of_manufacture'.
# print("Private attribute year_of_manufacture: ", car.__year_of_manufacture) 

# This is how you can access the private attribute using name mangling, but not really recommended
print("Private attribute year_of_manufacture: ", car._Car__year_of_manufacture)  # Accessing private attribute using name mangling