import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.categorias.vista_categorias import FormCategoriasVista
from controladores.controlador_categorias import CategoriasRepository
from persistence.modelo_categorias import CategoriaModelo
import util.encoding_decoding as end_dec
from forms.registration.form import FormRegister

class FormCategorias(FormCategoriasVista):

    def __init__(self, parent):
        self.CategoriasRepository = CategoriasRepository()
        super().__init__(parent)  # Llamar al constructor de la clase base
        # Ahora puedes hacer lo demás

        # Aquí llamas el método al cargar el formulario
        self.optenerTodos()

    def registrar_categorias(self):
        nombre = self.nombre.get()
        descripcion = self.descripcion.get()

        if not nombre or not descripcion:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

    def Register(self):
        nombre = self.nombre.get()
        descripcion = self.descripcion.get()

        if not nombre or not descripcion:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        
        # ✅ Crear instancia de Aut_user con los datos
        categorias = CategoriaModelo(
            nombre=self.nombre.get(),
            descripcion=self.descripcion.get()
        )

        # Buscar si el almacen ya existe
        categorias_db: CategoriaModelo = self.CategoriasRepository.getByName(self.nombre.get())

        if self.iscategoriaRegister(categorias_db):
            self.CategoriasRepository.register(categorias.nombre, categorias.descripcion)
            messagebox.showinfo(
                message="Se realizó el registro correctamente",
                title="Mensaje"
            )
            self.optenerTodos()
    
    def iscategoriaRegister(self, Categorias: CategoriaModelo):
        status: bool = True
        if(Categorias != None):
            status = False
            messagebox.showerror(
                message="Nombre de categoria ya se encuentra registrado", title="Mensaje")
        return status;

    def optenerTodos(self):
       listCategorias =  self.CategoriasRepository.obtener_Categorias()
       self.cargar_datos(listCategorias)       

    def cargar_datos(self, lista_categorias):
        # Limpiar primero el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for categorias in lista_categorias:
            self.tree.insert('', 'end', values=(categorias.nombre, categorias.descripcion))
            
        
    def inhabilitar(self):
        nombre = self.nombre.get()
        if nombre=="nombre":
            messagebox.showerror("Error", "Selecciona una categoria para inhabilitar.")
            return
    
        else:
            self.CategoriasRepository.inhabilitar(nombre)
            self.limpiar_campos()
            self.optenerTodos()
            messagebox.showinfo(
                message="Se realizó la inhabilitación correctamente",
                title="Mensaje"
            )
            messagebox.showerror("Error", "Selecciona un producto para inhabilitar")
    
    
    def limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.descripcion.delete(0, tk.END)
        self.nombre.focus()