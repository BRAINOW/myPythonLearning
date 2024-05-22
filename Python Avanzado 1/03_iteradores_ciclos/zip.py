nombres = ["Paco","Emilio","Javier"]
apellidos = ["Botero","Tafur","Quinonez"]

#La funcion zip une en tuplas cada nombre con su apellido

nombre_completo = list(zip(nombres,apellidos))
print(list(nombre_completo)) #[('Paco', 'Botero'), ('Emilio', 'Tafur'), ('Javier', 'Quinonez')]


nombres = ["Paco","Emilio","Javier","Ana"]
apellidos = ["Botero","Tafur","Quinonez"]
nombre_completo1 = list(zip(nombres,apellidos))
print(nombre_completo1) #[('Paco', 'Botero'), ('Emilio', 'Tafur'), ('Javier', 'Quinonez')]


print("\nDESENPAQUETAR")
nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

#Manejo de multiples iterables al mismo tiempo
for nombre, apellido in zip(nombres,apellidos):
    print(nombre,apellido)