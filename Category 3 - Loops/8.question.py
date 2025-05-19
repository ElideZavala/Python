# Reverse the following list using for loop

list = [10, 20, 30, 40, 50]
new_list = []


# new_list = "".join(map(str, list))
start = len(list) - 1
stop = -1
step = -1

for i in range(start, stop, step):
    new_list.append(list[i])

print(list)
print(new_list)

# len(list) - 1 #? da el indice del ultimo elemento de la lista
# -1 #? es el punto de parada, lo que significa que el bucle se detendrá antes de alcanzar el índice -1.
# -1 #? como el paso significa que el bucle disminuirá el índice en 1 en cada iteración, iterando efectivamente hacia atrás.


