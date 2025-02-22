from tkinter import *
from controlador import *

master =Tk()





nombre = Label(master, text="Nombre")
nombre.grid(row=0, column=0, sticky= W)

segundo_nombre = Label(master, text="Segundo Nombre")
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

fecha_ingreso = Label(master, text="Fecha de Ingreso")
fecha_ingreso.grid(row=7, column=0, sticky= W)

fecha_egreso = Label(master, text="Fecha de Egreso")
fecha_egreso.grid(row=8, column=0, sticky= W)

sexo = Label(master, text="Sexo")
sexo.grid(row=9, column=0, sticky= W)

##2

calle = Label(master, text="Calle")
calle.grid(row=0, column=2, sticky= W)

altura = Label(master, text="Altura")
altura.grid(row=1, column=2, sticky= W)

localidad = Label(master, text="Localidad")
localidad.grid(row=2, column=2, sticky= W)

provincia = Label(master, text="Provincia")
provincia.grid(row=3, column=2, sticky= W)

codigo_postal = Label(master, text="Codigo Postal")
codigo_postal.grid(row=4, column=2, sticky= W)

##3

telefono = Label(master, text="Telefono")
telefono.grid(row=0, column=4, sticky= W)

tipo = Label(master, text="Tipo")
tipo.grid(row=1, column=4, sticky= W)

##4

cargo = Label(master, text="Cargo")
cargo.grid(row=0, column=6, sticky= W)

salario = Label(master, text="Salario")
salario.grid(row=1, column=6, sticky= W)

##5

fecha = Label(master, text="Fecha")
fecha.grid(row=0, column=8, sticky= W)

hora_de_entrada = Label(master, text="Hora de Entrada")
hora_de_entrada.grid(row=1, column=8, sticky= W)

hora_de_salida = Label(master, text="Hora de Salida")
hora_de_salida.grid(row=2, column=8, sticky= W)









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

##2

entry_calle = Entry(master)
entry_calle.grid(row=0, column=3)

entry_altura = Entry(master)
entry_altura.grid(row=1, column=3)

entry_localidad = Entry(master)
entry_localidad.grid(row=2, column=3)

entry_provincia = Entry(master)
entry_provincia.grid(row=3, column=3)

entry_codigopostal = Entry(master)
entry_codigopostal.grid(row=4, column=3)

##3

entry_telefono = Entry(master)
entry_telefono.grid(row=0, column=5)

entry_tipo = Entry(master)
entry_tipo.grid(row=1, column=5)

##4

entry_cargo = Entry(master)
entry_cargo.grid(row=0, column=7)

entry_salario = Entry(master)
entry_salario.grid(row=1, column=7)

##5

entry_fecha = Entry(master)
entry_fecha.grid(row=0, column=9)

entry_hora_de_entrada = Entry(master)
entry_hora_de_entrada.grid(row=1, column=9)

entry_hora_de_salida = Entry(master)
entry_hora_de_salida.grid(row=2, column=9)



























master.mainloop()



