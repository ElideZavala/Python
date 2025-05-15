# Accept number from user and calculate the sum of all number from 1 to the given number

# Solution One

list_numbers = []

print("Escribe una lista de numeros a sumar, y al terminar escribe 'ok'")

while True:
    number = input()
    if number == "ok":
        suma = 0
        for i in list_numbers:
            suma += i

        print("El total de la suma es: ",suma)
        break
    else:
        list_numbers.append(int(number))
        


# Solution two
sum = 0

num = int(input("Enter a number "))

for i in range(1, num + 1, 1):
    sum += i


print("The sum is:", sum)