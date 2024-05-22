"""
#Cada elemento es el resultado de aplicar una funcion a cada elemento del objeto iterable

lista = [expresion(elemento) for elemento in objeto_iterable]
"""

def calcualar_cuadrado(numero):
    return numero**2

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados =[]

for num in lista_num:
    cuadrado = calcualar_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print("Ciclo for: ",lista_cuadrados) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista_comprehension = [num**2 for num in lista_num]
print("List comprehension: ",lista_comprehension) #List comprehension:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista_comprehensionf = [calcualar_cuadrado(num) for num in lista_num]
print("List comprehension + funcion: ",lista_comprehensionf) #List comprehension + funcion:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]