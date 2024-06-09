# -------------------------------------------------------------------------------------------------
# ---------------------------**## Dictionary Comprehension ##**------------------------------------

#! *************** Ejemplo 26 ***************
# coordinates = {}
# for x in range(5):
#     coordinates[x] = (((x * 5) / 2) + 12) - (2.4 / 1.2) * 6
# x = 0, 1, 2, 3, 4 que se asignan a la clave del diccionario
# (((x * 5) / 2) + 12) - (2.4 / 1.2) * 6 es el valor de cada clave
# print(coordinates) # {0: 12.0, 1: 14.0, 2: 16.0, 3: 18.0, 4: 20.0}

# coordinates = {x: (((x * 5) / 2) + 12) - (2.4 / 1.2) * 6 for x in range(5)}
# print(coordinates) # {0: 12.0, 1: 14.0, 2: 16.0, 3: 18.0, 4: 20.0}

#! *************** Ejemplo 27 ***************
# items prices in Dollars
# old_price = {"milk": 1.02, "coffee": 2.5, "bread": 1.89}

# dollar_to_pound = 0.76
# new_price = {item: value * dollar_to_pound for (item, value) in old_price.items()}

# item: value * dollar_to_pound es el valor de cada clave
# print({item:value for (item, value)in old_price.items()})

# lo que hacemos es multiplicar el valor de cada clave por el valor de la variable dollar_to_pound, con items() obtenemos las claves y valores del diccionario

# print(new_price) # {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.4344}
#! *************** Ejemplo 28 ***************
original_dict = {"jack": 38, "Lincoln": 48,
                 "Theodore": 33, "Cecile": 21, "Tony": 18}

event_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}

print(event_dict)
