from conexion.cursor import CursorPool as CursorPool
from modelos.persona import Persona
from modelos.contrato import Contrato

class PersonaDTO:
    @staticmethod
    def seleccionar():
        try:
            with CursorPool() as cp:
                cp.execute("SELECT * FROM persona")
                personas = [Persona.fromTupla(tupla) for tupla in cp.fetchall()]
                return personas
        except Exception as e:
            return None
    
    def seleccionarPorId(id):
        try:
            with CursorPool() as cp:
                cp.execute("SELECT * FROM persona WHERE id = %s", (id,))
                persona = Persona.fromTupla(cp.fetchone())
                return persona
        except Exception as e:
            return False
        
    def seleccionarContratosPorCorreo(correo):
        
        try: 
            with CursorPool() as cp:
                cp.execute("SELECT c.* FROM contrato as c join contrato_persona as cp on c.id= cp.id_contrato join persona as p on p.id = cp.id_persona  WHERE p.correo = %s", (correo,))
                contratos = [Contrato.fromTupla(tupla) for tupla in cp.fetchall()]
                return contratos
        except Exception as e:
            return False
   
    
    def insertar(persona = Persona):
        try:
            with CursorPool() as cp:
                cp.execute("INSERT INTO persona (nombre, edad, correo) VALUES (%s, %s, %s)", (persona.nombre, persona.edad, persona.correo))
                return True
        except Exception as e:
            return False
        
    def actualizar(persona = Persona):
        try:
            with CursorPool() as cp:
                cp.execute("UPDATE persona SET nombre = %s, edad = %s, correo = %s WHERE id = %s", (persona.nombre, persona.edad, persona.correo, persona.id))
                return True
        except Exception as e:
            return False
    def eliminar(id):
        try:
            with CursorPool() as cp:
                cp.execute("DELETE FROM persona WHERE id = %s", (id,))
                return True
        except Exception as e:
            return False