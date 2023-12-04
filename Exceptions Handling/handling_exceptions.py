try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You did no enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print('No exceptions where thrown')

print("Executions continues")


try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did no enter a valid age.")

else:
    print('No exceptions where thrown')

print("Executions continues")


def calculate_division(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 / age


try:
    calculate_division(-1)
except ValueError as error:
    print(error)