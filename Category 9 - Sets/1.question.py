# Add a list of elements to a given set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# newSet = sample_set.union(set(sample_list))
#2
sample_set.update(sample_list)

# 2
# for i  in sample_list:
#     sample_set.add(i)

print(sample_set)
# print(newSet)