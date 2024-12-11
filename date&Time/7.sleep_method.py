# ---------------------------------------------------------
# ------------ 7. sleep() method in Python ----------------

import time

# *-*- Example 24 sleep()  -*-*
# print("Inmediately")
# time.sleep(2.0)  # Despues de 4 segundos se ejecuta la siguiente linea
# print("Inmediately after 8 seconds")

# *-*- Example 25 creating a simple low level digital clock  -*-*

while True:
    local_time = time.localtime()
    result = time.strftime("%I:%M:%S", local_time)
    print(result)
    time.sleep(1)
