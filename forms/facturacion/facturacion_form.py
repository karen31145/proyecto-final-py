import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.facturacion.facturacion_vista import VistaFacturacion
from controladores.controlador_productos import ControladorProductoRepository
from controladores.controlador_ventas import VentasRepository
from persistence.modelo_productos import ProductosModelo
from persistence.modelo_ventas import VentaModelo
from typing import List
from datetime import datetime


class FacturacionForm(VistaFacturacion):
    def __init__(self, parent):
        self.ControladorProductoRepository = ControladorProductoRepository()
        self.VentasRepository = VentasRepository()
        super().__init__(parent)
        self.cargarProductos()
        self.valoresTabla = []

        def on_tree_click(event):
            region = self.tree.identify("region", event.x, event.y)
            if region == "cell":
                columna = self.tree.identify_column(event.x)
                fila = self.tree.identify_row(event.y)
                if columna == "#7":  # "editar" es la columna 12 (empieza desde 1)
                    valores = self.tree.item(fila, "values")
                    idtem = valores[0]  # SKU es la primera columna
                    self.quitar_producto(idtem)  # elimina el producto del listado

        self.tree.bind("<Button-1>", on_tree_click)     

    def cargarProductos(self):
        self.listaProductos: List[ProductosModelo] =self.ControladorProductoRepository.findByIndicadorHabilitado()
        if(len(self.listaProductos)<=0):
            messagebox.showwarning(title='Error', message='No se han encontrado productos')
        else:
            #Funcion para realizar un recorido por productos y arrojar un mensaje si el stock es bajo
            # Recorrido por productos buscando los que tienen un stock actual bajo
            productos_bajo_stock = [
                producto for producto in self.listaProductos
                if producto.stock_actual <= producto.stock_minimo
            ]
            print('Cantidad de produscos bajo de stock', len(productos_bajo_stock))
            #Si se encuentran productos se procede a crear un mensaje recorriendo la lista anterior
            if productos_bajo_stock:
                mensaje = "⚠ Productos con stock bajo:\n\n"
                for producto in productos_bajo_stock:
                    mensaje += f"- {producto.nombre} - {producto.descripcion}: actual {producto.stock_actual}, minimo {producto.stock_minimo}\n"
            messagebox.showwarning("Alerta de stock", mensaje)

            #LLama el metodo que llena la lista desplegable de productos
            self.llenarLista(self.listaProductos)

    def llenarLista(self, listaProductos):
        #Creacion de diccionario ListaProductos
        #Concateno el nombre y la descripcion para que en el listado sea mas diciente 
        self.prodducto_dict = {(f"{producto.nombre} - {producto.descripcion}"): producto.id_producto for producto in listaProductos }
        self.producto_id_to_nombre = {v: k for k, v in self.prodducto_dict.items()}
        nombres_productos =  ["Seleccione una opción"] + list(self.prodducto_dict.keys())
        self.combo_producto['values'] = nombres_productos
        self.combo_producto.current(0)
    
    ##En esta funcion se va capturar la informacion del producto
    ##llenamos la lista la cual se muestra en la tabla 
    ## Y armamos el objeto el cual va a ir a actualizar el registro de ventas (!!Importante todos los productos que se agreguen en el mismo momento deben tener el mismo codigo de venta)



    def agregar_producto(self):
        idProducto = self.prodducto_dict.get(self.var_producto.get())
        cantidad =  int(self.var_cantidad.get()) if self.var_cantidad.get() else 1

        print(f"Producto agregado: {self.var_producto.get()}")
        print(f"id producto {idProducto} cantidad {cantidad}")

        ## se valida al momento de agregar que los campos tenga datos válidos
        if(idProducto == None):
            messagebox.showerror('Información','Debes seleccionar un producto')
            return
        if(cantidad < 1):
            messagebox.showerror('Información','La cantidad no puede ser inferior a 1')
            return

        ## Aca empezamos el armado de la lista que se mostrar en la tabla 

        productoSeleccionado = next(
            (producto for producto in self.listaProductos if producto.id_producto == idProducto), None
        )

        
        productoAdd = {
            "idenTemp": len(self.valoresTabla)+1, ## Identificador temporal por si se desea eliminar un elemento
            "idproducto": productoSeleccionado.id_producto,
            "nombre": productoSeleccionado.nombre,
            "codigo": productoSeleccionado.sku,
            "cantidad": cantidad,
            "precioUn": productoSeleccionado.precio_venta,
            "precioTotal": (productoSeleccionado.precio_venta * cantidad)
        }
        
        self.valoresTabla.append(productoAdd)
        print(self.valoresTabla)
        self.actualizarTabla()
        productoAdd = None
        self.actualizar_stock_por_venta() #Actualizar lista
        self.llenarLista(self.listaProductos)

    #elimina los registros temporales de la lista 
    def quitar_producto(self,idtemp):
        confirmar = messagebox.askyesno('Confirmar','Deseas quitar el producto ' )
        if confirmar:
            print('Eliminando')
            #se hace un recorrido en la lista por y se excluye el idtemporal 
            self.valoresTabla = [
                producto for producto in self.valoresTabla
                if producto["idenTemp"] != int(idtemp)
            ]
            #cuando termina se envia a reorganizaar lo ids temporarles para evitar duplicados
            self.reorganizar_ids_temporales()
            print('nueva vista',self.valoresTabla)
            # y nuevamente actualiza la tabla con la nueva vista
            self.actualizarTabla()
        else:
            print('no se elimina')
    
    def actualizarTabla(self):
        # Limpiar todos los elementos del Treeview
        for item in self.tree.get_children():
             self.tree.delete(item)

        for i,productos in enumerate(self.valoresTabla, start=1):
            self.tree.insert('', 'end', values=(
                productos["idenTemp"],
                productos["nombre"],
                productos["codigo"],
                productos["cantidad"],
                productos["precioUn"],
                productos["precioTotal"],
                "Eliminar"
            ))
    
    #Reorganiza la los ids para que no queden duplicados 
    def reorganizar_ids_temporales(self):
        for idx, producto in enumerate(self.valoresTabla, start=1):
            producto["idenTemp"] = idx


    def confirmar_venta(self):
        ##Funcion épica tenemos que actualizar productos donde actualizaremos la cantidad  en stock y creamos el registro de ventas 
        # 1 Actualizamos la tabla productos 
        confirmar = messagebox.askyesno('Confirmar','¿ Deseas continuar con la venta ?' )
        if confirmar:
            #Creamos el regisro en la tabla de ventas
            self.AddVentas()
            #Actualizamos la lista de productos 
            self.actualizar_stock_por_venta()
            self.ControladorProductoRepository.update_all(self.listaProductos)
        else:
            return
        print("Venta confirmada")

        #Restablece tabla 
        self.restablecerTabla()

    def AddVentas(self):
        ventas_a_insertar = []
        for item in self.valoresTabla:
            venta = VentaModelo(
                id_producto=item['idproducto'],
                cantidad=item['cantidad'],
                fecha=datetime.now(),  # o usa self.fecha_venta si tienes una
                codigo_venta= "VEN" + datetime.now().strftime("%Y%m%d%H%M%S")  # asegúrate de tener este valor definido
            )
            ventas_a_insertar.append(venta)
        self.VentasRepository.AddAll(ventas_a_insertar)


    ##Funcion para acualizar la cantidad de los productos en la lista 
    def actualizar_stock_por_venta(self):
        for producto_tabla in self.valoresTabla:
            id_buscado = producto_tabla["idproducto"]
            cantidad_restar = producto_tabla["cantidad"]

            for producto_modelo in self.listaProductos:
                if producto_modelo.id_producto == id_buscado:
                    producto_modelo.stock_actual -= cantidad_restar
                    break  # Ya encontramos el producto, no es necesario seguir


    def restablecerTabla(self):
        self.valoresTabla =[]
        self.actualizarTabla()
