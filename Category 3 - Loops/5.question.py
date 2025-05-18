# Iterate the list below, and display numbers divisible by 5, and stop the iteration when hitting a number of greater that 100 in the list

# solution 1 (Propia)

list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
new_list = []

def divisible_for_five(list):
    for i in list:
        if (i % 5 == 0) & (i <= 100):
            new_list.append(i)
    
    return new_list

print(divisible_for_five(list))

# solution 2
for item in list:
    if (item > 100):
        break

    if (item % 5 == 0):
        print(item, end=", ")