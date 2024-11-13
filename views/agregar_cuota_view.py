import tkinter as tk
from tkinter import ttk, messagebox
from controllers import CuotaController

def agregar_cuota_view(root, app):
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

    # Cambiar el fondo de la ventana
    root.configure(bg="#f0f0f0")  # Fondo gris claro
    root.title("Agregar Cuota")
    root.geometry("450x350")

    # Crear el marco principal para los elementos de entrada
    main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    main_frame.pack(expand=True)

    # Título de la vista
    tk.Label(main_frame, text="Agregar Cuota", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Etiquetas y campos de entrada con los nuevos estilos
    tk.Label(main_frame, text="Tipo:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="e", pady=5)
    entry_tipo = tk.StringVar(value="Social")
    tk.OptionMenu(main_frame, entry_tipo, "Social", "No social", "Deportiva", "Invitado").grid(row=1, column=1, pady=5, sticky="w")

    tk.Label(main_frame, text="Deporte:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky="e", pady=5)
    entry_deporte = tk.StringVar(value="Fútbol")
    tk.OptionMenu(main_frame, entry_deporte, "Fútbol", "Vóley", "Básquet").grid(row=2, column=1, pady=5, sticky="w")

    tk.Label(main_frame, text="Monto:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=3, column=0, sticky="e", pady=5)
    entry_monto = tk.Entry(main_frame, font=("Arial", 12), width=20, bd=2, relief="solid")
    entry_monto.grid(row=3, column=1, pady=5)

    # Botón Agregar Cuota
    agregar_button = tk.Button(main_frame, text="Agregar Cuota", font=("Arial", 12, "bold"), width=20, bg="#4cae4c", fg="white", bd=0, relief="flat", command=agregar_cuota)
    agregar_button.grid(row=4, column=0, columnspan=2, pady=20)

    # Efecto de hover para el botón
    def on_enter(e):
        agregar_button.config(bg="#5cb85c")

    def on_leave(e):
        agregar_button.config(bg="#4cae4c")

    agregar_button.bind("<Enter>", on_enter)
    agregar_button.bind("<Leave>", on_leave)

    # Botón Volver al menú principal
    volver_button = tk.Button(main_frame, text="Volver al Menú Principal", font=("Arial", 12, "bold"), width=20, bg="#cccccc", fg="#333", bd=0, relief="flat", command=app.mostrar_menu)
    volver_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Efecto de hover para el botón Volver
    def on_volver_enter(e):
        volver_button.config(bg="#bbbbbb")

    def on_volver_leave(e):
        volver_button.config(bg="#cccccc")

    volver_button.bind("<Enter>", on_volver_enter)
    volver_button.bind("<Leave>", on_volver_leave)

    root.mainloop()
