def primeraRepetida(texto):
    texto = texto.lower() #Pasamos el texto a minuscula
    texto = texto.replace(" ","") #Quitamos los espacios

    historial = [] 
    for letra in texto: #Para cada letra
        if letra in historial: #Comprobamos que no fue encontrada antes
            return letra #Si se repite la retornamos
        else: 
            historial.append(letra) #Si es la primera aparicion la agregamos al historial
    
    return None #Si no encuentra repetidas retorna None

print(primeraRepetida("Hola"))
print(primeraRepetida("Hola Mundo"))

print(primeraRepetida("Brian"))
print(primeraRepetida("Issai"))

#La solucion del curso fue exactamente igual a la que hice 