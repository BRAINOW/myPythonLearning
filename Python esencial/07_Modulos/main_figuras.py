#los paquetes almacenan modulos cuyas fubnciones son comunes entre si
#El archivo "__init__.py" indica a python que es un paquete
from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.circulo import area_circulo, perimetro_circulo

lado = 4 
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print("Cuadrado: ", cuadrado)

radio = 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}

print("Circulo: ", circulo)