lista_num = [1,2,3,4,1,1,2,5,6,8]

set_pares = {num for num in lista_num if num%2==0}
print(set_pares) #{8, 2, 4, 6} #los sets no contienen numeros repetidos

vocales ="aeiou"
#                #Llave          #Valor          #Ciclo
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales} #{'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
print(diccionario)