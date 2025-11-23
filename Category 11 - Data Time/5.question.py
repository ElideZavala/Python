# Find the day of the week of a given date

from datetime import datetime
# given_date = datetime(2100, 12, 15)

day = datetime(2100, 12, 15).strftime("%A")
print(day) # Wednesday
