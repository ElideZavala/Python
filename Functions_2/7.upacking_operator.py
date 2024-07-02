# ----------------------------------------------------------------------------------
# ? Unpacking Operator

print("******************** Example 17 ********************")
# numbers = [1, 2, 3]
# print(numbers)  # [1, 2, 3]

# print(1, 2, 3)  # 1 2 3
# print(*numbers)  # 1 2 3 # Unpacking Operator

print("******************** Example 18 ********************")
# values = list(range(5))
# print(values)  # [0, 1, 2, 3, 4]
# print(*values)  # 0 1 2 3 4 # Unpacking Operator

# values = [*range(20)]  # create a list of values from 0 to 19
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(values)
# # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 # Unpacking Operator
# print(*values)

# print({*"Python"})  # {'P', 'y', 't', 'h', 'o', 'n'}
# Here we are unpacking a string into a set. The set constructor takes an iterable and unpacks it into individual elements.


print("******************* Example 19 *********************")
# cities = ["Rome", "Paris", "New York", "Istanbul", "Cd. de México", "Tokyo"]
# names = ["John", "Jane", "Alice", "Bob", "Eve", "Jack"]

# info = [*names, *cities]
# print(info) # ['John', 'Jane', 'Alice', 'Bob', 'Eve', 'Jack', 'Rome', 'Paris', 'New York', 'Istanbul', 'Cd. de México', 'Tokyo']

print("******************* Example 20 *********************")

dict_one = {
    "name": "Elide",
    "city": "Villahermosa",
}

dict_two = {
    "full name": "Dick Van Dyke",
    "address": "USA"
}

dict_three = {
    "name": "Willian",
    "job": "Developer"
}

combined = {**dict_one, **dict_two, **dict_three}
# {'name': 'Willian', 'city': 'Villahermosa', 'full name': 'Dick Van Dyke', 'address': 'USA', 'job': 'Developer'}
print("🐛 ", combined)
