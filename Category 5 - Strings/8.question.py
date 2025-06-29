# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
tiene_vacios = False

# for strs in str_list:
#     if (strs == "" or strs is None or (isinstance(strs, str) and strs.strip() == "")):    
#         print(strs, 'vacios')
#         tiene_vacios = True
#         break
#     else:
#         print(strs)

# tiene_vacios = any(elemento == "" or elemento is None or (isinstance(elemento, str) and elemento.strip() == "") for elemento in str_list)

# print(tiene_vacios)



filter_none = list(filter(None, str_list))
print(filter_none)




