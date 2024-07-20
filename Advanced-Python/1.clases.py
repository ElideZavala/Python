# --------------------------------------------------------------------------------------------
# ----------------------------- CLASES Y OBJETOS EN PYTHON -----------------------------------

"""
Object
1.- attributes
3.- behavior

# A class is a blueprint for creating objects
"""


class Robot:
    pass


"""
*-*-*-*-*-*-*-*-*-*-* INSTANCIAS DE CLASES *-*-*-*-*-*-*-*-*-*-*
"""

robot_obj = Robot()

# print(robot_obj) # <__main__.Robot object at 0x7f8b1f3b3d30>
# print(type(robot_obj)) # <class '__main__.Robot'>

# class of str for creating strings
name = "Elide Zavala Vinagre"
print(type(name))  # <class 'str'>

# class of int for creating intergers
x = 25
print(type(x))  # <class 'int'>

# clase of float for creating floating point numbers
y = 3.5
print(type(y))  # <class 'float'>

# class of bool for creating booleans
z = True
print(type(z))  # <class 'bool'>

# class of str for creating lists
my_list = [1, 2, 3]
print(type(my_list))  # <class 'list'>

# class of dict for creating dicts
my_info = {
    "name": "Muslim",
    "last name": "Helalee"
}

print(type(my_info))  # <class 'dict'>

# class of tuple for creating tuples
my_tuple = (1, 2, 3)
print(type(my_tuple))  # <class 'tuple'>

# class of set for creating sets
my_set = {1, 2, 3}
print(type(my_set))  # <class 'set'>
