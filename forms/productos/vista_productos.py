# form_productos_vista.py
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormProductosVista(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#fcfcfc')
        
        # Frame para agregar productos (parte superior)
        frame_agregar = tk.Frame(self, bd=0, relief=tk.SOLID, bg='red', height=300)
        frame_agregar.pack(side="top", fill=tk.X)

        # Frame para tabla de productos (parte inferior)
        frame_tabla = tk.Frame(self, bd=0, relief=tk.SOLID, bg='blue')
        frame_tabla.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)



        # Frame para divider la seccion de agregar productos en 2
        frame_agregar_sup = tk.Frame(frame_agregar,width= 300, height=100, bd=0, relief=tk.SOLID,bg='green')
        frame_agregar_sup.pack(side="top",fill=tk.X)

            # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(3):
            frame_agregar_sup.columnconfigure(i, weight=1)  # Esto reparte el ancho
            

        # frame_agregar_inf
        frame_agregar_inf = tk.Frame(frame_agregar,width=300,height=100, bd=0, relief=tk.SOLID,bg='yellow')
        frame_agregar_inf.pack(fill=tk.X)
        
         # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(3):
            frame_agregar_inf.columnconfigure(i, weight=1)  # Esto reparte el ancho
            
            
        # frame_agregar_inf_two
        frame_agregar_inf_two = tk.Frame(frame_agregar,width=300,height=100, bd=0, relief=tk.SOLID,bg='red')
        frame_agregar_inf_two.pack(expand=tk.YES,fill=tk.BOTH)
        
         # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(4):
            frame_agregar_inf_two.columnconfigure(i, weight=1)  # Esto reparte el ancho
            
            
            

        # Frame 1: Nombre producto
        contenedor_nombre = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='red')
        contenedor_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_nombre = tk.Label(contenedor_nombre, text="Nombre producto", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        
        self.nombre = ttk.Entry(contenedor_nombre, font=('Times', 14))
        self.nombre.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 2: Descripción
        contenedor_descripcion = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='red')
        contenedor_descripcion.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_descripcion = tk.Label(contenedor_descripcion, text="Descripción", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_descripcion.pack(fill=tk.X, padx=20, pady=5)
        
        self.descripcion = ttk.Entry(contenedor_descripcion, font=('Times', 14))
        self.descripcion.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 3: Categoría
        contenedor_categoria = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='red')
        contenedor_categoria.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_categoria = tk.Label(contenedor_categoria, text="Categoría", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_categoria.pack(fill=tk.X, padx=20, pady=5)
        
        self.categoria = ttk.Entry(contenedor_categoria, font=('Times', 14))
        self.categoria.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        # Frame 4: proveedor
        contenedor_proveedor = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='red')
        contenedor_proveedor.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_proveedor = tk.Label(contenedor_proveedor, text="Proveedor", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_proveedor.pack(fill=tk.X, padx=20, pady=5)
        
        self.proveedor = ttk.Entry(contenedor_proveedor, font=('Times', 14))
        self.proveedor.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 5: precio_compra
        contenedor_precio_compra = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='red')
        contenedor_precio_compra.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_precio_compra = tk.Label(contenedor_precio_compra, text="Precio de compra", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_precio_compra.pack(fill=tk.X, padx=20, pady=5)
        
        self.precio_compra = ttk.Entry(contenedor_precio_compra, font=('Times', 14))
        self.precio_compra.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 6: precio_venta
        contenedor_precio_venta = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_precio_venta.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_precio_venta = tk.Label(contenedor_precio_venta, text="Precio de venta", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_precio_venta.pack(fill=tk.X, padx=20, pady=5)
        
        self.precio_venta = ttk.Entry(contenedor_precio_venta, font=('Times', 14))
        self.precio_venta.pack(fill=tk.X, padx=20, pady=10)
        
        
         # Frame 6: almacen
       
        contenedor_almacen = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='red')
        contenedor_almacen.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_almacen = tk.Label(contenedor_almacen, text="almacen", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_almacen.pack(fill=tk.X, padx=20, pady=5)
        
        self.almacen = ttk.Entry(contenedor_almacen, font=('Times', 14))
        self.almacen.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='red')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        limpiar = tk.Button(contenedor_boton_limpiar,text="limpiar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        limpiar.pack(fill=tk.X, padx=20,pady=20)
        
        
        
        
        # frame 7: botones
        contenedor_boton_guardar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_guardar.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_guardar,text="guardar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        guardar.pack(fill=tk.X, padx=20,pady=20)
        guardar.bind("<Return>",(lambda event: self.validarContrasena()))
        
        contenedor_boton_Eliminar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_Eliminar.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_Eliminar,text="Eliminar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        guardar.pack(fill=tk.X, padx=20,pady=20)
        guardar.bind("<Return>",(lambda event: self.validarContrasena()))
        