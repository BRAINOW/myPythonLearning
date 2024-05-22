import csv 

"""
['nombre', 'apellido', 'edad']
['Paco', 'Botero', '26']
['Javier', 'Quinones', '24']
['Emilio', 'Tafur', '25']
"""

with open("datos.csv","r",encoding="UTF-8") as archivo :
    """
    reader = csv.reader(archivo)
    columnas = next(reader) #podemos saltarnos la linea de encabezados de columnas 
    print("Columnas: ", columnas)
    """

    #DictReader toma la primera linea del .csv como las llaves de los elementos del diccionario
    reader = csv.DictReader(archivo)
    for fila in reader :
        print(fila["nombre"]) #imprimimos los nombres
        