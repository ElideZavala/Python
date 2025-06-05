# Given an input string, count occurrences of all characters within a string

str = "Elide Zavala Vinagre"
lower_str = str.lower()

count_dict = dict()

for char in lower_str:
    count = lower_str.count(char)

    count_dict[char] = count

print(count_dict)