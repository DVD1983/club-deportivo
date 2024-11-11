from db.repository import BaseDeDatos
from models.pago import Pago

class PagoController:
    def __init__(self):
        self.db = BaseDeDatos()

    def registrar_pago_socio(self, dni, tipo_cuota, deporte):
        from controllers import SocioController
        socio_controller = SocioController()

        socio = socio_controller.buscar_socio(dni)
        if not socio:
            return None, "Socio no encontrado."

        self.db.insertar_pago_socio(dni, tipo_cuota, deporte)

