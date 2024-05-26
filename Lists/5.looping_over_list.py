# -------------------------------------------------------------------------------------
# -------------------------**## Looping over a list ##**-------------------------------

# ! ----------------- Example 16 -----------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# for letter in letters:
#     print(letter)

# ! ----------------- Example 17 -----------------
for letter in enumerate(letters):
    # print(letter)
    index, letter = letter
    print(index, letter)

# con enumerate() se obtiene una tupla con el indice y el valor de la lista

# ! ----------------- Example 18 -----------------
# items = (0, "a")
# index, letter = items
# print(index, letter)

# aqui se desempaqueta la tupla en dos variables, index y letter

# ! ----------------- Example 19 -----------------
for index, letter in enumerate(letters):
    print(index, letter)
