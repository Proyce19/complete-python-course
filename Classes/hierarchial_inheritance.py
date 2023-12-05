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


class Dog(Animal):

    def barks(self):
        print("Woof Woof")


dog = Dog()
dog.barks()
dog.eat()


class BirdDog(Dog, Bird):
    pass


bird_dog = BirdDog()
bird_dog.eat()
bird_dog.barks()
bird_dog.fly()
