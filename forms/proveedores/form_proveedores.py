from forms.proveedores.vista_proveedores import FormProveedoresVista
from controladores.controlador_proveedores import ControladorProveedoresReposito
from tkinter import messagebox
from persistence.modelo_proveedores import ProveedoresModel


class FormProveedores(FormProveedoresVista):
    def __init__(self, parent):
        self.ControladorProveedoresReposito = ControladorProveedoresReposito()
        super().__init__(parent)

            # Aquí llamas el método al cargar el formulario
        self.optenerTodos()


    def Register(self):
        nombre = self.nombre.get()
        contacto = self.contacto.get()
        telefono = self.telefono.get()
        email = self.email.get()
        direccion = self.direccion.get()
        indicador_habilitado = True

        if not nombre or not contacto or not telefono or not email or not direccion:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        
        # ✅ Crear instancia de Aut_user con los datos
        proveedor = ProveedoresModel(
        nombre = self.nombre.get(),
        contacto = self.contacto.get(),
        telefono = self.telefono.get(),
        email = self.email.get(),
        direccion = self.direccion.get(),
        indicador_habilitado = True
        )

        # Buscar si el almacen ya existe
        proveedor_db: ProveedoresModel = self.ControladorProveedoresReposito.getByName(self.nombre.get())

        if self.isProveedorRegister(proveedor_db):
            self.ControladorProveedoresReposito.register(nombre,contacto,telefono,email,direccion,indicador_habilitado)
            messagebox.showinfo(
                message="Se realizó el registro correctamente",
                title="Mensaje"
            )
            self.optenerTodos()
    
    def isProveedorRegister(self, provedor: ProveedoresModel):
        status: bool = True
        if(provedor != None):
            status = False
            messagebox.showerror(
                message="Nombre de proveedor ya se encuentra registrado", title="Mensaje")
        return status;

    def optenerTodos(self):
       listProveedores =  self.ControladorProveedoresReposito.obtener_proveedores()
       self.cargar_datos(listProveedores)       

    def cargar_datos(self, lista_proveedores):
        # Limpiar primero el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for proveedores in lista_proveedores:
            self.tree.insert('', 'end', values=(proveedores.nombre, proveedores.contacto, proveedores.telefono, proveedores.email,proveedores.direccion))

