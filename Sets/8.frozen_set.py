# ---------------------------------------------------------------------------------
# ---------------------------**## Frozen Set ##**----------------------------------

#! ****************** Example 30 ****************** Frozen Set
numbers = frozenset([1, 2, 3, 4, 5, 6])
some_nums = frozenset([3, 4, 5, 6])
print(numbers)  # frozenset({1, 2, 3, 4, 5, 6})
print(type(numbers))  # <class 'frozenset'>

# Frozen set is immutable, so we can't add or remove elements from it, but we can perform set operations on it.

print(numbers.isdisjoint(some_nums))  # False
print(numbers.difference(some_nums))  # frozenset({1, 2})

# with isdisjoint() method, we can check if two sets are disjoint or not.
# with difference() method, we can find the difference between two sets.

#! ****************** Example 31 ****************** Frozen Set
vowels = ('a', 'e', 'i', 'o', 'u')
frozen_vowels = frozenset(vowels)  # frozenset({'a', 'e', 'i', 'o', 'u'})
print(frozen_vowels)  # frozenset({'a', 'e', 'i', 'o', 'u'})

print("Empty Frozen Set", frozenset())  # Empty Frozen Set frozenset()
# AttributeError: 'frozenset' object has no attribute 'add'
print(frozenset().add)
