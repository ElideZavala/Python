# Count the total number of digits in a given number


# Solution 1 (Propia)
number = 9934767930
new_number = []


for i in str(number): 
    new_number.append(i)

print(len(new_number))

# solution 2
number2 = 91431956794
count = 0

while number2 != 0:
    number2 //= 10 # removera el ultimo digito del numero dado en cada iteracion
    count += 1 # contara las veces que el ciclo se corre,
    # es decir cada vez que a number2 se le remueva un elemento, este lo contara.

print("Total Digits are:", count)