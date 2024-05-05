# --------------------- #
""" String Methods """
# --------------------- #

# 1- len()
# len nos permite saber la longitud de un string
address = "Tabasco"
print(len(address))

# [] notation
# Nos permite acceder a un caracter en especifico
print('------------------------------------')
print(address[0])
print(address[6])
print(address[-1])
print(address[-4])

# [ : ] notation
# Nos permite acceder a un rango de caracteres
print('------------------------------------')
print(address[0:3])  # [start:stop] # Output = Tab
print(address[-7:-1])  # Output = Tabasc
print(address[0:])  # Output = Tabasco
print(address[:7])  # Output = Tabasco
print(address[:])   # Output = Tabasco

country = "USA"
city = "New york"
full_address = country + ", " + city

# 4- Concatenation ->>>> Formatted Strigs
full_address = f"{country}, {city}"  # Output = USA, New york
print(full_address, '2')

# 5- upper()
# Nos permite convertir un string a mayusculas
print('------------------------------------')
print(full_address.upper())
print(city[0] + city[1].upper() + city[2:7] + city[7].upper())

# 6- lower()
# Nos permite convertir un string a minusculas
print('------------------------------------')
print(city.lower())

# 7- title()
# Nos permite convertir un string a titulo
print('------------------------------------')
print(full_address.title())

# 8- strip()
# Nos permite eliminar espacios en blanco
print('------------------------------------')
job = "     Developer     "
print(job.strip())  # Elimina espacios en blanco a la derecha y a la izquierda
print(job.rstrip())  # Elimina espacios en blanco a la derecha
print(job.lstrip())  # Elimina espacios en blanco a la izquierda

# 9- find()
# Nos permite encontrar un caracter o una palabra en un string
# Si no encuentra el caracter o la palabra, regresa -1
print('------------------------------------')
print(address.find("o"))
print(address.find("a"))
print(address.find("r"))  # Regresa -1
print(address.find("T"))

# 10- replace()
# Nos permite reemplazar un caracter o una palabra en un string
print('------------------------------------')
print(address.replace("a", "u"))
print(address.replace("Tabasco", "Mexico"))

# 11- in operator
# Nos permite saber si un caracter o una palabra esta en un string
# Regresa un booleano
print('------------------------------------')
print("a" in city)
print("york" in city)

# 12- not in operator
# Nos permite saber si un caracter o una palabra no esta en un string
# Regresa un booleano
print('------------------------------------')
print("a" not in city)
print("york" not in city)
