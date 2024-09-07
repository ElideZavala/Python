# --------------------------------------------------------------------------------
#! Introduction to Closure

# Nested function
# nonlocal Variables

# ? Example 1 >>> a nested function
# def person(address):

#     def john():
#         print(address)

#     john()


# person("New York")


# ? Example 2 >>> a nonlocal variable modification
# def outer():
#     number = 85

#     def inner():
#         nonlocal number  # ! nonlocal keyword is used to modify the variable of the enclosing scope

#         number = 95

#         print("Inner Function:", number)

#     inner()

#     print("Outer Function", number)


# outer()


# ? Example 3 >>> defining a closure
# def person(address):

#     def john():
#         print(address)

#     return john


# john_address = person("USA")

# del person  # ? deleting the original/enclosing scope

# john_address() # USA

# # ! closure is a function object that has access to variables in its enclosing scope, even after the scope has closed
# ? Example 4 >>> deleting the original/enclosing scope

def person(address):

    def john():
        print(address)

    return john


john_address = person("USA")

del person  # ? deleting the original/enclosing scope

john_address()  # USA

# ! closure is a function object that has access to variables in its enclosing scope, even after the scope has closed
