def ordenaBurbuja(lista):
    aux = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    return lista

print(ordenaBurbuja([5,4,7,8,12,3,6,10]))

#########################Solucion del curso #########################
#Casi iguales
def ordenamiento_burbuja(lista):
    
    for i in range(len(lista)):
        for j in range(0,len(lista)-i-1):
            if lista[j+1] < lista[j]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    
    return lista

print(ordenamiento_burbuja([5,4,7,8,12,3,6,10]))

#####################################################################