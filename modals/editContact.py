import tkinter as tk
from tkinter import font, messagebox
from components.buttonStyle import boton_style
from app import edit_contact

def modified_contact(modal, mostrar_products, id, name_entry, phone_entry):
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    print("Nombre:", name)
    print("Teléfono:", phone)
    if(name and phone):
        edit_contact(id, name, phone)
        messagebox.showinfo("Éxito", "Contacto modificado exitosamente.")
        modal.destroy()
        mostrar_products()
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

def edit_Contact(id, ventana, mostrar_products):
    fuente_titulo = font.Font(family="Helvetica", size=20, weight="bold")
    fuente_label = font.Font(family="Helvetica", size=12, weight="normal")
    modal = tk.Toplevel(ventana)
    modal.geometry("400x300")
    modal.configure(bg="#1e1e1e")
    modal.transient(ventana)
    modal.attributes("-alpha", 0.98)
    modal.title("Crear Contacto")
    modal.configure(bg="#0F1C27")
    vcmd = (modal.register(lambda P: P.isdigit() or P == ""), '%P')
    tk.Label(modal, text="Editar Contacto", fg="white", bg="#1e1e1e", font=fuente_titulo).pack(pady=20)
    tk.Frame(modal, height=2, bg="#2A5072", ).pack(fill="x")
    tk.Label(modal, text="Modificar Nombre", fg="white", bg="#1e1e1e", font=fuente_label).pack(padx=20, fill="x")
    entrada_nombre = tk.Entry(modal, font=fuente_label, validate="key", bg="#CAD9E6", fg="#000", borderwidth=0)
    entrada_nombre.pack(fill="x", padx=20, pady=10)
    entrada_nombre.focus_set()
    tk.Label(modal, text="Modificar Número", fg="white", bg="#1e1e1e", font=fuente_label).pack(padx=20, fill="x")
    entrada_numero = tk.Entry(modal, font=fuente_label, bg="#CAD9E6", fg="#000", borderwidth=0, validatecommand=vcmd, validate="key")
    entrada_numero.pack(fill="x", padx=20, pady=10)
    # Botón para guardar el contacto
    # tk.Button(modal, text="Crear Contacto", bg="#35b5ff", fg="#fff", activeforeground="#fff", borderwidth=0, font=fuente_boton).pack()
    boton_style(modal, "Editar Contacto", lambda: modified_contact(modal, mostrar_products, id, entrada_nombre, entrada_numero), "top")
    # tk.Button(modal, text="Cerrar", command=modal.destroy).pack()