class Persona:
    atributo = 123

    def __init__(self, nombre, edad):
        print("Estoy en el constructor") #Se ejecuta al crear el objeto
        self.nombre  = nombre
        self.edad = edad

    def cumplir_anyos(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.nombre}, ahora tienes {self.edad}")

class Empleado(Persona): #Hereda de Persona

    def __init__(self,horas_totales,nombre,edad):
        super(Empleado,self).__init__(nombre,edad)
        self.horas_totales = horas_totales

    def trabajar (self, horas):
        self.horas_totales += horas
        print(f"Usted ha trabajado {horas} horas")
        print(f"Horas totales: {self.horas_totales}")

paco = Empleado(nombre="Paco",edad=20,horas_totales=30) #Hay que especificar bien los parametros
paco.trabajar(8)
paco.cumplir_anyos()