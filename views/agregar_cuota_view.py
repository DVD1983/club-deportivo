import tkinter as tk
from tkinter import ttk
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
                entry_tipo.set("Social")  # Restablecer al valor predeterminado
                entry_monto.delete(0, tk.END)
                entry_deporte.set("Fútbol")  # Restablecer al valor predeterminado
            except ValueError:
                messagebox.showwarning("Error", "El monto debe ser un número.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese todos los datos de la cuota.")

    # Limpiar la ventana actual
    for widget in root.winfo_children():
        widget.destroy()

    # Configuración de estilos
    style = ttk.Style()
    root.title("Agregar Cuota")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")  # Fondo gris claro
    
    # Estilos generales en negrita para etiquetas
    style.configure("TLabel", font=("Arial", 12, "bold"), background="#f0f0f0", foreground="#333")
    
    # Estilos generales para las entradas
    style.configure("TEntry", font=("Arial", 11), padding=5)
    
    # Estilo para el botón con fondo blanco, texto verde y negrita
    style.configure("WhiteGreenButton.TButton",
                    font=("Arial", 12, "bold"),  # Texto en negrita
                    padding=10,
                    relief="solid",  # Borde sólido
                    background="#fff",  # Fondo blanco
                    foreground="#4caf50",  # Texto verde
                    borderwidth=2)  # Borde más grueso

    style.map("WhiteGreenButton.TButton",
              background=[("active", "#e0e0e0")],  # Fondo gris claro cuando el botón está activo
              foreground=[("active", "#388e3c")])  # Texto verde oscuro al hacer clic
    
    # Crear los widgets de entrada
    tk.Label(root, text="Tipo:").grid(row=0, column=0, padx=10, pady=20, sticky="e")
    entry_tipo = tk.StringVar()
    entry_tipo.set("Social")  # Establecer "Social" como la opción predeterminada
    tk.OptionMenu(root, entry_tipo, "Social", "No social", "Deportiva", "Invitado").grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Deporte:").grid(row=1, column=0, padx=10, pady=20, sticky="e")
    entry_deporte = tk.StringVar()
    entry_deporte.set("Fútbol")  # Establecer "Fútbol" como la opción predeterminada
    tk.OptionMenu(root, entry_deporte, "Fútbol", "Vóley", "Básquet").grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Monto:").grid(row=2, column=0, padx=10, pady=20, sticky="e")
    entry_monto = tk.Entry(root,width=30, font=("Arial", 11))
    entry_monto.grid(row=2, column=1, padx=10, pady=10)

    # Botón con estilo
    button = ttk.Button(root, 
                        text="Agregar Cuota", 
                        command=agregar_cuota, 
                        style="WhiteGreenButton.TButton")
    button.grid(row=3, column=0, columnspan=2, pady=30)
    button.place(relx=0.5, rely=0.7, anchor="center")  # Centra el botón en el widget

    root.mainloop()



