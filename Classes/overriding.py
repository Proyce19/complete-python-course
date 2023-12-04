class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 1
        # If we don't add the super function the constructor in the Animal class will not be
        # executed because it will be replaced by the contractor
        # With the super() we can access any method on the animal class

    def walk(self):
        print("walk")


mammal = Mammal()
print(mammal.age)
print(mammal.weight)