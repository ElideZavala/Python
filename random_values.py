# ------------------------------------------------------------------
# --------------**## Working With Random Values ##**----------------
import random

# *_*_*_*_*_*_*_* Between zero & one
# print(random.random()) # numero random entre 0 y 1

# *_*_*_*_*_*_*_* Between two arbitrary numbers
# print(random.randint(1, 50))  # numero random entre 1 y 50

# *_*_*_*_*_*_*_* Randomly choosing a list items
# numero random entre 1 y 10
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# *_*_*_*_*_*_*_* Randomly choosing multiple list items
# numero random entre 1 y 10 repetido 2 veces Ejem. [1, 5]
# print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=5))
# [4, 10, 1, 5, 7]

# *_*_*_*_*_*_*_* shuffling a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)  # desordena los numeros
print(numbers)  # [6, 1, 4, 10, 3, 2, 9, 7, 8, 5]

# *_*_*_*_*_*_*_*
