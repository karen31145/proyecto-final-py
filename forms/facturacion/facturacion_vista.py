import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class VistaFacturacion(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#fcfcfc')

        # Frame principal dividido en dos mitades
        frame_izquierdo = tk.Frame(self, bg='#fcfcfc',width=300)
        frame_izquierdo.pack(side="left", fill=tk.BOTH)

        frame_derecho = tk.Frame(self, bg='#fcfcfc')
        frame_derecho.pack(side="right", expand=True, fill=tk.BOTH)

        # --------------------- PARTE IZQUIERDA ---------------------
        # --------------------- ESTILO PARA TREEVIEW ---------------------
        style = ttk.Style()
        style.theme_use("clam")  # Otras opciones: 'default', 'alt', etc.

        style.configure("Treeview",
            background="#f4f4f4",
            foreground="#000000",
            rowheight=28,
            fieldbackground="#f4f4f4",
            font=("Segoe UI", 10)
        )

        style.configure("Treeview.Heading",
            background="#2e86de",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )

        # --------------------- PARTE IZQUIERDA: TABLA ---------------------
        
        tree_scroll_y = ttk.Scrollbar(frame_izquierdo, orient=tk.VERTICAL)
        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(
            frame_izquierdo,
            columns=("item","producto", "codigo", "cantidad", "precioU", "precioTotal", "eliminar"),
            show="headings",
            yscrollcommand=tree_scroll_y.set
        )

        # Encabezados
        encabezados = {
            "item":"#",
            "producto": "Producto",
            "codigo": "Código",
            "cantidad": "Cantidad",
            "precioU": "Precio Un",
            "precioTotal": "Precio Tot",
            "eliminar": "Eliminar"
        }

        anchos_columnas = {
        "item": 40,
        "producto": 150,
        "codigo": 80,
        "cantidad": 80,
        "precioU": 100,
        "precioTotal": 110,
        "eliminar": 70
        }

        for col, titulo in encabezados.items():
            self.tree.heading(col, text=titulo)
            self.tree.column(col, anchor="center",width=anchos_columnas[col])

        self.tree.pack(expand=True, fill=tk.BOTH)
        tree_scroll_y.config(command=self.tree.yview)

        # Colores alternos en las filas
        self.tree.tag_configure('oddrow', background='#ffffff')
        self.tree.tag_configure('evenrow', background='#dff9fb')

        # --------------------- PARTE DERECHA ---------------------
        # Lista desplegable con buscador
        contenedor_combo = tk.Frame(frame_derecho, bg="#fcfcfc", pady=20)
        contenedor_combo.pack(fill=tk.X, padx=20)

        etiqueta_combo = tk.Label(contenedor_combo, text="Buscar producto", font=('Times', 14),fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_combo.pack(fill=tk.X,padx=20, pady=5)

        self.var_producto = tk.StringVar()
        self.combo_producto = ttk.Combobox(
            contenedor_combo, textvariable=self.var_producto,
            font=('Times', 12)
        )
        self.combo_producto.pack(fill=tk.X,  padx=20, pady=10)  # Espaciado inferior

        # Campo para ingresar la cantidad
        etiqueta_cantidad = tk.Label(contenedor_combo, text="Cantidad", font=('Times', 14),fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_cantidad.pack(fill=tk.X,padx=20, pady=5)

        self.var_cantidad = tk.StringVar()
        entrada_cantidad = crear_entry_numerico(
            contenedor_combo, textvariable=self.var_cantidad,
            font=('Times', 14), fg="#666a88", bg="#fcfcfc"
        )
        entrada_cantidad.pack(fill=tk.X, padx=20, pady=10)  # Espaciado inferior

        # Botones debajo
        contenedor_botones = tk.Frame(frame_derecho, bg="#fcfcfc")
        contenedor_botones.pack(pady=40)

        btn_agregar = tk.Button(
            contenedor_botones, text="Agregar",
            font=('Times', 14, BOLD), bg="#28a745", fg="#fff", bd=0,
            padx=20, pady=10, command=self.agregar_producto
        )
        btn_agregar.pack(fill=tk.X, padx=40, pady=10)


        btn_confirmar = tk.Button(
            contenedor_botones, text="Confirmar venta",
            font=('Times', 14, BOLD), bg="#3a7ff6", fg="#fff", bd=0,
            padx=20, pady=10, command=self.confirmar_venta
        )
        btn_confirmar.pack(fill=tk.X, padx=40, pady=10)

#Funcion para unicamente aceptar numeros 
def crear_entry_numerico(parent, **kwargs):
    def solo_numeros(valor):
        return valor.isdigit() or valor == ""
    vcmd = (parent.register(solo_numeros), "%P")
    entry = tk.Entry(parent, validate="key", validatecommand=vcmd, **kwargs)
    return entry

