import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controllers import UsuarioController

def registro_usuario_view(root):
    usuario_controller = UsuarioController()

    def agregar_usuario():
        nombre = entry_nombre.get()
        password = entry_password.get()
        rol = entry_rol.get()

        if nombre and password and rol:
            if len(password) < 6:
                messagebox.showwarning("Error", "La contraseña debe tener al menos 6 caracteres.")
                return

            resultado = usuario_controller.agregar_usuario(nombre, password, rol)
            if resultado:
                messagebox.showinfo("Éxito", f"Usuario {nombre} agregado como {rol}.")
            else:
                messagebox.showerror("Error", "No se pudo agregar al usuario.")
            
            entry_nombre.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            entry_rol.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor ingrese nombre, contraseña y rol.")

    # Configuración de estilos
    style = ttk.Style()
    root.title("Registro de Usuario")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")  # Fondo gris claro
    
    # Estilos generales en negrita para etiquetas
    style.configure("TLabel", font=("Arial", 12, "bold"), background="#f0f0f0", foreground="#333")
    
    # Estilos generales para las entradas
    style.configure("TEntry", font=("Arial", 11), padding=5)
    
    # Estilo para el botón con fondo verde y texto blanco
    style.configure("GreenButton.TButton",
                    font=("Arial", 12, "bold"),
                    padding=10,
                    relief="flat",
                    background="#4caf50",  # Fondo verde
                    foreground="#fff")  # Letras blancas
    
    style.map("GreenButton.TButton",
              background=[("active", "#45a049")])  # Color verde más oscuro al hacer clic

    # Destruir los widgets actuales
    for widget in root.winfo_children():
        widget.destroy()

    # Etiquetas y entradas con estilo
    ttk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=20, sticky="e")
    entry_nombre = ttk.Entry(root, width=30)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="Contraseña:").grid(row=1, column=0, padx=10, pady=20, sticky="e")
    entry_password = ttk.Entry(root, show="*", width=30)
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(root, text="Rol:").grid(row=2, column=0, padx=10, pady=20, sticky="e")
    entry_rol = ttk.Entry(root, width=30)
    entry_rol.grid(row=2, column=1, padx=10, pady=10)

    # Botón de registro con fondo verde y texto blanco
    button = ttk.Button(root, text="Registrar Usuario", command=agregar_usuario, style="GreenButton.TButton")
    button.grid(row=3, column=0, columnspan=2, pady=30)
    button.place(relx=0.5, rely=0.7, anchor="center")  # Centra el botón en el widget

    root.mainloop()
