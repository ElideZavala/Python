# Returns a new set with all items from both sets by removing duplicates

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

merge_set = set_one.union(set_two)
print(merge_set) # {70, 40, 10, 50, 20, 60, 30}