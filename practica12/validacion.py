from ventana import *


def validacioncontraseña():
    correo = str(entry.get())
    contraseña = str(entry2.get())
    if correo == "ejemplo@gmail.com" and contraseña == "1234":
        messagebox.showinfo("Acceso permitido","¡Bienvenido!")
    else:
        messagebox.showerror("Error","¡El correo y la contraseña son incorrectos!")
