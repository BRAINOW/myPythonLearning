"""
range(inicio,fin,paso) #inicia en 0 y termina en n-1
"""

serie_1 = range(5) 
print(list(serie_1)) #[0, 1, 2, 3, 4]

serie_2 = range(5,10)
print(list(serie_2)) #[5, 6, 7, 8, 9]

serie_3 = range(3,10,2) 
print(list(serie_3)) #[3, 5, 7, 9]

for element in serie_3: #un rango es un elemento iterable
    print(element)