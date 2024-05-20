def validar_x(x):
    if x<1 :
        raise Exception("La variable x debe ser mayor a 1")
    else:
        print("X es mayor a 1\n\n")

x = 2
validar_x(x)


x = 0.3
validar_x(x)
