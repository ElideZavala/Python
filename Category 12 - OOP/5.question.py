"""
Define property that should have the same value for every class instance
Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
"""


class Vehicle:

    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass                         

mycar = Car("Jabali", 250, 200000)
print(f"Car {mycar.color, mycar.max_speed, mycar.mileage}")

myBus = Bus("Mamut", 120, 250000)
print(f"Car {myBus.color, myBus.max_speed, myBus.mileage}")
