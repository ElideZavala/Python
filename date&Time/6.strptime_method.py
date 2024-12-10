# -----------------------------------------------------------------
# --------------- **## strptime() method ##** ---------------------

from datetime import datetime

# El metodo strptime() convierte una cadena en un objeto datetime y recibe dos argumentos: la cadena y el formato de la cadena

# *-*-*-*-*-*-*-*-*- Example 21 -*-*-*-*-*-*-*-*-*---> strptime() method
# date_str = "11 Aug, 2099"
# print(type(date_str))  # <class 'str'>

# date_obj = datetime.strptime(date_str, "%d %b, %Y")
# %d -> Day of the month as a zero-padded decimal number
# %B -> Month name
# %Y -> Year with century as a decimal number
# %b -> Month name abbreviation

# print(date_obj)  # 2024-12-21 00:00:00
# print(type(date_obj))  # <class 'datetime.datetime'>

# *-*-*-*-*-*-*-*-*- Example 22 -*-*-*-*-*-*-*-*-*---> string to datetime object
# *-*-*-*-*-*-*-*-*- Example 23 -*-*-*-*-*-*-*-*-*---> string to datetime object

date_str1 = "31/01/2200 19:10:10"
date_str2 = "12/31/2200 10:19:19"

# considering the date is in dd/mm/yyyy format
date_obj1 = datetime.strptime(date_str1, "%d/%m/%Y %H:%M:%S")
# %d -> Day of the month as a zero-padded decimal number
# %m -> Month as a zero-padded decimal number
# %Y -> Year with century as a decimal number
# %H -> Hour (24-hour clock) as a zero-padded decimal number
# %M -> Minute as a zero-padded decimal number
# %S -> Second as a zero-padded decimal number

print(date_obj1)  # 2200-01-31 19:10:10
print(type(date_obj1))  # <class 'datetime.datetime'>

# considering the date is in mm/dd/yyyy format
date_obj2 = datetime.strptime(date_str2, "%m/%d/%Y %H:%M:%S")
print(date_obj2)  # 2200-12-31 10:19:19
