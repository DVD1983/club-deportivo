from db.repository import BaseDeDatos
from controllers import UsuarioController
from models.usuario import Usuario

class LoginController:
    def __init__(self):
        self.db = BaseDeDatos()
        self.usuario_controller = UsuarioController()

    def verificar_password(self, nombre, password):
        usuario:Usuario = self.usuario_controller.buscar_usuario(nombre)
        if usuario:
            if usuario.password == password:
                return True
        return False