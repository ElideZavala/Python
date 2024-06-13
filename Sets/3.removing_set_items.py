# ---------------------------------------------------------------------------------
# ---------------------**## Removing Items from a Set ##**-------------------------

#! ********** Example 14 **********
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numbers)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numbers.discard(4)  # Removes 4 from the set
print(numbers)  # {1, 2, 3, 5, 6, 7, 8, 9, 10}
# The discard() method removes the specified item from the set.

#! ********** Example 15 ********** Item does not exist
numbers.discard(11)  # 11 does not exist in the set
print(numbers)  # {1, 2, 3, 5, 6, 7, 8, 9, 10}
# If the item does not exist, the discard() method does not raise an error.

#! ********** Example 16 ********** Removing an item using remove()
numbers.remove(5)  # Removes 5 from the set
print(numbers)  # {1, 2, 3, 6, 7, 8, 9, 10}

#! ********** Example 17 ********** Item does not exist
# numbers.remove(11)  # 11 does not exist in the set
# print(numbers)  # KeyError: 11 # If the item does not exist, the remove() method raises an error.

#! ********** Example 18 ********** Removing an item using pop()
numbers.pop()  # Removes the first item from the set
print(numbers)  # {2, 3, 6, 7, 8, 9, 10}

#! ********** Example 19 ********** Clearing the set
numbers.clear()  # Removes all items from the set
print(numbers)  # set()
