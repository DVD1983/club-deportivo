import tkinter as tk
from tkinter import ttk
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
        self.root.title("Gestor de Club 2024")
        self.root.geometry("500x600")
        self.root.configure(bg="#2E3B55")  # Fondo oscuro para un diseño moderno

        # Crear las tablas de la base de datos al inicio
        self.db = BaseDeDatos()
        self.db.crear_tablas()

        # Mostrar el menú
        self.mostrar_menu()

    def mostrar_menu(self):
        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear un frame para el menú
        menu_frame = tk.Frame(self.root, bg="#2E3B55")
        menu_frame.pack(expand=True)

        # Título y subtítulo estilizados
        tk.Label(menu_frame, text="Gestor de Club 2024", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#2E3B55").pack(pady=(20, 5))
        tk.Label(menu_frame, text="Menú Principal", font=("Arial", 18), fg="#CCCCCC", bg="#2E3B55").pack(pady=(0, 20))

        # Función para crear botones estilizados
        def crear_boton(texto, comando):
            boton = tk.Button(menu_frame, text=texto, command=comando,
                              font=("Arial", 14), bg="#4CAF50", fg="white",
                              activebackground="#45a049", activeforeground="white",
                              bd=0, highlightthickness=0, relief="flat",
                              width=25, pady=10, cursor="hand2")
            boton.bind("<Enter>", lambda e: boton.config(bg="#45a049"))
            boton.bind("<Leave>", lambda e: boton.config(bg="#4CAF50"))
            return boton

        # Botones de opciones en el menú
        botones = [
            ("Iniciar Sesión", self.abrir_login),
            ("Registrar Usuario", self.abrir_registrar_usuario),
            ("Agregar Cuota", self.abrir_agregar_cuota_view),
            ("Registrar Pago", self.registrar_pago_view),
            ("Generar Reporte Mensual", self.generar_reporte),
            ("Agregar Socio", self.abrir_agregar_socio_view)
        ]

        # Colocar botones en el menú
        for texto, comando in botones:
            crear_boton(texto, comando).pack(pady=10)

    def abrir_login(self):
        self.cambiar_vista(login_view)

    def abrir_registrar_usuario(self):
        self.cambiar_vista(lambda root: registro_usuario_view(root, self))

    def abrir_agregar_cuota_view(self):
        self.cambiar_vista(lambda root: agregar_cuota_view(root, self))

    def registrar_pago_view(self):
        self.cambiar_vista(lambda root: registrar_pago_view(root, self))

    def abrir_agregar_socio_view(self):
        self.cambiar_vista(lambda root: registro_socio_view(root, self))

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
