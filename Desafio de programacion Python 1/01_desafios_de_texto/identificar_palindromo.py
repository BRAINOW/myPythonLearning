def valida_palindromo(texto):
    texto = texto.lower() #lo pasamos a minuscula
    texto = texto.replace(" ","") #Quitamos los espacios
    
    for i in range(len(texto)): #Recorre el largo de la frase
        #Compara el caracter con el de la misma posicion desde atras
        if texto[i] != texto[(-1)*(i+1)]: 
            return False #si son diferentes termina
        
    return True

frase = "Anita lava la tina"
print(frase, valida_palindromo(frase))
frase = "Palindromo"
print(frase, valida_palindromo(frase))
frase = "oso"
print(frase, valida_palindromo(frase))
frase = "pollo"
print(frase, valida_palindromo(frase))

#########################Solucion del curso #########################
def esPalindromo(texto):
    texto = texto.lower() #lo pasamos a minuscula
    texto = texto.replace(" ","") #Quitamos los espacios

    #Con el primer ":" indica el primer caracter y con el segundo el ultimo
    #Agregando el "-1" indica que se invierta la cadena de texto
    return texto == texto[::-1] 

frase = "Anita lava la tina"
print(frase, esPalindromo(frase))
frase = "Palindromo"
print(frase, esPalindromo(frase))
frase = "oso"
print(frase, esPalindromo(frase))
frase = "pollo"
print(frase, esPalindromo(frase))

#####################################################################