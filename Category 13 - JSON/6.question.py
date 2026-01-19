# Convert the following JSON into Vehicle Object
import json

json_data = '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}'

objeto = json.loads(json_data)
print(objeto) # {'name': 'Toyota Rav4', 'engine': '2.5L', 'price': 32000}
print(type(object)) # <class 'type'>