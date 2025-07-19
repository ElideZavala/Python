# Given the following two sets find the intersection and remove those elements from the first set

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}

# primera forma
intersection = set1.intersection(set2)
print("🐛 intersection", intersection)

# segunda forma
intersection_and = set1 & set2 
#print("🐛 intersection_and ", intersection_and)

#for i in intersection:
#   set1.remove(i)

set1.difference_update(intersection)

print(set1)

# remove_elements = set1.remove(intersection)