import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controllers import UsuarioController

def registro_usuario_view(root, app):
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

    # Limpiar la ventana actual
    for widget in root.winfo_children():
        widget.destroy()

    # Configuración de la ventana y estilos
    root.title("Registro de Usuario")
    root.geometry("450x300")
    root.configure(bg="#f0f0f0")  # Fondo gris claro

    # Crear marco principal
    main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    main_frame.pack(expand=True)

    # Título de la vista
    tk.Label(main_frame, text="Registrar Usuario", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Etiquetas y entradas de texto
    tk.Label(main_frame, text="Nombre:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="e", pady=5)
    entry_nombre = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Contraseña:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky="e", pady=5)
    entry_password = tk.Entry(main_frame, font=("Arial", 12), show="*", width=25, bd=2, relief="solid")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Rol:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=3, column=0, sticky="e", pady=5)
    entry_rol = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")
    entry_rol.grid(row=3, column=1, padx=10, pady=5)

    # Botón de registro de usuario con efecto hover
    registrar_button = tk.Button(main_frame, text="Registrar Usuario", font=("Arial", 12, "bold"), width=20, bg="#4cae4c", fg="white", bd=0, relief="flat", command=agregar_usuario)
    registrar_button.grid(row=4, column=0, columnspan=2, pady=20)

    def on_enter(e):
        registrar_button.config(bg="#5cb85c")

    def on_leave(e):
        registrar_button.config(bg="#4cae4c")

    registrar_button.bind("<Enter>", on_enter)
    registrar_button.bind("<Leave>", on_leave)

    # Botón para volver al menú principal con efecto hover
    volver_button = tk.Button(main_frame, text="Volver al Menú Principal", font=("Arial", 12, "bold"), width=20, bg="#cccccc", fg="#333", bd=0, relief="flat", command=app.mostrar_menu)
    volver_button.grid(row=5, column=0, columnspan=2, pady=10)

    def on_volver_enter(e):
        volver_button.config(bg="#bbbbbb")

    def on_volver_leave(e):
        volver_button.config(bg="#cccccc")

    volver_button.bind("<Enter>", on_volver_enter)
    volver_button.bind("<Leave>", on_volver_leave)

    root.mainloop()
