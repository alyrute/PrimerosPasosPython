from tkinter import *
from PIL import Image, ImageTk
import tkinter




image= Image.open("C:\WSPython\Python\ea.png")
image = image.resize((150,150), Image.ANTIALIAS)


#Botones

def saludo():
    tkinter.Label(ventana, text="Hola pinche weiiiiii").pack()

def salir():
    ventana.destroy()

boton = tkinter.Button(ventana, text="Invoca un Saludo", command=saludo)
boton.place(x=300, y=300 , height=100   , width=200)

boton2 = tkinter.Button(ventana, text="Salir", command=salir)
boton2.place(x=0, y=300 , height=100   , width=200)


#mesagebox

#tkinter.messagebox.showinfo("aliciaaaaaaaaaaaaaaaaaa", "Hola mundo")


respuesta = tkinter.messagebox.askquestion("Pregunta", "¿Quieres salir de la aplicacion?")  
if respuesta == "yes": 
    ventana.destroy()
    
else:
    tkinter.Label(ventana, text="Gracias por quedarte").pack()  
    