class Point:
    point_color = "Red"

    # This is a class attribute, defined at the class level. And they are the same across all instances of the class.

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z}) and color {self.point_color}")


point_1 = Point(100, 200, 10)

# We can also define an attribute after we create a point object. Because objects are dynamic in Python we don't have
# to define all the attributes in the constructor. But ony this instance will have this attribute
point_1.name = "The First Point"

print(point_1.x)
print(point_1.name)
point_1.draw()

point_2 = Point(500, 900, 100)
print(point_2.x)

point_2.draw()

print(point_1.point_color)
# We can use this object reference to get access to the point color attribute (which is a default class attribute)
print(Point.point_color)
# In here we are using the Point Class to get access to the point color attribute

Point.point_color = "Blue"  # In here we change the Class attribute Point Color to blue

print(point_2.point_color)

point_1.point_color = "Yellow"

print(point_1.point_color)
print(point_2.point_color)
# In here we change the point color of this object but the Class Point color does not change.
