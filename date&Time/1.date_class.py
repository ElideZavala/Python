# ----------------------------------
# -------**## Date Class ##**-------

# *-*-*-*-*-*-*-*-*- Example 1 ->>> Getting the current Date & Time
# from datetime import datetime

# print(datetime.now())

# *-*-*-*-*-*-*-*-*- Example 2 ->>> Getting the current Date
# import datetime

# print(datetime.date.today())

# *-*-*-*-*-*-*-*-*- Example 3 ->>> Getting the Datetime atrributesb
# import datetime

# print(dir(datetime))

# *-*-*-*-*-*-*-*-*- Example 4 ->>> Creating a date object
# import datetime

# date = datetime.date(2100, 12, 31)  # Creamos una fecha

# print(date)  # 2100-12-31
# print(type(date)) # <class 'datetime.date'>

# *-*-*-*-*-*-*-*-*- Example 5 ->>> Importing the date class
# from datetime import date

# print(date(2100, 12, 30))

# *-*-*-*-*-*-*-*-*- Example 6 ->>> Getting date from a timestamp
# from datetime import date

# time_stamp = date.fromtimestamp(4098889999)
# print(time_stamp) # Convertimos el dato de los segundos en una fecha.

# *-*-*-*-*-*-*-*-*- Example 7 ->>> Getting today's year, month and day
from datetime import date
today = date.today()

print("Current Year:", today.year)
print("Current Mount:", today.month)
print("Current Day:", today.day)
