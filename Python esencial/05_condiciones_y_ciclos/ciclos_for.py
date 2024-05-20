for letra in "Texto": #Imprimimos cada letra de la strings
    print(letra)

print("\nLENGUAJES + break")
lenguajes = ["Python", "Java", "Golang"]
for elemento in lenguajes: 
    print(elemento)

    if elemento == "Java":
        break #Detenemos el ciclo con break



print("\nLENGUAJES + continue")
for elemento in lenguajes: 
    if elemento == "Java":
        continue #saltamos a la sioguiente iteracion usando continue
    print(elemento)
    
print("\n")
#range(n) inicia en 0 hasta n-1
for element in range(5):
    print(element)
        
print("\n")
for element in range(1,5):
    print(element)