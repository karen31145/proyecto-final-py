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
from datetime import date

class FormProductos(FormProductosVista):
    def __init__(self, parent):
        self.almacenesRepositorio = almacenesRepository()
        self.CategoriasRepository = CategoriasRepository()
        self.ControladorProductoRepository = ControladorProductoRepository()
        self.ControladorProveedoresReposito = ControladorProveedoresReposito()

        
        super().__init__(parent)
        self.cargaInicial()        
        
    def cargaInicial(self):
        listaCategoria = self.CategoriasRepository.obtener_Categorias()
        listaproveedor = self.ControladorProveedoresReposito.obtener_proveedores()
        listAlmacenes =  self.almacenesRepositorio.obtener_Almacenes()

        #Creacion de diccionario listaCategorias
        self.categorias_dict = {categoria.nombre: categoria.id_categoria for categoria in listaCategoria }
        nombres_categoria =  ["Seleccione una opción"] + list(self.categorias_dict.keys())
        self.categoria['values'] = nombres_categoria
        self.categoria.current(0)
        
        #Creacion de diccionario listaProvedor
        self.proveedor_dict = {proveedor.nombre: proveedor.id_proveedor for proveedor in listaproveedor }
        nombres_proveedor =  ["Seleccione una opción"] + list(self.proveedor_dict.keys())
        self.proveedor['values'] = nombres_proveedor
        self.proveedor.current(0)
        
        #LLenado de lista almacenes
        # Creamos un diccionario con nombre → id
        self.almacenes_dict = {almacen.nombre: almacen.id_almacen for almacen in listAlmacenes}
        # Insertamos el texto inicial
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
        fechaCreacion = date.today()
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
            fecha_creacion = fechaCreacion
        )

        self.ControladorProductoRepository.register(producto)
        messagebox.showinfo(
            message="Se realizó el registro correctamente",
            title="Mensaje"
        )
        
    def optenerTodos(self):
        ListProductosAll = self.ControladorProductoRepository.obtener_productosAll()
        self.cargar_tabla(ListProductosAll)
        
    def cargar_tabla(self, lista_productos):
        # Limpiar primero el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for productos in lista_productos:
            self.tree.insert('', 'end', values=(
                productos.nombre, 
                productos.descripcion, 
                productos.descripcion, 
                productos.id_proveedor,
                productos.precio_compra,
                productos.precio_venta,
                productos.stock_actual,
                productos.stock_minimo,
                productos.id_almacen,
                productos.fecha_creacion
                ))

    
        
        
    