# -----------------------------------------------------------------------------
#! Generator Expressions

# ? Example 3 creating a generator expression
numbers = [1, 2, 11, 9, 5, 2, 0, 1, -1]

# squaring each term using list comprehension
# sqrt_nums_LC = (x**2 for x in numbers)

# print(next(sqrt_nums_LC)) # 1
# print(next(sqrt_nums_LC)) # 4
# print(next(sqrt_nums_LC)) # 121
# print(next(sqrt_nums_LC)) # 81

# ? Example 4 generator expression as function argument

# obtaining the sum of the squares of the numbers
print(sum(x * 2 for x in numbers))  # 60

# obtaining the maximum of the squares of the numbers
print(max(x ** 2 for x in numbers))  # 144

# obtaining the minimum of the squares of the numbers
print(min(x for x in numbers))  # 0
