# -------------------------------------------------------------------------------------------

#! Introduction to Generators

# ? __iter__() & __next__() are implemented automatically

"""
Normal function
1.- return
2.- after return, the variables are garbage collected
3.- return terminates a function
4.- perform a task or calculates a value


Generator function
1.- yield
2.- access to variables after execution
3.- yield does not terminate a function
4.- return an iterator object
"""

# * Example 1 creating a generator


def first_generator():
    x = 1
    print("1st iteration")
    yield x

    x = 2
    print("2nd iteration")
    yield x

    x = 3
    print("3rd iteration")
    yield x


# my_gen = first_generator()
# print(next(my_gen))  # 1
# print(next(my_gen))  # 2
# print(next(my_gen))  # 3

# * Example 2 using a for loop
for element in first_generator():
    print(element)  # 1, 2, 3
