# ----------------------------------------------------------------------------------------
# ----------------------**## Tuple Packing and Unpacking **-------------------------------

#! ***************** Example 5 ***************** Tuple Unpacking
# Tuple packing is the process of putting values into a new tuple.
# Tuple packing is also known as tuple creation.
# Tuple packing is done when we want to create a tuple without using parentheses.
# Tuple packing is also used to create a tuple of multiple values.

to_do = "comprar cafe", "leer un libro", "terminar el proyecto"
# print(to_do)  # Output: ('comprar cafe', 'leer un libro', 'terminar el proyecto')
# print(type(to_do))  # Output: <class 'tuple'>
to_do1, to_do2, to_do3 = to_do
# print(to_do1)  # Output: comprar cafe
# print(to_do2)  # Output: leer un libro
# print(to_do3)  # Output: terminar el proyecto

# Tuple unpacking is the process of extracting values from a tuple.
#! ***************** Example 6 ***************** Tuple with 1 element
name = ("Tommy", )
print(name)
print(type(name))  # Output: <class 'tuple'>
