# Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

list_of_keys = list(sample_dict.values())

set1 = set(roll_number)
set2 = set(list_of_keys)

desiguales = set1.symmetric_difference(set2)

roll_number = [item for item in roll_number if item not in desiguales]

print("🐛 roll_number", roll_number)






