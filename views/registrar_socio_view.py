import tkinter as tk
from tkinter import messagebox
from controllers import SocioController

def registro_socio_view(root):
    socio_controller = SocioController()

    def agregar_socio():
        nombre = entry_nombre.get()
        dni = entry_dni.get()

        # Validar que ambos campos están llenos
        if nombre and dni:
            # Llamar al controlador para agregar el socio
            resultado = socio_controller.agregar_socio(nombre, dni)
            if resultado:
                messagebox.showinfo("Éxito", f"Socio {nombre} con DNI: {dni} agregado.")
            else:
                messagebox.showerror("Error", "No se pudo agregar al socio.")
            
            # Limpiar los campos después de agregar el socio
            entry_nombre.delete(0, tk.END)
            entry_dni.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor ingrese nombre y dni.")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1)

    tk.Label(root, text="Dni:").grid(row=1, column=0)
    entry_dni = tk.Entry(root)
    entry_dni.grid(row=1, column=1)

    tk.Button(root, text="Registrar socio", command=agregar_socio).grid(row=2, column=0, columnspan=2)

    root.mainloop()
