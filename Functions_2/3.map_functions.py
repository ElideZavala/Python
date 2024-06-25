# --------------------------------------------------------------------
# ? -------------------------- Map Functions --------------------------

#! Example 6

# Iterable
# numbers = (1, 2, 3, 4, 5)

# Function


# def calculate_square(n):
#     return n * n


# Map Function
# variable = map(function, iterable)
# result = map(calculate_square, numbers)

# converting a map object to set
# mum_square = set(result)
# print(mum_square)  # Output: {1, 4, 9, 16, 25}
# print(type(mum_square))  # Output: <class 'set'>

# converting a map object to list
# mum_square = list(result)
# print(mum_square)  # Output: {1, 4, 9, 16, 25}
# print(type(mum_square))  # Output: <class 'set'>

# converting a map object to tuple
# mum_square = tuple(result)
# print(mum_square)  # Output: {1, 4, 9, 16, 25}
# print(type(mum_square))  # Output: <class 'set'>

#! Example 7
# numbers = (1, 2, 3, 4, 5)
# letters = ["a", "b", "c"]

# result = map(lambda x: (x * x) / 2, numbers)

# converting a map object to set
# character = set(result)
# print(character)  # Output: {0.5, 2.0, 4.5, 8.0, 12.5}
# print(type(character))  # Output: <class 'set'>

# converting a map object to list
# character = list(result)
# print(character)  # Output: [0.5, 2.0, 4.5, 8.0, 12.5]
# print(type(character))b  # Output: <class 'list'>

# converting a map object to tuple
# character = tuple(result)
# print(character)  # Output: (0.5, 2.0, 4.5, 8.0, 12.5)
# print(type(character))  # Output: <class 'tuple'>

#! Example 8 - Passing Multiple Iterables to the map function

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [7, 8]

result = map(lambda n1, n2: n1 + n2, numbers1, numbers2)
print(tuple(result))  # Output: (8, 10)
