# Concatenate two lists in the following order


list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]

['Hello Dear', 'Hello Sir', 'Hi Dear', 'Hi Sir']


list_concatenate = [x + y for x in list1 for y in list2]
#for x in list2:
 #   list_concatenate.append(list1[0] + x )

#for z in list2:
#    list_concatenate.append(list1[1] + x)
    


print(list_concatenate) # result = [x + y for x in list1 for y in list2]
