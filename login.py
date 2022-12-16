import tkinter as tk
import baseDatos
from tkinter import messagebox

window = tk.Tk()
window.title("Ingresar")
window.geometry("380x300")

bienvenida=tk.Label(text="Ingreso al sistema", font="nonito")
bienvenida.place(x=120, y= 15)

nombreUsuarioLoginL=tk.Label(text="Ingrese su nombre de usuario:")
nombreUsuarioLoginL.place(x=10, y=100)
nombreUsuarioLogin = tk.Entry()
nombreUsuarioLogin.place(x=200, y=100)

contrasenhaLoginL=tk.Label(text="Ingrese su contraseña:")
contrasenhaLoginL.place(x=10, y=130)
contrasenhaLogin = tk.Entry(show="*")
contrasenhaLogin.place(x=200, y=130)

def login():
    username=nombreUsuarioLogin.get()
    password=contrasenhaLogin.get()
    if baseDatos.loginUser(username,password):
        messagebox.showinfo("Login","Ingreso correcto.")
    else:
        messagebox.showerror("Error","Ususario o contraseña incorrectos.")
        limpiarFormulario()

def limpiarFormulario():
    nombreUsuarioLogin.delete(0,tk.END)
    contrasenhaLogin.delete(0,tk.END)
   

buttonLogin = tk.Button(text="Ingresar",width=6,height=1,bg="green2", fg="white", command=login).place(x=130, y=200)
buttonRegistrar = tk.Button(text="Registrarse",bg="red",fg="white", command=limpiarFormulario).place(x=210, y=200)



tk.mainloop()