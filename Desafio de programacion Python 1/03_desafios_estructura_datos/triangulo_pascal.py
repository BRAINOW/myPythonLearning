"""
    1
   1,1
  1,2,1
 1,3,3,1
1,4,6,4,1

"""

def trianguloPascal(filas): #Recibe las filas del triangulo
    triangulo = []
    for i in range(filas): #Para cada fila
        fila = [] #Generamos una nueva fila vacia
        for j in range(len(triangulo)+1): #Recorremos hasta la longirud actual del triangulo + 1
            if j == len(triangulo) or j == 0: #En caso de ser la primera o ultima posicion
                fila.append(1) 
            else: 
                #Si ya esta en la segunda fila o mas
                if len(triangulo[i-1]) >= 2:
                    #Sumamos lal posicion j y j-1 de la fila anterior
                    fila.append(triangulo[i-1][j-1]+triangulo[i-1][j])
                else:
                    #en caso contrario no los suma
                    fila.append(triangulo[i-1][j])
        
        triangulo.append(fila) #Anexamos la fila al triangulo


    return triangulo

filas = 5
for fila in trianguloPascal(filas):
    print((" ")*(filas-len(fila)),fila)
"""     
         [1]
       [1, 1]
     [1, 2, 1]
   [1, 3, 3, 1]
 [1, 4, 6, 4, 1]
 
 """

#En el curso esta hecho practicamente igual