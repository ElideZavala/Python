# Given two lists create a third list by picking odd-index elements from the first list and even-index elements from the second.

list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]
combined_list2 = list()

ood_index = [list_one[i] for i in range(1, len (list_one), 2)] 
even_index = [list_two[i] for i in range(0, len(list_two), 2)]
combined_list = ood_index + even_index
print(combined_list)

print("****************************************")

ood_index2 = list_one[1::2]
even_index2 = list_two[0::2]
combined_list2.extend(ood_index2)
combined_list2.extend(even_index2)

print(combined_list2)




