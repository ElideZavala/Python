# ----------------------------------------------------------------------------------------------
# --------------------------------**## Modifying a Set ##**-------------------------------------

#! ************* Example 9 ************* creating a set
mixed_info = {"Python", "Dog"}
print(mixed_info)

#! ************* Example 10 ************* Not able to access the set using index
# mixed_info[1]
# TypeError: 'set' object does not support indexing

#! ************* Example 11 ************* add()
mixed_info.add(31)
print(mixed_info)  # {'Dog', 31, 'Python'}

#! ************* Example 12 ************* update()
mixed_info.update([12, "Jar", "Sand"])
print(mixed_info)  # {12, 'Dog', 31, 'Python', 'Jar', 'Sand'}
# Note: The update() method can take tuples, lists, strings or other sets as its argument, and add all elements of that argument to the set.

#! ************* Example 13 ************* update()
mixed_info.update(["Bird", "Island"], ("Cat", "Island"))
# {12, 'Dog', 31, 'Python', 'Jar', 'Sand', 'Bird', 'Island', 'Cat'}
print(mixed_info)
# In de code above, the update() method added the elements 'Bird' and 'Island' from the list, and 'Cat' from the tuple, not the string 'Island'.
