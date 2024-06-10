# -------------------------------------------------------------------------
# ----------------------**## Tuple Methods ##**----------------------------

#! *********** Example 1 *********** count() method
# The count() method returns the number of times a specified value appears in the tuple.
colors = ("red", "blue", "green", "violet", "lawngreen", "red")
# print(colors.count("green")) # Output: 1
# print(colors.count("red")) # Output: 2

#! *********** Example 2 *********** index() method
# The index() method returns the index of the first occurrence of the specified value.
print(colors.index("green"))  # Output: 2
print(colors.index("red"))  # Output: 0
# If the value is not found, the index() method will raise an error.
# print(colors.index("black")) # ValueError: tuple.index(x): x not in tuple
