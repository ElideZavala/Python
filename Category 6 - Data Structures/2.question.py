# Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list

list = [34, 54, 67, 89, 11, 43, 94]

index_four = list.pop(4)

# list[2] = index_four
list.insert(2, index_four)
list.append(index_four)
print(list)
