
lenguajes = ["python","java","golang"]
print(lenguajes)

lista = [1, 2.0, True, "python", 1] #pueden contener variables de cualquier tipo 
print(lista)
print(lista[3]) #number 4 element
print(len(lista)) #list size

print(lenguajes[-1]) #Ultimo elemento de la lista
print(lista[0:3])

programacion = [lenguajes, "dedicacion", "practica"]
print(programacion)
print(programacion[0][0])

lenguajes[0] = "dart"
print(lenguajes)

lenguajes.append("python")
print(lenguajes)

otros_lenguajes = ["C","C++"]
lenguajes.extend(otros_lenguajes)
print(lenguajes)