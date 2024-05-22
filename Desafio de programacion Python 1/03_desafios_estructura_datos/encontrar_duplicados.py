def duplicados(lista):
    dupli = []

    for element in lista:
        if lista.count(element) != 1 and element not in dupli:  #Si el elemento aparece mas de una vez y no lo hemos contado 
            dupli.append(element) 
    
    return dupli

print(duplicados([1,5,4,2,"Issai","Brian"])) #[]
print(duplicados([1,5,4,1,2,2,"Brian","Issai","Brian",5])) #[1, 5, 2, 'Brian']

#########################Solucion del curso #########################

#Mas complicada y mesnos eficiente (:

#####################################################################