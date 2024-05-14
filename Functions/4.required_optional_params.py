# ------------------------------------------------------------------------------------------------
# ? -------------**## Required and Optional Parameters in Python Functions ##**---------------------

# ! ************ Example 8 ************
# def working_condition(device, status="working"):
#     return f"The {device} is {status}."


# print(working_condition("Drill Press")) # el status por defecto es "working" por lo que no es necesario pasarlo
# print(working_condition("Welding Maching", "broken")) # si queremos cambiar el status, lo pasamos como argumento

# ! ************ Example 9 ************
def subtract(x, z, y=15):
    return x - y - z


print(subtract(20, 5))  # y toma el valor por defecto
print(subtract(20, 5, 10))  # y toma el valor que le pasamos como argumento
