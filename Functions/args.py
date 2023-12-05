def multiply(*numbers):
    print("args: ", numbers)
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(1, 2, 3, 4, 5))
print(multiply(1, 2, 3, 4, 5, 2))
print(multiply(0))
print(multiply())
