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

        # Frame para dividir la sección de agregar productos en 3
        frame_agregar_sup = tk.Frame(frame_agregar, width=300, height=100, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_agregar_sup.pack(side="top", fill=tk.X)

        for i in range(4):
            frame_agregar_sup.columnconfigure(i, weight=1)

        # Frame inferior con botones
        frame_agregar_inf = tk.Frame(frame_agregar, width=300, height=100, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_agregar_inf.pack(fill=tk.X)

        for i in range(4):
            frame_agregar_inf.columnconfigure(i, weight=1)

        # ID producto
        contenedor_id_producto = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_id_producto.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(contenedor_id_producto, text="id producto", font=('Times', 14), fg="#666a88", bg="#fcfcfc").pack(fill=tk.X, padx=20, pady=5)
        self.id_producto = ttk.Entry(contenedor_id_producto, font=('Times', 14))
        self.id_producto.pack(fill=tk.X, padx=20, pady=10)

        # Cantidad
        contenedor_cantidad = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_cantidad.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(contenedor_cantidad, text="Cantidad", font=('Times', 14), fg="#666a88", bg="#fcfcfc").pack(fill=tk.X, padx=20, pady=5)
        self.cantidad = ttk.Entry(contenedor_cantidad, font=('Times', 14))
        self.cantidad.pack(fill=tk.X, padx=20, pady=10)

        # Fecha
        contenedor_fecha = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_fecha.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tk.Label(contenedor_fecha, text="Fecha", font=('Times', 14), fg="#666a88", bg="#fcfcfc").pack(fill=tk.X, padx=20, pady=5)
        self.fecha = ttk.Entry(contenedor_fecha, font=('Times', 14))
        self.fecha.pack(fill=tk.X, padx=20, pady=10)

        # Código de venta
        contenedor_codigo_venta = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_codigo_venta.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        tk.Label(contenedor_codigo_venta, text="Código de Venta", font=('Times', 14), fg="#666a88", bg="#fcfcfc").pack(fill=tk.X, padx=20, pady=5)
        self.codigo_venta = ttk.Entry(contenedor_codigo_venta, font=('Times', 14))
        self.codigo_venta.pack(fill=tk.X, padx=20, pady=10)

        # Botón Limpiar
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        btn_limpiar = tk.Button(contenedor_boton_limpiar, text="Limpiar", font=('Times', 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff",command=self.limpiar_campos)
        btn_limpiar.pack(fill=tk.X, padx=20, pady=20)

        # Botón Guardar
        contenedor_boton_guardar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_guardar.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        self.btn_guardar = tk.Button(contenedor_boton_guardar, text="Guardar", font=('Times', 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff",command=self.Register)
        self.btn_guardar.pack(fill=tk.X, padx=20, pady=20)  # Bind para ejecutar la función Register al hacer clic

        # Botón Eliminar
        contenedor_boton_eliminar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_eliminar.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        btn_eliminar = tk.Button(contenedor_boton_eliminar, text="Desabilitar", font=('Times', 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff",command=self.Inhabilitar)
        btn_eliminar.pack(fill=tk.X, padx=20, pady=20)

        # Tabla de ventas
        tree_scroll = ttk.Scrollbar(frame_tabla)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(frame_tabla, show="headings", yscrollcommand=tree_scroll.set)
        self.tree.pack(expand=True, fill='both')
        tree_scroll.config(command=self.tree.yview)

        self.tree['columns'] = ("id_producto", "cantidad", "fecha", "codigo_venta")
        self.tree.column("id_producto", anchor="center")
        self.tree.column("cantidad", anchor="center")
        self.tree.column("fecha", anchor="center")
        self.tree.column("codigo_venta", anchor="center")

        self.tree.heading("id_producto", text="ID Producto")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("codigo_venta", text="Código de Venta")

        self.tree.tag_configure('oddrow', background='#ffffc0')
        self.tree.tag_configure('evenrow', background='#eafbea')


    def Register(self):
        pass 