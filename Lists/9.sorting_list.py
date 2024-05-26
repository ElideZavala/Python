# -------------------------------------------------------------------------------------------------------
# --------------------------------- **## Sorting a List ##** --------------------------------------------

numbers = [1, 5, 32, 124, 70, 854, 2356, 6589, 62, 8, 19, 999, 321]

# ! ************ Example 32 ************ sort() method
# numbers.sort()
# numbers.sort(reverse=False) # Ascending order
# print(numbers)

# numbers.sort(reverse=True) # Descending order
# print(numbers)
# print(sorted(numbers, reverse=True))

# ! ************ Example 33 ************ sorted() function
products = [
    ("Cup", 5),
    ("Plate", 10),
    ("Spoon", 3),
    ("Fork", 7),
    ("Knife", 8)
]

# products.sort()
# print(products)
# ! ************ Example 34 ************ sorted() function

def sort_products(product):
    return product[1] # Sort by price, is the second element in the tuple


products.sort(key=sort_products) # key why we want to sort by price
print(products)