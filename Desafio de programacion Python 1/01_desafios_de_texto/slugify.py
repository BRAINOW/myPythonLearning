def slugify(texto):
    texto = texto.strip().lower() #Quitamos espacios al inicio y al final y hacemos minuscula
    cadena_filtrada = ""
    for letra in texto: #recorremos cada letra
        if letra.isalnum() or letra==' ': #Si es alfanumerico o un espacio
            cadena_filtrada += letra 

    #Retornamos la cadena fintrada y cambiando los espacios por guiones
    return cadena_filtrada.replace(" ","-") 

print(slugify("Esto es u/n ejemplo de* una cadena_ de %texto 123!!!"))
#Esto-es-un-ejemplo-de-una-cadena-de-texto-123


print("\n")


#########################Solucion del curso #########################

import re #Expresiones regulares

def slugify_curso(texto):
    
    slug = (texto
        .lower() #Pasamos a minuscula
        .strip() #Quita los espacios antes y despues del texto
        .replace(" ", "-")
    )

    #"sub" Permite remplazar un conjunto de caracteres en la expresion
        # ^ indica que se buscaran los que no esten en la expresion
        # \w indica caracteres alfanumericos
        # \- indica guiones
    slug = re.sub(
                "[^\w\-]" #Expresion regular
                ,"" #Por lo que remplazara
                ,slug #Cadena donde se buscara
            ) 
        
    return slug

print(slugify_curso("Esto es u/n ejemplo de* una cadena_ de %texto 123!!!"))

#####################################################################