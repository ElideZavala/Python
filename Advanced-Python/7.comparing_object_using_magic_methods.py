# --------------------------------------------------------------------------------------------
# Comparing Objects Using Magic Methods

#! Comparing Objects
print("******************* Example 13 *********************")


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

# con _gt_ podemos obtener el mayor de los dos objetos


test = Robot(1, 2)
other_test = Robot(4.015, 9.2345)

# print(test == other_test)  # True
# print(id(test))  # 140070950522176
# print(id(other_test))  # 140070950522240

# print(test > other_test)  # True
# print(other_test > test)  # False
print(test < other_test)  # True


# No son iguales por que ocupan diferentes espacios en memoria

#! __eq__ method
print("******************* Example 14 *********************")

#! __gt__ method
print("******************* Example 15 *********************")
