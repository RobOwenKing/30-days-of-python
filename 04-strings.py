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
print("Coding For All".find("Coding"), "// find")
print("Coding" in "Coding For All", "// in")
print("Coding For All".index("Coding"), "// index")
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
