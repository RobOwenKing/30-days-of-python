import sys

# 30 Days of Python: Day 01
print("30 Days of Python: Day 01 - Introduction")

# 1
print("\n###LEVEL 1###")
print("All in the interactive shell")

# 2
print("\n###LEVEL 2###")

# 2.1
print("---2.1---")
print("You are currently using Python version", sys.version)

# 2.2
# Blame black for the ugly formatting
# of the ** and line-end comments!
print("---2.2---")
print(3 + 4)  # Should print 7
print(3 - 4)  # Should print -1
print(3 * 4)  # Should print 12
print(3 / 4)  # Should print 0.75
print(3**4)  # Should print 81
print(3 % 4)  # Should print 3
print(3 // 4)  # Should print 0

# 2.3
print("---2.3---")
print("Fakename")
print("McFakeface")
print("SomeCountry")
print("I am enjoying 30 days of python")

# 2.4
# NB: I've removed some repeats
print("---2.4---")
print(type(10))  # Should print <class 'int'>
print(type(3.14))  # Should print <class 'float'>
print(type(4 - 4j))  # Should print <class 'complex'>
print(type(["Asabeneh", "Python", "Finland"]))  # Should print <class 'list'>
print(type("Fakename McFakeface"))  # Should print <class 'str'>

# 3
print("\n###LEVEL 3###")

# 3.1
print("---3.1---")
print(type(42))  # Should print <class 'int'>
print(type(1.618))  # Should print <class 'float'>
print(type(1 + 1j))  # Should print <class 'complex'>
print(type("str"))  # Should print <class 'str'>
print(type(True))  # Should print <class 'bool'>
print(type(["str", 42]))  # Should print <class 'list'>
print(type(("str", 42)))  # Should print <class 'tuple'>
print(type({"str", 42}))  # Should print <class 'set'>
print(type({"str": 42}))  # Should print <class 'dict'>

# 3.2
print("---3.2---")
euc_dist = ((10 - 2) ** 2 + (8 - 3) ** 2) ** 0.5
print("The Euclidean distance between (2,3) and (10,8) is", euc_dist)
