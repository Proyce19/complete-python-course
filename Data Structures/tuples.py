# Tuples are basically read only lists, can not be change

points = (1, 2, 3)  # with parenthesis it is a Tuple
print(type(points))

points_1 = (1, 2, 3, 4, 5) + (6, 7, 8, 9)  # Concatenate a tuple
print(points_1)

points_2 = (1, 2, 3, 4, 5) * 3  # multiply a tuple
print(points_2)

text_tuple = tuple(
    "Hello World")  # Because a string is an iterable it can be converted to a tuple with the built in function tuple()
print(text_tuple)

# Tuple can be transformed into a list with the built-in list function
print(list(points_1))

# Like list ww can access an item by the index
print(points[1])

# Unpack tuple
x, y, z = points
print(f"x: {x}\ny: {y}\nz: {z}")

# Check if an item is in the Tuple
if 2 in points:
    print("Exists")
else:
    print("Not there")
