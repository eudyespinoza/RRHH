from tkinter import *

master = Tk()
master.geometry("1024x250")
nombre = StringVar()
segundo_nombre = StringVar()
apellido = StringVar()
segundo_apellido = StringVar()
dni = StringVar()
cuit = StringVar()
fecha_nacimiento = StringVar()
fecha_ingreso = StringVar()
fecha_egreso = StringVar()
sexo = StringVar()
calle = StringVar()
altura = StringVar()
localidad = StringVar()
provincia = StringVar()
codigo_postal = StringVar()
telefono = StringVar()
tipo = StringVar()
cargo = StringVar()
salario = StringVar()
fecha = StringVar()
hora_de_entrada = StringVar()
hora_de_salida = StringVar()

def guardar_usuario():
    nombre = nombre.get()
    segundo_nombre = segundo_nombre.get()
    apellido = apellido.get()
    segundo_apellido = segundo_apellido.get()
    dni = dni.get()
    cuit = cuit.get()
    fecha_nacimiento = fecha_nacimiento.get()
    fecha_ingreso = fecha_ingreso.get()
    fecha_egreso = fecha_egreso.get()
    sexo = sexo.get()
    calle = calle.get()
    altura = altura.get()
    localidad = localidad.get()
    provincia = provincia.get()
    codigo_postal = codigo_postal.get()
    telefono = telefono.get()
    tipo = tipo.get()
    cargo = cargo.get()
    salario = salario.get()
    fecha = fecha.get()
    hora_de_entrada = hora_de_entrada.get()
    hora_de_salida = hora_de_salida.get()

nombre = Label(master, text="Nombre")
nombre.grid(row=0, column=0, sticky=W)
entry_nombre = Entry(master)
entry_nombre.grid(row=0, column=1)

segundo_nombre = Label(master, text="Segundo Nombre")
segundo_nombre.grid(row=1, column=0, sticky=W)
entry_segundo_nombre = Entry(master)
entry_segundo_nombre.grid(row=1, column=1)

apellido = Label(master, text="Apellido")
apellido.grid(row=2, column=0, sticky=W)
entry_apellido = Entry(master)
entry_apellido.grid(row=2, column=1)

segundo_apellido = Label(master, text="Segundo Apellido")
segundo_apellido.grid(row=3, column=0, sticky=W)
entry_segundo_apellido = Entry(master)
entry_segundo_apellido.grid(row=3, column=1)

def mostrar():
    print(dni.get())

dni = Label(master, text="Dni")
dni.grid(row=4, column=0, sticky=W)
dni = Entry(master, textvariable=dni)
dni.grid(row=4, column=1)
Boton_dni = Button(master, text="Mostrar DNI", command=mostrar)
Boton_dni.grid(row=10, column=8, sticky=E)

cuit = Label(master, text="Cuit")
cuit.grid(row=5, column=0, sticky=W)
cuit = Entry(master)
cuit.grid(row=5, column=1)

fecha_nacimiento = Label(master, text="Fecha de Nacimiento")
fecha_nacimiento.grid(row=6, column=0, sticky=W)
fecha_nacimiento = Entry(master)
fecha_nacimiento.grid(row=6, column=1)

fecha_ingreso = Label(master, text="Fecha de Ingreso")
fecha_ingreso.grid(row=7, column=0, sticky=W)
fecha_ingreso = Entry(master)
fecha_ingreso.grid(row=7, column=1)

fecha_egreso = Label(master, text="Fecha de Egreso")
fecha_egreso.grid(row=8, column=0, sticky=W)
fecha_egreso = Entry(master)
fecha_egreso.grid(row=8, column=1)

sexo = Label(master, text="Sexo")
sexo.grid(row=9, column=0, sticky=W)
sexo = Entry(master)
sexo.grid(row=9, column=1)

##2

calle = Label(master, text="Calle")
calle.grid(row=0, column=2, sticky=W)
entry_calle = Entry(master)
entry_calle.grid(row=0, column=3)

altura = Label(master, text="Altura")
altura.grid(row=1, column=2, sticky=W)
entry_altura = Entry(master)
entry_altura.grid(row=1, column=3)

localidad = Label(master, text="Localidad")
localidad.grid(row=2, column=2, sticky=W)
entry_localidad = Entry(master)
entry_localidad.grid(row=2, column=3)

provincia = Label(master, text="Provincia")
provincia.grid(row=3, column=2, sticky=W)
entry_provincia = Entry(master)
entry_provincia.grid(row=3, column=3)

codigo_postal = Label(master, text="Codigo Postal")
codigo_postal.grid(row=4, column=2, sticky=W)
entry_codigopostal = Entry(master)
entry_codigopostal.grid(row=4, column=3)

##3

telefono = Label(master, text="Telefono")
telefono.grid(row=0, column=4, sticky=W)
entry_telefono = Entry(master)
entry_telefono.grid(row=0, column=5)

tipo = Label(master, text="Tipo")
tipo.grid(row=1, column=4, sticky=W)
entry_tipo = Entry(master)
entry_tipo.grid(row=1, column=5)

##4

cargo = Label(master, text="Cargo")
cargo.grid(row=0, column=6, sticky=W)
entry_cargo = Entry(master)
entry_cargo.grid(row=0, column=7)

salario = Label(master, text="Salario")
salario.grid(row=1, column=6, sticky=W)
entry_salario = Entry(master)
entry_salario.grid(row=1, column=7)

##5

fecha = Label(master, text="Fecha")
fecha.grid(row=0, column=8, sticky=W)
entry_fecha = Entry(master)
entry_fecha.grid(row=0, column=9)

hora_de_entrada = Label(master, text="Hora de Entrada")
hora_de_entrada.grid(row=1, column=8, sticky=W)
entry_hora_de_entrada = Entry(master)
entry_hora_de_entrada.grid(row=1, column=9)

hora_de_salida = Label(master, text="Hora de Salida")
hora_de_salida.grid(row=2, column=8, sticky=W)
entry_hora_de_salida = Entry(master)
entry_hora_de_salida.grid(row=2, column=9)

master.mainloop()