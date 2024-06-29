# -----------------------------------------------------------------------------------------------------------
# ? --- Zip Functions ---

#! Example 9
# numbers_list = [1, 2, 3]
# names_list = ["Adrianna", "Cecile", "Darcey"]

# No iterables are passed
# result = zip()

# Converting the iterator to a list
# result_list = list(result)
# print(result_list)  # []

# Two iterables are passed
# result = zip(numbers_list, names_list)

# Converting the iterator to a list
# result_list = set(result)
# print(result_list)  # {(1, 'Adrianna'), (2, 'Cecile'), (3, 'Darcey')}

#! ************** Example 10 ************** different number of iterables
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names_list = ["Adrianna", "Cecile", "Darcey"]
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX')

# result = zip(numbers_list, numbers_tuple)
# print("🐛 ", list(result)) # Output   [(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE'), (6, 'SIX')]

# the funtion not working because the number of elements in the iterables are different so the zip function will stop at the shortest iterable

# Converting to set
# result_set = set(result)
# {(1, 'ONE'), (2, 'TWO'), (3, 'THREE')}
# print(result_set)
# in set the order of the elements is not guaranteed because the set is unordered collection of elements

# result = zip(numbers_list, names_list, numbers_tuple)

# Converting to list
# result_list = list(result)
# [(1, 'Adrianna', 'ONE'), (2, 'Cecile', 'TWO'), (3, 'Darcey', 'THREE')]
# print(result_list)

# in this case the zip function with list only return the elements that are in the shortest iterable which is names_list in this case and the rest of the elements are ignored

print("****************** Example 11 **********************")
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)  # [('x', 3), ('y', 4), ('z', 5)]

unzipped_coordinates, unzipped_values = zip(*result_list)
print(unzipped_coordinates)  # ('x', 'y', 'z')
print(unzipped_values)  # (3, 4, 5)

# the zip function can be used to unzip the zipped elements by using the * operator to unpack the zipped elements
