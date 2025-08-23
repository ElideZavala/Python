# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

#solution
list_contatec = [i + j for i, j in zip(list1, list2)]
print("🐛 list_contatec", list_contatec)

