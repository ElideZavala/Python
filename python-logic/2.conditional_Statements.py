# -------------------------------------------------------------------------------------------------------------------
# Conditional Statements

"""
if (boolean expression):
    execute the statements

"""

# ******************---------------------------- Example ->> Check for a single condition
# temperature = 35
# temperature = 25
temperature = -10

# if temperature > 30:
#     print("es un buen dia para salir a caminar")

# print("It is not part of the if statement")

# ******************---------------------------- Example ->> Check for two condition
# if temperature > 25:
#     print("Awesome")
# else:
#     print("Cold")

# ******************---------------------------- Example ->> Check for multiple conditions
temperature = 25

if temperature >= 35:
    print("Hot")
elif temperature >= 25:
    print("Awesome")
elif temperature <= 20:
    print("Cold")
else:
    print("Undecided")
