# remove all occurrence of 20 from the list

list = [5, 20, 15, 20, 25, 50, 20]

while 20 in list:
    list.remove(20)

print(list) # [5, 15, 25, 50]

# alternativa
def remove_value(sample_list, val):
    return [value for value in sample_list if value != val]


result_list = remove_value(list, 20) # [5, 15, 25, 50]