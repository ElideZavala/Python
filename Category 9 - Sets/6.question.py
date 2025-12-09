# Return a set of all the unique elements in sets A & B

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_three = set_one.symmetric_difference(set_two)
print(set_three) # {20, 70, 10, 60}