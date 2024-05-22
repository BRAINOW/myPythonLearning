"""
enumerate(iterable,start=0)
"""

#en cada iteracion tienes el objeto iterable y su posicion en la lista

nombres = ["Paco","Emilio","Javier","Ana"]
nombres_enumerados = enumerate(nombres)
print(list(nombres_enumerados)) #[(0, 'Paco'), (1, 'Emilio'), (2, 'Javier'), (3, 'Ana')]

nombres_enumerados = enumerate(nombres,start=5)
print(list(nombres_enumerados)) #[(5, 'Paco'), (6, 'Emilio'), (7, 'Javier'), (8, 'Ana')]

for indice, elemento in enumerate(nombres):
    print(indice,elemento)
        #0 Paco
        #1 Emilio
        #2 Javier
        #3 Ana