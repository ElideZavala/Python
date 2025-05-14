# Print the following pattern
lista = []

for i in range(1):
    for j in range(5):
        
        j += 1
        lista.append(j )
        print(" ".join(map(str, lista)))

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
print()
last_num = 10

for row in range(1, last_num):
    for column in range(1, row + 1):
        print(column, end=" ")
    print("")
