# ----------------- Program Task Description
# Write a program that takes the dimenions of three sides of a triangle from the user, then using the Heron's Formula, calculates the area of the triangle and displays the result to the user.

side_A = int(input("write the side number A = "))
side_B = int(input("write the side number B = "))
side_C = int(input("write the side number C = "))

s = (side_A + side_B + side_C) / 2
print(s)
area = ((s * (s - side_A)) * ((s - side_B)) * ((s - side_C))) ** 0.5
area_fix = "{:.2f}".format(area) # aqui le podemos cortar los decimales

print(f"El area del tringulo es: {area_fix}")