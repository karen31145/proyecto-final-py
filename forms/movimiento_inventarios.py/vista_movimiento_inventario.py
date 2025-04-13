import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormMovimientoInventariosVista(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#fcfcfc')
        
        # Frame para agregar productos (parte superior)
        frame_agregar = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc', height=300)
        frame_agregar.pack(side="top", fill=tk.X)

        # Frame para tabla de productos (parte inferior)
        frame_tabla = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_tabla.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)


        # Frame para divider la seccion de agregar productos en 3
        frame_agregar_sup = tk.Frame(frame_agregar,width= 300, height=100, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_agregar_sup.pack(side="top",fill=tk.X)

            # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(3):
            frame_agregar_sup.columnconfigure(i, weight=1)  # Esto reparte el ancho
            

        # frame_agregar_inf
        frame_agregar_inf = tk.Frame(frame_agregar,width=300,height=100, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_agregar_inf.pack(fill=tk.X)
        
         # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(3):
            frame_agregar_inf.columnconfigure(i, weight=1)  # Esto reparte el ancho
            
            
        # frame_agregar_inf_two
        frame_agregar_inf_two = tk.Frame(frame_agregar,width=300,height=100, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_agregar_inf_two.pack(expand=tk.YES,fill=tk.BOTH)
        
         # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(4):
            frame_agregar_inf_two.columnconfigure(i, weight=1)  # Esto reparte el ancho
            
            
            

        # Frame 1:id_producto
        contenedor_id_producto = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_id_producto.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_id_producto = tk.Label(contenedor_id_producto, text="id producto", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_id_producto.pack(fill=tk.X, padx=20, pady=5)
        
        self.id_producto = ttk.Entry(contenedor_id_producto, font=('Times', 14))
        self.id_producto.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 2: tipo_movimiento
        contenedor_tipo_movimiento = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_tipo_movimiento.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_tipo_movimiento = tk.Label(contenedor_tipo_movimiento, text="tipo movimiento", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_tipo_movimiento.pack(fill=tk.X, padx=20, pady=5)
        
        self.tipo_movimiento = ttk.Entry(contenedor_tipo_movimiento, font=('Times', 14))
        self.tipo_movimiento.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 3: Cantidad
        contenedor_categoria = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_categoria.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_categoria = tk.Label(contenedor_categoria, text="Categoría", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_categoria.pack(fill=tk.X, padx=20, pady=5)
        
        self.categoria = ttk.Entry(contenedor_categoria, font=('Times', 14))
        self.categoria.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        # Frame 4: proveedor
        contenedor_proveedor = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_proveedor.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_proveedor = tk.Label(contenedor_proveedor, text="Proveedor", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_proveedor.pack(fill=tk.X, padx=20, pady=5)
        
        self.proveedor = ttk.Entry(contenedor_proveedor, font=('Times', 14))
        self.proveedor.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 5: precio_compra
        contenedor_precio_compra = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
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
       
        contenedor_almacen = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_almacen.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_almacen = tk.Label(contenedor_almacen, text="almacen", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_almacen.pack(fill=tk.X, padx=20, pady=5)
        
        self.almacen = ttk.Entry(contenedor_almacen, font=('Times', 14))
        self.almacen.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
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
        
        
        
        # Frame 8: tabla productos
        tree_scroll = ttk.Scrollbar(frame_tabla)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree=ttk.Treeview(frame_tabla,show="headings",yscrollcommand=tree_scroll.set)
        
        self.tree['columns']=("Nombre","Descripcion","Categoria","Proveedor","Precio de compra","Precio de venta","Almacen")
        self.tree.column("0")
        self.tree.column("Nombre")
        self.tree.column("Descripcion")
        self.tree.column("Categoria")
        self.tree.column("Proveedor")
        self.tree.column("Precio de compra")
        self.tree.column("Precio de venta")
        self.tree.column("Almacen")

        self.tree.heading(0,text="")
        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("Descripcion",text="Descripcion")
        self.tree.heading("Categoria",text="Categoria")
        self.tree.heading("Proveedor",text="Proveedor")
        self.tree.heading("Precio de compra",text="Precio de compra")
        self.tree.heading("Precio de venta",text="Precio de venta")
        self.tree.heading("Almacen",text="Almacen")
        
        self.tree.pack(expand=True,fill='both')
        
        self.tree.tag_configure('oddrow', background='#ffffc0')
        self.tree.tag_configure('evenrow', background='#eafbea')
        