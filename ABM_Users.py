import tkinter as tk

window = tk.Tk()
window.title("SISTEMA DE REGISTRO DE USUARIOS")
window.geometry("380x300")

bienvenida=tk.Label(text="Sistema de registro de usuarios", font="nonito")
bienvenida.place(x=80, y= 20)

"""
def limpiar():
    usuario=user.get()

    user.delete(first=0,last=)
 
"""



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

buttonGuardar = tk.Button(text="Guardar").place(x=130, y=200)
buttonNuevo = tk.Button(text="Nuevo", command=limpiar).place(x=210, y=200)

magia=tk.Label(text="", fg="red")
magia.place(x=140, y = 150)


   


tk.mainloop()