def greet(name):
    print(f"Hi {name}")


greet("Joe")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Joe")
print(message)
