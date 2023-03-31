from tkinter import *
from tkinter import ttk 
import tkinter as tk
from controladorDB import *

# Instancia: puente entre los 2 archivos
controlador = controladorDB()

# Metodo que usa mi objeto controlador para insertar
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#Funcion que usa el objeto controlador para buscar un usuario
def ejecutarSelectU():
    rsUsu = controlador.consultarUsuario(VarBus.get())
    #Iteramos el contenido de la consulta y lo guardamos en cadena
    for usu in rsUsu:
        cadena = str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])
        
    if(rsUsu):
        textBus.config(state = 'normal')
        textBus.delete(1.0, 'end')
        textBus.insert('end', cadena)
        textBus.config(state = 'disabled')
    else:
        messagebox.showerror("Error!","El usuario no existe")
    
ventana = Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

# Pestaña1: Formulario de registro
titulo = Label(pestana1,text="Registro Usuarios",fg="blue",font=("Modern",18)).pack()

varNom = tk.StringVar()
lblNom = Label(pestana1,text="Nombre: ").pack()
txtNom = Entry(pestana1,textvariable=varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1,text="Correo: ").pack()
txtCor = Entry(pestana1,textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1,text="Contraseña: ").pack()
txtCon = Entry(pestana1,textvariable=varCon).pack()

btnGuardar = Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()

# Pestaña2: Buscar usuario

titulo2 = Label(pestana2, text="Buscar Usuario", fg="green", font=("Modern",18)).pack()

VarBus = tk.StringVar()
lblid = Label(pestana2, text="Identificador de Usuario: ").pack()
txtid = Entry(pestana2, textvariable=VarBus).pack()
btnBus = Button(pestana2, text="Buscar", command=ejecutarSelectU).pack()

subBus = Label(pestana2, text="Registrado:", fg="blue", font=("Modern",15)).pack()
textBus = tk.Text(pestana2, height=5, width=52).pack()

# Pestaña3: Mostrar datos

titulo3 = Label(pestana3, text="Consultar Usuarios", fg="orange", font=("Modern",18)).pack()
btnconsulta = Button(pestana3, text="Mostrar datos").pack()


panel.add(pestana1,text="Formulario Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")



ventana.mainloop()
