import tkinter as tk
from tkinter import font, messagebox
from components.buttonStyle import boton_style
from app import create_contacto

def contact_save(modal, mostrar_products, name_entry, phone_entry):
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    print("Nombre:", name)
    print("Teléfono:", phone)
    if(name and phone):
        print("Validando datos...")
        print("Datos válidos, creando contacto...")
        create_contacto(name, phone)
        messagebox.showinfo("Éxito", "Contacto creado exitosamente.")
        modal.destroy()
        mostrar_products()
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

def create_Contact(ventana, mostrar_products):
    fuente_titulo = font.Font(family="Helvetica", size=20, weight="bold")
    fuente_label = font.Font(family="Helvetica", size=12, weight="normal")
    modal = tk.Toplevel(ventana)
    modal.geometry("400x300")
    modal.configure(bg="#1e1e1e")
    modal.transient(ventana)
    modal.attributes("-alpha", 0.98)
    modal.title("Crear Contacto")
    vcmd = (modal.register(lambda P: P.isdigit() or P == ""), '%P')
    modal.configure(bg="#0F1C27")
    tk.Label(modal, text="Crear Contacto", fg="white", bg="#1e1e1e", font=fuente_titulo).pack(pady=20)
    tk.Frame(modal, height=2, bg="#2A5072").pack(fill="x")
    tk.Label(modal, text="Ingresar Nombre", fg="white", bg="#1e1e1e", font=fuente_label).pack(padx=20, fill="x")
    entrada_nombre = tk.Entry(modal, font=fuente_label, validate="key", bg="#CAD9E6", fg="#000", borderwidth=0)
    entrada_nombre.pack(fill="x", padx=20, pady=10)
    entrada_nombre.focus_set()
    tk.Label(modal, text="Ingresar Número", fg="white", bg="#1e1e1e", font=fuente_label).pack(padx=20, fill="x")
    entrada_numero = tk.Entry(modal, font=fuente_label, bg="#CAD9E6", fg="#000", borderwidth=0, validatecommand=vcmd, validate="key")
    entrada_numero.pack(fill="x", padx=20, pady=10)
    # Botón para guardar el contacto
    # tk.Button(modal, text="Crear Contacto", bg="#35b5ff", fg="#fff", activeforeground="#fff", borderwidth=0, font=fuente_boton).pack()
    boton_style(modal, "Crear Contacto", lambda: contact_save(modal, mostrar_products, entrada_nombre, entrada_numero), "top")
    # tk.Button(modal, text="Cerrar", command=modal.destroy).pack()