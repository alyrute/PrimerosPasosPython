import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Clientes import * 
from Conexion import * 


class FormularioPersonas:
    def __init__(self):
        self.base = Tk()
        self.textBoxId = None
        self.textBoxNombre = None
        self.textBoxApellidos = None
        self.combo = None
        self.grupBox = None
        self.tree = None
        self.textBoxTlf = None
        self.textBoxEdad = None
        self.textBoxEmail = None
    
    def Formulario(self):
       
        global base, textBoxId , textBoxNombre , textBoxApellidos, textBoxTlf, textBoxEdad, textBoxEmail, combo, grupBox , tree
        
        try:
            
            self.base.geometry("1850x600")
            self.base.title("Formulario de registro de personas")
            
            self.grupBox= LabelFrame(self.base, text="Datos del Personal", padx=5, pady=5)
            self.grupBox.grid(row=0, column=0, padx=10, pady=10)
            
            self.grupBox= LabelFrame(self.base, text="Datos del Personal", padx=5, pady=5)
            self.grupBox.grid(row=0, column=0, padx=10, pady=10)
            
            labelId=Label( self.grupBox, text="ID:", width=13, font=("arial" , 14)).grid(row=0, column=0)
            self.textBoxId = Entry( self.grupBox, state="disabled")
            self.textBoxId.grid(row=0, column=1)
            

            labelNombre=Label(self.grupBox, text="Nombre:", width=13, font=("arial" , 14)).grid(row=1, column=0)
            self.textBoxNombre = Entry( self.grupBox)
            self.textBoxNombre.grid(row=1, column=1)
            
            
            labelApellidos=Label( self.grupBox, text="Apellidos:", width=13,font=("arial" , 14)).grid(row=2, column=0)
            self.textBoxApellidos = Entry( self.grupBox)
            self.textBoxApellidos.grid(row=2, column=1)
            
            #tlf
            labelTlf=Label( self.grupBox, text="Telefono:", width=13,font=("arial" , 14)).grid(row=3, column=0)
            self.textBoxTlf = Entry( self.grupBox)
            self.textBoxTlf.grid(row=3, column=1)
            
            #edad
            
            labelEdad=Label( self.grupBox, text="Edad:", width=13,font=("arial" , 14)).grid(row=4, column=0)
            self.textBoxEdad = Entry( self.grupBox)
            self.textBoxEdad.grid(row=4, column=1)
            
            
            #Email
            
            
            labelEmail=Label( self.grupBox, text="Email:", width=13,font=("arial" , 14)).grid(row=5, column=0)
            self.textBoxEmail = Entry( self.grupBox)
            self.textBoxEmail.grid(row=5, column=1)
            
            
            labelSexo=Label( self.grupBox, text="Sexo:", width=13,font=("arial" , 14)).grid(row=6, column=0)
            seleccionSexo = StringVar()
            self.combo = ttk.Combobox( self.grupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            self.combo.grid(row=6, column=1)
            seleccionSexo.set("Seleccione")
            
            
            Button(self.grupBox, text="Guardar", width=10 , command=self.guardarRegistros).grid(row=7, column=0)
            Button(self.grupBox, text="Modificar", width=10).grid(row=7, column=1)
            Button(self.grupBox, text="Eliminar", width=10).grid(row=7, column=2)
            
            
            self.grupBox = LabelFrame( self.base, text="Lista de personas", padx=5, pady=5)
            self.grupBox.grid(row=0, column=1, padx=5, pady=5)
            
            #Creamos un treeview
            
            tree= ttk.Treeview( self.grupBox,  columns=("ID", "Nombre", "Apellidos","Telefono" , "Edad", "Email",  "Sexo"), show='headings', height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="ID")
            
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombre")
            
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellidos")
            
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Telefono")
            
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="Edad")
            
            tree.column("# 6", anchor=CENTER)
            tree.heading("# 6", text="Email")
            
            tree.column("# 7", anchor=CENTER)
            tree.heading("# 7", text="Sexo")
            tree.pack()
            
            
        except ValueError as error:
            print("Error al mostrar la interfaz, error : {}".format(error))
            
            
    def guardarRegistros(self):
       
        
        try:
            #Verificar su los widgest estan inicializados. 
# if textBoxNombre is None or textBoxApellidos is None or combo is None:
 #               print(" los widgets no estan inicializados")
  #              return"""
            nombre = self.textBoxNombre.get()
            apellido= self.textBoxApellidos.get()
            telefono= self.textBoxTlf.get()
            edad= self.textBoxEdad.get()
            email=self.textBoxEmail.get()
            sexo= self.combo.get()
            
           
            
            Cclientes.ingresarCliente(nombre, apellido, telefono, edad, email, sexo)
            messagebox.showinfo("Perfecto!", "Los datos fueron guardados correctamente.")
            
            #Luego limpiamos los campos
            
            self.textBoxNombre.delete(0,END)
            self.textBoxApellidos.delete(0,END)
            self.textBoxTlf.delete(0,END)
            self.textBoxEdad.delete(0,END)
            self.textBoxEmail.delete(0,END)
           
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))
            
            
app = FormularioPersonas()
app.Formulario()
app.base.mainloop()