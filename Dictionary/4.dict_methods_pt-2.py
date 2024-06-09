# ---------------------------------------------------------------------------------------------
# -----------------------**## 4. Dictionary Methods (Part 2) ##**------------------------------

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

# ! ********** Example 11 **********  **********
# print(employee_info)
# print(employee_info.items()) # dict_items([('Name', 'John'), ('Last Name', 'Doe'), ('Address', '1234 Elm Street'), ('Job', {'Developer', 'Salesperson'}), ('Age', 17), ('Hobbies', ('Soccer', 'Reading', 'Gaming')), (1992, 'Year of Birth'), ('Married', True), ('Favorite Songs', ['Un Poco Loco', 'Remember Me', 'Proud Corazon']), ('Best Friends', {'Name': 'Gerald'}), ('Special One', None)])

# lo que hace items() es devolver una vista de los pares clave-valor del diccionario

# ! ********** Example 12 ********** del **********
del employee_info["Best Friends"]
# dict_items([('Name', 'John'), ('Last Name', 'Doe'), ('Address', '1234 Elm Street'), ('Job', {'Developer', 'Salesperson'}), ('Age', 17), ('Hobbies', ('Soccer', 'Reading', 'Gaming')), (1992, 'Year of Birth'), ('Married', True), ('Favorite Songs', ['Un Poco Loco', 'Remember Me', 'Proud Corazon']), ('Special One', None)])
# print(employee_info.items())

# Con del se puede eliminar un elemento del diccionario

# ! ********** Example 13 ********** keys() **********
# dict_keys(['Name', 'Last Name', 'Address', 'Job', 'Age', 'Hobbies', 1992, 'Married', 'Favorite Songs', 'Special One'])
# print(employee_info.keys())

# keys() devuelve una vista de las claves del diccionario

# ! ********** Example 14 ********** del & keys **********
del employee_info["Hobbies"]
# dict_keys(['Name', 'Last Name', 'Address', 'Job', 'Age', 1992, 'Married', 'Favorite Songs', 'Special One'])
print(employee_info.keys())
