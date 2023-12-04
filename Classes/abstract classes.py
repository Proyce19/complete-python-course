from abc import ABC, abstractmethod


# Abstract class definition
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete implementation of the abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Concrete implementation of the abstract class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Using abstract classes and their implementations
circle = Circle(radius=5)
square = Square(side=4)

print("Circle Area:", circle.area())  # Outputs: Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter())  # Outputs: Circle Perimeter: 31.400000000000002

print("Square Area:", square.area())  # Outputs: Square Area: 16
print("Square Perimeter:", square.perimeter())  # Outputs: Square Perimeter: 16
