# -----------------------------------------------------------------------------------------------------------------
# The Bad Side of Raising Exceptions

from timeit import timeit

print("******************* Example 19 *********************")

# test_run1 = """
# def calculate_age(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less")

#     return 10 / age


# try:
#     calculate_age(15)
# except ValueError as error:
#     print(error)

# """

# print("Test 1:", timeit(test_run1, number=1000000))


print("******************* Example 20 *********************")

test_run2 = """

def calculate_age(age):
    if age <= 0:
        return None

    return 10 / age

result = calculate_age(0)

if result == None:
    pass
"""

print("Test 2:", timeit(test_run2, number=10000))
