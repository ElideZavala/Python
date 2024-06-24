# ----------------------------------------------------------------------------------
# -------------------------**## Filter Function ##**--------------------------------

#! ********** Example 1 **********
# Our Iterable
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Function


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if (letter in vowels):
        return True
    else:
        return False


filtered_vowels = filter(filter_vowels, letters)
# aceptara solo los valores que sean True, no tomara en cuenta los False
# y los valores que sean True los guardara en una lista
# print(filtered_vowels) # <filter object at 0x7f8b1b3b3d30>

# print(type(filtered_vowels)) # <class 'filter'>

# print("The filtered vowels are: ") # The filtered vowels are:

# for vowel in filtered_vowels:
#     print(vowel)    # a, e, i

#! ********** Example 2 **********
random_list = [1, 'a', 0, False, True, '0']
filtered_list = filter(None, random_list)
print(filtered_list)  # <filter object at 0x7f8b1b3b3d30>

print("Truthy values are:")
print(list(filtered_list))  # [1, 'a', True, '0']
# Solo toma los valores que son True, los demas los ignora
# y los valores que son True los guarda en una lista
# no se imprimen sin list porque es un objeto de tipo filter
for value in filtered_list:
    print(value)  # 1, a, True, 0
