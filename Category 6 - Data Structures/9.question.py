# Remove duplicate from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

list_not_duplicate = list(set(sample_list))

my_tuple_list = tuple(list_not_duplicate)
minimum = min(my_tuple_list)
maximum = max(my_tuple_list)

print(my_tuple_list)
print("****************************************\n")
print("🐛 minimum", minimum)
print("🐛 maximum", maximum)

