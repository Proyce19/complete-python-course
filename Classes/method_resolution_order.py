"""Method Resolution Order (MRO) is the order in which the base classes are searched when looking for a method in a
class hierarchy. In Python, classes can be involved in multiple inheritance, meaning a class can inherit attributes
and methods from more than one base class. The MRO defines the sequence in which these base classes are searched to
resolve a method or attribute."""


class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")
        super().method()


class C(A):
    def method(self):
        print("C")
        super().method()


class D(C, B):
    pass


d_instance = D()
d_instance.method()


"""
Depth-First, Left-to-Right (DPLR):

The MRO starts from the derived class and follows a depth-first, left-to-right traversal of the class hierarchy.
In a class hierarchy with multiple inheritance, the MRO ensures that each class is considered only once,
and the order of appearance in the inheritance list is preserved.
"""