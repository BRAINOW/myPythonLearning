def calcular_perimetro(*args): #args recibe los datos a travez de una tupla
    perimetro = 0 
    print(args)
    for lado in args:
        perimetro += lado 
    return perimetro

perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)

triangulo = calcular_perimetro(1,2,3)
print(triangulo)

