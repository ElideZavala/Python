# ----------------------------------------------------------------------------------------
#! Inheritance !#

# Inheritance is a way to form new classes using classes that have already been defined.

# ? method inheritance
print("******************* Example 34 *********************")


# class John:
#     def sing(self):
#         print("John is singing")

#     def run(self):
#         print("Running")


# class Jane:
#     def since(self):
#         print("Singing")

#     def jog(self):
#         print("Jogging")

# # define a parent/base class
# class Person:
#     def sing(self):
#         print("Singing")


# class John(Person):  # John inherits from Person
#     def sing(self):
#         print("John is singing")


# class Jane(Person):  # Jane inherits from Person
#     def jog(self):
#         print("Jogging")


# julieta = Jane()
# julieta.sing()  # Singing
# julieta.jog()  # Jogging

# ? attribute inheritance
print("******************* Example 35 *********************")


# class Person:
#     def __init__(self):
#         self.employed = True

#     def sing(self):
#         print("Singing")

# # sub-chid-derived class


# class John(Person):
#     def run(self):
#         print("Running")


# class Jane(Person):
#     def jog(self):
#         print("Jogging")


# runner = John()
# runner.sing()  # Singing

# jogger = Jane()
# jogger.sing()  # Singing

# Ambas clases heredan los atributo de la clase Person
#! attribute inheritance
print("******************* Example 35 *********************")


class Person:
    def __init__(self):
        self.employed = True

        def sing(self):
            print("Singing")


class John(Person):
    def run(self):
        print("Running")


class Jane(Person):
    def jog(self):
        print("Jogging")


runner = John()
print("🐛 ", runner.employed)  # True
