import tkinter as tk
from tkinter import messagebox
from controllers import LoginController

def login_view(root):
    login_controller = LoginController()

    def login():
        nombre = entry_nombre.get()
        password = entry_password.get()
        if nombre and password:
            if login_controller.verificar_password(nombre, password):
                messagebox.showinfo("Éxito", f"Bienvenido, {nombre}!")
            else:
                messagebox.showwarning("Error", "Nombre o contraseña incorrecta")
        else:
            messagebox.showwarning("Error", "Por favor ingrese nombre y contraseña.")

    # Limpiar la ventana actual antes de mostrar el login
    for widget in root.winfo_children():
        widget.destroy()

    # Cambiar el fondo de la ventana
    root.config(bg="#f0f0f0")

    # Crear el marco de login
    login_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    login_frame.grid(row=0, column=0, padx=50, pady=50)

    # Título con estilo moderno
    tk.Label(login_frame, text="Iniciar Sesión", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)

    # Etiquetas y campos de entrada estilizados
    tk.Label(login_frame, text="Nombre:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="w", pady=10)
    entry_nombre = tk.Entry(login_frame, font=("Arial", 12), width=25, bd=2, relief="solid")
    entry_nombre.grid(row=1, column=1, pady=5)

    tk.Label(login_frame, text="Contraseña:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky="w", pady=10)
    entry_password = tk.Entry(login_frame, font=("Arial", 12), width=25, show="*", bd=2, relief="solid")
    entry_password.grid(row=2, column=1, pady=5)

    # Función para cambiar el color del botón al pasar el mouse
    def on_enter(e):
        login_button.config(bg="#5cb85c", fg="white")

    def on_leave(e):
        login_button.config(bg="#4cae4c", fg="white")

    # Botón de inicio de sesión estilizado
    login_button = tk.Button(login_frame, text="Iniciar sesión", font=("Arial", 12), width=20, height=2, bg="#4cae4c", fg="white", bd=0, relief="flat", command=login)
    login_button.grid(row=3, column=0, columnspan=2, pady=15)

    # Añadir el efecto hover al botón
    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)
