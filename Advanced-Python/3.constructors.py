# ------------------------------------------------------------------
# Constructor

print("******************** Example 3 ********************")


# class Robot:
#     def walk(self):
#         print("walking")


# robot = Robot()
# robot.walk()  # walking

# robot = Robot(2.4, 6.5)


print("******************** Example 4 ********************")


# class Robot:
#     def __init__(self, x, y):
#         # Defalut value
#         # self.x = 10
#         self.x = x
#         self.y = y

#     def walk(self):
#         print(self.x, self.y)


# robot = Robot(2.4, 6.5)

# robot.walk()  # walking

print("******************** Example 5 ********************")


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking ({self.x} {self.y})")


robot = Robot(2.4, 6.5)

robot.walk()  # walking
