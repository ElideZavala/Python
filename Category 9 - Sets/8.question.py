# Update set1 by adding items from set2, except common items


set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_one = set_one.symmetric_difference(set_two)

# Nos traemos los valores que no estan repetidos en ambos 😜
print(set_one) # {20, 70, 10, 60}