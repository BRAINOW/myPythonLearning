lista_numeros = [1,2,3,4,5,6,7,8]

                        #filtro                         #Argumento
lista_pares = list(filter( lambda numero:numero % 2 == 0, lista_numeros))

#print(lista_pares)

nueva_lista = list(map(lambda numero:numero*10,lista_numeros)) #aplica la lambda para cada elemento de la lista de numeros
print(nueva_lista)
