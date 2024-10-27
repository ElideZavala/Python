# --------------------------------------------------------------------------
# Raising Exceptions

#! Raising a nexceptions
print("******************* Example 17 *********************")


# def calculate_age(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less")

#     return 10 / age


# print(calculate_age(20))

#! raising an exception and handling it
print("******************* Example 18 *********************")


def calculate_age(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")

    return 10 / age


try:
    calculate_age(15)
except ValueError as error:
    print(error)
