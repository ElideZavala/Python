# --------------------------------------------------------------------------------------------------------
# --------------------------------**## List Comprehension Part 1 ##**-------------------------------------

# basic syntax of list an LC
# [expression for item in list]

numbers = [23, 54, 67, 89, 15, 99]
fruits = ["Apple", "Orange", "Banana"]

# ! *********** Example 36 ***********
# numbers2 = [num for num in numbers]
# print(numbers2) # [23, 54, 67, 89, 15, 99]

# Con esto se crea una copia de la lista numbers en numbers2 con la misma referencia
# ! *********** Example 37 ***********
# numbers2 = [num*2 for num in numbers]
# print(numbers2) # [46, 108, 134, 178, 30, 198]
# Con esto se crea una lista con los valores de numbers multiplicados por 2

# ! *********** Example 38 ***********
# numbers2 = [(num / 2) * 5 for num in numbers]
# print(numbers2) # [57.5, 135.0, 167.5, 222.5, 37.5, 247.5]

# Con esto se crea una lista con los valores de numbers divididos entre 2 y multiplicados por 5

# ! *********** Example 39 ***********
# fruits2 = [fruit.lower() for fruit in fruits]
# print(fruits2)  # ['apple', 'orange', 'banana']

# fruits3 = [fruit.upper() for fruit in fruits]
# print(fruits3)  # ['APPLE', 'ORANGE', 'BANANA']

# ! *********** Example 40 ***********
products = [
    ("Cup", 5),
    ("T-shirt", 10),
    ("Jeans", 20),
    ("Shoes", 50),
    ("Hat", 15),
    ("Watch", 100)
]

items = [item for item in products]  # hacemos una copia de la lista products

# obtenemos solo los nombres de los productos
items = [item[0] for item in products]
print(items)

# obtenemos solo los precios de los productos
prices = [item[1] for item in products]
print(prices)
