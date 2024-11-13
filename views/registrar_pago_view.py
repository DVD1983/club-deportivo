import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controllers import PagoController

def registrar_pago_view(root, app):
    pago_controller = PagoController()

    def registrar_pago():
        tipo_cuota = tipo_var.get()
        deporte = deporte_pago_var.get()

        if tipo_cuota in ["Social", "Deportiva"]:
            numero_socio = entry_numero_socio.get()
            if not numero_socio:
                messagebox.showwarning("Error", "Por favor ingrese el número de socio.")
                return

            resultado, message = pago_controller.registrar_pago_socio(numero_socio, tipo_cuota, deporte)
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

            resultado, message = pago_controller.registrar_pago_no_socio(nombre, tipo_cuota, deporte, dni)
            if resultado is None:
                messagebox.showwarning("Error", message)
            else:
                messagebox.showinfo("Éxito", "Pago registrado correctamente.")

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

    root.title("Registro de Pago")
    root.geometry("450x400")
    root.configure(bg="#f0f0f0")

    main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    main_frame.pack(expand=True)

    tk.Label(main_frame, text="Registrar Pago", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

    tk.Label(main_frame, text="Tipo:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="e", pady=5)
    tipo_var = tk.StringVar()
    tipo_var.set("Seleccione")
    tipo_menu = ttk.OptionMenu(main_frame, tipo_var, "Seleccione", "Social", "No social", "Deportiva", "Invitado", command=actualizar_formulario)
    tipo_menu.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Deporte:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky="e", pady=5)
    deporte_pago_var = tk.StringVar()
    deporte_pago_var.set("Seleccione")
    deporte_menu = ttk.OptionMenu(main_frame, deporte_pago_var, "Seleccione", "Fútbol", "Vóley", "Básquet")
    deporte_menu.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Número de Socio:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=3, column=0, sticky="e", pady=5)
    entry_numero_socio = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")

    tk.Label(main_frame, text="Nombre:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=3, column=0, sticky="e", pady=5)
    entry_nombre = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")

    tk.Label(main_frame, text="DNI:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=4, column=0, sticky="e", pady=5)
    entry_dni = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")

    registrar_button = tk.Button(main_frame, text="Registrar Pago", font=("Arial", 12, "bold"), width=20, bg="#4cae4c", fg="white", bd=0, relief="flat", command=registrar_pago)
    registrar_button.grid(row=5, column=0, columnspan=2, pady=20)

    def on_enter(e):
        registrar_button.config(bg="#5cb85c")

    def on_leave(e):
        registrar_button.config(bg="#4cae4c")

    registrar_button.bind("<Enter>", on_enter)
    registrar_button.bind("<Leave>", on_leave)

    volver_button = tk.Button(main_frame, text="Volver al Menú Principal", font=("Arial", 12, "bold"), width=20, bg="#cccccc", fg="#333", bd=0, relief="flat", command=app.mostrar_menu)
    volver_button.grid(row=6, column=0, columnspan=2, pady=10)

    def on_volver_enter(e):
        volver_button.config(bg="#bbbbbb")

    def on_volver_leave(e):
        volver_button.config(bg="#cccccc")

    volver_button.bind("<Enter>", on_volver_enter)
    volver_button.bind("<Leave>", on_volver_leave)

    entry_numero_socio.grid_remove()
    entry_nombre.grid_remove()
    entry_dni.grid_remove()

    root.mainloop()
