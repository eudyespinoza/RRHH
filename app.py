"""
IMPORTAR LIBRERIAS
"""
from tkinter import *


"""
______
MODELO
______
"""
empleados = {}
next_id = 1

def agregar_empleado_db(dni, cuil, nombre, segundo_nombre, apellido, segundo_apellido, fecha_nacimiento, edad, sexo,
                        fecha_ingreso):
    global next_id
    if dni in empleados:
        print("El empleado ya existe")
        return False, "Ya existe un empleado con el DNI ingresado."
    if not all([cuil, nombre, apellido, edad, sexo]):
        print("Debe completar todos los datos")
        return False, "Debe completar todos los datos obligatorios."

    # Se crea el registro del empleado incluyendo el ID
    empleado = {
        "id": next_id,
        "dni": dni,
        "cuil": cuil,
        "nombre": nombre,
        "segundo_nombre": segundo_nombre or '',
        "apellido": apellido,
        "segundo_apellido": segundo_apellido or '',
        "fecha_nacimiento": fecha_nacimiento,
        "edad": edad,
        "sexo": sexo,
        "fecha_ingreso": fecha_ingreso,
        "telefonos": [],
        "direcciones": []
    }
    empleados[dni] = empleado
    next_id += 1
    print(listar_empleados_db())
    return True, "Empleado agregado con éxito."

def agregar_telefono_db(dni, telefono):
    if dni not in empleados:
        return False, "Empleado no encontrado."
    empleados[dni]["telefonos"].append(telefono)
    return True, "Teléfono agregado correctamente."

def agregar_direccion_db(dni, direccion):
    if dni not in empleados:
        return False, "Empleado no encontrado."
    empleados[dni]["direcciones"].append(direccion)
    return True, "Dirección agregada correctamente."

def obtener_empleado_db(dni):
    return empleados.get(dni, None)

def listar_empleados_db():
    return list(empleados.items())

"""
___________
CONTROLADOR
___________
"""

def guardar_usuario():
    data_nombre = nombre.get()
    data_segundo_nombre = segundo_nombre.get()
    data_apellido = apellido.get()
    data_segundo_apellido = segundo_apellido.get()
    data_dni = dni.get()
    data_cuit = cuit.get()
    data_fecha_nacimiento = fecha_nacimiento.get()
    data_edad = edad.get()
    data_fecha_ingreso = fecha_ingreso.get()
    data_fecha_egreso = fecha_egreso.get()
    data_sexo = sexo.get()
    data_calle = calle.get()
    data_altura = altura.get()
    data_localidad = localidad.get()
    data_provincia = provincia.get()
    data_codigo_postal = codigo_postal.get()
    data_telefono = telefono.get()
    data_tipo = tipo.get()
    data_cargo = cargo.get()
    data_salario = salario.get()
    data_fecha = fecha.get()
    data_hora_de_entrada = hora_de_entrada.get()
    data_hora_de_salida = hora_de_salida.get()
    print(data_dni, data_cuit, data_nombre, data_segundo_nombre, data_apellido, data_segundo_apellido, data_fecha_nacimiento, data_edad, data_sexo,
                        data_fecha_ingreso)
    agregado = agregar_empleado_db(data_dni, data_cuit, data_nombre, data_segundo_nombre, data_apellido, data_segundo_apellido, data_fecha_nacimiento, data_edad, data_sexo,
                        data_fecha_ingreso)
    datos = [data_nombre, data_segundo_nombre, data_apellido, data_segundo_apellido, data_dni, data_cuit, data_fecha_nacimiento, data_fecha_ingreso,
                    data_fecha_egreso, data_sexo, data_calle, data_altura, data_localidad, data_provincia, data_codigo_postal, data_telefono, data_tipo, data_cargo,
                    data_salario, data_fecha, data_hora_de_entrada, data_hora_de_salida]

    if not agregado:
        return False
    return agregado

"""
_____
VISTA
_____
"""

master = Tk()
master.geometry("1024x250")
nombre = StringVar()
segundo_nombre = StringVar()
apellido = StringVar()
segundo_apellido = StringVar()
dni = StringVar()
cuit = StringVar()
fecha_nacimiento = StringVar()
edad = StringVar()
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

label_nombre = Label(master, text="Nombre")
label_nombre.grid(row=0, column=0, sticky=W)
entry_nombre = Entry(master, textvariable=nombre)
entry_nombre.grid(row=0, column=1)

label_segundo_nombre = Label(master, text="Segundo Nombre")
label_segundo_nombre.grid(row=1, column=0, sticky=W)
entry_segundo_nombre = Entry(master, textvariable=segundo_nombre)
entry_segundo_nombre.grid(row=1, column=1)

label_apellido = Label(master, text="Apellido")
label_apellido.grid(row=2, column=0, sticky=W)
entry_apellido = Entry(master, textvariable=apellido)
entry_apellido.grid(row=2, column=1)

label_segundo_apellido = Label(master, text="Segundo Apellido")
label_segundo_apellido.grid(row=3, column=0, sticky=W)
entry_segundo_apellido = Entry(master, textvariable=segundo_apellido)
entry_segundo_apellido.grid(row=3, column=1)

def mostrar():
    print(dni.get())

label_dni = Label(master, text="Dni")
label_dni.grid(row=4, column=0, sticky=W)
dni = Entry(master, textvariable=dni)
dni.grid(row=4, column=1)
Boton_dni = Button(master, text="GUARDAR", command=guardar_usuario)
Boton_dni.grid(row=10, column=8, sticky=E)

label_cuit = Label(master, text="Cuit")
label_cuit.grid(row=5, column=0, sticky=W)
cuit = Entry(master)
cuit.grid(row=5, column=1)

label_fecha_nacimiento = Label(master, text="Fecha de Nacimiento")
label_fecha_nacimiento.grid(row=6, column=0, sticky=W)
fecha_nacimiento = Entry(master, textvariable=fecha_nacimiento)
fecha_nacimiento.grid(row=6, column=1)

label_edad = Label(master, text="Edad")
label_edad.grid(row=7, column=0, sticky=W)
edad = Entry(master, textvariable=edad)
edad.grid(row=7, column=1)

label_fecha_ingreso = Label(master, text="Fecha de Ingreso")
label_fecha_ingreso.grid(row=8, column=0, sticky=W)
fecha_ingreso = Entry(master, textvariable=fecha_ingreso)
fecha_ingreso.grid(row=8, column=1)

label_fecha_egreso = Label(master, text="Fecha de Egreso")
label_fecha_egreso.grid(row=9, column=0, sticky=W)
fecha_egreso = Entry(master, textvariable=fecha_egreso)
fecha_egreso.grid(row=9, column=1)

label_sexo = Label(master, text="Sexo")
label_sexo.grid(row=10, column=0, sticky=W)
sexo = Entry(master, textvariable=sexo)
sexo.grid(row=10, column=1)

##2

label_calle = Label(master, text="Calle")
label_calle.grid(row=0, column=2, sticky=W)
entry_calle = Entry(master, textvariable=calle)
entry_calle.grid(row=0, column=3)

label_altura = Label(master, text="Altura")
label_altura.grid(row=1, column=2, sticky=W)
entry_altura = Entry(master,textvariable=altura)
entry_altura.grid(row=1, column=3)

label_localidad = Label(master, text="Localidad")
label_localidad.grid(row=2, column=2, sticky=W)
entry_localidad = Entry(master, textvariable=localidad)
entry_localidad.grid(row=2, column=3)

label_provincia = Label(master, text="Provincia")
label_provincia.grid(row=3, column=2, sticky=W)
entry_provincia = Entry(master, textvariable=provincia)
entry_provincia.grid(row=3, column=3)

label_codigo_postal = Label(master, text="Codigo Postal")
label_codigo_postal.grid(row=4, column=2, sticky=W)
entry_codigopostal = Entry(master, textvariable=codigo_postal)
entry_codigopostal.grid(row=4, column=3)

##3

label_telefono = Label(master, text="Telefono")
label_telefono.grid(row=0, column=4, sticky=W)
entry_telefono = Entry(master, textvariable=telefono)
entry_telefono.grid(row=0, column=5)

label_tipo = Label(master, text="Tipo")
label_tipo.grid(row=1, column=4, sticky=W)
entry_tipo = Entry(master, textvariable=tipo)
entry_tipo.grid(row=1, column=5)

##4

label_cargo = Label(master, text="Cargo")
label_cargo.grid(row=0, column=6, sticky=W)
entry_cargo = Entry(master, textvariable=cargo)
entry_cargo.grid(row=0, column=7)

label_salario = Label(master, text="Salario")
label_salario.grid(row=1, column=6, sticky=W)
entry_salario = Entry(master, textvariable=salario)
entry_salario.grid(row=1, column=7)

##5

label_fecha = Label(master, text="Fecha")
label_fecha.grid(row=0, column=8, sticky=W)
entry_fecha = Entry(master, textvariable=fecha)
entry_fecha.grid(row=0, column=9)

label_hora_de_entrada = Label(master, text="Hora de Entrada")
label_hora_de_entrada.grid(row=1, column=8, sticky=W)
entry_hora_de_entrada = Entry(master, textvariable=hora_de_entrada)
entry_hora_de_entrada.grid(row=1, column=9)

label_hora_de_salida = Label(master, text="Hora de Salida")
label_hora_de_salida.grid(row=2, column=8, sticky=W)
entry_hora_de_salida = Entry(master, textvariable=hora_de_salida)
entry_hora_de_salida.grid(row=2, column=9)

master.mainloop()
