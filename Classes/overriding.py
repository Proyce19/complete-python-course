class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 1

    def walk(self):
        print("walk")


mammal = Mammal()
print(mammal.age)
print(mammal.weight)
