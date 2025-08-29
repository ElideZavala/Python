# Initialize dictionary with default values
import json

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

create_dictionary = dict.fromkeys(employees, defaults)

# for name in employees:

print(json.dumps(create_dictionary, indent=4, ensure_ascii = False))

