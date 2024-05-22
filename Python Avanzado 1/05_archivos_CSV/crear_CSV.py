import csv
import os #nos permite leer parametros del sistema operativo

#almacenamos ruta del archivo
ruta = "csv_vacio.csv"
ruta_absoluta = "C:\\Users\\brian\\OneDrive\\Escritorio\\Python\\PYTHON_AVANZADO\\05_archivos_CSV\\csv_vacio.csv"

ruta_absoluta_os = os.path.join(os.getcwd(),"csv_vacio.csv") #Permite ingrsar el nombre de las carpetas y el nombre del archivo

print(ruta_absoluta)
print(ruta_absoluta_os)

archivo_abierto = open(ruta_absoluta,"w") #lo abrimos para escribir
writer = csv.writer(archivo_abierto, delimiter=",")

archivo_abierto.close()