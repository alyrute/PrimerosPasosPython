import tkinter
import tkinter.messagebox

import mysql.connector

server= 'localhost'
port = '3306'
bd = 'bbddprueba'
usuario = 'ali'
contrasena = 'ali1'

try:
    conexion = mysql.connector.connect(
        host=server,
        port=port,
        database=bd,
        user=usuario,
        password=contrasena)
    
    if conexion.is_connected():
        print("Conexión exitosa")
      
        
except Exception as e:
    print("Error en la conexion")
    print(e)
    
    
cursor = conexion.cursor()
cursor.execute("SELECT * FROM persona")


# Definir la función consulta
def consulta(conexion, query):
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#------------Ventana-------------

ventana= tkinter.Tk()
ventana.title("Ventana de prueba")
ventana.geometry("500x500")
#para no dejar que cambien el tamaño de la ventana
ventana.resizable(0,0)

#Eticquetas

cabezera = tkinter.Label(ventana, text="Hola Mundo")
cabezera.pack()

  
    
    
    #recuerda que necesita las ruta completa

#img=tkinter.PhotoImage(file="C:\WSPython\Python\ea.png")   
#lbl_img = tkinter.Label(ventana, image=img)
#lbl_img.pack()



from tkinter import *



lista= tkinter.Listbox(ventana)
lista.insert(1, "Hola")

# Llamar a la función consulta
personas = consulta(conexion, "SELECT * FROM persona")
for persona in personas:
    print(persona)

lista.pack()
    
ventana.mainloop()

lista.pack()
    
    
    
    
    
ventana.mainloop()
