"""Inheritance is a mechanism that allows a class (subclass/derived class) to inherit properties and behaviors (
attributes and methods) from another class (superclass/base class). The subclass can reuse, extend, or override the
functionality of the superclass."""


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):  # Here the Mammal class is inheriting the function and attributes from the Animal class
    # def eat(self): # And so we do not need to repeat the same function
    #     print("eat")

    def walk(self):
        print("walk")


class Fish(Animal):  # Here the Fish class is inheriting the function and atributes from the Animal class
    # def eat(self): # And so we do not need to repeat the same function
    #     print("eat")

    def swim(self):
        print("swim")


m = Mammal()
m.eat()  # the Mammal class is using the 'eat' funtion from the Animal class

f = Fish()
print(f.age)  # The Fish class is using the age attribute from the Animal class

# The Animal class is called the Parent or Base class
# The Fish and Mammal classes are the Child or Sub class
