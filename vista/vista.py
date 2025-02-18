from tkinter import *

master =Tk()

nombre = Label(master, text="Nombre")
nombre.grid(row=0, column=0, sticky= W)

segundo_nombre = Label(master, text="Segundo nombre")
segundo_nombre.grid(row=1, column=0, sticky= W)

apellido = Label(master, text="Apellido")
apellido.grid(row=2, column=0, sticky= W)

segundo_apellido = Label(master, text="Segundo Apellido")
segundo_apellido.grid(row=3, column=0, sticky= W)

dni = Label(master, text="Dni")
dni.grid(row=4, column=0, sticky= W)

cuit = Label(master, text="Cuit")
cuit.grid(row=5, column=0, sticky= W)

fecha_nacimiento = Label(master, text="Fecha de Nacimiento")
fecha_nacimiento.grid(row=6, column=0, sticky= W)

fecha_ingreso = Label(master, text="Fecha de ingreso")
fecha_ingreso.grid(row=7, column=0, sticky= W)

fecha_egreso = Label(master, text="Fecha de egreso")
fecha_egreso.grid(row=8, column=0, sticky= W)

sexo = Label(master, text="Sexo")
sexo.grid(row=9, column=0, sticky= W)

fecha_creacion = Label(master, text="Fecha de Creacion")
fecha_creacion.grid(row=10, column=0, sticky= W)

fecha_modificacion = Label(master, text="Fecha modificacion")
fecha_modificacion.grid(row=11, column=0, sticky= W)




entry_nombre = Entry(master)
entry_nombre.grid(row=0, column=1)

entry_segundo_nombre = Entry(master)
entry_segundo_nombre.grid(row=1, column=1)

entry_apellido = Entry(master)
entry_apellido.grid(row=2, column=1)

entry_segundo_apellido = Entry(master)
entry_segundo_apellido.grid(row=3, column=1)

dni = Entry(master)
dni.grid(row=4, column=1)

cuit = Entry(master)
cuit.grid(row=5, column=1)

fecha_nacimiento = Entry(master)
fecha_nacimiento.grid(row=6, column=1)

fecha_ingreso = Entry(master)
fecha_ingreso.grid(row=7, column=1)

fecha_egreso = Entry(master)
fecha_egreso.grid(row=8, column=1)

sexo = Entry(master)
sexo.grid(row=9, column=1)

fecha_creacion = Entry(master)
fecha_creacion.grid(row=10, column=1)

fecha_modificacion = Entry(master)
fecha_modificacion.grid(row=11, column=1)









"""def funcion():
   print("Hola")


boton_g = Button(master, text="Guardar", command=funcion)
boton_g.grid(row=2, column=1)
"""
master.mainloop()



