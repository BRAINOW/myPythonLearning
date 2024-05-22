"""
lista = [expresion(elemento) for elemento in objeto_iterable if condicion]
lista = [expresion(elemento) for elemento in objeto_iterable]
"""

def calcular_cuadrado(numero):
    return numero**2

def es_par(numero):
    return numero % 2 == 0

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = [calcular_cuadrado(num) for num in lista_num]
print(lista_cuadrados) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#                            #Funcion                #Ciclo              #Condicion
lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)] 
print(lista_cuadrados_pares) #[4, 16, 36, 64, 100]

#                       #Funcion            #if             #else       #Ciclo
lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print(lista_resultados) #[0, 4, 0, 16, 0, 36, 0, 64, 0, 100]