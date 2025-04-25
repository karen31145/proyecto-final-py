import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.productos.vista_productos import FormProductosVista
import util.generic as utl
from controladores.almacenes_controlador import almacenesRepository
from controladores.controlador_categorias import CategoriasRepository
from controladores.controlador_proveedores import ControladorProveedoresReposito
from controladores.controlador_productos import ControladorProductoRepository
from persistence.modelo_productos import ProductosModelo
from datetime import datetime

class FormProductos(FormProductosVista):
    def __init__(self, parent):
        self.almacenesRepositorio = almacenesRepository()
        self.CategoriasRepository = CategoriasRepository()
        self.ControladorProductoRepository = ControladorProductoRepository()
        self.ControladorProveedoresReposito = ControladorProveedoresReposito()

        
        super().__init__(parent)
        self.cargaInicial()   
        
        def on_tree_click(event):
            region = self.tree.identify("region", event.x, event.y)
            if region == "cell":
                columna = self.tree.identify_column(event.x)
                fila = self.tree.identify_row(event.y)
                if columna == "#12":  # "editar" es la columna 12 (empieza desde 1)
                    valores = self.tree.item(fila, "values")
                    sku = valores[0]  # SKU es la primera columna
                    self.ediar_producto(sku)  # Llama a la función de edición

        self.tree.bind("<Button-1>", on_tree_click)     
        
    def cargaInicial(self):
        listaCategoria = self.CategoriasRepository.obtener_Categorias()
        listaproveedor = self.ControladorProveedoresReposito.obtener_proveedores()
        listAlmacenes =  self.almacenesRepositorio.obtener_Almacenes()

        #Creacion de diccionario listaCategorias
        self.categorias_dict = {categoria.nombre: categoria.id_categoria for categoria in listaCategoria }
        self.categorias_id_to_nombre = {v: k for k, v in self.categorias_dict.items()}
        nombres_categoria =  ["Seleccione una opción"] + list(self.categorias_dict.keys())
        self.categoria['values'] = nombres_categoria
        self.categoria.current(0)
        
        #Creacion de diccionario listaProvedor
        self.proveedor_dict = {proveedor.nombre: proveedor.id_proveedor for proveedor in listaproveedor }
        self.proveedor_id_to_nombre = {v: k for k, v in self.proveedor_dict.items()}
        nombres_proveedor =  ["Seleccione una opción"] + list(self.proveedor_dict.keys())
        self.proveedor['values'] = nombres_proveedor
        self.proveedor.current(0)
        
        #LLenado de lista almacenes
        # Creamos un diccionario con nombre → id
        self.almacenes_dict = {almacen.nombre: almacen.id_almacen for almacen in listAlmacenes}
        # Insertamos el texto inicial
        self.almacen_id_to_nombre = {v: k for k, v in self.almacenes_dict.items()}
        nombres_almacenes = ["Seleccione una opción"] + list(self.almacenes_dict.keys())
        self.almacen['values'] = nombres_almacenes
        self.almacen.current(0)  # Seleccionar el primero por defecto

        self.codigoSku.insert(0,"Codigo SKU")
        self.codigoSku.config(state= 'disabled')
        
        self.optenerTodos()
        
    def Register(self):
        nombre= self.nombre.get()
        descripcion = self.descripcion.get()
        idcategoria = self.categorias_dict.get(self.categoria.get())
        stock = self.cantStock.get()
        stockMin = self.stockMin.get()
        codigoSku = self.codigoSku.get()
        idproveedor = self.proveedor_dict.get(self.proveedor.get())
        precioCompra = self.precio_compra.get()
        precioVenta = self.precio_venta.get()
        idalmacen = self.almacenes_dict.get(self.almacen.get())
        fechaCreacion = datetime.now()
        idProd = None
        
        if not nombre or not idcategoria or not codigoSku or not idproveedor or not idalmacen:
            messagebox.showerror(
                "Error", "Completa los campos nombre, categoria, proveedor y almacen para poder continuar ")
            return

        producto = ProductosModelo(
            id_producto = idProd,
            nombre = nombre,
            descripcion = descripcion,
            sku = codigoSku,
            id_categoria = idcategoria,
            id_proveedor = idproveedor,
            precio_compra = precioCompra,
            precio_venta = precioVenta,
            stock_actual = stock,
            stock_minimo = stockMin,
            id_almacen = idalmacen,
            fecha_creacion = fechaCreacion,
            indicadorHabilitado = 1 # 1 = habilitado, 0 = deshabilitado
        )
        print("editando", self.editando)
        if self.editando:
            self.ControladorProductoRepository.update(producto)
            messagebox.showinfo(
            message="Se actualizó el registro correctamente",
            title="Mensaje"
            )
            self.editando = False  # Restablecer el estado después de editar
        else:
            self.ControladorProductoRepository.register(producto)
            messagebox.showinfo(
                message="Se realizó el registro correctamente",
                title="Mensaje"
            )
        self.limpiar_campos()
        self.optenerTodos()
        
        
    def Inhabilitar(self):
        sku = self.codigoSku.get()
        if sku == "Codigo SKU":
            # Si el SKU es el valor por defecto, no se puede inhabilitar
            messagebox.showerror(
                "Error", "Selecciona un producto para inhabilitar")
            return
        else:
           
            self.ControladorProductoRepository.inhabilitar(sku)   
            self.limpiar_campos()
            self.optenerTodos()
            # Mostrar mensaje de éxito
            messagebox.showinfo(
                message="Se realizó el registro correctamente",
                title="Mensaje"
            )   
            messagebox.showerror("Error", "Selecciona un producto para inhabilitar")
            
    def optenerTodos(self):
        ListProductosAll = self.ControladorProductoRepository.obtener_productosAll()
        self.cargar_tabla(ListProductosAll)
        if ListProductosAll:
            ultimo_producto = ListProductosAll[-1].id_producto
            self.totalProductos=(len(ListProductosAll)+ultimo_producto)
        else:
            self.totalProductos = 0
            
    def cargar_tabla(self, lista_productos):
        # Limpiar primero el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for productos in lista_productos:
            self.tree.insert('', 'end', values=(
                productos.sku,
                productos.nombre, 
                productos.descripcion,
                productos.precio_compra,
                productos.precio_venta, 
                self.categorias_id_to_nombre.get(productos.id_categoria, "Desconocido"), 
                self.proveedor_id_to_nombre.get(productos.id_proveedor, "Desconocido"),
                productos.stock_actual,
                productos.stock_minimo,
                self.almacen_id_to_nombre.get(productos.id_almacen, "Desconocido"),
                "SI" if productos.indicadorHabilitado == 1 else "NO",
                "Editar"
                ))
            
    def crear_codigo_SKU(self, event=None):
        
        if(len(self.nombre.get()) > 2 and self.editando == False):
            
            nombre = self.nombre.get()[:3].upper()
            total = str(self.totalProductos+1)
            codigo = (nombre + total )
            self.codigoSku.config(state='normal')
            self.codigoSku.delete(0,tk.END)
            self.codigoSku.insert(0,codigo)
            self.codigoSku.config(state= 'disabled')

    def ediar_producto(self, sku):
        # Aquí puedes implementar la lógica para editar el producto
        # Por ejemplo, abrir un nuevo formulario con los datos del producto seleccionado
        print("Editar producto con SKU:", sku)
        productoAEditar = self.ControladorProductoRepository.getSku(sku)
        if productoAEditar:
            # Llenar los campos con los datos del producto
            self.nombre.delete(0, tk.END)
            self.nombre.insert(0, productoAEditar.nombre)
            self.descripcion.delete(0, tk.END)
            self.descripcion.insert(0, productoAEditar.descripcion)
            valorescat = list(self.categorias_dict.values())
            if productoAEditar.id_categoria in valorescat:
                indicecat = valorescat.index(productoAEditar.id_categoria)
                self.categoria.current(indicecat+1)  # +1 para omitir "Seleccione una opción"
            self.cantStock.delete(0, tk.END)
            self.cantStock.insert(0, int(productoAEditar.stock_actual))
            self.stockMin.delete(0, tk.END)
            self.stockMin.insert(0, int(productoAEditar.stock_minimo))
            self.codigoSku.config(state='normal')
            self.codigoSku.delete(0, tk.END)
            self.codigoSku.insert(0, productoAEditar.sku)
            self.codigoSku.config(state='disabled')
            valoresprov = list(self.proveedor_dict.values())
            if productoAEditar.id_proveedor in valoresprov:
                indiceprov = valoresprov.index(productoAEditar.id_proveedor)
                self.proveedor.current(indiceprov+1)  # +1 para omitir "Seleccione una opción"
            self.precio_compra.delete(0, tk.END)
            self.precio_compra.insert(0, int(productoAEditar.precio_compra))
            self.precio_venta.delete(0, tk.END)
            self.precio_venta.insert(0, int(productoAEditar.precio_venta))
            valoresalm = list(self.almacenes_dict.values())
            if productoAEditar.id_almacen in valoresalm:
                indicealm = valoresalm.index(productoAEditar.id_almacen)
                self.almacen.current(indicealm+1)  # +1 para omitir "Seleccione una opción"
            self.editando = True  # Cambia el estado a editando
        # Puedes usar un nuevo formulario o ventana emergente para editar el producto
        
    def limpiar_campos(self):
        print("Ingresa a limpiar")
        self.nombre.delete(0,tk.END)
        self.descripcion.delete(0,tk.END)
        self.categoria.current(0)
        self.cantStock.delete(0,tk.END)
        self.stockMin.delete(0,tk.END)
        self.codigoSku.config(state='normal')
        self.codigoSku.delete(0,tk.END)
        self.codigoSku.insert(0,"Codigo SKU")
        self.codigoSku.config(state= 'disabled')
        self.proveedor.current(0)
        self.precio_compra.delete(0,tk.END)
        self.precio_venta.delete(0,tk.END)
        self.almacen.current(0)
        self.editando = False

    
        
        
    