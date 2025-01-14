class Employee:
    def greet(self):
        print("Greet Employee")


class Person:
    def greet(self):
        print("Greet Person")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()


# We will get Greet Employee, because the Employee class is called first.
# If the Employee class didn't have the greet method then the greet method in the person class would be called.


# It is better to use multiple Inheritance, with classes small classes that have nothing in common.
