# ------------------------------------------------------------------------
# -----------------*## Iterating Over Dictionaries ##**-------------------

#! ************* Example 34 *************
# random = {
#     1: 456,
#     2: 123,
#     45: "Hey",
#     "is_employed": False
# }

# for key in random:
#     print(key)
# Output
# 1, 2, 45, is_employed

#! ************* Example 35 *************
employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York, USA",
    "Job": "Salesperson",
    "Age": 34
}

for i in employee_info:
    print(i)
    # Output
    # Name, Last Name, Address, Job, Age
