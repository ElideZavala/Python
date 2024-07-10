# --------------------------------------------------------------------------------------
# Exception Handling Part 3

#! try...except...else...finally
print("******************* Example 4 *********************")

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
#     note.close()
# except (ValueError, ZeroDivisionError):
#     print("Plese enter a valid age")
# else:
#     print("No exceptions were thrown")

# ? Solution 1 -> moving the close() method to the except clause
# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Plese enter a valid age")
#     note.close()
# else:
#     print("No exceptions were thrown")


# ? Solution 2 -> duplicate the close to the else clause
# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
#     # note.write(x)
# except (ValueError, ZeroDivisionError):
#     print("Plese enter a valid age")
#     note.close()
# else:
#     print("No exceptions were thrown")
#     note.close()

# ? Solution 3 -> using finally clause
try:
    note = open("someFile.txt")
    age = int(input("Age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("Plese enter a valid age")
else:
    print("No exceptions were thrown")
finally:
    note.close()
    print("Closing the file...")
