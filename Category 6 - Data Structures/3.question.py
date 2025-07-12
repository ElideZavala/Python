# Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

counts_elements = {}

for x in sample_list:
    counts_elements[x] = sample_list.count(x)


print("🐛 ", counts_elements)
    