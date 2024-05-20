import datetime as dt #Le asignamos un alias "dt"
from datetime import datetime #Importamos el submodulo principal solamente

hora_actual = dt.datetime.now()
print(hora_actual)

hora_actual2 = datetime.now() 
print(hora_actual2)