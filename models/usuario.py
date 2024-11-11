class Usuario:
    def __init__(self, nombre, password, rol):
        self.nombre = nombre
        self.password = password
        self.rol = rol
    
    def __str__(self):
        return f"{self.nombre} ({self.rol})"