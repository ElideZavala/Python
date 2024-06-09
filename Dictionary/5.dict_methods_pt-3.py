# ---------------------------------------------------------------------------------------------
# -----------------------**## 5. Dictionary Methods (Part 3) ##**------------------------------

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

# ! ********** Example 15 ********** values() **********
# print(employee_info.values())
# dict_values(['John', 'Doe', '1234 Elm Street', {'Developer', 'Salesperson'}, 17, ('Soccer', 'Reading', 'Gaming'), 'Year of Birth', True, ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], {'Name': 'Gerald'}, None])

# values() devuelve una vista de los valores del diccionario

# ! ********** Example 16 ********** del & values **********
# del employee_info["Age"]

# print(employee_info.values()) # dict_values(['John', 'Doe', '1234 Elm Street', {'Developer', 'Salesperson'}, ('Soccer', 'Reading', 'Gaming'), 1992, 'Year of Birth', True, ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], {'Name': 'Gerald'}, None])

# ! ********** Example 17 ********** pop() **********
# print(employee_info.popitem())  # ('Special One', None)
# # con popitem() se elimina el último elemento del diccionario y se devuelve una tupla con la clave y el valor

# print(employee_info.pop("Married"))  # True
# # con pop() se elimina el elemento con la clave especificada y se devuelve el valor
# print(employee_info) # {'Name': 'John', 'Last Name': 'Doe', 'Address': '1234 Elm Street', 'Job': {'Developer', 'Salesperson'}, 'Hobbies': ('Soccer', 'Reading', 'Gaming'), 1992: 'Year of Birth', 'Favorite Songs': ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], 'Best Friends': {'Name': 'Gerald'}}

# ! ********** Example 18 ********** setdefault() **********
# 17, nos regresa el valor de la clave especificada
print(employee_info.setdefault("Age"))

# None, si la clave no existe, se crea con el valor None
print(employee_info.setdefault("Smoking"))

# N/A, si la clave no existe, se crea con el valor especificado
print(employee_info.setdefault("Allergies", "N/A"))

# {'Name': 'John', 'Last Name': 'Doe', 'Address': '1234 Elm Street', 'Job': {'Developer', 'Salesperson'}, 'Hobbies': ('Soccer', 'Reading', 'Gaming'), 1992: 'Year of Birth', 'Favorite Songs': ['Un Poco Loco', 'Remember Me', 'Proud Corazon'], 'Best Friends': {'Name': 'Gerald'}, 'Age': 17, 'Smoking': None}
print(employee_info)
