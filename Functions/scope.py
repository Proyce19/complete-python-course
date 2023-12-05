
# Local an Global variables

# In programming we have a very important concept called Scope witch refers to the regions of the code where the
# variable is defined.


def greet(name):
    message = "a"

# The Scope of the variables "name" and "message" are in the greet function, they are local in this function.
# They don't exist anywhere else in the code.


message = "a"
# In contrast, the variable "message" above is a global variable, that is accessible anywhere in this code.
