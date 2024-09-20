# -----------------------------------------------------------------------------------------------------------
# ? (*args) & (**kwargs)

# *args: It is used to pass a variable number of non-keyworded arguments list to a function.
#! <<<< Ejemplo 7 >>>> *args
# def multiply(func):

#     def digits(*args):

#         func(*args)

#     return digits


# @multiply
# def operation(x, y, z):
#     print(x * y * z)

# operation(2, 3, 4)
#! <<<< Ejemplo 8 >>>> *args
# def do_arithmetic(func):

#     def number(*numbers):

#         func(*numbers)

#     return number

# @do_arithmetic
# def operation(x, y, z, a, b, c):
#     print((a + b) + z + (x * y) / c)

# operation(100, 200, 300, 400, 500, 600)
#! <<<< Ejemplo 9 >>>> *kwargs
def do_arithmetic(func):

    def number(**kwargs):

        func(**kwargs)

    return number


@do_arithmetic
def operation(**numbers):
    total = 0
    for number in numbers:
        total += numbers[number]
        print(number + ":", numbers[number])

    print(f"total:", total)


operation(x=100, y=200, z=300, a=400, b=500, c=600)
# x: 100
# y: 200
# z: 300
# a: 400
# b: 500
# c: 600
# total: 2100
