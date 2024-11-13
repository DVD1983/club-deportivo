import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controllers import SocioController

def registro_socio_view(root, app):
    socio_controller = SocioController()

    def agregar_socio():
        nombre = entry_nombre.get()
        dni = entry_dni.get()

        if nombre and dni:
            resultado = socio_controller.agregar_socio(nombre, dni)
            if resultado:
                messagebox.showinfo("Éxito", f"Socio {nombre} con DNI: {dni} agregado.")
            else:
                messagebox.showerror("Error", "No se pudo agregar al socio.")
            
            entry_nombre.delete(0, tk.END)
            entry_dni.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor ingrese nombre y dni.")

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#f0f0f0")
    root.title("Registro de Socio")
    root.geometry("450x300")

    main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    main_frame.pack(expand=True)

    tk.Label(main_frame, text="Registrar Socio", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

    tk.Label(main_frame, text="Nombre:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="e", pady=5)
    entry_nombre = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")
    entry_nombre.grid(row=1, column=1, pady=5, padx=10)

    tk.Label(main_frame, text="DNI:", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky="e", pady=5)
    entry_dni = tk.Entry(main_frame, font=("Arial", 12), width=25, bd=2, relief="solid")
    entry_dni.grid(row=2, column=1, pady=5, padx=10)

    registrar_button = tk.Button(main_frame, text="Registrar socio", font=("Arial", 12, "bold"), width=20, bg="#4cae4c", fg="white", bd=0, relief="flat", command=agregar_socio)
    registrar_button.grid(row=3, column=0, columnspan=2, pady=20)

    def on_enter(e):
        registrar_button.config(bg="#5cb85c")

    def on_leave(e):
        registrar_button.config(bg="#4cae4c")

    registrar_button.bind("<Enter>", on_enter)
    registrar_button.bind("<Leave>", on_leave)

    volver_button = tk.Button(main_frame, text="Volver al Menú Principal", font=("Arial", 12, "bold"), width=20, bg="#cccccc", fg="#333", bd=0, relief="flat", command=app.mostrar_menu)
    volver_button.grid(row=4, column=0, columnspan=2, pady=10)

    def on_volver_enter(e):
        volver_button.config(bg="#bbbbbb")

    def on_volver_leave(e):
        volver_button.config(bg="#cccccc")

    volver_button.bind("<Enter>", on_volver_enter)
    volver_button.bind("<Leave>", on_volver_leave)

    root.mainloop()
