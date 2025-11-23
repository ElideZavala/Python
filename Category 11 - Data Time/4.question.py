# Print a date in a the following format

# Day_name  Day_number  Month_name  Year
from datetime import datetime

today = datetime.now() 
print(today) # 2025-11-17 21:41:38.381537

formatted_date = today.strftime("%A %d %B %Y")
print(formatted_date) # Monday 17 November 2025

# given_date = datetime(2025, 11, 17)

# ============================================================================
# TODOS LOS FORMATOS POSIBLES CON strftime EN PYTHON
# ============================================================================

# FECHA:
# %a  - Nombre del día abreviado (Mon, Tue, Wed, etc.)
# %A  - Nombre del día completo (Monday, Tuesday, Wednesday, etc.)
# %w  - Día de la semana como número (0=Sunday, 6=Saturday)
# %d  - Día del mes como número con cero inicial (01-31)
# %-d - Día del mes como número sin cero inicial (1-31) [Solo Unix]
# %b  - Nombre del mes abreviado (Jan, Feb, Mar, etc.)
# %B  - Nombre del mes completo (January, February, March, etc.)
# %m  - Mes como número con cero inicial (01-12)
# %-m - Mes como número sin cero inicial (1-12) [Solo Unix]
# %y  - Año sin siglo, con cero inicial (00-99)
# %Y  - Año completo (2025, 2026, etc.)
# %j  - Día del año (001-366)
# %U  - Número de semana del año (00-53), domingo como primer día
# %W  - Número de semana del año (00-53), lunes como primer día
# %V  - Número de semana ISO (01-53)
# %G  - Año ISO (año de la semana ISO)
# %g  - Año ISO sin siglo (00-99)

# HORA:
# %H  - Hora en formato 24 horas con cero inicial (00-23)
# %-H - Hora en formato 24 horas sin cero inicial (0-23) [Solo Unix]
# %I  - Hora en formato 12 horas con cero inicial (01-12)
# %-I - Hora en formato 12 horas sin cero inicial (1-12) [Solo Unix]
# %p  - AM/PM (AM, PM)
# %M  - Minutos con cero inicial (00-59)
# %-M - Minutos sin cero inicial (0-59) [Solo Unix]
# %S  - Segundos con cero inicial (00-59)
# %-S - Segundos sin cero inicial (0-59) [Solo Unix]
# %f  - Microsegundos (000000-999999)
# %z  - Desplazamiento UTC (ejemplo: +0000, -0500)
# %Z  - Nombre de la zona horaria (ejemplo: UTC, EST, CST)
# %X  - Representación de hora local (equivale a %H:%M:%S)

# FECHA Y HORA:
# %c  - Fecha y hora local (ejemplo: Mon Nov 17 21:41:38 2025)
# %x  - Representación de fecha local (ejemplo: 11/17/25)
# %r  - Hora en formato 12 horas (ejemplo: 09:41:38 PM)
# %R  - Hora en formato 24 horas (ejemplo: 21:41)
# %T  - Hora en formato 24 horas con segundos (ejemplo: 21:41:38)

# CARACTERES ESPECIALES:
# %%  - Literal % (para imprimir el símbolo %)
# %t  - Carácter tabulación
# %n  - Carácter nueva línea

# EJEMPLOS DE USO:
print("\n=== EJEMPLOS DE FORMATOS strftime ===\n")

# Fecha completa
print(f"Fecha completa: {today.strftime('%A, %d de %B de %Y')}")
# Salida: Monday, 17 de November de 2025

# Fecha corta
print(f"Fecha corta: {today.strftime('%d/%m/%Y')}")
# Salida: 17/11/2025

# Fecha con día del año
print(f"Día del año: {today.strftime('%Y-%m-%d (día %j del año)')}")
# Salida: 2025-11-17 (día 321 del año)

# Hora completa
print(f"Hora completa: {today.strftime('%H:%M:%S')}")
# Salida: 21:41:38

# Hora 12 horas
print(f"Hora 12h: {today.strftime('%I:%M:%S %p')}")
# Salida: 09:41:38 PM

# Fecha y hora ISO
print(f"ISO: {today.strftime('%Y-%m-%d %H:%M:%S')}")
# Salida: 2025-11-17 21:41:38

# Fecha con zona horaria
print(f"Con zona: {today.strftime('%Y-%m-%d %H:%M:%S %Z')}")
# Salida: 2025-11-17 21:41:38 (depende de la zona horaria)

# Formato personalizado
print(f"Personalizado: {today.strftime('%d-%b-%Y %I:%M %p')}")
# Salida: 17-Nov-2025 09:41 PM

# Semana del año
print(f"Semana del año: {today.strftime('Semana %W del año %Y')}")
# Salida: Semana 46 del año 2025