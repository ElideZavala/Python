# Check if two sets have any elements in common. If yes, display the common elements.

set_one = {10, 20, 30, 40, 50}
set_two = {60, 70, 80, 90, 10}


if set_one.isdisjoint(set_two):
    print('Si yay')
else:
    print(set_one.intersection(set_two))
