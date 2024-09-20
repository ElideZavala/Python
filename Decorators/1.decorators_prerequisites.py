# ----------------------------------------------------------------------------
# ! Decorators Prerequisites #

# ? >>>>> Example 1 <<<<< Functions with different names
# def name1(name):
#     print(name)


# name1("John")
# name2 = name1
# name2("Elide")

# print(id(name1("Jose")))
# print(id(name2("Mauricio")))

# Como podemos ver en el ejemplo anterior, las funciones name1 y name2 son iguales, ya que ambas apuntan a la misma dirección de memoria, por lo que si modificamos una, la otra también se verá afectad, el id de ambas funciones es el mismo por lo tanto ocupan el mismo espacio en memoria.

# ? >>>>> Example 2 <<<<< higher order functions
# def increment(x):
#     return x + 1


# def decrement(x):
#     return x - 1


# def operation(result, x):
# output = result(x)

# return output


# number_inc = operation(increment, 50)
# number_dec = operation(decrement, 10)

# print("🐛 ", number_inc)  # 51
# print("🐛 ", number_dec)  # 9
# ? >>>>> Example 3 <<<<< fuction returning function
def operation():

    def increment():
        print("The number has been added")

    return increment


# number_inc = operation()
# number_inc()
operation()()

# Esto es un ejemplo de una función que retorna otra función, en este caso la función increment() es retornada por la función operation(), por lo que podemos llamar a la función increment() de la siguiente manera operation()().
# Esto es condiderado como una mal práctica, ya que no es recomendable tener funciones anidadas, ya que esto puede hacer que el código sea más difícil de leer y mantener.
