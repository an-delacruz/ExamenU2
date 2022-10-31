class Contrato:
    id = 0
    no_contrato = 0
    costo = 0
    fecha_inicio = ''
    fecha_fin = ''

    def __init__(self,  costo,fecha_inicio, fecha_fin,no_contrato = 0, id = 0):
        self.id = id
        self.no_contrato = no_contrato
        self.costo = costo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    @classmethod
    def fromTupla(cls, tupla):
        return cls( tupla[2], tupla[3],tupla[4],tupla[1], tupla[0])

    def __str__(self) -> str:
        return f'Id: {self.id}\nNo. Contrato: {self.no_contrato}\nCosto: {self.costo}\nFecha Inicio: {self.fecha_inicio}\nFecha Fin: {self.fecha_fin}'