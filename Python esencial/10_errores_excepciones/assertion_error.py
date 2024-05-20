def promedio(lista):
    assert len(lista) > 0, "La lista esta vacia" #Si se cumple la condicion imprime el texto
    return sum(lista) / len(lista)


promed = promedio(lista=[1,3,5]) #Funciona

print(promed)

promed = promedio(lista=[]) #Detona assert