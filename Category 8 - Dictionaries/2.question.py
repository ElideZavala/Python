# Merge following two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# metodo 1
# merge_dict = dict1 | dict2

# metodo 2
merge_dict = {**dict1, **dict2}
print('merge_dict: ', merge_dict)

