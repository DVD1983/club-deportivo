import tkinter as tk
from tkinter import messagebox
from controllers import PagoController

def registrar_pago_view(root):
    pago_controller = PagoController()

    def registrar_pago():
        tipo_cuota = tipo_var.get()
        deporte = deporte_pago_var.get()

        if tipo_cuota in ["Social", "Deportiva"]:
            numero_socio = entry_numero_socio.get()
            if not numero_socio:
                messagebox.showwarning("Error", "Por favor ingrese el número de socio.")
                return

            # Llamar al método del controller y capturar el mensaje
            resultado, message = pago_controller.registrar_pago_socio(numero_socio, tipo_cuota, deporte)

            # Si el resultado es None, significa que hubo un error (por ejemplo, no encontrado)
            if resultado is None:
                messagebox.showwarning("Error", message)
            else:
                messagebox.showinfo("Éxito", "Pago registrado correctamente.")

        else:
            nombre = entry_nombre.get()
            dni = entry_dni.get()
            if not nombre or not dni:
                messagebox.showwarning("Error", "Por favor ingrese el nombre y el DNI.")
                return

            # Llamar al método del controller y capturar el mensaje
            resultado, message = pago_controller.registrar_pago_no_socio(nombre, tipo_cuota, deporte, dni)

            # Si el resultado es None, significa que hubo un error (por ejemplo, no encontrado)
            if resultado is None:
                messagebox.showwarning("Error", message)
            else:
                messagebox.showinfo("Éxito", "Pago registrado correctamente.")

        # Limpiar entradas después del registro
        entry_numero_socio.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_dni.delete(0, tk.END)
    
    def actualizar_formulario(event=None):
        tipo_cuota = tipo_var.get()
        if tipo_cuota in ["Social", "Deportiva"]:
            entry_numero_socio.grid(row=3, column=1)
            entry_nombre.grid_remove()
            entry_dni.grid_remove()
        else:
            entry_numero_socio.grid_remove()
            entry_nombre.grid(row=3, column=1)
            entry_dni.grid(row=4, column=1)

    for widget in root.winfo_children():
        widget.destroy()

    # Tipo de cuota
    tk.Label(root, text="Tipo:").grid(row=0, column=0)
    tipo_var = tk.StringVar()
    tipo_var.set("Seleccione")
    tipo_menu = tk.OptionMenu(root, tipo_var, "Social", "No social", "Deportiva", "Invitado", command=actualizar_formulario)
    tipo_menu.grid(row=0, column=1)

    # Deporte
    tk.Label(root, text="Deporte:").grid(row=1, column=0)
    deporte_pago_var = tk.StringVar()
    deporte_pago_var.set("Seleccione")
    tk.OptionMenu(root, deporte_pago_var, "Fútbol", "Vóley", "Básquet").grid(row=1, column=1)

    # Campos para "Social" o "Deportiva" (Número de socio)
    tk.Label(root, text="Número de Socio:").grid(row=3, column=0)
    entry_numero_socio = tk.Entry(root)

    # Campos para "No social" o "Invitado" (Nombre y DNI)
    tk.Label(root, text="Nombre:").grid(row=3, column=0)
    entry_nombre = tk.Entry(root)

    tk.Label(root, text="DNI:").grid(row=4, column=0)
    entry_dni = tk.Entry(root)

    # Botón para registrar el pago
    tk.Button(root, text="Registrar Pago", command=registrar_pago).grid(row=5, column=0, columnspan=2)

    # Inicialmente, ocultamos los campos específicos hasta que se seleccione el tipo de cuota
    entry_numero_socio.grid_remove()
    entry_nombre.grid_remove()
    entry_dni.grid_remove()
