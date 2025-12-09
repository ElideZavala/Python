# Convert string into a datetime object
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
datetime_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p") 
# 2020-02-25 16:20:00

# date_string = "Feb 25 2300 4:20PM"
# datetime_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(type(date_string)) # <class 'str'>

print(type(datetime_obj)) # <class 'datetime.datetime'>
print(datetime_obj) # 2020-02-25 16:20:00

