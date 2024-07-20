# --------------------------------------------------
# Instance Attributes VS Class Attributes

# 1. Instance Attributes
# 3. Class Attributes

# Instance Attributes
# print("******************** Example 6 ********************")


# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def walk(self):
#         print(f"walking ({self.x} && {self.y})")


# # 1st instantiation
# test_walk1 = Robot(8.9, 99.7)
# test_walk1.walk()
# print("🐛 ", test_walk1.x)
# print("🐛 ", test_walk1.y)

# # 2nd instantiation
# test_walk2 = Robot(4.5, 6.7)
# test_walk2.walk()

# print("🔥 ", test_walk2.x)
# print("🔥 ", test_walk2.y)

# # diferent Instance attr
# print("******************* Example 7 *********************")
# test_walk1.z = 2.3

# print("🔥 ", test_walk1.z) # 2.3
# print("🐛 ", test_walk2.z) # AttributeError: 'Robot' object has no attribute 'z'

class Robot:

    # a class attribute
    cordinate_z = 45.87

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x} && {self.y})")


# 1st instantiation
test_walk1 = Robot(8.9, 99.7)
print(test_walk1.cordinate_z)  # 45.87

# 2nd instantiation
test_walk2 = Robot(4.5, 6.7)
print(test_walk2.cordinate_z)  # 45.87
