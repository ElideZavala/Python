# ---===---===---===---===---===---===---===---===---===---===---===---===
# JSON Files

import json
from pathlib import Path

products = [
    {"Product": "Laptop", "Price": 1000, "Stock Availability": 5},
    {"Product": "Mouse", "Price": 20, "Stock Availability": 50},
    {"Product": "Keyboard", "Price": 50, "Stock Availability": 20},
    {"Product": "Monitor", "Price": 200, "Stock Availability": 10},
    {"Product": "Headset", "Price": 100, "Stock Availability": 15},
]

# *-*-*-*-*-*-*-*-* Writing JSON Data *-*-*-*-*-*-*-*-*
products_data = json.dumps(products)
# print(products_data)

# crear el archivo .json
Path("ecommerce").mkdir(exist_ok=True)  # Create a directory
# con exist_ok=True, no se genera error si la carpeta ya existe

# escribir el archivo .json
Path("ecommerce/products.json").write_text(products_data)

# *-*-*-*-*-*-*-*-* Reading JSON Data *-*-*-*-*-*-*-*-*
json_data = Path("ecommerce/products.json").read_text()

# print(json_data)

# convertir el archivo .json a un diccionario
readable_data = json.loads(json_data)  # Convert JSON data to a dictionary
print(readable_data)

# [{'Product': 'Laptop', 'Price': 1000, 'Stock Availability': 5}, {'Product': 'Mouse', 'Price': 20, 'Stock Availability': 50}, {'Product': 'Keyboard', 'Price': 50, 'Stock Availability': 20}, {'Product': 'Monitor', 'Price': 200, 'Stock Availability': 10}, {'Product': 'Headset', 'Price': 100, 'Stock Availability': 15}]
# {'Product': 'Laptop', 'Price': 1000, 'Stock Availability': 5}

print(readable_data[0])
# {'Product': 'Laptop', 'Price': 1000, 'Stock Availability': 5}

print(readable_data[0]["Product"])  # Laptop
print(readable_data[2]["Price"])  # 50
print(readable_data[3]["Stock Availability"])  # 10
