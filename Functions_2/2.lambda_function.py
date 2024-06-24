# ------------------------------------------------------------------
# -------------- Anonymus Function (Lambda Function) ---------------

# Lambda functions are small functions usually not more than a line.
# It can have any number of arguments just like a normal function.

# The body of lambda functions is very small and consists of only one expression.
# The result of the expression is the value when the lambda is applied to an argument.
#! Example 3
# Syntax
# lambda arguments: expression
# The expression is executed and the result is returned:
products = [
    ("Product-1", 15),
    ("Product-2", 25),
    ("Product-3", 10),
    ("Product-4", 20),
    ("Product-5", 30),
    ("Product-6", 45),
]

# products.sort(key=lambda product: product[1])
# print(products)

# la key es una funcion que se aplica a cada elemento antes de comparar.
# es product[1] por que

#! Example 4
my_list = [1, 5, 4, 6, 8, 11]
# new_list = filter(lambda x: (x % 2 == 0), my_list)

# print(new_list)
# for num in new_list:
#     print(num)
#     event_nums = list(new_list)
#     print(event_nums)
#     odd_num = list(new_list)
#     print(odd_num)

# odd_num esta vacio por que ya se recorrio la lista y se agotaron los valores,
# si se quiere imprimir los valores de odd_num se debe de volver a recorrer la lista

#! Example 5
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
