# -----------------------------------------------------------------------------------------
# ---------------------------**## Introduction to Tuple ##**-------------------------------

#! ***************** Example 1 *****************
# first_tuple = ()
# print(first_tuple)  # Output: ()

#! ***************** Example 2 *****************
# num = (1, 2, 3, 4, 5)
# print(num)  # Output: (1, 2, 3, 4, 5)
# print(type(num))  # Output: <class 'tuple'>

#! ***************** Example 3 *****************
# mixed = (1, 2.5, "Hello", True)
# print(mixed)  # Output: (1, 2.5, 'Hello', True)

#! ***************** Example 4 *****************
mixed = ({"Name": "Elide", "Job": "Developer"}, [
    4, 5, 15], (1.23, 2.36, 3.14), True, "Asia")
# Output: ({'Name': 'Elide', 'Job': 'Developer'}, [4, 5, 15], (1.23, 2.36, 3.14), True, 'Asia')
print(mixed)
print(type(mixed))  # Output: <class 'tuple'>
