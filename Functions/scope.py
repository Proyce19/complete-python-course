

# The variable "message" above is a global variable, that is accessible anywhere in this code.

message = "Hi"


def greet(name):
    message = "Bye"
    print(message)
    print(name)


greet("Joe")
print(message)
# The Scope of the variables "name" and "message" are in the greet function, they are local in this function.
# They don't exist anywhere else in the code.
