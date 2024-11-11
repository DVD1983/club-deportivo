import tkinter as tk
from tkinter import messagebox
from db.repository import BaseDeDatos
from views import login_view, registro_socio_view, registro_usuario_view, agregar_cuota_view, registrar_pago_view
from controllers import PagoController, CuotaController, UsuarioController

class MainApp:
    def __init__(self, root):
        # Instanciar los controladores
        self.usuario_controller = UsuarioController()
        self.cuota_controller = CuotaController()
        self.pago_controller = PagoController()

        self.root = root
        self.root.title("Menú Principal")
        
        # Crear las tablas de la base de datos al inicio
        self.db = BaseDeDatos()
        self.db.crear_tablas()

        # Mostrar el menú
        self.mostrar_menu()

    def mostrar_menu(self):
        # Crear un frame para el menú
        menu_frame = tk.Frame(self.root)
        menu_frame.pack()

        tk.Label(menu_frame, text="Gestor de club 2024").pack(pady=10)
        tk.Label(menu_frame, text="Menú Principal").pack(pady=10)

        tk.Button(menu_frame, text="Iniciar Sesión", command=self.abrir_login).pack(pady=10)
        tk.Button(menu_frame, text="Registrar Usuario", command=self.abrir_registrar_usuario).pack(pady=10)
        tk.Button(menu_frame, text="Agregar Cuota", command=self.abrir_agregar_cuota_view).pack(pady=10)
        tk.Button(menu_frame, text="Registrar Pago", command=self.registrar_pago_view).pack(pady=10)
        tk.Button(menu_frame, text="Generar Reporte Mensual", command=self.generar_reporte).pack(pady=10)
        tk.Button(menu_frame, text="Agregar socio", command=self.abrir_agregar_socio_view).pack(pady=10)

    def abrir_login(self):
        self.cambiar_vista(login_view)

    def abrir_registrar_usuario(self):
        self.cambiar_vista(registro_usuario_view)

    def abrir_agregar_cuota_view(self):
        self.cambiar_vista(agregar_cuota_view)

    def registrar_pago_view(self):
        self.cambiar_vista(registrar_pago_view)

    def abrir_agregar_socio_view(self):
        self.cambiar_vista(registro_socio_view)

    def generar_reporte(self):
        reporte = self.club.generar_reporte_mensual()
        messagebox.showinfo("Reporte Mensual", reporte)

    def cambiar_vista(self, vista):
        for widget in self.root.winfo_children():
            widget.destroy()  # Eliminar widgets de la vista actual
        vista(self.root)  # Llamar a la nueva vista

# Ejecutar el menú solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
