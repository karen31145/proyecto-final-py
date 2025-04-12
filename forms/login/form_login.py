import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.vista_login import FormLoginVista

class FormLogin(FormLoginVista):
    def validarContrasena(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="Usuario o contraseña no es correcto",title="Error")
    
    def __init__(self):
        super().__init__()
                                     