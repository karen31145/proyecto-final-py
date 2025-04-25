import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormProductosVista(tk.Frame):
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

        frame_agregar_sup_two = tk.Frame(frame_agregar,width= 300, height=100, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_agregar_sup_two.pack(fill=tk.X)

            # Configuramos las 3 columnas para que se repartan el ancho equitativamente
        for i in range(3):
            frame_agregar_sup_two.columnconfigure(i, weight=1)  # Esto reparte el ancho
                    

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
            
            
            

        # Frame 1: Nombre producto
        contenedor_nombre = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_nombre = tk.Label(contenedor_nombre, text="Nombre producto", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        
        self.nombre = ttk.Entry(contenedor_nombre, font=('Times', 14))
        self.nombre.pack(fill=tk.X, padx=20, pady=10)
        self.nombre.bind("<KeyRelease>",self.crear_codigo_SKU)
        
        # Frame 2: Descripción
        contenedor_descripcion = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_descripcion.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_descripcion = tk.Label(contenedor_descripcion, text="Descripción", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_descripcion.pack(fill=tk.X, padx=20, pady=5)
        
        self.descripcion = ttk.Entry(contenedor_descripcion, font=('Times', 14))
        self.descripcion.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 3: Categoría
        contenedor_categoria = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_categoria.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_categoria = tk.Label(contenedor_categoria, text="Categoría", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_categoria.pack(fill=tk.X, padx=20, pady=5)
        
        self.categoria =ttk.Combobox(contenedor_categoria, font=('Times', 14),state='readonly')
        self.categoria.pack(fill=tk.X, padx=20, pady=10)
       
       
       
        # Frame 1: Nombre producto
        contenedor_cstock = tk.Frame(frame_agregar_sup_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_cstock.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_stock = tk.Label(contenedor_cstock, text="Cantidad en stock", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_stock.pack(fill=tk.X, padx=20, pady=5)
        
        self.cantStock = crear_entry_numerico(contenedor_cstock, font=('Times', 14))
        self.cantStock.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        # Frame 2: Descripción
        contenedor_stocMin = tk.Frame(frame_agregar_sup_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_stocMin.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_stockMin = tk.Label(contenedor_stocMin, text="Stock Minimo", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_stockMin.pack(fill=tk.X, padx=20, pady=5)
        
        self.stockMin = crear_entry_numerico(contenedor_stocMin, font=('Times', 14))
        self.stockMin.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 3: Categoría
        contenedor_codigoSku = tk.Frame(frame_agregar_sup_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_codigoSku.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_sku = tk.Label(contenedor_codigoSku, text="SKU", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_sku.pack(fill=tk.X, padx=20, pady=5)
        
        self.codigoSku =ttk.Entry(contenedor_codigoSku, font=('Times', 14))
        self.codigoSku.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        # Frame 4: proveedor
        contenedor_proveedor = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_proveedor.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_proveedor = tk.Label(contenedor_proveedor, text="Proveedor", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_proveedor.pack(fill=tk.X, padx=20, pady=5)
        
        self.proveedor = ttk.Combobox(contenedor_proveedor, font=('Times', 14),state='readonly')
        self.proveedor.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 5: precio_compra
        contenedor_precio_compra = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_precio_compra.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_precio_compra = tk.Label(contenedor_precio_compra, text="Precio de compra", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_precio_compra.pack(fill=tk.X, padx=20, pady=5)
        
        self.precio_compra = crear_entry_numerico(contenedor_precio_compra, font=('Times', 14))
        self.precio_compra.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 6: precio_venta
        contenedor_precio_venta = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_precio_venta.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_precio_venta = tk.Label(contenedor_precio_venta, text="Precio de venta", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_precio_venta.pack(fill=tk.X, padx=20, pady=5)
        
        self.precio_venta = crear_entry_numerico(contenedor_precio_venta, font=('Times', 14))
        self.precio_venta.pack(fill=tk.X, padx=20, pady=10)
        
        
         # Frame 7: almacen
       
        contenedor_almacen = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_almacen.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_almacen = tk.Label(contenedor_almacen, text="almacen", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_almacen.pack(fill=tk.X, padx=20, pady=5)
        
        self.almacen = ttk.Combobox(contenedor_almacen, font=('Times', 14),state='readonly')
        self.almacen.pack(fill=tk.X, padx=20, pady=10)
        
        
        
        
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        limpiar = tk.Button(contenedor_boton_limpiar,text="limpiar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.limpiar_campos)
        limpiar.pack(fill=tk.X, padx=20,pady=20)
        
        
        
        
        # frame 7: botones
        contenedor_boton_guardar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_guardar.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_guardar,text="guardar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.Register)
        guardar.pack(fill=tk.X, padx=20,pady=20)
        guardar.bind("<Return>",(lambda event: self.validarContrasena()))
        
        contenedor_boton_Eliminar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_Eliminar.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_Eliminar,text="Desabilitar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.Inhabilitar)
        guardar.pack(fill=tk.X, padx=20,pady=20)
        guardar.bind("<Return>",(lambda event: self.validarContrasena()))
        
        
        style = ttk.Style()
        style.theme_use("clam")  # Puedes probar también 'default', 'alt', 'vista', 'xpnative'
        
        # Personalización general del Treeview
        style.configure("Treeview",
            background="#f4f4f4",
            foreground="#000000",
            rowheight=28,
            fieldbackground="#f4f4f4",
            font=("Segoe UI", 10)
        )
        
        # Encabezados bonitos
        style.configure("Treeview.Heading",
            background="#2e86de",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )

        
        
        # Frame 8: tabla productos
        tree_scroll_y = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL)
        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree_scroll_x = ttk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        # Treeview con columnas
        self.tree = ttk.Treeview(
            frame_tabla,
            show="headings",
            yscrollcommand=tree_scroll_y.set,
            xscrollcommand=tree_scroll_x.set
        )
    
        self.tree['columns'] = (
        "SKU", "Nombre", "Descripcion", "Precio de compra", "Precio de venta",
        "Categoria", "Proveedor", "Stock actual", "Stock minimo", "Almacen","Habilitado", "editar"
        )
        
# Ajuste y alineación de columnas
        col_config = {
            "SKU": 80,
            "Nombre": 150,
            "Descripcion": 200,
            "Precio de compra": 120,
            "Precio de venta": 120,
            "Categoria": 100,
            "Proveedor": 120,
            "Stock actual": 100,
            "Stock minimo": 100,
            "Almacen": 100,
            "Habilitado": 80,
            "editar": 80
        }
        
        for col, ancho in col_config.items():
            self.tree.column(col, width=ancho, anchor="center")

        for col in self.tree['columns']:
            self.tree.heading(col, text=col)

        self.tree.pack(expand=True, fill='both')

        # Conectar los scrollbars
        tree_scroll_y.config(command=self.tree.yview)
        tree_scroll_x.config(command=self.tree.xview)
        
        self.tree.heading(0,text="")
        self.tree.heading("SKU",text="SKU")
        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("Descripcion",text="Descripcion")
        self.tree.heading("Precio de compra",text="Precio de compra")
        self.tree.heading("Precio de venta",text="Precio de venta")
        self.tree.heading("Categoria",text="Categoria")
        self.tree.heading("Proveedor",text="Proveedor")
        self.tree.heading("Stock actual",text="Stock actual")
        self.tree.heading("Stock minimo",text="Stock minimo")
        self.tree.heading("Almacen",text="Almacen")
        self.tree.heading("Habilitado",text="Habilitado")
        self.tree.heading("editar",text="Editar")
        
        self.tree.pack(expand=True,fill='both')
        
        self.tree.tag_configure('oddrow', background='#ffffc0')
        self.tree.tag_configure('evenrow', background='#eafbea')
                # Colores alternos en las filas
        self.tree.tag_configure('oddrow', background='#ffffff')
        self.tree.tag_configure('evenrow', background='#dff9fb')
        
    def Register(self):
        pass    
    def limpiar_campos(self):
        pass
    def crear_codigo_SKU(self):
        pass
    def Inhabilitar(self):
        pass
    


#Funcion para unicamente aceptar numeros 
def crear_entry_numerico(parent, **kwargs):
    def solo_numeros(valor):
        return valor.isdigit() or valor == ""
    vcmd = (parent.register(solo_numeros), "%P")
    entry = ttk.Entry(parent, validate="key", validatecommand=vcmd, **kwargs)
    return entry



