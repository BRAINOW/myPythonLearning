class Persona:
    #Atributo normal, es el moismo para todos los objetos de la clase
    atributo = 123

    #los atributos de instancia se definen dentro del constructor de la clase
    def __init__(self, nombre, edad):
        print("Estoy en el constructor") #Se ejecuta al crear el objeto
        self.nombre  = nombre
        self.edad = edad

    def cumplir_anyos(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.nombre}, ahora tienes {self.edad}")

paco = Persona(nombre="paco", edad=20)

##podemos acceder a los atributos de la clase
print("Nombre", paco.nombre)
print("Edad", paco.edad)

print(paco.atributo)

paco.cumplir_anyos()
