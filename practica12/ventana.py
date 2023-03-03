from tkinter import *
from tkinter import messagebox, ttk


ventana=Tk()
ventana.title("Login")
ventana.geometry("600x300")

seccion1=Frame(ventana,bg="#dcdcfa")
seccion1.pack(expand=True,fill='both')

textbox2 = ttk.Label(ventana, text="Correo Electronico:", background="#dcdcfa")
textbox2.place(x="100",y="160")

textbox = ttk.Label(ventana, text="Contraseña:", background="#dcdcfa")
textbox.place(x="150",y="200")

entry = ttk.Entry(seccion1)
entry.place(x="240",y="160")

entry2 = ttk.Entry(seccion1)
entry2.config (show="*")
entry2.place(x="240",y="200")

botonLogin = Button(seccion1,text="login",fg="black",width="15",command=validacioncontraseña)
botonLogin.place(x="250",y="250")
botonLogin.pack()

    
    
ventana.mainloop()