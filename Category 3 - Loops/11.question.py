# Write a program to display all prime numbers within a range



# start_numbers = 25
# end_loop = 50

# for i in range(start_numbers, end_loop + 1):
#     if (i % 3) == 0:
#         print("Numero primo: " ,  i)

print('\n')
start = 1
end = 50


print(f"Imprime el numero entre {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num)