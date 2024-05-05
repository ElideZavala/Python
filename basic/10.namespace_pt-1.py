# ---------------------------------------------------------------------
# Namespace is a container where names are mapped to objects, mostly
# ***********************______________ Example _______________***********************
number = 1001

# print(id(number))  # 2360400339824
# print(id(1001))  # 2360400339824

# ***********______________ Example _______________***********

a = 2
print("a:", id(a))

a = a + 1
print("a:", id(a)) # esta asociado al numero 3 y no al 2
print("Three:", id(3)) # sera el mismo id que el de a porque a esta asociado al numero 3

b = 2
print("b:", id(b))
print("Two:", id(2))   

# ***********______________ Example _______________***********

something = 12
something = "Jack"
something = ["a", 2, True] # es una lista

# ***********______________ Example _______________***********

def hello():
    print("Hello")

something = hello
something()  # Hello

