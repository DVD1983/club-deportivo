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

        # Verificar si la cuota existe
        cuota = self.db.obtener_cuota(tipo_cuota, deporte)
        if not cuota:
            return None, "La cuota no existe en la base de datos."

        self.db.insertar_pago_socio(dni, tipo_cuota, deporte)

    def registrar_pago_no_socio(self, nombre, tipo_cuota, deporte, dni):
        # Verificar si la cuota existe
        cuota = self.db.obtener_cuota(tipo_cuota, deporte)
        if not cuota:
            return None, "La cuota no existe en la base de datos."

        self.db.insertar_pago_no_socio(dni, tipo_cuota, deporte)
