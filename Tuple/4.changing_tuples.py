# ---------------------------------------------------------------------------------------
# -------------------------------- **## 4. Changing Tuples ** ---------------------------

#! ************** Example 11 **************
numbers = (1, 2, 3, [5, 6, 7, 8])
# numbers[0] = 4  # TypeError: 'tuple' object does not support item assignment

# The above code will raise an error because tuples are immutable, and you cannot change the value of an element in a tuple. However, you can change the value of an element in a list that is inside a tuple.

# print(numbers)  # Output: (1, 2, 3, [5, 6, 7, 8])
# numbers[3][2] = 111
# print(numbers)  # Output: (1, 2, 3, [5, 6, 111, 8])

# In the above code, we have changed the value of the third element of the list inside the tuple numbers. The value of the tuple numbers is now (1, 2, 3, [5, 6, 111, 8]).

#! ************** Example 12 ************** reassigning the tuple

# numers = (222, 333, 444)
# print(numers)  # Output: (222, 333, 444)k

# Equal puting the same values in a new tuple and reassigning it to the old tuple

#! ************** Example 13 ************** repeating a tuple items
# print(("Movie", ) * 5)  # Output: ('Movie', 'Movie', 'Movie', 'Movie', 'Movie')

# In the above code, we have repeated the tuple ("Movie",) five times. The output will be ('Movie', 'Movie', 'Movie', 'Movie', 'Movie').

#! ************** Example 14 ************** concatenating tuples
letters = ("e", "l", "i", "d", "e")
mixed = numbers + letters
# print(mixed)  # Output: (1, 2, 3, [5, 6, 111, 8], 'e', 'l', 'i', 'd', 'e')

# In the above code, we have concatenated the tuples numbers and letters. The output will be (1, 2, 3, [5, 6, 111, 8], 'e', 'l', 'i', 'd', 'e').

#! ************** Example 15 ************** deleting a tuple
del mixed
print(mixed)  # Output: NameError: name 'mixed' is not defined

# In the above code, we have deleted the tuple mixed. The output will be NameError: name 'mixed' is not defined.
