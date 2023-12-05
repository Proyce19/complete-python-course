calculate = lambda x: x * 2
result = calculate(3)
print(result)

# useful example
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

# Sorting the dictionary by values
print(my_dict.items())  # dict_items([('apple', 5), ('banana', 2), ('orange', 8), ('grape', 1)])

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Displaying the sorted dictionary
print(sorted_dict)
