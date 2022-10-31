from conexion.cursor import CursorPool as CursorPool
from modelos.contrato import Contrato
class ContratoDTO:
    @staticmethod
    def seleccionar():
        try:
            with CursorPool() as cp:
                cp.execute("SELECT * FROM contrato")
                contratos = [Contrato.fromTupla(tupla) for tupla in cp.fetchall()]
                return contratos
        except Exception as e:
            return None
    def seleccionarPorId(id):
        try:
            with CursorPool() as cp:
                cp.execute("SELECT * FROM contrato WHERE id = %s", (id,))
                contrato = Contrato.fromTupla(cp.fetchone())
                return contrato
        except Exception as e:
            return False
        
    def insertar(contrato = Contrato):
        try:
            with CursorPool() as cp:
                cp.execute("INSERT INTO contrato (costo, fecha_inicio, fecha_fin) VALUES (%s, %s, %s)", (contrato.costo, contrato.fecha_inicio, contrato.fecha_fin))
                return True
        except Exception as e:
            return False
    
    def actualizar(contrato = Contrato):
        try:
            with CursorPool() as cp:
                cp.execute("UPDATE contrato SET costo = %s, fecha_inicio = %s, fecha_fin = %s WHERE id = %s", (contrato.costo, contrato.fecha_inicio, contrato.fecha_fin, contrato.id))
                return True
        except Exception as e:
            return False
    def eliminar(id):
        try:
            with CursorPool() as cp:
                cp.execute("DELETE FROM contrato WHERE id = %s", (id,))
                return True
        except Exception as e:
            return False
