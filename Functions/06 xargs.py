def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(1, 3, 6, 2, 8))
