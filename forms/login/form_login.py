import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.vista_login import FormLoginVista
from persistence.repositorio.auth_user_repository import AuthUserRepository
from persistence.modelo import Aut_user
import util.encoding_decoding as end_dec
from forms.registration.form import FormRegister

class FormLogin(FormLoginVista):

    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()
    #inhabilitar la funcion de la validacion en base de dato
    def validarContrasena(self):
    
        user_db: Aut_user = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)

    def userRegister(self):
        FormRegister().mainloop()

    
    def isUser(self,user : Aut_user):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe por favor registrate", title="Mensaje"
            )
        return status
    
    def isPassword(self, password: str, user : Aut_user):
        b_password = user.password
        if(password  == end_dec.decrypt(b_password)):
            self.ventana.destroy()
            MasterPanel()
            messagebox.showerror(
                message="El usuario no existe por favor registrate", title="Mensaje"
            )

    def cancelarLogin(self):
        self.ventana.destroy()
        MasterPanel()

                                     