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
