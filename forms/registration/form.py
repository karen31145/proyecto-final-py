from forms.registration.form_designer import FormRegisterDesigner
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk
from persistence.repositorio.auth_user_repository import AuthUserRepository
from persistence.modelo import Aut_user

class FormRegister(FormRegisterDesigner):
    
    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()
    
    def Register(self):
        if self.isConfirmationPassword():
            # ✅ Crear instancia de Aut_user con los datos
            user = Aut_user(
                nombre_usuario=self.usuario.get(),
                password=end_dec.encrypted(self.password.get())
            )

        # Buscar si el usuario ya existe
        user_db: Aut_user = self.auth_repository.getUserByUserName(self.usuario.get())

        if self.isUserRegister(user_db):
            self.auth_repository.insertUser(user)
            messagebox.showinfo(
                message="Se realizó el registro correctamente",
                title="Mensaje"
            )
            self.ventana.destroy()

            
    def isConfirmationPassword(self):
        status: bool = True
        if(self.password.get() != self.confirmacion.get()):
            status = False
            messagebox.showerror(
                message="La contraseña no coinciden por favor inenta nuevamente", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmacion.delete(0, tk.END)
        return status;

    def isUserRegister(self, user: Aut_user):
        status: bool = True
        if(user != None):
            status = False
            messagebox.showerror(
                message="Nombre de usuario ya se encuentra registrado", title="Mensaje")
        return status;
