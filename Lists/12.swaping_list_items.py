# -----------------------------------------------------------------------------------------
# -----------------------------**## Swaping List Items ##**--------------------------------

# ! ********* Example 43 *********
# numbers = [2, 4, 6]

# numbers[0], numbers[1], numbers[2] = numbers[2], numbers[1], numbers[0]

# # lo que estamos haciendo es que estamos asignando los valores de la derecha a la izquierda y viceversa, este método es muy útil para hacer un swap de valores, es decir intercambiar valores de una lista
# print(numbers)  # [6, 4, 2]

# ! ********* Example 44 *********
full_name = ["Elide", "Zavala", "Vinagre"]
full_name[0], full_name[1], full_name[2] = full_name[1], full_name[2], full_name[0]
# quitar corchetes para ver el resultado y ajuntar todo como un string
print(full_name)  # ['Zavala', 'Vinagre', 'Elide']
