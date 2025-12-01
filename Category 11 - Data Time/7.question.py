# Print current time in milliseconds
from datetime import datetime

date_now = datetime.now()
print(date_now)

# miliseconds = int(date_now.timestamp() * 1000)
microseconds = int(date_now.strftime("%f"))
milliseconds_from_time = microseconds // 1000

print(milliseconds_from_time, "milisegundos") 

# timestamp 


