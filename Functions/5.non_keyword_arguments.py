# -----------------------------------------------------------------
# ? ----------------**## Non-Keyword Arguments ##**----------------

# ! *********** Ejemplo 9 ************
# def sum(x, y):
#     return x + y


def num(*numbers):
    return numbers  # ? Devuelve una tupla

# print(num(10, 21, 65, 112, 555, 666)) #  (10, 21, 65, 112, 555, 666)


def subtract(*nums):
    number = 100
    for x in nums:
        number = number - x
    return number  # debe ir ahi porqq si no se va a restar 100 - 0


print(subtract(10, 20, 30, 40, 50))
