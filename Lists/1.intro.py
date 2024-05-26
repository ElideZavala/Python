# -----------------------------------------------------------------------------------------------
# -----------------------------**## Lists Introduction ##**--------------------------------------

# ! ********* Example 1 *********
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["John", "Mark", "Emily", "Sandra"]
# print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(names) # ['John', 'Mark', 'Emily', 'Sandra']

# ! ********* Example 2 *********
likes = [["tv", "gmaing"], ["pizza", "pasta"]]
# print(likes) # [['tv', 'gmaing'], ['pizza', 'pasta']]

# ! ********* Example 3 ********* --> a list of lists of lists
mixed = [[1, True], "Cat", "Dog", [["wind", "water"], ["earth", "fire"]]]
# [[1, True], 'Cat', 'Dog', [['wind', 'water'], ['earth', 'fire']]]
# print(mixed)

# ! ********* Example 4 ********* --> list multiplication (repetition)
animal = ["cat"] * 10
# print(animal) # ['cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat']

# ! ********* Example 5 ********* --> list merging/concatenation
event_nums = [2, 4, 6, 8, 10]
odd_nums = [1, 3, 5, 7, 9]
cities = ["Lagos", "Abuja", "Kano", "Port Harcourt"]
boolean = [True, False]

mixed_data = event_nums + odd_nums + cities + boolean
# [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 'Lagos', 'Abuja', 'Kano', 'Port Harcourt', True, False]
print(mixed_data)
