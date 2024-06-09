# ---------------------------------------------------------------------------------
# -----------------------**## Dictionary Part-2 ##**-------------------------------

# #! *************** Ejemplo 29 *************** Multiple if conditions - Dictionary Comprehension

original_dict = {"jack": 38, "Lincoln": 48,
                 "Theodore": 57, "Cecile": 21, "Tony": 18}

# new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
# # {'jack': 38, 'Tony': 18} # solo se imprimen los valores que cumplen con las dos condiciones
# print(new_dict)

#! *************** Ejemplo 30 *************** else Dictionary Comprehension

# new_dict = {k: "old" if v > 40 else "young" for (
#     k, v) in original_dict.items()}

# # {'jack': 'young', 'Lincoln': 'old', 'Theodore': 'old', 'Cecile': 'young', 'Tony': 'young'}
# print(new_dict)

#! *************** Ejemplo 31 *************** Nested Dictionary Comprehension
new_dict = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
# Output
# {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}, 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}

# k1 sera de 2 a 4
# k2 sera de 1 a 5

# pasos
# 1. k1 = 2, k2 = 1, 2*1 = 2
# 2. k1 = 2, k2 = 2, 2*2 = 4
# 3. k1 = 2, k2 = 3, 2*3 = 6
# 4. k1 = 2, k2 = 4, 2*4 = 8
# 5. k1 = 2, k2 = 5, 2*5 = 10
# 6. k1 = 3, k2 = 1, 3*1 = 3
# 7. k1 = 3, k2 = 2, 3*2 = 6
# 8. k1 = 3, k2 = 3, 3*3 = 9
# 9. k1 = 3, k2 = 4, 3*4 = 12
# 10. k1 = 3, k2 = 5, 3*5 = 15
# 11. k1 = 4, k2 = 1, 4*1 = 4
# 12. k1 = 4, k2 = 2, 4*2 = 8
# 13. k1 = 4, k2 = 3, 4*3 = 12
# 14. k1 = 4, k2 = 4, 4*4 = 16
# 15. k1 = 4, k2 = 5, 4*5 = 20


#! *************** Ejemplo 32 *************** Nested Dictionary Comprehension
# print(new_dict)
# new_dict = {}
# for k1 in range(2, 5):
#     new_dict[k1] = {k2: k1 * k2 for k2 in range(1, 6)}
# print(new_dict)

# Lo que hacemos es que primero se ejecuta el for de afuera y luego el de adentro y se va guardando en el diccionario new_dict = {}
# Output
# {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}, 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}

#! *************** Ejemplo 33 *************** Nested Dictionary Comprehension
new_dict = {}  # diccionario vacio
for k1 in range(2, 5):  # 2, 3, 4
    new_dict[k1] = {}  # se crea un diccionario vacio dentro de new_dict
    for k2 in range(1, 6):  # 1, 2, 3, 4, 5
        new_dict[k1][k2] = k1 * k2  # se va guardando en el diccionario vacio

print(new_dict)  # Output

# {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}, 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}
