import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormVentasVista(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#fcfcfc')
        
        # Frame para agregar ventas (parte superior)
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
            
            
            
            
            
            

        # Frame 1: id_producto
        contenedor_id_producto = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_id_producto.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_id_producto= tk.Label(contenedor_id_producto, text="id producto", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_id_producto.pack(fill=tk.X, padx=20, pady=5)
        
        self.id_producto = ttk.Entry(contenedor_id_producto, font=('Times', 14))
        self.id_producto.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 2: cantidad
        contenedor_cantidad = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_cantidad.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_cantidad = tk.Label(contenedor_cantidad, text="Cantidad", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_cantidad.pack(fill=tk.X, padx=20, pady=5)
        
        self.cantidad= ttk.Entry(contenedor_cantidad, font=('Times', 14))
        self.cantidad.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 3: fecha
        contenedor_fecha = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_fecha.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_fecha= tk.Label(contenedor_fecha, text="Fecha", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_fecha.pack(fill=tk.X, padx=20, pady=5)
        
        self.fecha= ttk.Entry(contenedor_fecha, font=('Times', 14))
        self.fecha.pack(fill=tk.X, padx=20, pady=10)
        
         
       
        #contenedores
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        limpiar = tk.Button(contenedor_boton_limpiar,text="limpiar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        limpiar.pack(fill=tk.X, padx=20,pady=20)
        
        
         # frame 4: botones
        contenedor_boton_guardar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_guardar.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_guardar,text="guardar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        guardar.pack(fill=tk.X, padx=20,pady=20)
        guardar.bind("<Return>",(lambda event: self.validarContrasena()))
        
        contenedor_boton_Eliminar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_Eliminar.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_Eliminar,text="Eliminar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff")
        guardar.pack(fill=tk.X, padx=20,pady=20)
        guardar.bind("<Return>",(lambda event: self.validarContrasena()))
        
        
        
        # Frame 5: tabla de almacenes
        tree_scroll = ttk.Scrollbar(frame_agregar_inf_two)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree=ttk.Treeview(frame_agregar_inf_two,show="headings",yscrollcommand=tree_scroll.set)
        
        self.tree['columns']=("id_producto","cantidad","fecha","codigo_venta")
        self.tree.column("0")
        self.tree.column("id_producto")
        self.tree.column("cantidad")
        self.tree.column("fecha")
        self.tree.column("codigo_venta")

        self.tree.heading(0,text="")
        self.tree.heading("id_producto",text="id producto")
        self.tree.heading("cantidad",text="cantidad")
        self.tree.heading("fecha",text="fecha")
        self.tree.heading("codigo_venta",text="codigo de venta")
        
        self.tree.pack(expand=True,fill='both')
        
        self.tree.tag_configure('oddrow', background='#ffffc0')
        self.tree.tag_configure('evenrow', background='#eafbea')
        
        
