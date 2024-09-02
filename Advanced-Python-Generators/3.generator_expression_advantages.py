# ------------------------------------------------------------------------------------------------------------------
# ! Generator Expressions Advantages

# ? 1 Memory Efficient
# ? 2 Ease of Impementation
# ? 3 Representing Inifinite Stream
# ? 4 Pipelining Generators

# * Example 5 >> Ease of Implementation
# def number_power(maxi_num):
#     n = 0
#     while n < maxi_num:  # miestras n sea menor que el numero maximo
#         yield 2 ** n  # 2 elevado a la n
#         n += 1  # incrementamos n


# # Using Generator Expression
# numers = number_power(5)
# print(next(numers)) # 2^0 = 1
# print(next(numers)) # 2^1 = 2
# print(next(numers)) # 2^2 = 4
# print(next(numers)) # 2^3 = 8
# print(next(numers)) # 2^4 = 16
# print(next(numers))  # StopIteration

# * Example 6 >> Representing Infinite Stream
# def even_nums():
#     n = 0
#     while True:
#         yield n
#         n + 2


# all_even = even_nums()
# print(next(all_even))  # 0
# print(next(all_even))  # 2
# print(next(all_even))  # 4
# print(next(all_even))  # 6


# * Example 7 >> Pipelining Generators
# Fib Num Series ->>> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def fibinacci_numbers(nums):
    x, y = 0, 1  # x = 0, y = 1

    for _ in range(nums):
        x, y = y, x + y  # x = y, y = x + y

        yield x  # return x

# fib_nums = fibinacci_numbers(10)
# print(next(fib_nums)) # 1
# print(next(fib_nums)) # 1
# print(next(fib_nums)) # 2

# for num in fib_nums:
    # print(num) # 3, 5, 8, 13, 21, 34, 55


def square(nums):
    for num in nums:
        yield num ** 2


sqrt_nums = square(fibinacci_numbers(10))
print(next(sqrt_nums))  # 1
print(next(sqrt_nums))  # 1
print(next(sqrt_nums))  # 4
print(next(sqrt_nums))  # 9
print(next(sqrt_nums))  # 25
print(next(sqrt_nums))  # 64
print(next(sqrt_nums))  # 169
print(next(sqrt_nums))  # 441
print(next(sqrt_nums))  # 1156
print(next(sqrt_nums))  # 3025


# convinamos las dos funciones, square y fibinacci_numbers para obtener el cuadrado de los numeros


def cube(nums):
    for num in nums:
        yield num ** 3
