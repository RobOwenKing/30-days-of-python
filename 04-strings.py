# 30 Days of Python: Day 04
print("30 Days of Python: Day 04 - Strings")

# 1
print("---1---")
print(" ".join(["Thirty", "Days", "Of", "Python"]))
# 2
print("---2---")
print(" ".join(["Coding", "For", "All"]))
# 3
company = "Coding For All"
# 4
print("---4---")
print("company =", company)
# 5
print("---5---")
print("length =", len(company))
# 6
print("---6---")
print("all the characters".upper())
# 7
print("---7---")
print("ALL THE CHARACTERS".lower())
# 8
print("---8---")
print("Coding For All".capitalize())
print("Coding For All".title())
print("Coding For All".swapcase())
# 9
print("---9---")
print("Coding For All"[:6])
# 10
print("---10---")
print("Coding For All".find("Coding"), "# find")
print("Coding" in "Coding For All", "# in")
print("Coding For All".index("Coding"), "# index")
# 11
print("---11---")
print("Coding For All".replace("Coding", "Python"))
# 12
print("---12---")
print("Python For Everyone".replace("Everyone", "All"))
# 13
print("---13---")
print("Coding For All".split(" "))
# 14
print("---14---")
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
# 15
print("---15---")
print(f"\"{'Coding For All'[0]}\"")
# 16
print("---16---")
print(f"\"{'Coding For All'[-1]}\"")
# 17
print("---17---")
print(f"\"{'Coding For All'[10]}\"")
# 18
print("---18---")


def abbreviate(str):
    return "".join([s[0] for s in str.split()])


print(abbreviate("Python For Everyone"))
# 19
print("---19---")
print(abbreviate("Coding For All"))
# 20
print("---20---")
print("Coding For All".index("C"))
# 21
print("---21---")
print("Coding For All".index("F"))
# 22
print("---22---")
print("Coding For All People".rfind("l"))
# 23
print("---23---")
long_string = "You cannot end a sentence with because because because is a conjunction"
print(long_string.index("because"), "# index")
print(long_string.find("because"), "# find")
# 24
print("---24---")
print(long_string.rindex("because"), "# rindex")
print(long_string.rfind("because"), "# rfind")
# 25
print("---25---")
substr = "because because because"
start = long_string.index(substr)
end = start + len(substr)
print(long_string[:start] + long_string[end:])
# 26 is the same as 23
# 27 is the same as 25
# 28
print("---28---")
print("Coding For All".startswith("Coding"))
# 29
print("---29---")
print("Coding For All".endswith("Coding"))
# 30
print("---30---")
print(f"\"{'   Coding For All      '.strip()}\"")  # "" to prove whitespace gone
