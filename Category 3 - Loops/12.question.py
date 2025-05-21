# Reverse an integer
number = 3586540
reversed_num = 0

while number > 0:
    remainder = number % 10 # Se obtiene el ultimo digito del numero actual   
    reversed_num = (reversed_num * 10) + remainder # se multiplica reversed_num por 10 para desplazar los digitos existentes hacia la izquieda y luego se añade el remaider.
    number = number // 10 # Se elimina el último dígito del número orginal.
    
print(reversed_num) # Se imprime el reversed_num que contendrá en número invertido.