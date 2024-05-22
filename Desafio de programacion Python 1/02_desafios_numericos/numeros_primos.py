#un numero primo es aquel numero mayor a uno que solo es divisible entre "1 y el mismo numero"
#El numero 1m no es primo, si recibe "1" es False

def esPrimo(numero):
    if numero <= 1: return False

    for n in range(2,numero): #Recorremos desde el numero "2" hasta "numero-1"
        if numero%n == 0: #Si es divisible entre "n" entonces no es primo
            return False
    
    return True #Si no fue divisible entonces es primo

print(esPrimo(1))
print(esPrimo(3))
print(esPrimo(7))
print(esPrimo(12))
print(esPrimo(43))

#########################Solucion del curso #########################

#Lo hice igual 

#####################################################################