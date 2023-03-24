from tkinter import messagebox
import sqlite3 
import bcrypt

class controladorDB:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C:/Users/benav/Documents/GitHub/POO182/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la base de datos")
            return conexion
            
        except sqlite3.OperationalError:
            print("No se pudo conectar a la base de datos")
    
    def guardarUsuario(self,nom,cor,con):
        
        #1. Llamando el metodo conexion
        conx = self.conexionBD()
        
        #2. Validar los vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Error!","Formulario incompleto")
            conx.close()
        else:
            #3. Realizar insert a la base de datos
            #4. Preparamos las variables necesarias
            cursor = conx.cursor()
            conH = self.encriptarContra(con)
            datos = (nom,cor,conH)
            sqlInsert = " insert into tbregistrados(nombre,correo,contra) values(?,?,?)"
            
            #5. Ejecutamos el insert
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario guardado")
    
    def encriptarContra(self,con):
        
        #1. Preparamos la contraseña y la sal para Hash
        conPlana = con
        conPlana = conPlana.encode() # Convertir contraseña a bytes
        sal = bcrypt.gensalt()
        
        #2. Encriptar la conrtaseña
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)
        
        #2. Regresamos la contraseña encriptada
        return conHa
    
        