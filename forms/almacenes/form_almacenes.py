import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.almacenes.vista_almacenes import FormAlmacenesVista
from controladores.almacenes_controlador import almacenesRepository
from persistence.modelo_almacenes import Alamacenes
import util.encoding_decoding as end_dec
from forms.registration.form import FormRegister

class FormAlmacen(FormAlmacenesVista):

    def __init__(self, parent):
        self.almacenesRepositorio = almacenesRepository()
        super().__init__(parent)  # Llamar al constructor de la clase base
        # Ahora puedes hacer lo demás

        # Aquí llamas el método al cargar el formulario
        self.optenerTodos()

    def registrar_almacen(self):
        nombre = self.nombre.get()
        ubicacion = self.ubicacion.get()

        if not nombre or not ubicacion:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

    def Register(self):
        nombre = self.nombre.get()
        ubicacion = self.ubicacion.get()

        if not nombre or not ubicacion:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        
        # ✅ Crear instancia de Aut_user con los datos
        alamacen = Alamacenes(
            nombre=self.nombre.get(),
            ubicacion=self.ubicacion.get()
        )

        # Buscar si el almacen ya existe
        Alamacenes_db: Alamacenes = self.almacenesRepositorio.getByName(self.nombre.get())

        if self.isAlmacenRegister(Alamacenes_db):
            self.almacenesRepositorio.register(alamacen.nombre, alamacen.ubicacion)
            messagebox.showinfo(
                message="Se realizó el registro correctamente",
                title="Mensaje"
            )
            self.optenerTodos()
    
    def isAlmacenRegister(self, almacen: Alamacenes):
        status: bool = True
        if(almacen != None):
            status = False
            messagebox.showerror(
                message="Nombre de Almacen ya se encuentra registrado", title="Mensaje")
        return status;

    def optenerTodos(self):
       listAlmacenes =  self.almacenesRepositorio.obtener_Almacenes()
       self.cargar_datos(listAlmacenes)       

    def cargar_datos(self, lista_almacenes):
        # Limpiar primero el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for almacen in lista_almacenes:
            self.tree.insert('', 'end', values=(almacen.nombre, almacen.ubicacion))
            
            
    def Inhabilitar(self):
        nombre = self.nombre.get()
        if nombre=="nombre":
            messagebox.showerror("Error", "Selecciona un almacen para inhabilitar.")
        else:
             # Aquí llamas el método al cargar el formulario
            self.almacenesRepositorio.Inhabilitar(nombre)
            self.limpiarCampos()
            self.optenerTodos
            messagebox.showinfo(
                message="Se realizó la inhabilitación correctamente",
                title="Mensaje"
            )
            messagebox.showerror("Error", "Selecciona un producto para inhabilitar")
            
            
            
    def limpiar_campos(self):
        print("ingresa a limpiar")
        self.nombre.delete(0, tk.END)
        self.ubicacion.delete(0, tk.END)
        self.editando = False