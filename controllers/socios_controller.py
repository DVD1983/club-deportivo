from db.repository import BaseDeDatos
from models.socio import Socio

class SocioController:
    def __init__(self):
        self.db = BaseDeDatos()

    def agregar_socio(self, nombre, dni):
        try:
            self.db.insertar_socio(nombre, dni)
            return True
        except Exception as e:
            raise Exception(e)

    def buscar_socio(self, dni):
        socio = self.db.obtener_socio(dni)
        if socio:
            return Socio(socio[0], socio[1])
        return None
