# --------------------------------------------------------------------------
# ------------- **##For Loops Part 2**## ----------------

# # ********___Example 6___********
# status = True

# for number in range(1, 4):
#     print(f"Attempt {number}")

#     if status:
#         print("Success")
#         break

# # ********___Example 7___********
status = False

for number in range(1, 4):
    print(f"Attempt {number}")

    if status:
        print("Success")
        break
else:  # Correra lo anterior y si no se cumple la condicion del if, se ejecutara el else
    print("Failed")
