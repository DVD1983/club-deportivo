import tkinter as tk
from tkinter import messagebox
from controllers import UsuarioController
def registro_usuario_view(root):
    usuario_controller = UsuarioController()

    def agregar_usuario():
        nombre = entry_nombre.get()
        password = entry_password.get()
        rol = entry_rol.get()

        # Validar que ambos campos están llenos
        if nombre and password and rol:
            # Llamar al controlador para agregar el usuario
            resultado = usuario_controller.agregar_usuario(nombre, password, rol)
            if resultado:
                messagebox.showinfo("Éxito", f"Usuario {nombre} agregado como {rol}.")
            else:
                messagebox.showerror("Error", "No se pudo agregar al usuario.")
            
            # Limpiar los campos después de agregar el usuario
            entry_nombre.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            entry_rol.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor ingrese nombre, contraseña y rol.")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1)

    tk.Label(root, text="Contraseña:").grid(row=1, column=0)
    entry_password = tk.Entry(root)
    entry_password.grid(row=1, column=1)

    tk.Label(root, text="Rol:").grid(row=2, column=0)
    entry_rol = tk.Entry(root)
    entry_rol.grid(row=2, column=1)

    tk.Button(root, text="Registrar Usuario", command=agregar_usuario).grid(row=3, column=0, columnspan=2)

    root.mainloop()
