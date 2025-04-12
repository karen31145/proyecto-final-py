import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

def ListaProductos():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('lista de productos')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana,800,500)
        

        #Frame logo
        #configuracion del contenedor
        frame_logo = tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID,padx=10,pady=10,bg='green')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        #ajusta la configuracion del label
        label = tk.Label(frame_logo,image=logo,bg='green')
        label.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES, fill=tk.BOTH)
        #end frame form

        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Times',30), fg="#666a88",bg="#fcfcfc",pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
        
        etiqueta_usuario = tk.Label(frame_form_fill,text="Usuario", font=('Times', 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill,font=('Times',14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill,text="Contraseña", font=('Times', 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill,font=('Times',14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Inicio sesion",font=('Times',15, BOLD),bg="#3a7ff6",bd=0,fg="#fff", command=self.validarContrasena)
        inicio.pack(fill=tk.X, padx=20,pady=20)
        inicio.bind("<Return>",(lambda event: self.validarContrasena()))

        registro = tk.Button(frame_form_fill,text="Registrar usuario",font=('Times',15, BOLD),bg="white",bd=0,fg="#3a7ff6", command=self.userRegister)
        registro.pack(fill=tk.X, padx=20,pady=20)     
        registro.bind("<Return>",(lambda event: self.userRegister()))
        #end frame_form_fill
        
        
        self.ventana.mainloop()
    