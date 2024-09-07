# --------------------------------------------------------
# * When to use Clousure

#! Example 5 !#

def number(n):

    def multiply_by(x):
        return x * n

    return multiply_by


three = number(3)
four = number(4)
five = number(5)
string = number("Elide")

# print(three) # <function number.<locals>.multiply_by at 0x7f8b1b3b7d30>
# print(type(three)) # <class 'function'>

# print(three(9))  # 27
# print(four(9))  # 36
# print(five(9))  # 45

print(three.__closure__[0].cell_contents)  # 3
print('-----------------')
# Elide # ! accessing the value of the variable in the enclosing scope
print(string.__closure__[0].cell_contents)
print('-----------------')
print(four.__closure__[0].cell_contents)  # 4
