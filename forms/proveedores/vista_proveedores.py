# form_productos_vista.py
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormProveedoresVista(tk.Frame):
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
            
            
            

        # Frame 1: Nombre proveedor
        contenedor_nombre = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_nombre = tk.Label(contenedor_nombre, text="Nombre proveedor", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        
        self.nombre = ttk.Entry(contenedor_nombre, font=('Times', 14))
        self.nombre.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 2: contacto
        contenedor_contacto = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_contacto.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_contacto = tk.Label(contenedor_contacto, text="contacto", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_contacto.pack(fill=tk.X, padx=20, pady=5)
        
        self.contacto = ttk.Entry(contenedor_contacto, font=('Times', 14))
        self.contacto.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 3: telefono
        contenedor_telefono = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_telefono.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        etiqueta_telefono = tk.Label(contenedor_telefono, text="telefono", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_telefono.pack(fill=tk.X, padx=20, pady=5)
        
        self.telefono = ttk.Entry(contenedor_telefono, font=('Times', 14))
        self.telefono.pack(fill=tk.X, padx=20, pady=10)
         
        
        # Frame 4: email
        contenedor_email = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_email.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_email = tk.Label(contenedor_email, text="email", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_email.pack(fill=tk.X, padx=20, pady=5)
        
        self.email = ttk.Entry(contenedor_email, font=('Times', 14))
        self.email.pack(fill=tk.X, padx=20, pady=10)
        
        
        # Frame 5: direccion
        contenedor_direccion = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_direccion.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_direccion = tk.Label(contenedor_direccion, text="direccion", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_direccion.pack(fill=tk.X, padx=20, pady=5)
        
        self.direccion = ttk.Entry(contenedor_direccion, font=('Times', 14))
        self.direccion.pack(fill=tk.X, padx=20, pady=10)
        
        
        #contenedor de botones
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        limpiar = tk.Button(contenedor_boton_limpiar,text="limpiar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.limpiar_campos)
        limpiar.pack(fill=tk.X, padx=20,pady=20)
        
        
        # frame 6: botones
        contenedor_boton_guardar = tk.Frame(frame_agregar_inf_two, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_guardar.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_guardar,text="guardar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.Register)
        guardar.pack(fill=tk.X, padx=20,pady=20)
        
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

        
        
        
        
        # Frame 7: tabla proveedores
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
        
                
        self.tree['columns']=("Nombre","contacto","telefono","email","direccion")
        self.tree.column("0")
        self.tree.column("Nombre")
        self.tree.column("contacto")
        self.tree.column("telefono")
        self.tree.column("email")
        self.tree.column("direccion")
        

        self.tree.heading(0,text="")
        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("contacto",text="contacto")
        self.tree.heading("telefono",text="telefono")
        self.tree.heading("email",text="email")
        self.tree.heading("direccion",text="direccion")
       
        
        self.tree.pack(expand=True,fill='both')
        
        self.tree.tag_configure('oddrow', background='#ffffc0')
        self.tree.tag_configure('evenrow', background='#eafbea')

    def Register(self):
        pass    
    def limpiar_campos(self):
        pass
    def crear_codigo_SKU(self):
        pass
    def Inhabilitar(self):
        pass
         
