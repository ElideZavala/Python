rows = 5

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end="  ")
    print("\n")

# i sera igual a 0 y 0 + 1 = 1
# i sera igual a 1 y 1 + 1 = 2 
# i sera igual a 2 y 2 + 1 = 3 
# i sera igual a 3 y 3 + 1 = 4 

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end="  ")
    print("\n")

# i sera igual a 5 y 5 - 1 = 4
# i sera igual a 4 y 4 - 1 = 3 
# i sera igual a 5 y 3 - 1 = 2 
# i sera igual a 2 y 2 - 1 = 1 
