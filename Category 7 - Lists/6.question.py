# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1.remove("")

# for i, elemento in enumerate(list1):
#     if (elemento == ""):
#         list1.remove(elemento)
    

list1 = list(filter(None, list1))
print(list1)

