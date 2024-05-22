import json

with open("Persona.json","r") as archivo_json:
    datos_json = json.load(archivo_json)

print(type(datos_json)) #<class 'dict'>
print(datos_json) #{'nombre': 'Javier', 'apellido': 'Quinones', 'edad': 24}
print(datos_json["nombre"]) #Javier