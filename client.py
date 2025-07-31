import tkinter as tk
from tkinter import font, messagebox
from modals.createContact import create_Contact
from modals.editContact import edit_Contact
from components.buttonStyle import boton_style, boton_delete
from app import get_contacts, delete_contact

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Contactos")
ventana.attributes("-alpha", 0.98)
ventana.configure(bg="#0F1C27")

# Icono de la ventana
icono = tk.PhotoImage(file="icon.png")
ventana.iconphoto(True, icono)

# Fuentes capo
fuente_titulo = font.Font(family="Helvetica", size=20, weight="bold")
fuente_contact_name = font.Font(family="Helvetica", size=14, weight="normal")
fuente_label = font.Font(family="Helvetica", size=12, weight="normal")
fuente_number = font.Font(family="Helvetica", size=12, weight="bold")
fuente_boton = font.Font(family="Helvetica", size=12)

flex_container = tk.Frame(ventana, bg="#0F1C27")
flex_container.pack(fill="x", padx=20, pady=20)

def boton_reutilizable(posicion, texto, comando, color_fondo, color_texto, color_activo_fondo, color_activo_texto, font, side, padX, padY):
    return tk.Button(posicion, text=texto, command=comando, bg=color_fondo, fg=color_texto, font=font, activebackground=color_activo_fondo, activeforeground=color_activo_texto, borderwidth=0).pack(side=side, padx= padX, pady=padY)

# El hr de Tkinter XD
hr = tk.Frame(ventana, height=2, bg="#2A5072").pack(fill="x")
titulo = tk.Label(flex_container, text="Contactos", bg="#0F1C27", foreground="#fff", font=fuente_titulo)
titulo.pack(side="left")

content_product = tk.Frame(ventana, bg="#0F1C27", highlightthickness=0, highlightbackground="#0F1C27")
content_product.pack(fill="both", padx=20, pady=10)


boton = tk.Button(flex_container, text="Crear Contacto", bg="#00a2ff", fg="#fff", activebackground="#35b5ff", activeforeground="#fff", borderwidth=0, font=fuente_boton, command=lambda: create_Contact(ventana, mostrar_contactos))
boton.pack(side="right")

def delete_contacto(id):
    print("Eliminando contacto con ID:", id)
    if(id):
        delete_contact(id)
        messagebox.showinfo("Éxito", "Contacto eliminado exitosamente.")
        mostrar_contactos()

def mostrar_contactos():
    for widget in content_product.winfo_children():
        widget.destroy()
    for contact in get_contacts():
        lista_contactos = tk.Frame(content_product, bg="#0F1C27", highlightthickness=0, highlightbackground="#0F1C27")
        lista_contactos.pack(fill="both", padx=20, pady=10)
        lista_article = tk.Frame(lista_contactos, bg="#0F1C27", highlightthickness=0, highlightbackground="#0F1C27")
        lista_article.pack(fill="both")

        boton_delete(lista_article, "Eliminar Contacto", lambda id=contact[0]: delete_contacto(id), "right")

        boton_style(lista_article, "Editar Contacto", lambda id=contact[0]: edit_Contact((id), ventana, mostrar_contactos), "right")

        tk.Label(lista_article, text=f"{contact[1]}", bg="#0F1C27", foreground="#fff", font=fuente_contact_name).pack(anchor="w")
        tk.Label(lista_article, text=f"{contact[2]}", bg="#0F1C27", foreground="#fff", font=fuente_number).pack(anchor="w")
mostrar_contactos()
ventana.mainloop()