# ----------------- Program Task Description

import math
# Write a program that takes a number from the user, calculates and displays the square root of that number.
number = int(input("Escribe un numero = "))

# divmod: nos regresa el numero por el cual se divide y su decimal mas cercano
# nummd = divmod(33, 8)

# raiz_cuadrada = number ** 0.5 # primera forma
raiz_cuadrada = math.sqrt(number) # segunda forma
print(f"La raiz cuadrada de {number} es {raiz_cuadrada}") 
print("vuelve pronto")


