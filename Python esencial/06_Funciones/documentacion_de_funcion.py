#Descripcion corta
def perimetro_cuadrado(lado):
    """Calcular el perimetro de un cuadrado""" 
    perimetro = lado * 4
    return perimetro

#Descripcion larga
def area_cuadrado(lado): 
    """Calcular el perimetro de un cuadrado

    Esta funcionn recibe el valor de un lado de un cuadrado y calcula el area del mismo y la retorna

    Args: 
        lado (int): medida del lado del cuadrado

    Returns:
        area (int): valor del area del cuadrado
    """
    area = lado * lado
    return area

#Se muestra la documentacion de la funcion
perimetro_cuadrado(5) 
area_cuadrado(5)