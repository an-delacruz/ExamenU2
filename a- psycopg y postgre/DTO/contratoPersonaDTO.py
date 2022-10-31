from conexion.cursor import CursorPool as CursorPool
from modelos.contratoPersona import ContratoPersona

class ContratoPersonaDTO:
    
    @staticmethod
    def seleccionar():
        try:
            with CursorPool() as cp:
                cp.execute("SELECT * FROM contrato_persona")
                contratosPersonas = [ContratoPersona.fromTupla(tupla) for tupla in cp.fetchall()]
                return contratosPersonas
        except Exception as e:
            return None
        
    def seleccionarPorId(id):
        try:
            with CursorPool() as cp:
                cp.execute("SELECT * FROM contrato_persona WHERE id = %s", (id,))
                contratoPersona = ContratoPersona.fromTupla(cp.fetchone())
                return contratoPersona
            
        except Exception as e:
            return False
        
    def insertar(contratoPersona = ContratoPersona):
        try:
            with CursorPool() as cp:
                cp.execute("INSERT INTO contrato_persona (id_contrato, id_persona) VALUES (%s, %s)", (contratoPersona.id_contrato, contratoPersona.id_persona))
                return True
        except Exception as e:
            return False
