# Add a week (7 days) and 12 hours to a given date

from datetime import datetime, timedelta

given_date = datetime(2050, 3, 15, 10, 0, 0)
new_date = given_date + timedelta(days=7, hours=12)
print(new_date) # 2050-03-22 22:00:00


