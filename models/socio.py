class Socio:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
    
    def __str__(self):
        return f"{self.nombre} ({self.dni})"