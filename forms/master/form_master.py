import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{w}x{h}+0+0")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        # Dividir en dos frames: menú (izquierda) y contenido (derecha)
        self.frame_menu = tk.Frame(self.ventana, bg='#2c3e50', width=250, height=h)
        self.frame_menu.pack(side='left', fill='y')

        self.frame_contenido = tk.Frame(self.ventana, bg='#fcfcfc', width=w-250, height=h)
        self.frame_contenido.pack(side='right', fill='both', expand=True)

        # Menú lateral con botones
        opciones = ['Inicio', 'Perfil', 'Configuración', 'Salir']
        for idx, texto in enumerate(opciones):
            btn = tk.Button(self.frame_menu, text=texto, bg='#34495e', fg='white', font=('Arial', 12, BOLD), relief='flat', padx=10, pady=10)
            btn.pack(fill='x', pady=2)

        # Imagen en el área de contenido
        logo = utl.leer_imagen("./imagenes/logo-python.png", (300, 300))
        label = tk.Label(self.frame_contenido, image=logo, bg='#fcfcfc')
        label.image = logo  # Referencia para evitar que se elimine el objeto de memoria
        label.place(relx=0.5, rely=0.5, anchor='center')

        self.ventana.mainloop()
