# Given two list of equal size create a Python set such that it shows the element from CC

list_one = [2, 3, 4, 5, 6, 7, 8]
list_two = [4, 9, 16, 25, 36, 49, 64]

# zip, se utiliza para cobinar dos o mas listas en una sola lista de tuplas.
set_list = set(zip(list_one, list_two))

#set_list2 = list(zip(list_one, list_two))
print("🐛 merge_list ", set_list ) # {(7, 49), (2, 4), (4, 16), (8, 64), (6, 36), (3, 9), (5, 25)}
