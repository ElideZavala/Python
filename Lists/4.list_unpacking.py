# --------------------------------------------------------------------------------------
# ---------------------------**## List Unpacking ##**-----------------------------------

# # ! *************** Example 13 ***************

# numbers = [23, 49, 85, 45, 1, 2, 3, 4, 5]
# num1, num2, *other_nums = numbers
# print(num1)  # 23
# print(num2)  # 49
# # [ 85, 45, 1, 2, 3, 4, 5] Impriime el resto de los elementos
# print(other_nums)

# # ! *************** Example 14 ***************
numbers = [23, 49, 85, 45, 1, 2, 3, 4, 5]
# Imprime el primer y ultimo elemento de la lista y el resto de los elementos
num1, num2, *other_nums, num3, num4 = numbers
print(num1)  # 23
print(num2)  # 49
print(num3)  # 4
print(num4)  # 5
print(other_nums)  # [85, 45, 1, 2, 3]
