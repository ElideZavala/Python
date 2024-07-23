# -------------------------------------------------------------------
# Magic Methods

# Magic methods Reference: https://rszalski.github.io/magicmethods/

# * Magic methods Reference
print("******************** Example 11 ********************")


# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def walk(self):
#         print(f"walking coordinates ({self.x}, {self.y})")


# test = Robot(0.1, 0.5)
# print(test)

# * Converting to a string
print("******************** Example 12********************")


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f"I am magic method with coordinates ({self.x}, {self.y})"

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


test = Robot(0.1, 0.5)
print(test)  # I am magic method with coordinates (0.1, 0.5)
