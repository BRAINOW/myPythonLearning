def balanceado(texto):
    contador_abre = 0
    contador_cierra = 0

    for c in texto: #Recorremos cada catacter
        if c == '(':
            contador_abre+=1 #Aumentamos contador cuando se abre parentesis
        elif c == ')':
            contador_cierra+=1

            #Si se cierran mas de los que estan abiertos es incorrecto
            if contador_cierra > contador_abre: 
                return False

    if (contador_abre - contador_cierra) != 0: #Al final deben cerrarce los mismos que se abren
        return False
    
    return True

print(balanceado("(()())()(())"))
print(balanceado("()((())"))
print(balanceado("())()"))
print(balanceado("))()"))
print(balanceado("()("))

print("\n")

#########################Solucion del curso #########################

def parentesis_balanceados(texto):
    apertura = 0 #Contador
    for parentesis in texto:
        if parentesis == "(": #Si se abre un parentesis
            apertura +=1
        elif parentesis == ")":
            apertura -= 1

            #Si se cerraron mas parentesis de los que hay entonces es incorrecto el orden
            if apertura < 0: 
                return False
    
    return apertura == 0 #Al final no deben quedar parentesis sin cerrar
            
print(parentesis_balanceados("(()())()(())"))
print(parentesis_balanceados("()((())"))
print(parentesis_balanceados("())()"))
print(parentesis_balanceados("))()"))
print(parentesis_balanceados("()("))

#####################################################################