# --------------------------------------------------------------------------------------------------------
# ---------------------------------**## Accessing Tuple Elements ##**-------------------------------------

#! ************** Example 8 **************
mixed = (False, 3.14159, "Python", ["Web", "Mobile"], 45)
# print(mixed[0])  # Output: False
# print(mixed[1])  # Output: 3.14159
# print(mixed[2])  # Output: Python
# print(mixed[3])  # Output: ['Web', 'Mobile']
# print(mixed[4])  # Output: 45
# print(mixed[5])  # Output: IndexError: tuple index out of range
# # mixed[0] = True  # TypeError: 'tuple' object does not support item assignment
# print(mixed["a"]) # Output: TypeError: tuple indices must be integers or slices, not str

#! ************** Example 9 ************** Negative Indexing
# print(mixed[-1])  # Output: 45 (last element)
# print(mixed[-2])  # Output: ['Web', 'Mobile'] (second last element)
# print(mixed[-3])  # Output: Python (third last element)
# print(mixed[-4])  # Output: 3.14159 (fourth last element)
# print(mixed[-5])  # Output: False (fifth last element)

#! ************** Example 10 ************** Slicing
print(mixed[0:2]) # Output: (False, 3.14159) (from index 0 to 2)
print(mixed[1:4]) # Output: (3.14159, 'Python', ['Web', 'Mobile']) (from index 1 to 4)
print(mixed[:3])  # Output: (False, 3.14159, 'Python') (from index 0 to 3)
print(mixed[2:])  # Output: ('Python', ['Web', 'Mobile'], 45) (from index 2 to last)
print(mixed[:])   # Output: (False, 3.14159, 'Python', ['Web', 'Mobile'], 45) (from index 0 to last)
print(mixed[::2]) # Output: (False, 'Python', 45) (every 2nd element)
print(mixed[::-1]) # Output: (45, ['Web', 'Mobile'], 'Python', 3.14159, False) (reverse the tuple)
print(mixed[::-2]) # Output: (45, 'Python', False) (reverse the tuple and get every 2nd element)
