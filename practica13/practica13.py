from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from generador import *

axc = 


ventana=Tk()
ventana.title("Generador de passwords automatico")
ventana.geometry("600x300")

seccion1=Frame(ventana,bg="#dcdcfa").pack(expand=True,fill='both')

txt1 = ttk.Label(ventana, text="Longitud de la contraseña:", background="#dcdcfa").place(x="30",y="20")

var1 = tk.StringVar()
longitud = ttk.Entry(seccion1, textvariable=var1).place(x="220",y="20")

mayusculas = Checkbutton(ventana, text="Mayusculas", background="#dcdcfa").place(x="30",y="50")

caracteres = Checkbutton(ventana, text="Caracteres especiales", background="#dcdcfa").place(x="30",y="80")


boton = Button(seccion1,text="Generar contraseña", bg="white", command=validacion). place(x="220",y="120")


ventana.mainloop()