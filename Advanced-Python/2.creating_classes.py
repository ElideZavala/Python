# ---------------------------------------------------------------
# Creating Classes

print("******************** Example 1 ********************")


class Robot:
    def walk(self):
        print("Robot is walking")

    def run(self):
        print("Robot is running")

# walk() es un metodo de la clase Robot y self es un parametro que se pasa automaticamente a cada metodo de una clase


robot = Robot()  # Instancia de la clase Robot

robot.walk()  # Robot is walking
robot.run()  # Robot is running

print(type(robot))  # <class '__main__.Robot'>gf

# Una clase puede tener multiples instancias
# True # robot es una instancia de la clase Robot
print(isinstance(robot, Robot))
