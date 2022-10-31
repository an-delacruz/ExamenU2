from statistics import correlation


class Persona:
    id = 0
    nombre = '' 
    edad = 0
    correo = ''
    
    def __init__(self, nombre, edad, correo, id = 0):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        
        
    @classmethod
    def fromTupla(cls, tupla):
        return cls(tupla[1], tupla[2], tupla[3], tupla[0])

    def __str__(self):
        return f'Id: {self.id}\nNombre: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo}'