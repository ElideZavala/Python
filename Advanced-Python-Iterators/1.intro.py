# ------------------------------------------------------------------------
# Introduction to Iterators

#! Example 1 >>> __iter__() and __next__() methods
numbers = [1, 2, 3, 4, 5]

first_iterator = iter(numbers)
print(next(first_iterator))  # 1
print(next(first_iterator))  # 2

# next() == __next__()

print(first_iterator.__next__())  # 3
print(first_iterator.__next__())  # 4
print(type(first_iterator.__next__()))
# print(first_iterator.__next__()) # 5

#! Example 2 >>> using a for loop
for number in numbers:
    print(number)
