# ----------------------------------------------------------------------------
# ---------------------**## Dictionary Methods ##**---------------------------

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
# ! ********** Example 8 ********** clear method **********
# employee_info.clear() # Removes all the elements from the dictionary
# print(employee_info)

# ! ********** Example 9 ********** copy method **********
# gerald_info = employee_info.copy()  # Returns a copy of the dictionary
# gerald_info["Best Friend"] = "Elide Zavala"
# print(gerald_info)
# print(employee_info)

# ! ********** Example 10 ********** fromkeys method **********
letters = ["a", "e", "i", "o", "u"]
numbers = [1, 2]

vowels = dict.fromkeys(letters, numbers)
# {'a': [1, 2], 'e': [1, 2], 'i': [1, 2], 'o': [1, 2], 'u': [1, 2]}
# print(vowels)

# con fromkeys() se puede asignar un valor por defecto a todas las claves,
# si no se especifica el valor por defecto es None
vowels = dict.fromkeys(letters)
# print(vowels)  # {'a': None, 'e': None, 'i': None, 'o': None, 'u': None}
# las keys son diferentes, pero los valores son los mismos

print({}.fromkeys(employee_info))
# {'Name': None, 'Last Name': None, 'Address': None, 'Job': None, 'Age': None,
# {'Name': 'Unknown', 'Last Name': 'Unknown', 'Address': 'Unknown', 'Job': 'Unknown', 'Age': 'Unknown',
print({}.fromkeys(employee_info, "Unknown"))
