from db.repository import BaseDeDatos
from models.cuota import Cuota

class CuotaController:
    def __init__(self):
        self.db = BaseDeDatos()

    def agregar_cuota(self, tipo, deporte, monto):
        self.db.insertar_cuota(tipo, deporte, monto)

    def listar_cuotas(self):
        cuotas = self.db.obtener_cuotas()
        # Convierte las cuotas a instancias de Cuota
        return [Cuota(cuota[0], cuota[1], cuota[2], cuota[3], cuota[4]) for cuota in cuotas]
