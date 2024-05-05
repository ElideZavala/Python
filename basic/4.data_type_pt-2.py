# --------------------- #
""" Data Types part 1 """
# --------------------- #

"""
--Data Types--           --Class--           --Value--
integer                  int                 1, 2, 3, 4, 5
float                    float               1.0, 2.0, 3.0, 4.0, 5.0
boolean                  bool                True/False
string                   str                 "Hello", "World"
list                     list                [1, 2, 3, 4, 5]
dictionary               dict                {"name": "Elide", "age": 23}
tuple                    tuple               (1, 2, 3, 4, 5)
set                      set                 {"cat", 99}
"""

# ---------- List ---------- #
# Ordered
mixed = [1, 2, 3.4, 4.7, 5.2, True, "Elide Zavala", [1, 2, 3]]
print(mixed)
print(type(mixed))

# ---------- Dictionary ---------- #
# Unordered
print('------------------')
person = {
    "name": "Elide",
    "age": 23,
    "is_awesome": True,
    "is_cool": False,
    "fav_foods": ["pizza", "chocolate", "tacos"]
}

print(person)
print(person['fav_foods'])
print(type(person))

# ---------- Tuple ---------- #
# Ordered
print('------------------')
person = ("Elide", 23, True, False, ["pizza", "chocolate", "tacos"])
print(person)
print(type(person))

# ---------- Set ---------- #
# Unordered
print('------------------')
person = {"Elide", 23, True, False, "pizza", "chocolate", "tacos"}
