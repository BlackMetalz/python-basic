"""
class Square:
    side = 4
    def area(self):
        print("Area of square:", self.side * self.side)

class Rectangle:
    width = 5
    length = 10

    def area(self):
        print("Area of rectangle:", self.width * self.length)

square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()
"""

from abc import ABCMeta, abstractmethod
# After implementing an abstract base class (ABC) for the above code, it would look like this:
class Shape(metaclass = ABCMeta):

    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square:", self.side * self.side)

class Rectangle(Shape):
    width = 5
    length = 10

    def area(self):
        print("Area of rectangle:", self.width * self.length)

square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()
