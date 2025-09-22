# Remove items from set1 that are not common to both set1 and set2

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

# Actualizar un conjunto con la intersección de sí mismo y otro.
# Regresa elemenos que son comunes entre si.
set_one.intersection_update(set_two)
print(set_one)