class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")

    def eat(self):
        print("pecks")


class Chicken(Bird):
    # The class chicken will inherit all the features of the "Bird" class as well as the "Animal" class
    def fly(self):
        print("does not fly")


chick = Chicken()
chick.fly()
chick.eat()
