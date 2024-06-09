# ------------------------------------------------------------------------
# -------------------------**## Introduction ##**-------------------------

# Python Dictionary is a collection of key-value pairs. It is unordered, changeable, and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.

# ! ********* Example 1 *********
contacts = {
    "Samantha": 456,
    "John": 987,
}

print(contacts)  # {'Samantha': 456, 'John': 987}

# ! ********* Example 2 *********
employee_info = {
    "name": "John",
    "last_name": "Doe",
    "age": 25,
    "position": "Software Developer",
    "Adress": "123 Main St",
}

# {'name': 'John', 'last_name': 'Doe', 'age': 25, 'position': 'Software Developer', 'Adress': '123 Main St'}
print(employee_info)

# ! ********* Example 3 *********
animal_names = dict(dog="Toby", cat="Whiskers", bird="Polly")
print(animal_names)  # {'dog': 'Toby', 'cat': 'Whiskers', 'bird': 'Polly'}

# creamos un diccionario con el método dict() y le pasamos los valores

# ! ********* Example 4 *********
