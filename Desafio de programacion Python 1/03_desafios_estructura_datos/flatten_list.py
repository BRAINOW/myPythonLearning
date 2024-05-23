def flatten(lista):
    flat = []
    for i in range(len(lista)): #Recorremos la lista original
        if type(lista[i]) == list: #En caso de que sea una lista 

            #Recorremos la lista anidada y guardamos cada uno de sus elementos
            for j in range(len(lista[i])): 
                flat.append(lista[i][j])
        else:
            #Si no es una lista lo agregamos
            flat.append(lista[i]) 

    return flat

print(flatten( [1,2,[1,2],3,4,[1,2,3]] )) #[1, 2, 1, 2, 3, 4, 1, 2, 3]

#########################Solucion del curso #########################

def aplanar_lista(lista):
    nueva_lista = []
    for elemento in lista :
        if type(elemento) is list: #si es una lista
            nueva_lista.extend(elemento) #Agregamos lo elementos de la lista a la nueva lista
        else:
            nueva_lista.append(elemento) #Agregamos el elemento en caso de no ser una lista
    return nueva_lista

print(aplanar_lista( [1,2,[1,2],3,4,[1,2,3]] )) #[1, 2, 1, 2, 3, 4, 1, 2, 3]

#####################################################################