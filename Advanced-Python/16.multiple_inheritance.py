# ------------------------------------------------------------------
# Multiple Inheritance:

#! Bad Multiple Inheritance
print("******************** Example 39 ********************")


# class Person:
#     def sport_status(self):
#         print("Runner")


# class John:
#     def sport_status(self):
#         print("jogger")


# class Jane(Person, John):
#     pass


# jane = Jane()
# jane.sport_status()

# jane = Jane()
#! Goof Multiple Inheritance
print("******************** Example 40 ********************")


class Person:
    def runner(self):
        print("Runner")


class John:
    def jogger(self):
        print("jogger")


class Jane(Person, John):
    pass


jane = Jane()
jane.runner()  # Runner
jane.jogger()  # jogger
