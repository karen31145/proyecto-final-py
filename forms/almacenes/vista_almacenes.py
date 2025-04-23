import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormAlmacenesVista(tk.Frame):
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
            
            
            
            

        # Frame 1: Nombre
        contenedor_nombre = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # sticky=nsew hace que se expanda
        
        etiqueta_nombre = tk.Label(contenedor_nombre, text="Nombre", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        
        self.nombre = ttk.Entry(contenedor_nombre, font=('Times', 14))
        self.nombre.pack(fill=tk.X, padx=20, pady=10)
        
        # Frame 2: ubicacion
        contenedor_ubicacion = tk.Frame(frame_agregar_sup, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_ubicacion.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        etiqueta_ubicacion = tk.Label(contenedor_ubicacion, text="Ubicacion", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_ubicacion.pack(fill=tk.X, padx=20, pady=5)
        
        self.ubicacion= ttk.Entry(contenedor_ubicacion, font=('Times', 14))
        self.ubicacion.pack(fill=tk.X, padx=20, pady=10)
        
       
        #contenedores botones
        contenedor_boton_limpiar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_limpiar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        limpiar = tk.Button(contenedor_boton_limpiar,text="limpiar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.limpiar_campos)
        limpiar.pack(fill=tk.X, padx=20,pady=20)
        
        
        contenedor_boton_guardar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_guardar.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_guardar,text="guardar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff", command=self.Register)
        guardar.pack(fill=tk.X, padx=20,pady=20)
        contenedor_boton_Eliminar = tk.Frame(frame_agregar_inf, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        contenedor_boton_Eliminar.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        guardar = tk.Button(contenedor_boton_Eliminar,text="Desabilitar",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.Inhabilitar)
        guardar.pack(fill=tk.X, padx=20,pady=20)
        
        
        
        # Frame 5: tabla de almacenes

        style = ttk.Style()
        style.theme_use("default")

# Estilo de encabezados
        style.configure("Treeview.Heading", 
                        font=('Segoe UI', 12, 'bold'), 
                        foreground="#ffffff", 
                        background="#3a7ff6")

# Estilo general de celdas
        style.configure("Treeview", 
                        font=('Segoe UI', 11),
                        background="#f0f0f0",
                        foreground="#333333",
                        rowheight=30,
                        fieldbackground="#f0f0f0")

# Colores alternos en filas
        style.map("Treeview", background=[('selected', '#3a7ff6')], foreground=[('selected', '#ffffff')])
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # quita bordes feos


        tree_scroll = ttk.Scrollbar(frame_agregar_inf_two, orient="vertical")
        tree_scroll.grid(row=0, column=4, sticky='ns')
        
        
        self.tree = ttk.Treeview(frame_agregar_inf_two, 
                         show="headings",
                         yscrollcommand=tree_scroll.set,
                         style="Treeview")

        tree_scroll.config(command=self.tree.yview)

        self.tree['columns'] = ("Nombre", "ubicacion")

        self.tree.column("Nombre", anchor=tk.W, width=200)
        self.tree.column("ubicacion", anchor=tk.W, width=200)

        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("ubicacion", text="Ubicación")

        self.tree.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        frame_agregar_inf.grid_rowconfigure(1, weight=1)
        frame_agregar_inf.grid_columnconfigure(0, weight=1)

    
    def Register(self):
        pass        
        