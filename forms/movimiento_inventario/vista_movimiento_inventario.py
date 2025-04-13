import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormMovimientoInventarioVista(tk.Frame):
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
        contenedor_Cantidad = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_Cantidad.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_Cantidad = tk.Label(contenedor_Cantidad, text="Cantidad", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_Cantidad.pack(fill=tk.X, padx=20, pady=5)
        
        self.Cantidad = ttk.Entry(contenedor_Cantidad, font=('Times', 14))
        self.Cantidad.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 4: fecha_movimiento
        contenedor_fecha_movimiento = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_fecha_movimiento.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_fecha_movimiento = tk.Label(contenedor_fecha_movimiento, text="Proveedor", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_fecha_movimiento.pack(fill=tk.X, padx=20, pady=5)
        
        self.fecha_movimiento = ttk.Entry(contenedor_fecha_movimiento, font=('Times', 14))
        self.fecha_movimiento.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 5: id_almacen
        contenedor_id_almacen = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_id_almacen.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_id_almacen = tk.Label(contenedor_id_almacen, text="id almacen", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_id_almacen.pack(fill=tk.X, padx=20, pady=5)
        
        self.precio_id_almacen = ttk.Entry(contenedor_id_almacen, font=('Times', 14))
        self.precio_id_almacen.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 6: referencia
        contenedor_referencia= tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_referencia.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_referencia = tk.Label(contenedor_referencia, text="Referencia", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_referencia.pack(fill=tk.X, padx=20, pady=5)
        
        self.referencia = ttk.Entry(contenedor_referencia, font=('Times', 14))
        self.referencia.pack(fill=tk.X, padx=20, pady=10)
        
        
         # Frame 7: observaciones
        contenedor_observaciones = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_observaciones.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_observaciones = tk.Label(contenedor_observaciones, text="Observaciones", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_observaciones.pack(fill=tk.X, padx=20, pady=5)
        
        self.observaciones = ttk.Entry(contenedor_observaciones, font=('Times', 14))
        self.observaciones.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        limpiar = tk.Button(contenedor_boton_limpiar,text="limpiar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        limpiar.pack(fill=tk.X, padx=20,pady=20)
        
        
        # frame 8: botones
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
        
         
        # Frame 8: tabla movimineto de inventarios
        tree_scroll = ttk.Scrollbar(frame_tabla)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree=ttk.Treeview(frame_tabla,show="headings",yscrollcommand=tree_scroll.set)
        
        self.tree['columns']=("id_producto","tipo_movimiento","Cantidad","fecha_movimiento","id_almacen","referencia","observaciones")
        self.tree.column("0")
        self.tree.column("id_producto")
        self.tree.column("tipo_movimiento")
        self.tree.column("Cantidad")
        self.tree.column("fecha_movimiento")
        self.tree.column("id_almacen")
        self.tree.column("referencia")
        self.tree.column("observaciones")

        self.tree.heading(0,text="")
        self.tree.heading("id_producto",text="producto")
        self.tree.heading("tipo_movimiento",text="tipo de moviminento")
        self.tree.heading("Cantidad",text="cantidad")
        self.tree.heading("fecha_movimiento",text="fecha de movimiento")
        self.tree.heading("id_almacen",text="id de almacen")
        self.tree.heading("referencia",text="referencias")
        self.tree.heading("observaciones",text="observaciones")
        
        self.tree.pack(expand=True,fill='both')
        
        self.tree.tag_configure('oddrow', background='#ffffc0')
        self.tree.tag_configure('evenrow', background='#eafbea')
        