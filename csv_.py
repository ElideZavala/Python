# -----------------------------------------------------------------------------
# ----------------------------- *## CSV File ##* ------------------------------

import csv

# ******************* Task One *******************

# *-*-*-*-*-*-*-*-* Opening a CSV file and inserting simple data in it *-*-*-*-*-*-*-*-*

with open("users_info/users.csv", "w", newline="") as users_data:
    CSV_writer_data = csv.writer(users_data)

    # row 1 ->>>> table heading
    CSV_writer_data.writerow(["User Name", "User ID", "Status"])

    # row 2 ->>>> first row of user data
    CSV_writer_data.writerow(["Elideee", 123, "Online"])

    # row 3 ->>>> second row of user data
    CSV_writer_data.writerow(["Vania", 126, "offline"])

    # row 4 ->>>> third row of user data
    CSV_writer_data.writerow(["Criss", 230, "Online"])

    # row 5 ->>>> forth row of user data
    CSV_writer_data.writerow(["Maricarmen", 245, "Online"])

# ******************* Task Two *******************
# *-*-*-*-*-*-*-*-* Reading a CSV file *-*-*-*-*-*-*-*-*

with open("users_info/users.csv") as users_data:
    CSV_writer_data = csv.reader(users_data)
    # print(list(CSV_writer_data))

    for data_row in CSV_writer_data:
        print(data_row)
