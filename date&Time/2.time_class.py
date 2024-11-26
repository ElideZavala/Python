# -----------------------------------------------------------------
# ---------------------**## Time Class ##** -----------------------
from datetime import time

# *-*-*-*-*-*- Example 8 ->> Time object to represent
time_1 = time()
print("Time A:", time_1) # Time A: 00:00:00

time_2 = time(13, 55, 00)
print("Time B:", time_2) # Time B: 13:55:00

time_3 = time(hour=9, minute=55, second=15)
print("Time C:", time_3) # Time C: 09:55:15

time_4 = time(13, 55, 00, 100000)
print("Time D:", time_4) # Time D: 13:55:00.100000  

time_5 = time(11, 34, 56)
print("Hour:", time_5.hour)
print("Hour:", time_5.minute)
print("Hour:", time_5.second)
print("Hour:", time_5.microsecond)

# *-*-*-*-*-*- Example 9 ->> Getting hour, minute, second and microsecond

# Esto se usa
