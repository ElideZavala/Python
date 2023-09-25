import math
# --------------------- #
""" Number Methods & Operations """
# --------------------- #

# ---------- Arithmetic Operations ----------- #
# print(23 + 12)  # 35
# print(50 - 10)  # 11
# print(50 * 10)  # 500
# print(25 / 10)  # 2.5 division
# print(50 // 10)  # 5 division entera
# print(50 % 10)  # 0 resto de una division
# print(2 ** 5)  # 32 potencia

# -------- Augmented Assignment Operator --------- #
# +=, -=, *=, /=, //=, %=, **=

# numer = 10
# # numer = numer + 5
# # numer += 5
# # numer *= 5
# # numer /= 5
# print(numer)  # 15

# ---------- round() ----------- #
# los numeros se redondean a la unidad mas cercana
# print(round(3.131416))
# print(round(11.356))
# print(round(526.855))

# ---------- abs() ----------- #
# devuelve el valor absoluto de un numero
# print(abs(-20))
# print(abs(20))
# print(abs(-30.5))

# ---------- math module ----------- #
# import math
# https://docs.python.org/3/library/math.html

print(math.acos(0.5))

# obtiene el punto negativo de un numero
print(math.sin(180))
# obtiene el coseno de un numero
print(math.cos(0))
# obtiene la tangente de un numero
print(math.tan(0))
# obtiene el valor de pi
print(math.pi)
# obtiene el valor de e
print(math.e)
# obtiene el valor infinito
print(math.inf)
# obtiene el valor NaN
print(math.nan)
# obtiene el logaritmo natural de un numero
print(math.log(math.e))
# obtiene el logaritmo de un numero en base 10
print(math.log(100, 10))
# obtiene el logaritmo de un numero en base 10
print(math.log10(100))
# obtiene el logaritmo de un numero en base 2
print(math.log2(100))
# obtiene la raiz cuadrada de un numero
print(math.sqrt(100))

print("--------- Redonceo ---------")
# obtiene la parte entera de un numero, redondea hacia abajo
print(math.floor(3.999))

# obtiene la parte entera de un numero, redondea hacia arriba
print(math.ceil(3.0001))

# obtiene la parte entera de un numero, redondea hacia abajo
print(math.floor(3.999))

# obtiene la parte entera de un numero, redondea hacia abajo pero a difererencia de floor, no redondea hacia arriba
print(math.trunc(3.999))

print("------------------")

# obtiene el factorial de un numero
print(math.factorial(5))
# obtiene la potencia de un numero
print(math.pow(2, 5))
# obtiene los grados de un numero
print(math.degrees(math.pi))
# obtiene los radianes de un numero
print(math.radians(180))
# obtiene el seno de un numero
print(math.sin(math.radians(90)))
# obtiene la hipotenusa de un numero
print(math.hypot(3, 4))
# obtiene los grados de un numero
print(math.degrees(math.atan2(4, 3)))
# obtiene los grados de un numero
print(math.degrees(math.atan2(3, 4)))

# print(math.tan(0))
# print(math.pi)
# print(math.e)
# print(math.inf)
# print(math.nan)
# print(math.log(math.e))
# print(math.log(100, 10))
# print(math.log10(100))
# print(math.log2(100))
# print(math.sqrt(100))
# print(math.floor(3.999))
# print(math.ceil(3.0001))
# print(math.floor(3.999))
# print(math.trunc(3.999))
# print(math.factorial(5))
# print(math.pow(2, 5))
# print(math.degrees(math.pi))
# print(math.radians(180))
# print(math.sin(math.radians(90)))
# print(math.hypot(3, 4))
# print(math.degrees(math.atan2(4, 3)))
# print(math.degrees(math.atan2(3, 4)))
# print(math.degrees(math.atan(1)))
# print(math.degrees(math.atan(0.5)))
