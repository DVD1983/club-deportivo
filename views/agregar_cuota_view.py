import tkinter as tk
from tkinter import messagebox
from controllers import CuotaController

def agregar_cuota_view(root):
    cuota_controller = CuotaController()

    def agregar_cuota():
        tipo = entry_tipo.get()
        monto = entry_monto.get()
        deporte = entry_deporte.get()

        if tipo and monto and deporte:
            try:
                monto = float(monto)
                cuota_controller.agregar_cuota(tipo, deporte, monto)
                messagebox.showinfo("Éxito", f"Cuota de tipo {tipo} de {deporte} por el monto {monto} agregada.")
                entry_tipo.delete(0, tk.END)
                entry_monto.delete(0, tk.END)
                entry_deporte.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Error", "El monto debe ser un número.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese todos los datos de la cuota.")

    for widget in root.winfo_children():
        widget.destroy()


    
    tk.Label(root, text="Tipo:").grid(row=0, column=0)
    entry_tipo = tk.StringVar()
    entry_tipo.set(None)
    tk.OptionMenu(root, entry_tipo, "Social", "No social", "Deportiva", "Invitado").grid(row=0, column=1)

    tk.Label(root, text="Deporte:").grid(row=1, column=0)
    entry_deporte = tk.StringVar()
    entry_deporte.set(None)
    tk.OptionMenu(root, entry_deporte, "Fútbol", "Vóley", "Básquet").grid(row=1, column=1)

    tk.Label(root, text="Monto:").grid(row=2, column=0)
    entry_monto = tk.Entry(root)
    entry_monto.grid(row=2, column=1)

    tk.Button(root, text="Agregar Cuota", command=agregar_cuota).grid(row=3, column=0, columnspan=2)
    
    root.mainloop()
