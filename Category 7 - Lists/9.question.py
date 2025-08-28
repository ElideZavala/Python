# find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list = [5, 10, 15, 20, 25, 50, 20]

number = 20
index = list.index(number)
list[index] = 200

print(list)
