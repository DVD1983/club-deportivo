class Cuota:
    def __init__(self, tipo, monto, frecuencia, deporte=None):
        self.tipo = tipo  # 'social', 'deportiva'
        self.monto = monto
        self.frecuencia = frecuencia  # 'mensual', 'anual', 'por clase'
        self.deporte = deporte
    
    def __str__(self):
        deporte_str = f" - Deporte: {self.deporte.nombre}" if self.deporte else ""
        return f"{self.tipo.capitalize()} - {self.monto} ({self.frecuencia}){deporte_str}"
