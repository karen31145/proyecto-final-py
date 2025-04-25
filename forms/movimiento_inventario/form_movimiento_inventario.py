import tkinter as tk
from tkinter import messagebox

from forms.movimiento_inventario.vista_movimiento_inventario import FormMovimientoInventarioVista
from controladores.controlador_movimiento_inventario import ControladorMovimientoInventarioRepository
from persistence.modelo_movimiento_inventarios import MovimientoInventariosModel


class FormMovimientoInventario(FormMovimientoInventarioVista):
    def __init__(self, parent):
        self.controladorMovimientoInventarioRepository = ControladorMovimientoInventarioRepository()
        self.editando = False
        self.totalMovimientoInventario = 0
        super().__init__(parent)
        self.obtener_todos()

    def Register(self):
        id_producto = self.id_producto.get()
        tipo_movimiento = self.tipo_movimiento.get()    
        cantidad = self.cantidad.get()
        proveedor = self.proveedor.get()
        id_almacen = self.id_almacen.get()
        referencia = self.referencia.get()
        observaciones = self.observaciones.get()

        if not all([id_producto, tipo_movimiento, cantidad, proveedor, id_almacen, referencia, observaciones]):
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        movimiento = MovimientoInventariosModel(
            id_producto=id_producto,
            tipo_movimiento=tipo_movimiento,
            cantidad=cantidad,
            proveedor=proveedor,
            id_almacen=id_almacen,
            referencia=referencia,
            observaciones=observaciones
        )

        if self.editando:
            self.controladorMovimientoInventarioRepository.update(movimiento)
            messagebox.showinfo("Mensaje", "Se actualizó el registro correctamente")
            self.editando = False
        else:
            self.controladorMovimientoInventarioRepository.register(movimiento)
            messagebox.showinfo("Mensaje", "Se realizó el registro correctamente")

        self.limpiar_campos()
        self.obtener_todos()

    def Inhabilitar(self):
        sku = self.codigoSku.get()
        if sku == "Codigo SKU" or not sku:
            messagebox.showerror("Error", "Selecciona un producto para inhabilitar")
            return

        self.controladorMovimientoInventarioRepository.inhabilitar(sku)
        self.limpiar_campos()
        self.obtener_todos()
        messagebox.showinfo("Mensaje", "Producto inhabilitado correctamente")

    def obtener_todos(self):
        lista = self.controladorMovimientoInventarioRepository.obtener_movimientoinventarioAll()
        self.tree.delete(*self.tree.get_children())  # Limpiar la tabla

        self.totalMovimientoInventario = (len(lista) + lista[-1].id_producto) if lista else 0

        for mi in lista:
            self.tree.insert('', 'end', values=(
                mi.id_producto,
                mi.tipo_movimiento,
                mi.cantidad,
                mi.proveedor,
                mi.id_almacen,
                mi.referencia,
                mi.observaciones
            ))

    def crear_codigo_SKU(self, event=None):
        nombre = self.nombre.get()
        if len(nombre) > 2 and not self.editando:
            codigo = nombre[:3].upper() + str(self.totalMovimientoInventario + 1)
            self.codigoSku.config(state='normal')
            self.codigoSku.delete(0, tk.END)
            self.codigoSku.insert(0, codigo)
            self.codigoSku.config(state='disabled')

    def editar_movimiento_almacen(self, sku):
        movimiento = self.controladorMovimientoInventarioRepository.getSku(sku)
        if movimiento:
            self.id_producto.delete(0, tk.END)
            self.id_producto.insert(0, movimiento.id_producto)

            self.tipo_movimiento.delete(0, tk.END)
            self.tipo_movimiento.insert(0, movimiento.tipo_movimiento)

            self.cantidad.delete(0, tk.END)
            self.cantidad.insert(0, movimiento.cantidad)

            self.proveedor.delete(0, tk.END)
            self.proveedor.insert(0, movimiento.proveedor)

            self.id_almacen.delete(0, tk.END)
            self.id_almacen.insert(0, movimiento.id_almacen)

            self.referencia.delete(0, tk.END)
            self.referencia.insert(0, movimiento.referencia)

            self.observaciones.delete(0, tk.END)
            self.observaciones.insert(0, movimiento.observaciones)

            self.editando = True

    def limpiar_campos(self):
        self.id_producto.delete(0, tk.END)
        self.tipo_movimiento.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.proveedor.delete(0, tk.END)
        self.id_almacen.delete(0, tk.END)
        self.referencia.delete(0, tk.END)
        self.observaciones.delete(0, tk.END)
        
        self.codigoSku.config(state='normal')
        self.codigoSku.delete(0, tk.END)
        self.codigoSku.insert(0, "Codigo SKU")
        self.codigoSku.config(state='disabled')

        self.editando = False
