# --------------------------------------------------------------------
# ---------- **## Function Parameters and Arguments ##** -------------

# **********______ Ejemplo 5 ______**********
def arithmetic_operations(x, y):
    print(f"{x} * {y} = {x * y}")   # Multiplicacion
    print(f"{x} / {y} = {x / y}")   # Division
    print(f"{x} + {y} = {x + y}")   # Suma
    print(f"{x} - {y} = {x - y}")   # Resta


# arithmetic_operations(10, 5)
# arithmetic_operations(112, 32)
# arithmetic_operations(301, 201)

# **********______ Ejemplo 6 ______**********
def legal_age(name, age, allowed_age):
    if age >= allowed_age:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")


legal_age("Josevo", 10, 18)  # Josevo is not allowed to drive
legal_age("Manuela", 20, 18)  # Manuela is allowed to drive
legal_age("Lorenzo", 18, 21)  # Lorenzo is not allowed to drive
