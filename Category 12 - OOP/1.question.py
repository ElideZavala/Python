# Create a Vehicle class with max_speed and mileage instance attributes

class Vehicule:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage   = mileage

mi_vehiculo = Vehicule(220, 90)
print(f"mi carro corre a {mi_vehiculo.max_speed} con un kilometraje de {mi_vehiculo.mileage}")
