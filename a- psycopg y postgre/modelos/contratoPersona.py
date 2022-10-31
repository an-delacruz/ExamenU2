class ContratoPersona:
    id = 0
    id_persona = 0
    id_contrato = 0

    def __init__(self, id_contrato,id_persona, id = 0):
        self.id = id
        self.id_persona = id_persona
        self.id_contrato = id_contrato
        
    @classmethod
    def fromTupla(cls, tupla):
        return cls( tupla[1], tupla[2], tupla[0])

    def __str__(self) -> str:
        return f'Id: {self.id}\nId Persona: {self.id_persona}\nId Contrato: {self.id_contrato}'