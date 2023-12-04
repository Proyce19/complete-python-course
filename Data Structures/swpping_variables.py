# 16 Swapping Variables

# Tow sawp to variable we can use a third variable to back up the first variable

x = 10
y = 20

# z = x
# x = y
# y = z

print(f"x: {x}\ny: {y}")

# In python, we can swap the value os two variable using only one line of code and with the third variable

x, y = y, x

print(f"x: {x}\ny: {y}")