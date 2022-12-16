import tkinter as tk
import baseDatos
import utils
from tkinter import messagebox
import base64
#from funcionesComprobacio import comprobarContrasenha

window = tk.Tk()
window.title("REGISTRO DE USUARIOS")
window.geometry("380x300")

bienvenida=tk.Label(text="Sistema de registro de usuarios", font="nonito")
bienvenida.place(x=80, y= 15)


userL=tk.Label(text="Ingrese su e-mail:")
userL.place(x=10, y=60)
user = tk.Entry()
user.place(x=200, y=60)

nombreL=tk.Label(text="Ingrese su nombre:")
nombreL.place(x=10, y=85)
nombre = tk.Entry()
nombre.place(x=200, y=85)

apellidoL=tk.Label(text="Ingrese su apellido:")
apellidoL.place(x=10, y=110)
apellido = tk.Entry()
apellido.place(x=200, y=110)

dniL=tk.Label(text="Ingrese su DNI:")
dniL.place(x=10, y=135)
dni = tk.Entry()
dni.place(x=200, y=135)

nacL=tk.Label(text="Ingrese su fecha de nacimiento:")
nacL.place(x=10, y=160)
nac = tk.Entry()
nac.place(x=200, y=160)

nombreUsuarioL=tk.Label(text="Ingrese su nombre de usuario:")
nombreUsuarioL.place(x=10, y=185)
nombreUsuario = tk.Entry()
nombreUsuario.place(x=200, y=185)

contrasenhaL=tk.Label(text="Ingrese su contraseña:")
contrasenhaL.place(x=10, y=210)
contrasenha = tk.Entry(show="*")
contrasenha.place(x=200, y=210)

contrasenhaRL=tk.Label(text="Repita su contraseña:")
contrasenhaRL.place(x=10, y=235)
contrasenhaR = tk.Entry(show="*")
contrasenhaR.place(x=200, y=235)

contraIncorrect=tk.Label(text="",fg="red")
contraIncorrect.place(x=190, y=250)

def guardar():

    while contrasenha.get()==contrasenhaR.get():
        
    #comprobarContrasenha(contrasenhaAprove)
        nombreBDD=nombre.get()
        apellidoBDD=apellido.get()
        dniBDD=dni.get()    
        username=nombreUsuario.get()
        email=user.get()
        nacimiento=nac.get()
        password=contrasenha.get()
        password=password.encode('ascii')
        password=base64.b64encode(password)

        if utils.nameValidator(username):
            if utils.dateValidator(nacimiento):
                if utils.emailValidator(email):
                    try:
                        baseDatos.saveData(username,email,nombreBDD,apellidoBDD,dniBDD,nacimiento,password)
                        messagebox.showinfo("Mensaje","El usuario se ha registrado correctamente")
                        limpiarForm()
                    except:
                        messagebox.showinfo("Mensaje","El usuario no pudo ser registrado")
                        limpiarForm()
                else:
                    messagebox.showinfo("Mensaje", "Correo eléctronico con formato incorrecto")
                    break
            else:
                messagebox.showinfo("Mensaje", "Fecha con formato incorrecto")
                break
        
        else:
            messagebox.showinfo("Mensaje","Nombre de usuario con Formato Incorrecto")
            break
        
        #limpiarForm()
    else:
        messagebox.showinfo("Mensaje","Las contraseñas no coinciden")
    
def limpiarForm():
    nombreUsuario.delete(0,tk.END)
    user.delete(0,tk.END)
    nac.delete(0,tk.END)
    contrasenha.delete(0,tk.END)
    nombre.delete(0,tk.END)
    apellido.delete(0,tk.END)
    dni.delete(0,tk.END)
    contrasenhaR.delete(0,tk.END)
    contraIncorrect["text"]=""
    
buttonGuardar = tk.Button(text="Guardar",width=6,height=1,bg="green2", fg="white",command=guardar).place(x=130, y=270)
buttonNuevo = tk.Button(text="Nuevo",bg="red",fg="white",command=limpiarForm).place(x=210, y=270)

tk.mainloop()