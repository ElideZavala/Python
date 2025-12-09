# Print current date and time in Python
from datetime import datetime, date, time

ahora = datetime.now() 
mi_hora = ahora.time() 
print(ahora.strftime("%d/%m/%Y")) # 26/10/2025
print(ahora.strftime("%I:%M %p")) # 07:39 PM

print("\n")
hoy = date.today()
print(hoy)
