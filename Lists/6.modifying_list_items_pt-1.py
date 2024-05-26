# ----------------------------------------------------------------------------------------
# -------------------- **## Modifying List Items Part-1 ##** -----------------------------

numbers = [1, 55, 64, 124, 654]
names = ['John', 'Doe', 'Jane', 'Doe']
fruits = ['Apple', 'Banana', 'Cherry', 'Date']

# # ! ********* Ejemplo 20 ********* append()
# names.append('Elide')  # Add an item to the end of the list
# print(names)

# # ! ********* Ejemplo 21 ********* insert()
# fruits.insert(1, "lemon")  # Add an item at the specified index
# fruits.insert(0, "Peach")  # Add an item at the specified index
# print(fruits)

# # ! ********* Ejemplo 22 ********* pop()
# numbers.pop()  # Remove the last item from the list
# numbers.pop(-1) # Remove the position item from the list is the some as numbers.pop()

# # ! ********* Ejemplo 23 ********* pop(index)
# numbers.pop(1) # Remove the item at the specified index
# print(numbers)

# # ! ********* Ejemplo 24 ********* remove()
# fruits.remove('Banana')  # Remove the first item with the specified value
# print(fruits)

# # ! ********* Ejemplo 25 ********* del
del numbers[0]  # Remove the item at the specified index
print(numbers)

# # ! ********* Ejemplo 26 ********* del start:end
del numbers[1:4]  # Remove the items in the specified range
print(numbers)
