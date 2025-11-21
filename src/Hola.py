import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "botón presionado")

ventana= tk.Tk()
ventana.title ("Ventana simple")

label = tk.Label (ventana, text = "Hola Mundo")
label.pack(pady=10)

boton = tk.Button (ventana, text = "Haz click aqui", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()