# Subtract a week (7 days)  from a given date.s

from datetime import datetime, timedelta

# year, month, day
given_date = datetime(2025, 11, 17) # lo convertimos a datetime

new_date = given_date - timedelta(days=7) # le restamos el datetime nuestro, menos los dias.
# restamos dias - timedelta(days=7)
# restamos semanas - timedelta(weeks=1)

print("Fecha original:", given_date) # 2025-11-17 00:00:00
print("Fecha después de restar una semana:", new_date) # 2025-11-10 00:00:00
