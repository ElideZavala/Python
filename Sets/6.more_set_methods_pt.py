# -----------------------------------------------------------------------------------------------------
# ----------------------------**## More Set Methods Part 2 ##**----------------------------------------

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
D = {3, 4, 5}

#! ************ Example 26  ************ insubset() method
print(A.issubset(B))  # Output: True
print(A.issubset(C))  # Output: False
print(B.issubset(A))  # Output: False
print(B.issubset(C))  # Output: False
print(C.issubset(B))  # Output: True
print(D.issubset(B))  # Output: True

# issubset() method returns True if all elements of a set are present in another set (passed as an argument), otherwise it returns False.


#! ************ Example 27  ************ issuperset() method
print(A.issuperset(B))  # Output: False
print(A.issuperset(C))  # Output: False
print(B.issuperset(A))  # Output: True
print(B.issuperset(C))  # Output: True
print(C.issuperset(B))  # Output: False
print(D.issuperset(B))  # Output: False


# issuperset() in python is the opposite to issubset(),
