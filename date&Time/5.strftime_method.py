# ----------------------------------------------------------------

# ---------*## strftime() method ##*---------

# Data Formts
# US ->> MM/DD/YYYY
# UK ->> DD/MM/YYYY

from datetime import datetime

# Example 16: --> Formatting date using strftime() method

# current date & time
# now = datetime.now()
#
# time = now.strftime("%H:%M:%S")
# print("Time:", time) # Time: 15:10:00
#
# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("s1:", s1) # s1: 12/01/2024, 14:06:32

# Example 17: --> detetime to string strftime() method
now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
# print("Year:", year) # Year: 2024
# print("Month:", month) # Month: 12
# print("Day:", day) # Day: 01


# Example 18: --> Creating string from a timestamp
timestamp = 4333259999 # Fecha en formato timestamp
date_time = datetime.fromtimestamp(timestamp)

# print(date_time) # 2107-04-26 05:19:59
# print(type(date_time)) # <class 'datetime.datetime'>

date = date_time.strftime("%m/%d/%Y, %H:%M:%S") # 04/26/2107, 05:19:59
# print("Date:", date) # Date: 04/26/2107, 05:19:59
# print(type(date)) # <class 'str'>

# read more about date and time on the python documentation and find more directives
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

date2 = date_time.strftime("%d %b, %Y") # 26 Apr, 2107
# -> %d -> Day of the month as a zero-padded decimal number
# -> %b -> Month name abbreviation
# -> %Y -> Year with century as a decimal number
# print("Date2:", date2) # Date2: 26 Apr, 2107

date3 = date_time.strftime("%d %B, %Y") # 26 April, 2107
# %B -> Month name
# %b -> Month name abbreviation
# print("Date3:", date3) # Date3: 26 April, 2107

time2 = date_time.strftime("%I%p") # 05AM
#I -> 12-hour clock
#p -> AM/PM
# print("Time2:", time2) # Time2: 05AM

# Example 19 --> locale's apropiate date and time
# timestamp = 4333259999 # Fecha en formato timestamp
# date_time = datetime.fromtimestamp(timestamp)
#
# d1 = date_time.strftime("%c") # Tue Apr 26 05:19:59 2107
# # -> %c -> Locale's appropriate date and time representation
# print("d1:", d1) # d1: Tue Apr 26 05:19:59 2107
#
# d2 = date_time.strftime("%x") # 04/26/07
# # -> %x -> Locale's appropriate date representation of the date
# print("d2:", d2) # 04/26/07
#
# d3 = date_time.strftime("%X") # 05:19:59
# # -> %X -> Locale's appropriate time representation of the time
# print("d3:", d3) # 05:19:59

# Example 20 --> python datetime to timestamp

now = datetime.now()

# converting to timestamp
time_stamp = datetime.timestamp(now)
# timestamp() method return the time in seconds since the epoch as a floating point number
print("Timestamp:", time_stamp) # Timestamp: 1670480192.0

# converting from timestamp
date_time = datetime.fromtimestamp(time_stamp)
print("Date and Time:", date_time) # Date and Time: 2024-12-01 15:10:00