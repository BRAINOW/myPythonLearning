def calcular_area_cuadrado(lado):
    """Calcula el area de un cuadrado al recibir la longitud de su lado"""
    area = lado*lado
    return area

lado_cuadrados = [1,3,5]
area_cuadrados = []

for lado in lado_cuadrados:
    area = calcular_area_cuadrado(lado)
    area_cuadrados.append(area)

# python -m pdb .\area_cuadrado.py
# continue -> se detiene en el siguiente break (B)
# display var -> Ver cambios de la variable
# restart -> reinicia los 