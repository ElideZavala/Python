# ---------------------------------------------------------------------------------------

from sys import getsizeof

# ? Generator Expression

# print("******************* Example 13*********************")
# numbers = []
# print(numbers)
# print(type(numbers))

# for x in numbers:
#     print(x) # No output because numbers is empty

print("******************* Example 14*********************")
numbers_gen = (x * 2 for x in range(10))  # 208 bytes
numbers_gen = (x * 2 for x in range(100))  # 208 bytes
numbers_gen = (x * 2 for x in range(1000))  # 208 bytes

print("Generator Object:", getsizeof(numbers_gen))  # 208 bytes

numbers_list = [x * 2 for x in range(10)]  # 184 bytes
numbers_list = [x * 2 for x in range(100)]  # 920 bytes
numbers_list = [x * 2 for x in range(1000)]  # 8856 bytes

print("LCE:", getsizeof(numbers_list))  # 184 bytes
