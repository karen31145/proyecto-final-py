# master_panel.py
import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from forms.productos.vista_productos import FormProductosVista 
from forms.proveedores.vista_proveedores import FormProveedoresVista  # Importamos la vista
from forms.movimiento_inventarios.vista_movimiento_inventario import  FormMovimientoInventariosVista  # Importamos la vista
 # Importamos la vista

class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{w}x{h}+0+0")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        # Dividir en dos frames: menú y contenido
        self.frame_menu = tk.Frame(self.ventana, bg='#2c3e50', width=250, height=h)
        self.frame_menu.pack(side='left', fill='y')

        self.frame_contenido = tk.Frame(self.ventana, bg='#fcfcfc', width=w-250, height=h)
        self.frame_contenido.pack(side='right', fill='both', expand=True)

        # Imagen inicial (logo)
        self.logo = utl.leer_imagen("./imagenes/logo-python.png", (300, 300))
        self.label_logo = tk.Label(self.frame_contenido, image=self.logo, bg='#fcfcfc')
        self.label_logo.image = self.logo
        self.label_logo.place(relx=0.5, rely=0.5, anchor='center')

        # Botones del menú
        opciones = [
            ('Productos', self.mostrar_productos),
            ('Proveedores', self.mostrar_proveedores),
            ('Movimientos de inventario', self.mostrar_movimientos),
            ('Configuración', lambda: print("Configuración")),
            ('Salir', self.ventana.quit)
        ]

        for texto, comando in opciones:
            btn = tk.Button(self.frame_menu, text=texto, bg='#34495e', fg='white',
                            font=('Arial', 12, BOLD), relief='flat', padx=10, pady=10,
                            command=comando)
            btn.pack(fill='x', pady=2)

        self.ventana.mainloop()

    def mostrar_productos(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de productos
        vista_productos = FormProductosVista(self.frame_contenido)
        vista_productos.pack(fill='both', expand=True)

    def mostrar_proveedores(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de proveedores
        vista_provedores = FormProveedoresVista(self.frame_contenido)
        vista_provedores.pack(fill='both', expand=True)

    def mostrar_movimientos(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de proveedores
        vista_provedores = FormMovimientoInventariosVista(self.frame_contenido)
        vista_provedores.pack(fill='both', expand=True)
