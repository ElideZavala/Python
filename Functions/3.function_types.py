# --------------------------------------------------
# ---------- **## Function Types ##** --------------

# 1- Functions that perform a task
# 2- Functions that calculate and return a value


# ! ************ Example 6 ************
def facebook(name, status):
    return f"{name} is {status}"


user1_status = facebook("Josevo", "online")
user2_status = facebook("Emanuel", "offline")

print(user1_status)
print(user2_status)

# ! ************ Example 7 ************


def multiply(number, by):
    return number * by


print(multiply(2, 3))
# podemos cambiar el orden de los argumentos y aun asi funcionara
print(multiply(by=3, number=2))
print(multiply(2.3, 3.4))
