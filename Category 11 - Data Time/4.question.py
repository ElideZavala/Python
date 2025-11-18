# Print a date in a the following format

# Day_name  Day_number  Month_name  Year
from datetime import datetime

today = datetime.now() 
print(today) # 2025-11-17 21:41:38.381537

formatted_date = today.strftime("%A %d %B %Y")
print(formatted_date) # Monday 17 November 2025

# given_date = datetime(2025, 11, 17)
