lenguajes = ["Python","Java","Golang"]

#impresion con for-in
for element in lenguajes:
    print(element)

print("\n")

#impresion con for + range
for index in range(len(lenguajes)):
    print(lenguajes[index], index)

print("\n")

#impresion de una lista con while
i = 0
while i < len(lenguajes):
    print(lenguajes[i], i)
    i += 1