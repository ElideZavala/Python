# --------------------------------------------------------------------------------
# * Arrays

from array import array
print("******************* Example 12 ********************")

numbers = array("i", [1, 2, 3])
numbers.append(4)
print("🐛 ", numbers)

# numbers[0] = 2.3 # TypeError: integer argument expected, got float

# in the above code, we are trying to assign a float value to an integer array, which is not allowed in python.
