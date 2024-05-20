#las tuplas son inmutables 
#se definen entre parentesis

lenguajes = ("Pyhon","C","C++")
print(lenguajes)

lenguajes2 = "Pyhon","C","C++" #De no poner parentesis se interpreta como tupla
print(lenguajes2)
print(lenguajes2[0])
print(lenguajes2[-1])# ultimo elemento

#lenguajes2[0] = "Java" #TypeError: 'tuple' object does not support item assignment
    #Mejor usar una lista