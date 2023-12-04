"""Polymorphism is the ability of different classes to be used interchangeably based on a common interface.
 It allows
objects of different types to be treated as objects of a common type."""


class Bird:
    def fly(self):
        pass


class Eagle(Bird):
    def fly(self):
        return "Eagle can fly!"


class Penguin(Bird):
    def fly(self):
        return "Penguin can't fly."


# Using polymorphism
eagle = Eagle()
penguin = Penguin()


def make_bird_fly(bird):
    return bird.fly()


print(make_bird_fly(eagle))  # Outputs: Eagle can fly!
print(make_bird_fly(penguin))  # Outputs: Penguin can't fly.
