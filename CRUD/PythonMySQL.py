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
            self.textBoxId = Entry( self.grupBox)
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
            Button(self.grupBox, text="Modificar", width=10, command=self.modificarRegistro).grid(row=7, column=1)
            Button(self.grupBox, text="Eliminar", width=10).grid(row=7, column=2)
            
            
            self.grupBox = LabelFrame( self.base, text="Lista de personas", padx=5, pady=5)
            self.grupBox.grid(row=0, column=1, padx=5, pady=5)
            
            #Creamos un treeview
            
            self.tree= ttk.Treeview( self.grupBox,  columns=("ID", "Nombre", "Apellidos","Telefono" , "Edad", "Email",  "Sexo"), show='headings', height=5)
            self.tree.column("# 1", anchor=CENTER)
            self.tree.heading("# 1", text="ID")
            
            self.tree.column("# 2", anchor=CENTER)
            self.tree.heading("# 2", text="Nombre")
            
            self.tree.column("# 3", anchor=CENTER)
            self.tree.heading("# 3", text="Apellidos")
            
            self.tree.column("# 4", anchor=CENTER)
            self.tree.heading("# 4", text="Telefono")
            
            self.tree.column("# 5", anchor=CENTER)
            self.tree.heading("# 5", text="Edad")
            
            self.tree.column("# 6", anchor=CENTER)
            self.tree.heading("# 6", text="Email")
            
            self.tree.column("# 7", anchor=CENTER)
            self.tree.heading("# 7", text="Sexo")
           
            for row in Cclientes.mostrarClientes():
               self.tree.insert("","end", values=row)
               
            #Ejecutar la funcion de hacer click y mostrar el resultado. 
            self.tree.bind("<<TreeviewSelect>>", self.seleccionarRegistro)
            
           
            
        except ValueError as error:
            print("Error al mostrar la interfaz, error : {}".format(error))
        
        self.tree.pack()  
            
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
            
            
            self.actualizarTreeView()
            
            
            #Luego limpiamos los campos
            
            self.textBoxNombre.delete(0,END)
            self.textBoxApellidos.delete(0,END)
            self.textBoxTlf.delete(0,END)
            self.textBoxEdad.delete(0,END)
            self.textBoxEmail.delete(0,END)
           
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))
            
     
     
     
     
    def actualizarTreeView(self):
        global tree
        try:
            #Borrar todos los elementos actuales del TreeView
            self.tree.delete(*self.tree.get_children())
            
            #Obtenemos los nuevos datos que queremos mostrar. 
            self.datos= Cclientes.mostrarClientes()
            
            #Insertamos los nuevos datos en el TreeView
            for row in Cclientes.mostrarClientes():
                self.tree.insert("","end", values=row)
                
        except ValueError as error:
            print("Error al actualizar tablas {}".format(error))    

    def seleccionarRegistro (self, event):
        try:
            #Obtener elemento seleccionado. 
            self.itensSeleccionado=self.tree.focus()
            
            
            if self.itensSeleccionado:
                #Obtenemos los valores por columnas, 
                self.values=self.tree.item(self.itensSeleccionado)['values']
                self.textBoxId.delete(0,END)
                self.textBoxId.insert(0,self.values[0])
                
                self.textBoxNombre.delete(0,END)
                self.textBoxNombre.insert(0,self.values[1])
                
                self.textBoxApellidos.delete(0,END)
                self.textBoxApellidos.insert(0,self.values[2])
                
                
                self.textBoxTlf.delete(0,END)
                self.textBoxTlf.insert(0,self.values[3])
                
                
                self.textBoxEdad.delete(0,END)
                self.textBoxEdad.insert(0,self.values[4])
                
                
                self.textBoxEmail.delete(0,END)
                self.textBoxEmail.insert(0,self.values[5])
                
                self.combo.set(self.values[6])
                
                
                
                 
        
        except ValueError as error:
            print("HAY UN ERROR CHICA! {}".format(error))    
     
     
     
    def modificarRegistro(self):
       
        global base, textBoxId , textBoxNombre , textBoxApellidos, textBoxTlf, textBoxEdad, textBoxEmail, combo, grupBox , tree
        
        try:
            if self.textBoxId is None or self.textBoxNombre is None or self.textBoxApellidos is None or self.textBoxTlf is None or self.textBoxEdad is None or self.textBoxEmail is None or self.combo is None:
                print("Los widgest no estan inicializados.") 
                return
            
            id=self.textBoxId.get()
            nombre = self.textBoxNombre.get()
            apellido= self.textBoxApellidos.get()
            telefono= self.textBoxTlf.get()
            edad= self.textBoxEdad.get()
            email=self.textBoxEmail.get()
            sexo= self.combo.get()
            
           
            
            Cclientes.modificarCliente(id,nombre, apellido, telefono, edad, email, sexo)
            messagebox.showinfo("Perfecto!", "Los datos fuero actualizados correctamente..")
            
            
            self.actualizarTreeView()
            
            
            #Luego limpiamos los campos
            self.textBoxId.delete(0,END)
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