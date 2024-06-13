# ----------------------------------------------------------------------------------------------
# -----------------------------**## Introduction to Sets ##**-----------------------------------

#! ************* Example 1 *************
first_set = {21, 32, 54, 666, 999}
print(first_set)
# Output: {32, 21, 54, 999, 666}

#! ************* Example 2 *************
mixed = {5.19, "Set", ("London", "Paris")}
print(mixed)
# Output: {5.19, 'Set', ('London', 'Paris')}

#! ************* Example 3 *************
numbers = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
print(numbers)
# Output: {1, 2, 3, 4, 5, 6}
# Note: Duplicates are not allowed in sets.

#! ************* Example 4 ************* creating a set from a tuple
colors = set(("blue", "red", "green", "blue", "yellow", "red"))
print(colors)
# Output: {'blue', 'yellow', 'green', 'red'}

#! ************* Example 5 ************* creating a set from a list
fruits = set(["apple", "banana", "cherry", "apple", "banana", "cherry"])
print(fruits)
# Output: {'banana', 'apple', 'cherry'}

#! ************* Example 6 ************* creating a set from a dictionary
cars = set({"BMW": "Germany", "Toyota": "Japan", "Ford": "USA", "BMW": "Germany", "Nissan": "Japan", "Chevrolet": "USA", "Volkswagen": "Germany", "Chery": "China", "Hyundai": "South Korea", "Kia": "South Korea", "Renault": "France",
           "Peugeot": "France", "Citroen": "France", "Jaguar": "UK", "Land Rover": "UK", "Rolls Royce": "UK", "Aston Martin": "UK", "Ferrari": "Italy", "Lamborghini": "Italy", "Maserati": "Italy", "Alfa Romeo": "Italy"})

print(cars) # Output: {'BMW', 'Toyota', 'Ford', 'Nissan', 'Chevrolet', 'Volkswagen', 'Chery', 'Hyundai', 'Kia', 'Renault', 'Peugeot', 'Citroen', 'Jaguar', 'Land Rover', 'Rolls Royce', 'Aston Martin', 'Ferrari', 'Lamborghini', 'Maserati', 'Alfa Romeo'}
# Note: In the above example, the duplicates are removed and only unique keys are stored in the set.    

    #! ************* Example 7 ************* a set cannot have a mutable data typy as an element
    # colors = {"blue", "red", ["green", "yellow"]}
    # print(colors) # Output: TypeError: unhashable type: 'list'

    #! ************* Example 8 ************* creating an empty set
    name = {}
    print(name) # Output: {}
    print(type(name)) # Output: <class 'dict'>

    empty_set = set()
    print(empty_set) # Output: set()
    print(type(empty_set)) # Output: <class 'set'>

    # in the above example, name is a dictionary and empty_set is a set and not a dictionary.
