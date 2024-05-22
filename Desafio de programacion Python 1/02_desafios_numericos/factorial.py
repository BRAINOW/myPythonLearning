def factorial(n):
    if n == 0: return 1 #El factorial de 0 es 1
    if n != 1: #Ejecutamos la llamada recursiva hasta que lleguemos a 1
        n = n*factorial(n-1)
    
    return n 

print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(4))
print(factorial(5))

#########################Solucion del curso #########################

#Por ciclo
def calcular_factorial(numero):
    factorial = 1
    for i in range(2,numero+1): #Multiplicamos desde el 2 al valor del numero cada uno de sus antecesores
        factorial *= i
    return factorial

print(calcular_factorial(0))
print(calcular_factorial(3))
print(calcular_factorial(4))
print(calcular_factorial(5))

#####################################################################

#Recursivamente
def calcular_factorial_recursivo(numero):
    if numero == 0 or numero == 1:  #En caso de ser "0" o "1" retornamos 1
        return 1
    return numero * calcular_factorial_recursivo(numero-1) #Llamada recursiva

print(calcular_factorial_recursivo(0))
print(calcular_factorial_recursivo(3))
print(calcular_factorial_recursivo(4))
print(calcular_factorial_recursivo(5))

#####################################################################
