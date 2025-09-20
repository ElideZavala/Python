# Remove items 10, 20, 30 from the following set at once

set = {10, 20, 30, 40, 50}
list_D= [10, 20, 30]

#1
set.difference_update({10, 20, 30})

#2
# for i in list_D:
#     set.discard(i)

print(set)