from datetime import datetime

class Pago:
    def __init__(self, usuario, cuota):
        self.usuario = usuario
        self.cuota = cuota
        self.fecha = datetime.now()
    
    def generar_comprobante(self):
        deporte_str = f" - Deporte: {self.cuota.deporte.nombre}" if self.cuota.deporte else ""
        return f"Comprobante:\nUsuario: {self.usuario.nombre}\nConcepto: {self.cuota.tipo}\nMonto: ${self.cuota.monto}\nFecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}{deporte_str}"
