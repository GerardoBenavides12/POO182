from tkinter import *
from tkinter import messagebox, ttk

#Ventana
ventana=Tk()
ventana.title("Login")
ventana.geometry("600x300")

#Frame
seccion1=Frame(ventana,bg="#dcdcfa")
seccion1.pack(expand=True,fill='both')

#Texto
textbox2 = ttk.Label(ventana, text="Correo Electronico:", background="#dcdcfa")
textbox2.place(x="150",y="160")

textbox = ttk.Label(ventana, text="Contraseña:", background="#dcdcfa")
textbox.place(x="100",y="200")

#Input
entry = ttk.Entry()
entry.place(x="240",y="200")

entry2 = ttk.Entry()
entry2.place(x="240",y="160")

#Boton
botonLogin=Button(seccion1,text="login",fg="black",width="15")
botonLogin.place(x="250",y="250")

def revisarUsuario():
    print(textbox.cget)



ventana.mainloop()