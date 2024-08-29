# --------------------------------------------------------------------------------
#! Infinite Iterators

# ? Example 6 Infinite iterators using the next() method
# print(int())

# number = iter(int, 1)
# iter funciona como un bucle infinito, pero se detiene cuando se cumple la condición
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))

# ? Example 7 Infinite iterators using for loops
# for element in number:
#     print(element)

# ? Example 8 Infinite iterators using classes
class OddNums:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2  # Increment by 2 for odd numbers
        return num


odd_nums = OddNums()

iterable_nums = iter(odd_nums)  # Convert the class to an iterator

print(next(iterable_nums))  # 1
print(next(iterable_nums))  # 3
print(next(iterable_nums))  # 5
print(next(iterable_nums))  # 7
print(next(iterable_nums))  # 9

# ? Example 9 Infinite iterators using the takewhile() method
