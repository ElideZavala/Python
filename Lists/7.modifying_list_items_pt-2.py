# -------------------------------------------------------------------------------------------------------
# -------------------------------- **## Modifying List Items Part 2 ##** --------------------------------

numbers = [1, 55, 64, 124, 654]
names = ['John', 'Doe', 'Jane', 'Elide']
fruits = ['Apple', 'Banana', 'Cherry', 'Date']

# ! ********* Ejemplo 26 ********* clear()
# print(fruits.clear())  # Remove all items from the list
# output: None

# ! ********* Ejemplo 27 ********* reverse()
names.reverse()  # Reverse the order of the list
# print(names)
# output: ['Elide', 'Jane', 'Doe', 'John']

numbers.reverse()  # Reverse the order of the list
# print(numbers)
# output: [654, 124, 64, 55, 1]

# ! ********* Ejemplo 28 ********* join()
print("".join(names))  # Join the list items
# output: ElideJaneDoeJohn
print(" - ".join(names))  # Join the list items
# output: Elide - Jane - Doe - John
