# -------------------------------------------------------------
# Arithmetic operations using magic methods

# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __sub__(self, other):
#         return f"Coordinates({self.x - other.x}, {self.y - other.y})"


# test = Robot(12, 1)
# other_test = Robot(4.12, 8.45)

# print(test.x)  # 12
# print(test.y)  # 1
# print(other_test.x)  # 4.12
# print(other_test.y)  # 8.45

# print(test - other_test)  # Coordinates(16.12, 9.45)

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __floordiv__(self, other):
        return f"Coordinates({self.x // other.x}, {self.y // other.y})"


test = Robot(10, 20)
other_test = Robot(2, 8)

print(test // other_test)  # Coordinates(5, 2)