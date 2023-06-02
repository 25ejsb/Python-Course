# numbers
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Eitan"
new_list_2 = [letter for letter in name]
print(new_list_2)

# double list
range_list = [new_item * 2 for new_item in range(1, 5)]
print(range_list)

# Conditional lists
names = ["Alex", "Byron", "Badcc", "Alan", "Frank"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
capital_names = [name.upper() for name in names if len(name) >= 5]
print(capital_names)