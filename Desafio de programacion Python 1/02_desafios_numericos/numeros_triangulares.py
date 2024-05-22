def triangular(n):
    if n == 1:
        return 1
    
    return n+triangular(n-1)

print(triangular(2))
print(triangular(4))
print(triangular(6))

#########################Solucion del curso #########################

#Por ciclo
def numero_triangular(numero):
    triangular = 0
    for i in range(1,numero+1):
        triangular += i
    return triangular

print(numero_triangular(2))
print(numero_triangular(4))
print(numero_triangular(6))

#####################################################################