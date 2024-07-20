# --------------------------------------------------------------------------------
# Instance Methods VS Class Methods

# TODO Instance methods
print("******************* Example 9 *********************")


# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def walk(self):
#         print(f"walking coordinates ({self.x}, {self.y})")

# test_walk = Robot(1.1, 4.6)
# test_walk.walk()

# TODO Class methods
print("******************* Example 10 *********************")


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # decorator
    @classmethod
    def specific_coordinates(cls):
        return cls(2.2, 3.3)

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


# con el decorador @classmethod, se puede llamar al método sin instanciar la clase
# se inicializa la clase con las coordenadas (2.2, 3.3)

test_walk = Robot(1.1, 4.6)
test_walk.walk()

test_walk2 = Robot.specific_coordinates()  # class method
print(test_walk2.x, test_walk2.y)
