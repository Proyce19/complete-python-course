# When dealing with a large sequence of number (10 000 or more), arrays are better, they perform better in memory
# Only use arrays when encounter performance problems, otherwise, use List or Tuples

from array import array

# This module defines an object type which can compactly represent an array of basic values: characters, integers,
# floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects
# stored in them is constrained. The type is specified at object creation time by using a type code, which is a
# single character. The following type codes are defined:

# 'b' : Signed integer (char)
# 'B' : Unsigned integer (unsigned char)
# 'h' : Signed short integer
# 'H' : Unsigned short integer
# 'i' : Signed integer
# 'I' : Unsigned integer
# 'l' : Signed long integer
# 'L' : Unsigned long integer
# 'f' : Floating point
# 'd' : Double-precision floating point


numbers = array("i", [1, 2, 3])
print("object")
print(numbers)
print('elements using join')
print('\n'.join(map(str, numbers)))
print('elements using for loop')
for item in numbers:
    print(item)
