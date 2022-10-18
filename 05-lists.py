import math

# 30 Days of Python: Day 04
print("30 Days of Python: Day 05 - Lists")

# 1
print("---1---")
empty_list = []
print(empty_list)
# 2
print("---2---")
more_than_five = [1, 2, 3, 4, 5, 6, 7]
print(more_than_five)
# 3
print("---3---")
len_mtf = len(more_than_five)
print(f"len(more_than_five) = {len_mtf} > 5")
# 4
print("---4---")
print(f"First item: {more_than_five[0]}")
print(f"Middle item: {more_than_five[len_mtf//2]}")
print(f"Last item: {more_than_five[-1]}")
# 5
print("---5---")
mixed_data_types = ["string", 42, 4.2, False]
print(mixed_data_types)
# 6
# print("---6---")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# 7
print("---7---")
print(it_companies)
# 8
print("---8---")
len_itc = len(it_companies)
print(len_itc)
# 9
print("---9---")
print(f"First company: {it_companies[0]}")
print(f"Middle company: {it_companies[len_itc//2]}")
print(f"Last company: {it_companies[-1]}")
# 10
print("---10---")
it_companies[0] = "Meta"
print(it_companies)
# 11
print("---11---")
it_companies.append("Samsung")
print(it_companies)
# 12
print("---12---")
it_companies.insert(len(it_companies) // 2, "Mozilla")
print(it_companies)
# 13
print("---13---")
it_companies[0] = it_companies[0].upper()
print(it_companies)
# 14
print("---14---")
print("; ".join(it_companies))
# 15
print("---15---")
print('"META" in it_companies?', "META" in it_companies)
print('"Meta" in it_companies?', "Meta" in it_companies)
# 16
print("---16---")
print(f"sorted(): {sorted(it_companies)}")
print(f"it_companies: {it_companies}")
print(f".sort(): {it_companies.sort()}")
print(f"it_companies: {it_companies}")
# 17
print("---17---")
print(f".reverse(): {it_companies.reverse()}")
print(f"it_companies: {it_companies}")
# 18
print("---18---")
print(it_companies[:3])
# 19
print("---19---")
print(it_companies[-3:])
# 20
print("---20---")
mid = len(it_companies) / 2
print(it_companies[math.floor(mid - 0.5) : math.ceil(mid + 0.5)])
# test = [1, 2, 3, 4]
# mid = len(test) / 2
# print(test[math.floor(mid - 0.5) : math.ceil(mid + 0.5)])
# 21
print("---21---")
print(it_companies)
it_companies.pop(0)
print(it_companies)
# 22
print("---22---")
mid = math.ceil(len(it_companies) / 2)
it_companies.pop(mid - 1)
# If new length odd, original was even
# => Need to delete a second element
if len(it_companies) % 2 == 1:
    it_companies.pop(mid - 1)
print(it_companies)
# 23
print("---23---")
it_companies.pop()
print(it_companies)
# 24
print("---24---")
it_companies.clear()
print(it_companies)
# 25
print("---25---")
del it_companies
try:
    print(it_companies)
except NameError as e:
    print(e)
# 26
print("---26---")
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
joined_list = front_end + back_end
print(joined_list)
# 27
print("---27---")
full_stack = joined_list.copy()
i = full_stack.index("Redux") + 1
full_stack.insert(i, "SQL")
full_stack.insert(i, "Python")
print(f"joined_list: {joined_list}")
print(f"full_stack: {full_stack}")
