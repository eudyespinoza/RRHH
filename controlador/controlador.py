from modelo.model import agregar_empleado_db
from vista import *
from model import *

def guardar_usuario():
    nombre = nombre.get()
    segundo_nombre = segundo_nombre.get()
    apellido = apellido.get()
    apellido2 = apellido2.get()
    dni = dni.get()

    guardado, mensaje = agregar_empleado_db(dni, nombre, apellido, apellido2)

    if guardado:


    print(mensaje)
