#Estructura de datos que permite almacenar informacion
#Almacenan datos en llave y valor
    # llave:valor
#Los diccionarios se definen entre llaves y separados por ","

lenguajes = {
    "nombre": "python",
    "creador": "Guido"
}   

print(lenguajes)

#se usa llave para obtener su valor 
print(lenguajes["nombre"])
lenguajes["anio_lanzamiento"] = 1991
print(lenguajes)
lenguajes["anio_lanzamiento"] = 1999
print(lenguajes)

lenguajes["caracteristicas"] = ["sencillo","facil","genial"]
print(lenguajes)


print(lenguajes.items()) #lista de tuplas de la combinacion de la llave con su valor
print(lenguajes.keys())
print(lenguajes.values())