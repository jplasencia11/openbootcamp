class Persona:
    edad=0
    nombre=""
    telefono=0

    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def getInfo(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Telefono: {self.telefono}")

class Cliente (Persona):
    credito = ""
    
    def __init__(self, nombre, edad, telefono, credito):
        super().__init__(nombre, edad, telefono)
        self.credito = credito

    def getInfo(self):
        info = super().getInfo() + (f", Crédito: {self.credito}")
        return (info)

class trabajador (Persona):
    salario = 0
    
    def __init__(self, nombre, edad, telefono, salario):
        super().__init__(nombre, edad, telefono)
        self.salario = salario

    def getInfo(self):
        info = super().getInfo() + (f", Salario: {self.salario}")
        return (info)

if __name__=='__main__':
    t1= trabajador("Juan Loya", 42, 563218590, 2350)
    print (t1.getInfo())
    c1= Cliente("Robert Guerra", 28, 632251852,"Pyme")
    print (c1.getInfo())
    p1= Persona("Marlon Correa", 25, 523694501)
    print (p1.getInfo())