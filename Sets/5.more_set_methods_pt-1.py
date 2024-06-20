# -----------------------------------------------------------------------------------------
# -----------------------------**## More Set Methods ##**----------------------------------

#! ************* Example 23 *************
# numbers = {101, 202, 303, 404, 505, 606}
# other_numbers = numbers
# print(other_numbers)  # Output: {101, 202, 303, 404, 505, 606}
# print(numbers)  # Output: {101, 202, 303, 404, 505, 606}

# numbers.remove(505)
# print(numbers)  # Output: {101, 202, 303, 404, 606}
# print(other_numbers)  # Output: {101, 202, 303, 404, 606}

# in some cases, we want to create a copy of a set, not a reference to the original set.
# we can use the copy() method to create a copy of a set.

# other_numbers.discard(505)
# print(numbers)  # Output: {101, 202, 303, 404, 606}
# print(other_numbers)  # Output: {101, 202, 303, 404, 606}

# The difference between the remove() and discard() methods is that remove() raises an error if the element is not found in the set, while discard() does not raise an error.

# some_numbers = numbers.copy()
# print(numbers)  # Output: {101, 202, 303, 404, 606}
# print(other_numbers)  # Output: {101, 202, 303, 404, 606}
# print(some_numbers)  # Output: {101, 202, 303, 404, 606}

# some_numbers.add(707)
# print(numbers)  # Output: {101, 202, 303, 404, 606}
# print(other_numbers)  # Output: {101, 202, 303, 404, 606}
# print(some_numbers)  # Output: {101, 202, 303, 404, 606, 707}

# The copy() method creates a shallow copy of the set. This means that the elements of the new set are references to the same objects as the elements of the original set. If the elements are mutable objects, changes to the elements in the new set will affect the elements in the original set.

# print(id(numbers))  # Output: 140071366366784
# print(id(other_numbers))  # Output: 140071366366784
# print(id(some_numbers))  # Output: 140071366366976
#! ********** Example 24 ********** isdisjoint() method
# A = {1, 2, 3, 4}
# B = {5, 6, 7}
# C = {4, 5, 6}
# D = {10, 20, 30, 7}
# print('Are A and B disjoint?', A.isdisjoint(B))  # Output: True
# print('Are A and C disjoint?', A.isdisjoint(C))  # Output: False
# print('Are B and C disjoint?', B.isdisjoint(C))  # Output: False
# print('Are A and D disjoint?', A.isdisjoint(D))  # Output: True
# print('Are B and D disjoint?', B.isdisjoint(D))  # Output: False
# print('Are C and D disjoint?', C.isdisjoint(D))  # Output: True

# The isdisjoint() method returns True if two sets have no elements in common, otherwise it returns False.

#! ********** Example 25 ********** isdisjoint() method with other iterables
A = {'a', 'b', 'c', 'd'}
B = {'b', 'e', 'f'}
C = '5de4'
D = {1: 'a', 2: 'b'}
E = {'a': 1, 'b': 2}
F = ("z", "g", "s")

print('Are A and B disjoint?', A.isdisjoint(B))  # Output: False
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))
print('Are A and F disjoint?', A.isdisjoint(F))
# print('Are C and D disjoint?', C.isdisjoint(D))
