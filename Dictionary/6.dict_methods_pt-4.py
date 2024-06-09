# ---------------------------------------------------------------------------------------------
# -----------------------**## 5. Dictionary Methods (Part 4) ##**------------------------------

employee_info = {
    "Name": "John",
    "Last Name": "Doe",
    "Address": "1234 Elm Street",
    "Job": {"Salesperson", "Developer"},
    "Age": 17,
    "Hobbies": ("Soccer", "Reading", "Gaming"),
    1992: "Year of Birth",
    "Married": True,
    "Favorite Songs": ["Un Poco Loco", "Remember Me", "Proud Corazon"],
    "Best Friends": {"Name": "Gerald"},
    "Special One": None
}

# Case #1
# target_item1 = employee_info.pop("Smoking", "no")
# # En caso de que la clave no exista, se regresa el valor especificado
# print(target_item1)  # 17
# print(employee_info)

#! ********** Example 21 ********** pop() **********
# target_item_2 = employee_info.pop("Allergies")
# print(target_item_2)   # Devuelve un KeyError por que la clave no existe

#! ********** Example 22 ********** pop() **********
# target_item_3 = employee_info.pop("Best Friend", "COCO")
# # En caso de que la clave no exista, se regresa el valor especificado
# print(target_item_3)  # COCO
# print(employee_info)  # {'Name': 'John', 'Last Name': 'Doe', 'Address': '1234 Elm Street', 'Job': {'Developer', 'Salesperson'}, 'Age': 17, 'Hobbies': ('Soccer', 'Reading', 'Gaming'), 1992: 'Year of Birth', 'Married': True, 'Favorite Songs': ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], 'Best Friends': {'Name': 'Gerald'}, 'Special One': None}

#! ********** Example 23 ********** update() **********
# ? Case 1
lost_key = {"Favorite Movie": "The Blood Diamond"}
employee_info.update(lost_key)
# {'Name': 'John', 'Last Name': 'Doe', 'Address': '1234 Elm Street', 'Job': {'Developer', 'Salesperson'}, 'Age': 17, 'Hobbies': ('Soccer', 'Reading', 'Gaming'), 1992: 'Year of Birth', 'Married': True, 'Favorite Songs': ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], 'Best Friends': {'Name': 'Gerald'}, 'Special One': None, 'Favorite Movie': 'The Blood Diamond'}

# Con update() se añade un diccionario a otro diccionario existente
# {'Name': 'John', 'Last Name': 'Doe', 'Address': '1234 Elm Street', 'Job': {'Developer', 'Salesperson'}, 'Age': 17, 'Hobbies': ('Soccer', 'Reading', 'Gaming'), 1992: 'Year of Birth', 'Married': True, 'Favorite Songs': ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], 'Best Friends': {'Name': 'Gerald'}, 'Special One': None, 'Favorite Movie': 'The Blood Diamond'}
print(employee_info)

print("\n")

# ? Case 2
# fount_key = {"Favorite Movie": "Titanic"}
# employee_info.update(fount_key)

# Aqui actualizamos el valor de la clave "Favorite Movie" con el valor "Titanic"
# print(employee_info) # {'Name': 'John', 'Last Name': 'Doe', 'Address': '1234 Elm Street', 'Job': {'Developer', 'Salesperson'}, 'Age': 17, 'Hobbies': ('Soccer', 'Reading', 'Gaming'), 1992: 'Year of Birth', 'Married': True, 'Favorite Songs': ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], 'Best Friends': {'Name': 'Gerald'}, 'Special One': None, 'Favorite Movie': 'Titanic'}

# ? Case 3
employee_info.update(Dog_Name="Krypto", Bird_Name="Precious")
print(employee_info)

# Con update() se añaden nuevas claves y valores al diccionario existente
