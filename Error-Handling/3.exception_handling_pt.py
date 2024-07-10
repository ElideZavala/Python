# --------------------------------------------------------------------------------------
# 1. Exception Handling part 2

#! get a ZeroDivisionError
print("******************** Ejercicio 11 ********************")
try:
    age = int(input("Age: "))
    x = 10 / age
except ValueError:
    print("please enter a valid age")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No Error Heres")

#! create a tuple of errors
print("******************** Ejercicio 12 ********************")
try:
    age = int(input("Age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("please enter a valid age")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No Error Heres")
