import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinones",
    "edad" : 24
}

objeto_json = json.dumps(persona,indent=4) #"dumps()" serializamos los datos a tipo json


with open("Persona.json","w") as archivo_json:
    archivo_json.write(objeto_json)
    #json.dump(persona,archivo_json)