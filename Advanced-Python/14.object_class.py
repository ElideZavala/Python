class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    def run(self):
        print("Running")


runner = John()
print(isinstance(runner, John))   # True
print(isinstance(runner, Person))  # True
# con isinstance() podemos verificar si un objeto es una instancia de una clase

print(isinstance(Person, object))   # True
# Todas las clases en Python heredan de la clase object

base_object = object()
print(isinstance(base_object, object))  # True

print(isinstance(John, object))  # True
