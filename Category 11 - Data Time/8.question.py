#  Convert the following datetime into a string

from datetime import datetime

def converSpanish(day):
    dias_ingles = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dias_espanol = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    if day in dias_ingles:
        indice = dias_ingles.index(day)
        print(indice)
        return dias_espanol[indice]
    return day

given_date = datetime(2035, 5, 20)
date_in_string = given_date.strftime("%Y-%m-%d")
day_english = given_date.strftime("%A")
day_spanish = converSpanish(day_english)
date_in_string = given_date.strftime(f"{day_spanish}, %d de %B de %Y")
# date_in_string = given_date.ctime()

print(type(date_in_string))
print(date_in_string)