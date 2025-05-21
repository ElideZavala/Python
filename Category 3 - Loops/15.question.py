# Print the following pattern

"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * *
* * 
*
"""

string = list("*")

for i in range(0, 5, 1):
    for j in range(0, -i, -1):
        print("*", end=" ")
    print("")

# Va a empezr desde 0 que sera i, el menos i indica que ira hacia abajo, ejemplo si i es 2, este ira hacia abajo, por que igual le agregamos el conteno con -1 en cual indica que ira a la reversa. 
#  el primero ira del 0 al 1, solo imprimira 1
# el segundio ira de 0 al 2, imprimira 2
# el tercero ira del 0 al 3, imprimira 3
# y asi sucesibamentem siempre y cuando el conteo sea al revez. 

for i in range(0, 5, 1):
    for j in range(i, 5, 1):
        print("*", end=" ")
    print("")


# va a empezar desde el 0 que sera i, luego seguira 1 que igual sera i, luego seguira 2 que igual sera i
# siempre sera 6
# va ir de 1 en 1
# con end unimos cada loop