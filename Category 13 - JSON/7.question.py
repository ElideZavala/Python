# Parse the following JSON to get all the values of a key ‘name’ within an array
import json

list = """[
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]
"""

data = []

try:
    data = json.loads(list) # Convierte una cadena JSON en un objeto de Python
except:
    print('no ser obtubieron todos los valores.')

data_list = [item.get('name') for item in data] # ['name1', 'name2']

print(data_list)
