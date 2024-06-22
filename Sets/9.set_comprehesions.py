# -----------------------------------------------------------------------------------
# ------------------------**## Set Comprehensions ##**-------------------------------

#! ************ Example 32 ************
number1 = {number ** 2 for number in range(10)}
# Output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# Explanation: This is an example of set comprehension. It creates a set of squares of numbers from 0 to 9.

number2 = {number ** 3 for number in range(5)}
print(number1)  # Output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(number2)  # Output: {0, 1, 8, 27, 64}
