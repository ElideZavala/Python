# ----------------------------------------
# ---- *## Datetime CLass ##* ----
from datetime import datetime

# Example 10 >>>>> Python datetime object
time_1 = datetime(2100, 1, 1)
print(time_1)

time_2 = datetime(2050, 10, 25, 20, 50, 50)
print(time_2)
# Example 11 >>>>>  getting year, month, day, hour, minute,b second, microsecond

time_3 = datetime(2050, 10, 25, 20, 50, 50)
print(time_3)

print("year:", time_3.year)  # 2050
print("mes:", time_3.month)  # 10
print("dia:", time_3.day)  # 25
print("hora:", time_3.hour)  # 20
print("minuto:", time_3.minute)  # 50
print("segundo:", time_3.second)  # 50
