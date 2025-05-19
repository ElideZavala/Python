# Display a message “Done” after successful execution of a for loop
# Forma Propia
try:
    for i in range(5):
        print(i)
except:
    print("Ocurrio un error en el proceso")
finally:
    print("Hecho")

print("")

# Forma orginal
for j in range(5):
    print(j)
else: 
    print("Done!!!")