#inmportamos los modulos "area_cuadrado, perimetro_cuadrado"
from cuadrado import area_cuadrado, perimetro_cuadrado 

lado = 5 
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado)