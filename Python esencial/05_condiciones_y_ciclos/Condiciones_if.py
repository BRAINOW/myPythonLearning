a = 1
b = 2

if a <  b :
    print("a es menor que b")


a = False
if a:
    print("A es Verdadero")
else:
    print("A es Falso")


a = 3
if a <  b :
    print("a es menor que b")
elif a > b :
    print("a es mayor que b")
else: # a==b
    print("a es igual que b")


if type(a) is bool:
    print("A es Boleano")
else:
    print("A es otro tipo de dato")


b = 3
a = 2
c = 1

if a <  b and a > c :
    print("1")
elif a > b and c>b :
    print("2")
else: 
    print("3")