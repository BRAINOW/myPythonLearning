def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

def area_cuadrado(lado):
    area = lado * lado
    return area

#Podemos retornar mas de una variable en una funcion
def calcular_cuadrado(lado):
    per = lado*4
    are = lado*lado
    return per, are

perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(5)

print(f"Area: {area}, Perimetro: {perimetro}")

#Asignamos dos variables retornadas por la funcion a dos variables en una sola linea
area, perimetro = calcular_cuadrado(10) 
print(f"Area: {area}, Perimetro: {perimetro}")

#Si lo asignamos a una sola variable vamos a recibir una tupla
cuadrado = calcular_cuadrado(100) 
print(cuadrado)

#Si queremos asignar el valor de una funcion que no retorna nada a una variable, esta tebndra el valor de "none"