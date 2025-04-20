# master_panel.py
import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from forms.productos.form_productos import FormProductos 
from forms.proveedores.form_proveedores import FormProveedores  # Importamos la vista
from forms.almacenes.form_almacenes import FormAlmacen
from forms.categorias.form_categorias import FormCategorias  # Importamos la vista de categorías
from forms.movimiento_inventario.vista_movimiento_inventario import FormMovimientoInventarioVista  # Importamos la vista de movimientos de inventarios
from forms.ventas.form_ventas import FormVentas  # Importamos la vista de ventas


class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        
        screen_w = self.ventana.winfo_screenwidth()
        screen_h = self.ventana.winfo_screenheight()
        w = int(screen_w * 0.98)
        h = int(screen_h * 0.87)
        
        x = int((screen_w - w) / 2)
        y = int((screen_h - h) / 2)
        self.ventana.geometry(f"{w}x{h}+{x}+{y}")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        # Dividir en dos frames: menú y contenido
        self.frame_menu = tk.Frame(self.ventana, bg='#2c3e50', width=250, height=h)
        self.frame_menu.pack(side='left', fill='y')

        self.frame_contenido = tk.Frame(self.ventana, bg='#d3d2cc', width=w-250, height=h)
        self.frame_contenido.pack(side='right', fill='both', expand=True)

        # Imagen inicial (logo)
        self.logo = utl.leer_imagen("./imagenes/nuevoLogo.png", (300, 300))
        self.label_logo = tk.Label(self.frame_contenido, image=self.logo, bg='#d3d2cc')
        self.label_logo.image = self.logo
        self.label_logo.place(relx=0.5, rely=0.5, anchor='center')

        # Botones del menú
        opciones = [
            ('Productos', self.mostrar_productos),
            ('Proveedores', self.mostrar_proveedores),  
            ('almacenes', self.mostrar_almacenes),
            ('categorías', self.mostrar_categorias),
            ('movimiento de inventario', self.mostrar_movimiento_inventario),
            ('ventas', self.mostrar_ventas),
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
        vista_productos = FormProductos(self.frame_contenido)
        vista_productos.pack(fill='both', expand=True)

    def mostrar_proveedores(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de proveedores
        vista_provedores = FormProveedores(self.frame_contenido)
        vista_provedores.pack(fill='both', expand=True)
        
        
    def mostrar_almacenes(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de almacenes
        vista = FormAlmacen(self.frame_contenido)
        vista.pack(fill='both', expand=True)
        

    def mostrar_categorias(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de ctegorias
        vista_categorias = FormCategorias(self.frame_contenido)
        vista_categorias.pack(fill='both', expand=True)
        
        
    def mostrar_movimiento_inventario(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de movimiento_inventarios
        vista_movimiento_inventario = FormMovimientoInventarioVista(self.frame_contenido)
        vista_movimiento_inventario.pack(fill='both', expand=True)
        
        
    def mostrar_ventas(self):
        # Eliminar contenido actual del frame_contenido
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Cargar vista de ventas
        vista_ventas = FormVentas(self.frame_contenido)
        vista_ventas.pack(fill='both', expand=True)
        
        
    
        
        
    
        
    
