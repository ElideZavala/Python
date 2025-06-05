# Find all occurrences of “is” in a given string ignoring the case

str = "My cat is awesome. You're cat is amazing. Is his cat asleep?"

sub_string = "is"

temp_string = str.lower() # Convertimos todo el texto en minuscula.

count = temp_string.count(sub_string.lower()) # Vamos a contar la cantidad de veces que aparece "is" en la cadena, esa misma variable de busqueda, la convertimos en minuscula.

print("🐛 ", count) # 4
