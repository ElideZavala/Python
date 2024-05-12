# --------------------------------------------------------
# --------- **## Nested Loops ##** ------------------------

# ********___Example 8___********
# for x in range(2):
#     for y in range(5):
#         print(f"Point({x}, {y})")

# ********___Example 9___********
for x in range(1):  # si y termina, se regresa a x
    for y in range(3):  # si z termina, se regresa a y
        for z in range(1):  # hace primero toda la interacion aqui
            print(f"Point({x}, {y}, {z})")
