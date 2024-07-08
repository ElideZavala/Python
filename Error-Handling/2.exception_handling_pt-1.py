# -------------------------------------------------------------------------------------
# -------------------- Exception Handling in Python - Part 1 --------------------------

import sys

print("********************* Example 8 *******************")

# try:
#     age = int(input("Age: "))
# except ValueError as exp_error:
#     # if the user enters a string, the program will print this message, otherwise it will print the age
#     print("Please enter a valid age")
#     print(exp_error)
#     print(type(exp_error))
# else:
#     print("No exceptions Here")
print("********************* Example 9 *******************")

random_list = ["a", 0, 2]
for entry in random_list:
    try:
        print("The entry is:", entry)
        r = 1 / int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        # print("Next entry.")
        print(sys.exc_info()[0])

print()
print("The reciprocal of", entry, "is", r)  # The reciprocal of 2 is 0.5
