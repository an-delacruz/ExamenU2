from app import db

class Teclado(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    precio = db.Column(db.DECIMAL(10,2))
    unidades = db.Column(db.Integer)

    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Marca: {self.marca},'
                f'Modelo: {self.modelo},'
                f'Precio: {self.precio},'
                f'Unidades: {self.unidades}')
                
        
class Mouse(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    precio = db.Column(db.DECIMAL(10,2))
    unidades = db.Column(db.Integer)

    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Marca: {self.marca},'
                f'Modelo: {self.modelo},'
                f'Precio: {self.precio},'
                f'Unidades: {self.unidades}')

class Monitor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    tamanio = db.Column(db.String(50))
    precio = db.Column(db.DECIMAL(10,2))
    unidades = db.Column(db.Integer)

    
    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Marca: {self.marca},'
                f'Modelo: {self.modelo},'
                f'Tamaño: {self.tamanio},'
                f'Precio: {self.precio},'
                f'Unidades: {self.unidades}')
        
class Laptop(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    color = db.Column(db.String(50))
    precio = db.Column(db.DECIMAL(10,2))
    unidades = db.Column(db.Integer)    
    
    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Marca: {self.marca},'
                f'Modelo: {self.modelo},'
                f'Color: {self.color},'
                f'Precio: {self.precio},'
                f'Unidades: {self.unidades}')

class Accesorio(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    marca = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    precio = db.Column(db.DECIMAL(10,2))
    unidades = db.Column(db.Integer)    
    
    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Marca: {self.marca},'
                f'Descripción: {self.descripcion},'
                f'Precio: {self.precio},'
                f'Unidades: {self.unidades}')
