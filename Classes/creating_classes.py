class Point:
    # to name classes we use Camelcase naming convention for example "ClassName" with each word in upper case
    # letter and no underscore
    def draw(self):
        # Then we define a function and by convention every function in the class should have at least one
        # parameter, and we call this parameter self.
        print("draw")


point = Point()
point.draw()
print(type(point))
# Prints <class '__main__.Point'> # __main__ is the name of our module

print(isinstance(point,
                 Point))  # Sometimes we have an object and want to see if that object is an instance of a given class
