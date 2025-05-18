# Print the following pattern using for loop

"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""

# Solution Propia

number = 0 
for i in range(6, 0, -1):
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print(" ")

num1 = 5
num2 = 5

# Solution 
for i in range(0, num1 + 1 ):
    # print(i)
    for j in range(num2 - i, 0, -1):
        print(j, end=" ") 
    print("")