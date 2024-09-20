# ------------------------------------
#! Introduction to Decorators
# __call__() ->>>>> a decorator
def operation(func):
    def increment():
        print("before the func")

        # the execution of the decrement function
        func()

        print("after the func")

    return increment  # return the function increment

# decorated


@operation
def decrement():
    print("The number has been decremented")


decrement()

# ? @operation is equivalent to decrement = operation(decrement)
# ? The function decrement is passed to the operation function
# ? The operation function returns the increment function
#! @operation == decrement = operation(decrement) == increment
