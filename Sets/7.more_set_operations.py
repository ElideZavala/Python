# ----------------------------------------------------------------------------
# ----------------------**## More Set Operations ##**-------------------------

#! **************** Example 28 **************** Membership Test
numers = {1, 2, 3, 4}
print(1 in numers)  # Output: True
print(5 in numers)  # Output: False
print(4 in numers)  # Output: True
print("a" in numers)  # Output: False

# The in operator is used to check if an element is present in a set. It returns True if the element is present, otherwise it returns False.
#! **************** Example 29 **************** Iterating Through a Set
for num in numers:
    print(num)
    print("number", num)
