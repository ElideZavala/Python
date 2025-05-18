# Print the multiplication table for a number
def multiplication_table(number):

    for i in range(1, 10 + 1, 1):
        print(f"{number} * {i} = {number * i}")

multiplication_table(10)