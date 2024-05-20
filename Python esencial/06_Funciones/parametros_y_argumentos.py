def perimetroCuadrado(lado, unidades):
    perimetro = lado*4
    print(f"El perimetro es {perimetro} {unidades}")

perimetroCuadrado(10,"metros") #Envio de parametros por orden
print("\n")
perimetroCuadrado(unidades="centimetros",lado=25) #Envio de parametros por variable