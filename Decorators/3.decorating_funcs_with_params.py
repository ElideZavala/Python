# --------------------------------------------------------------
#! Decorating Functions with Parameters

# * Example 6 >>>>>>> function with parameters
def operation(func):

    def inner(x, y):
        print(f"{x} / {y} =")

        if y == 0:
            print("cannot divide by sero")
            return

        return func(x, y)

    return inner


@operation
def divide(x, y):
    print(x / y)
# print(operation(10, 20))
# print(operation(101, 32))


# to use a decorator
divide(2, 5)  # 0.4
print("🐛 ", )
divide(20, 5)  # 4.0
print("🐛 ", )
divide(790, 0)  # cannot divide by zero
