lenguaje = {
    "nombre": "python",
    "creador": "Guido van Rossum"
}

for llave in lenguaje:
    print("llave:", llave)
    print("valor:", lenguaje[llave])
    print("\n")

print("\n")

#Usando keys y values
for element in lenguaje.keys():
    print(element)
print("\n")
for element in lenguaje.values():
    print(element)

print("\n")

#Con items(), retorna dos valores (en forma de una lista de tuplas)
for llave, valor in lenguaje.items():
    print(llave,", ", valor)
print("\n")
for elemento in lenguaje.items():
    print(elemento)