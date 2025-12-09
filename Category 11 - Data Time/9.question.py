# Calculate the date 4 months from the given date

from datetime import datetime 
from dateutil.relativedelta import relativedelta

given_date = datetime(2035, 5, 20).date()
print(given_date) # 2035-05-20

new_date = given_date + relativedelta(months=4)  
print(new_date) # 2035-09-20


