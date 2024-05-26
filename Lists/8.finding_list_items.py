# ------------------------------------------------------------------------------------
# --------------------------**## Finding List Items ##**------------------------------

fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# # ! ************ Example 29 ************
# print(fruits.index('banana'))  # 1 # Returns the index of the first element with the specified value.

# print(fruits.index('melon'))  # 5

# # print(fruits.index('sandia'))  # ValueError: 'sandia' is not in list
# # ! ************ Example 30 ************
# if "sandia" in fruits:
#     print(fruits.index('sandia'))
# else:
#     print("sandia is not in the list")

# ! ************ Example 31 ************
# print(fruits.count('apple'))  # 1 # Returns the number of elements with the specified value.
# print(fruits.count('kiwi'))  # 1
# print(fruits.count('sandia'))  # 0
numbers = [1, 2, 1, 1, 1, 1, 1] * 5
print(numbers.count(1))  # 30
