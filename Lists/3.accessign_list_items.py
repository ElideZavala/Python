# --------------------------------------------------------------------------------------------------
# ----------------------------**## Accessing List Items ##**----------------------------------------

# ! ********* Example 9 *********
collection = [28, "M", 12, "H", "Parrot", "Sea Biscuit"]

# remplazamos el valor en la posición 5
# collection[5] = "Python"

print(collection)

# # print(collection[0])  # 28
# # print(collection[1])  # M
# # print(collection[2])  # 12
# # print(collection[3])  # H
# # print(collection[4])  # Parrot

# print(collection[0:2]) # [28, 'M'] # obtenemos los valores de la posición 0 y 1 de la lista, en el 2 se detiene
# print(collection[2:4]) # [12, 'H'] # obtenemos los valores de la posición 2 y 3 de la lista, en el 4 se detiene
# print(collection[4:6]) # ['Parrot', 'Sea Biscuit'] # obtenemos los valores de la posición 4 y 5 de la lista, en el 6 se detiene

# print(collection[:5]) # [28, 'M', 12, 'H', 'Parrot'] # obtenemos los valores de la posición 0 al 4 de la lista

# print(collection[:]) # [28, 'M', 12, 'H', 'Parrot', 'Sea Biscuit'] # obtenemos todos los valores de la lista

# print(collection[::2]) # [28, 12, 'Parrot'] # obtenemos los valores de la lista de 2 en 2

# print(collection[::-1]) # ['Sea Biscuit', 'Parrot', 'H', 12, 'M', 28] # obtenemos los valores de la lista en reversa

# print(collection[1:5:2]) # ['M', 'H'] # obtenemos los valores de la lista de la posición 1 a la 4 de 2 en 2

# print(collection[0:]) # [28, 'M', 12, 'H', 'Parrot', 'Sea Biscuit'] # obtenemos los valores de la lista de la posición 0 hasta el final

# print(collection[:0]) # [] # obtenemos los valores de la lista de la posición 0 hasta la 0
