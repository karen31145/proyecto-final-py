import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.ventas.vista_ventas import FormVentasVista
from controladores.controlador_ventas import VentasRepository
from persistence.modelo_ventas import VentaModelo

class FormVentas(FormVentasVista):
    def __init__(self, parent):
        self.VentasRepository = VentasRepository()
        super().__init__(parent)

        # Obtener todas las ventas al inicio
        self.obtenerTodos()

    def Register(self):
        print('ingresa a register del form')
        # Obtener los valores de los campos del formulario
        id_producto = self.id_producto.get()
        cantidad = self.cantidad.get()
        fecha = self.fecha.get()
        codigo_venta = self.codigo_venta.get()

        # Validar que los campos no estén vacíos
        if not cantidad or not fecha or not codigo_venta:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        # Verificar si la venta ya está registrada por código de venta
        venta_db = self.VentasRepository.getByCodigo(codigo_venta)

        # Si la venta no está registrada, registrar la nueva venta
        if not self.isVentaRegistrada(venta_db):
            self.VentasRepository.register(
                id_producto = id_producto,
                cantidad=cantidad,
                fecha=fecha,
                codigo_venta=codigo_venta
            )
            messagebox.showinfo("Mensaje", "Se realizó el registro correctamente")
            self.obtenerTodos()  # Recargar las ventas después del registro
        else:
            messagebox.showerror("Error", "El código de venta ya está registrado.")

    def isVentaRegistrada(self, venta: VentaModelo):
        # Si la venta ya está registrada, no permitir el registro
        return venta is not None

    def obtenerTodos(self):
        # Obtener todas las ventas de la base de datos y cargar los datos
        lista_ventas = self.VentasRepository.obtener_Ventas()
        self.cargar_datos(lista_ventas)

    def cargar_datos(self, lista_ventas):
        # Limpiar la tabla antes de cargar nuevos datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar las ventas en la tabla
        for ventas in lista_ventas:
            self.tree.insert('', 'end', values=(
                ventas.id_producto,
                ventas.cantidad,
                ventas.fecha,
                ventas.codigo_venta
            ))
            
    def Inhabilitar(self):
        id_producto = self.id_producto.get()
        if id_producto=="id producto":
            messagebox.showerror("Error", "Ingrese el ID del producto a eliminar.")
            return      
        else:
            
            self.VentasRepository.inhabilitar(id_producto)
            self.limpiar_campos()
            self.obtenerTodos()
            messagebox.showinfo(
                message="Se realizó la inhabilitación correctamente",
                title="Mensaje"
            )
            messagebox.showerror("Error", "Selecciona un producto para inhabilitar")
    def limpiar_campos(self):
        # Limpiar los campos del formulario
        self.id_producto.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.fecha.delete(0, tk.END)
        self.codigo_venta.delete(0, tk.END)