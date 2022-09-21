class Persona:
    def __init__(self):
        self._edad = 0
        self._nombre = 0
        self._telefono = 0

    def get_edad(self):
        return self._edad 
    def get_nombre(self):
        return self._nombre
    def get_telefono(self):
        return self._telefono

    def set_edad(self, a):
        self._edad  = a
    def set_nombre(self, b):
        self._nombre = b
    def set_telefono(self, c):
        self._telefono = c
    
    edad  = property(get_edad, set_edad)
    nombre  = property(get_nombre, set_nombre)
    telefono  = property(get_telefono, set_telefono)

mark = Persona()

mark.edad  = 10

mark.nombre  = "Raul Rodrigues"

mark.telefono = 603819201

print("Edad de la persona:")
print(mark.edad )
print("Nombre de la persona:")
print(mark.nombre)
print("Telefono de la persona:")
print(mark.telefono)