# Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates

from typing import List, Any

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

list_of_values = list(set(speed.values()))
print("🐛 list_of_values", list_of_values) # [44, 47, 52, 53, 54]
