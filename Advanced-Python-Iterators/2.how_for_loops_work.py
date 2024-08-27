# ----------------------------------------------------------------------
# How For Loops Work in Python

#! Example 3  the working of a for loop
numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

iterable_obj = iter(numbers)

# infinite while loop
while True:
    try:
        # get the next item
        element = next(iterable_obj)

        # do something with the element
        print(f"Element: { element }")
    except StopIteration:
        break

# StopIteration para la iteración cuando el iterable se agota y no hay más elementos para iterar.
# break para salir del bucle while.
