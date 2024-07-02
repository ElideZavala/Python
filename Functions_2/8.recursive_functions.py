# ----------------------------------------------------------------------------------------------
# ? Recursive Functions

#!~!~!~!~!~!~ Example 21 !~!~!~!~!~!~
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


print("🐛 ", factorial(3))
# in de above function, the function calls itself. This is called recursion. It is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
