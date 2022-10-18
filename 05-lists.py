import math

# 30 Days of Python: Day 04
print("30 Days of Python: Day 05 - Lists")

# 1
print("\n###LEVEL 1###")

# 1.1
print("---1.1---")
empty_list = []
print(empty_list)
# 1.2
print("---1.2---")
more_than_five = [1, 2, 3, 4, 5, 6, 7]
print(more_than_five)
# 1.3
print("---1.3---")
len_mtf = len(more_than_five)
print(f"len(more_than_five) = {len_mtf} > 5")
# 1.4
print("---1.4---")
print(f"First item: {more_than_five[0]}")
print(f"Middle item: {more_than_five[len_mtf//2]}")
print(f"Last item: {more_than_five[-1]}")
# 1.5
print("---1.5---")
mixed_data_types = ["string", 42, 4.2, False]
print(mixed_data_types)
# 1.6
# print("---1.6---")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# 1.7
print("---1.7---")
print(it_companies)
# 1.8
print("---1.8---")
len_itc = len(it_companies)
print(len_itc)
# 1.9
print("---1.9---")
print(f"First company: {it_companies[0]}")
print(f"Middle company: {it_companies[len_itc//2]}")
print(f"Last company: {it_companies[-1]}")
# 1.10
print("---1.10---")
it_companies[0] = "Meta"
print(it_companies)
# 1.11
print("---1.11---")
it_companies.append("Samsung")
print(it_companies)
# 1.12
print("---1.12---")
it_companies.insert(len(it_companies) // 2, "Mozilla")
print(it_companies)
# 1.13
print("---1.13---")
it_companies[0] = it_companies[0].upper()
print(it_companies)
# 1.14
print("---1.14---")
print("; ".join(it_companies))
# 1.15
print("---1.15---")
print('"META" in it_companies?', "META" in it_companies)
print('"Meta" in it_companies?', "Meta" in it_companies)
# 1.16
print("---1.16---")
print(f"sorted(): {sorted(it_companies)}")
print(f"it_companies: {it_companies}")
print(f".sort(): {it_companies.sort()}")
print(f"it_companies: {it_companies}")
# 1.17
print("---1.17---")
print(f".reverse(): {it_companies.reverse()}")
print(f"it_companies: {it_companies}")
# 1.18
print("---1.18---")
print(it_companies[:3])
# 1.19
print("---1.19---")
print(it_companies[-3:])
# 1.20
print("---1.20---")
mid = len(it_companies) / 2
print(it_companies[math.floor(mid - 0.5) : math.ceil(mid + 0.5)])
# test = [1, 2, 3, 4]
# mid = len(test) / 2
# print(test[math.floor(mid - 0.5) : math.ceil(mid + 0.5)])
# 1.21
print("---1.21---")
print(it_companies)
it_companies.pop(0)
print(it_companies)
# 1.22
print("---1.22---")
mid = math.ceil(len(it_companies) / 2)
it_companies.pop(mid - 1)
# If new length odd, original was even
# => Need to delete a second element
if len(it_companies) % 2 == 1:
    it_companies.pop(mid - 1)
print(it_companies)
# 1.23
print("---1.23---")
it_companies.pop()
print(it_companies)
# 1.24
print("---1.24---")
it_companies.clear()
print(it_companies)
# 1.25
print("---1.25---")
del it_companies
try:
    print(it_companies)
except NameError as e:
    print(e)
# 1.26
print("---1.26---")
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
joined_list = front_end + back_end
print(joined_list)
# 1.27
print("---1.27---")
full_stack = joined_list.copy()
i = full_stack.index("Redux") + 1
full_stack.insert(i, "SQL")
full_stack.insert(i, "Python")
print(f"joined_list: {joined_list}")
print(f"full_stack: {full_stack}")
