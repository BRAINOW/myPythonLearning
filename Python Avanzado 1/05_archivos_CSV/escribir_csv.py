import csv

columnas = ["nombre","apellido","edad"]
dato = ["Paco","Botero",26]

datos_lista = [
    ["Paco","Botero",26],
    ["Javier","Quinones",24],
    ["Emilio","Tafur",25]
]

datos_dict = [
    {"nombre": "Paco", "apellido":"Botero", "edad": 26},
    {"nombre": "Javier", "apellido":"Quinones", "edad": 24},
    {"nombre": "Emilio", "apellido":"Tafur", "edad": 25}
]

#archivo = open("datos.csv", "w")
#Indicamos con newline="" que no queremos una linea vacia cada que agreguemos una nueva columna
with open("datos.csv", "w",newline="") as archivo: 
    """
    writer = csv.writer(archivo,delimiter=",")
    writer.writerow(columnas)
    #writer.writerow(dato)
    writer.writerows(datos_lista) #Ahora contiene 3 filas de datos
    
    """

    #Para trabajar especificamente con diccionarios:
    writer = csv.DictWriter(archivo,fieldnames=columnas)
    writer.writeheader() #Escribe la primera fila con el nombre de las columnas 
    writer.writerows(datos_dict)