from db.repository import BaseDeDatos
from models.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.db = BaseDeDatos()

    def agregar_usuario(self, nombre, password, rol):
        try:
            self.db.insertar_usuario(nombre, password, rol)
            return True
        except Exception as e:
            raise Exception(e)

    def buscar_usuario(self, nombre):
        usuario = self.db.obtener_usuario(nombre)
        if usuario:
            return Usuario(usuario[1], usuario[2], usuario[3])
        return None
