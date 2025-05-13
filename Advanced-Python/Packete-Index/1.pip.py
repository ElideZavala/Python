# --------------------------------------
# ---- PIP (Python Package Index) ----

import requests
from datetime import datetime
import pytz

response = requests.get('https://www.google.com')
print(response)

local = datetime.now()
print("Local:", local.strftime('%m/%d/%Y'))

tz_NY = pytz.timezone("America/New_York")
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime('%m/%d/%Y, %H:%M:%S'))

# Funcion de esta forma: python -m pip install
# esto se debe a que python no esta en las variables de entorno
# Para agregar python a las variables de entorno se debe hacer lo siguiente:
# 1. Ir a la carpeta donde esta instalado python
# 2. Copiar la ruta de la carpeta
# 3. Ir a las variables de entorno
# 4. Agregar una nueva variable de entorno llamada PATH
# 5. Pegar la ruta de la carpeta de python
# 6. Guardar los cambios
# 7. Reiniciar la terminal
# 8. Listo, ahora se puede usar pip
