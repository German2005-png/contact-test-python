import tkinter as tk
from tkinter import font

def boton_style(posicion, texto, comando, side):
    fuente_boton = font.Font(family="Helvetica", size=12)
    return tk.Button(posicion, text=texto, command=comando, bg="#00a2ff", activebackground="#35b5ff", fg="#fff", activeforeground="#fff", borderwidth=0, font=fuente_boton).pack(side=side, padx=5, pady=0)

def boton_delete(posicion, texto, comando, side="right"):
    fuente_boton = font.Font(family="Helvetica", size=12)
    return tk.Button(posicion, text=texto, command=comando, bg="#ff1e00", activebackground="#ff624d", fg="#fff", activeforeground="#fff", borderwidth=0, font=fuente_boton).pack(side=side, padx=5, pady=0)
