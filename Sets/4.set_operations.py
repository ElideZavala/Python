# ------------------------------------------------------------------------------------------------------
# -----------------------------------**## Set Operations ##**-------------------------------------------

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#! ************ Example 19  ************

# ? union operator
# print(A | B)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# with the union we can make multiple

# OR
# print(B | A)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# ? union() method
# print(A.union(B))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# OR
# print(B.union(A))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

#! ************ Example 20  ************
# ? intersection operator
# print(A & B)  # Output: {4, 5}
# OR
# print(B & A)  # Output: {4, 5}
# in the intersection we cam get the common elemen

# ? intersection() method
# print(A.intersection(B))  # Output: {4, 5}
# OR
# print(B.intersection(A))  # Output: {4, 5}

#! ************ Example 21  ************
# ? difference operator
# print(A - B) # Output: {1, 2, 3}
# OR
# print(B - A) # Output: {8, 6, 7}

# With the difference we can get the elements that are not common in the two sets

# ? difference() method
# print(A.difference(B)) # Output: {1, 2, 3}
# OR
# print(B.difference(A)) # Output: {8, 6, 7}

#! ************ Example 22  ************
# ? symmetric difference operator
print(A ^ B)  # Output: {1, 2, 3, 6, 7, 8}
# OR
print(B ^ A)  # Output: {1, 2, 3, 6, 7, 8}
# With the symmetric difference we can get the elements that are not common in the two sets

# ? symmetric_difference() method
print(A.symmetric_difference(B))  # Output: {1, 2, 3, 6, 7, 8}
# OR
print(B.symmetric_difference(A))  # Output: {1, 2, 3, 6, 7, 8}
