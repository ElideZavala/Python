# --------------------------------------------------------------------------------------
# Accessing dictionary key values

# To access the value of a specific key in a dictionary, you can use the square brackets `[]` and the key name. If the key does not exist, you will get a KeyError.

employee_info = {
    "name": "John",
    "last_name": "Doe",
    "age": 25,
    "position": "Software Developer",
    "Adress": "123 Main St",
    "Favorite Color": "Blue"
}

# ! ********* Example 5 *********
# print(employee_info["position"])  # Software Developer
# employee_info["position"] = "Arquitect"
# employee_info["Hobbies"] = ["Reading", "Traveling", "Coding"]
# print(employee_info["position"])  # Arquitect
# print(employee_info["Hobbies"])  # ['Reading', 'Traveling', 'Coding']

# {'name': 'John', 'last_name': 'Doe', 'age': 25, 'position': 'Software Developer', 'Adress': '123 Main St'}
# print(employee_info)

# Asignamos nuevo valor a la key "position" y a la key "Hobbies" y luego imprimimos el diccionario completo

# ! ********* Example 6 *********
# Acceder a la key del diccionario
# # 1. Checando que la key exista.
if "Favorite Color" in employee_info:
    print(employee_info["Favorite Color"])  # Blue

# 2. get() method
print(employee_info.get("Favorite Color"))  # Blue
print(employee_info.get("Favorite animal"))  # None
print(employee_info.get("Favorite animal", "Key not found"))  # Key not found
