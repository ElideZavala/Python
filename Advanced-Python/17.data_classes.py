# -------------------------------------------------------------------------------------------
# * Data Classes *#

#! Example 41 issue
# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# robot1 = Robot(1, 2)
# robot2 = Robot(1, 2)


# print("🐛 ", robot1 == robot2) # True
# print("🐛 ", id(robot1)) # 2263528125200
# print("🐛 ", id(robot2)) # 2263528125072
#! Example 42 issue Solution 1 -> __eq__
# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# robot1 = Robot(1, 2)
# robot2 = Robot(1, 2)


# print("🐛 ", robot1 == robot2) # True
# print("🐛 ", id(robot1)) # 2263528125200
# print("🐛 ", id(robot2)) # 2263528125072
#! Example 43 solution 2 -> namedtuple()
from collections import namedtuple
Robot = namedtuple("Robot", ["x", "y"])
# namedtuple
robot1 = Robot(x=1, y=2)
robot2 = Robot(x=1, y=2)

print(robot1 == robot2)
