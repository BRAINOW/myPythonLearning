#permiten guardar elementos unicos
#definidos entre llaves
#separados entre comas

set1 = {1,2,3}
print(set1)

#print set1[0] #error

#Solo pueden tener un elemento igual
set2 = {1,1,2,3}
print(set2)

set3 = {1,2.0,"string"}
print(set3)

#Los sets son inmutables pero podemos agregar elementos usando .add()
set1.add(4)
print(set1)

set1.update([4,5,6]) #El 4 solo esta 1 vez
print(set1)

print(len(set1))

#Eliminar elementos del set con .discard()
set1.discard(2)
set1.discard(2) #Como ya no existe no lo remueve pero no tira error
print(set1)

set1.remove(3)
print(set1)
#set1.remove(3) #Como ya no existe la funcion remove tira error
print(set1)

set1.clear()
print(set1)