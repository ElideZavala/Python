# Display the cube of the number up to a given integer

# Solution One
number = 6
start = number + 1
number_cube = 0

while start > 0:
    start = start - 1
    number_cube = start ** 3

    if start == 0:
        break

    print(number_cube)

#Solution Two
input_num = 6

for i in range(1, input_num + 1):
    print(f"El actual numero es {i} y el cubo es {i * i * i}")
