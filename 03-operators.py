import math

# 30 Days of Python: Day 03
print("30 Days of Python: Day 03 - Operators")

# 1
age = 101
# 2
height = 1.84
# 3
sqrt_i = 0.7 + 0.7j
# 4
"""
print("---4---")
base = input("Enter base: ")
hght = input("Enter height: ")
print("The area of the triangle is", 0.5 * float(base) * float(hght))
"""
# 5
"""
print("---5---")
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
print("The area of the triangle is", float(side_a) + float(side_b) + float(side_c))
"""
# 6
"""
print("---6---")
lgth = input("Enter length: ")
wdth = input("Enter width: ")
print("The area of the rectangle is", float(lgth) * float(wdth))
print("The perimetre of the rectangle is", 2 * (float(lgth) + float(wdth)))
"""
# 7
"""
print("---7---")
radius = input("Enter radius: ")
print("The area of the circle is", math.pi * (float(radius) ** 2))
print("The circumference of the circle is", 2 * math.pi * float(radius))
"""
# 8
"""
print("---8---")
x_1 = 1
x_2 = 2
slope_8 = ((2 * x_2 - 2) - (2 * x_1 - 2)) / (x_2 - x_1)
x_intercept = (0 + 2) / 2
y_intercept = (2 * 0) - 2
print(
    "Slope: {}; x = 0, y = {}; x = {}, y = 0".format(slope_8, y_intercept, x_intercept)
)
"""
# 9
"""
print("---9---")
x_1, y_1 = 2, 2
x_2, y_2 = 6, 10
slope_9 = (y_2 - y_1) / (x_2 - x_1)
euc_dist = ((y_2 - y_1) ** 2 + (x_2 - x_1) ** 2) ** 0.5
print("Slope: {}; Euclidean distance: {}".format(slope_9, euc_dist))
"""
# 10
"""
print("---10---")
print("Does the slope in 8 equal the slope in 9?", slope_8 == slope_9)
"""
# 11
print("---11---")


def calculate_y(x):
    return (x**2) + (6 * x) + 9


print("0 => {}".format(calculate_y(0)))
print("1 => {}".format(calculate_y(1)))
print("2 => {}".format(calculate_y(2)))
print("10 => {}".format(calculate_y(10)))
print("-1 => {}".format(calculate_y(-1)))
print("-3 => {}".format(calculate_y(-3)))
