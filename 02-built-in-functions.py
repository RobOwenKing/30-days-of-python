# 30 Days of Python: Day 02
print("30 Days of Python: Day 02 - Built-In Functions")

# Variables from ./02-variables.py
first_name = "Fakeson"
last_name = "McFakeface"
full_name = first_name + " " + last_name
year = 1879
is_true = True
a_list, a_tuple, a_set = [1, 2], (1, 2), {1, 2}

# 2
# 2.1
print("---2.1---")
print(type(full_name))  # Should print <class 'str'>
print(type(year))  # Should print <class 'int'>
print(type(is_true))  # Should print <class 'bool'>
print(type(a_list))  # Should print <class 'list'>
print(type(a_tuple))  # Should print <class 'tuple'>
print(type(a_set))  # Should print <class 'set'>

# 2.2
print("---2.2---")
print("The given first_name is of length", len(first_name))

# 2.3
print("---2.3---")
print("Is first_name longer than last_name?", len(first_name) > len(last_name))

# 2.4
print("---2.4---")
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two
