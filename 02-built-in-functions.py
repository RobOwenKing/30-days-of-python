import math

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
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

print(num_one, "+", num_two, "=", total)
print(num_one, "-", num_two, "=", diff)
print(num_one, "*", num_two, "=", product)
print(num_one, "/", num_two, "=", division)
print(num_one, "%", num_two, "=", remainder)
print(num_one, "**", num_two, "=", exp)
print(num_one, "//", num_two, "=", floor_division)

# 2.5
print("---2.5---")


def print_circle_details(r):
    area_of_circle = math.pi * (r**2)
    circum_of_circle = 2 * math.pi * r
    print(
        "A circle with radius {} has area {} and circumference {}".format(
            r, area_of_circle, circum_of_circle
        )
    )


radius = 30
print_circle_details(radius)
input_radius = int(input("Give a radius: "))
print_circle_details(input_radius)

# 2.6
print("---2.6---")
user_name = input("What's your name? ")
user_country = input("Where are you from? ")
user_age = int(input("How old are you? "))
