# --------------------------------------------------------------------------------------------------------
# --------------------------------**## List Comprehension Part 2 ##**-------------------------------------

products = [
    ("Cup", 5),
    ("Plate", 10),
    ("Spoon", 3),
    ("Fork", 7),
    ("Knife", 8)
]

numbers = [1, 5, 32, 124, 70, 854, 2356, 6589, 62, 8, 19, 999, 321]

# ! ************ Example 41 ************ Single Condition
# items = [item[1] for item in products if item[1] >= 5]
# print(items) # [5, 10, 7, 8] # Solo los productos con precio mayor o igual a 5

# # traernos los nombres de los productos que tengan cinco letras
# items = [item[0] for item in products if len(item[0]) == 5]

# ! ************ Example 42 ************ Two Conditions
item = [item for item in numbers if item % 2 == 0]
print(item)  # [32, 124, 70, 854, 2356, 62, 8] # Solo los números pares

modified_numbers = [num if num > 100 else num / 2 for num in numbers]
# [0.5, 2.5, 16.0, 62.0, 35.0, 854, 2356, 6589, 62, 4.0, 19, 999, 321]
modified_numbers = [num if num < 100 else num / 2 for num in numbers]
print(modified_numbers)
# nos traeremos los num que sean mayores a 100 y si no lo son los   dividiremos entre 2
