# ----------------------------------------------------------------
# ----------------**## Method Overriding ##**---------------------

#! overriding
print("******************** Example 37 ********************")


# class Person:
#     def __init__(self):
#         self.employed = True

#     def sing(self):
#         print("Singing")


# class John(Person):
#     # method overriding
#     def __init__(self):
#         self.jogger = True

#     def run(self):
#         print("Running")


# runner = John()
# print(runner.jogger)  # True
# print(runner.employed) # AttributeError: 'John' object has no attribute 'employed'

# ? The error is because the __init__ method of the Person class is not called in the __init__ method of the John class.
#! fixing overriding
print("******************** Example 38 ********************")


class Person:
    def __init__(self):

        print("🐛 Base class", )
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    # method overriding
    def __init__(self):
        super().__init__()
        self.jogger = True

        print("🐛 Sub clase", )

    def run(self):
        print("Running")


runner = John()
print(runner.jogger)  # True
print(runner.employed)  # True
