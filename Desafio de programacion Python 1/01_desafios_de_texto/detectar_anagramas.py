def detectarAnagrama(palabra1, palabra2): #Recibimos las 2 palabras
    if len(palabra1) != len(palabra2): #Si son de distinto tamano no son anagramas
        return False
    
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    #Si la letra no esta en la otra palabra no es anagrama
    for letra in palabra1: 
        if not (letra in palabra2):
            return False
    
    for letra in palabra2:
        if not (letra in palabra1):
            return False
    
    #Si no encontro letras faltantes entonces son anagramas
    return True
    
print(detectarAnagrama("ramo","mora")) #True
print(detectarAnagrama("ramo","moras")) #False
print(detectarAnagrama("ramo","roma")) #True
print(detectarAnagrama("ramo","taco")) #False
print(detectarAnagrama("Brian","nairB")) #True

print(detectarAnagrama("lama","Mala")) #True
print(detectarAnagrama("calor","Coral")) #True
print(detectarAnagrama("cama","casa")) #False

#########################Solucion del curso #########################
#Lo queria hacer asi pero no supe como usar "sorted()", ahora si se'
print("\n\n\n")

def es_anagrama(palabra_1, palabra_2):
    letrasP1 = sorted(palabra_1.lower())
    letrasP2 = sorted(palabra_2.lower())
    return letrasP1 == letrasP2

print(es_anagrama("lama","Mala")) #True
print(es_anagrama("calor","Coral")) #True
print(es_anagrama("cama","casa")) #False

####################################################################