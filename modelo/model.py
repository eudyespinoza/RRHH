empleados = {}
next_id = 1

def agregar_empleado_db(dni, cuil, nombre, segundo_nombre, apellido, segundo_apellido, fecha_nacimiento, edad, sexo,
                        fecha_ingreso):
    global next_id
    if dni in empleados:
        return False, "Ya existe un empleado con el DNI ingresado."
    if not all([cuil, nombre, apellido, edad, sexo]):
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


empleado_guardado, mensaje_empleado = agregar_empleado_db("98981592", "20-98981592-6", "Eudy", "David",
                                                          "Espinoza", "Leal", "28-10-1983", "41",
                                                          "M", "01-01-2020")

telefono_guardado, mensaje_telefono = agregar_telefono_db("95981592", "3435229159")
direccion_guardada, mensaje_direccion = agregar_direccion_db("95981592", "Alvarado 2381")

print(empleado_guardado)
print(telefono_guardado)
print(direccion_guardada)
print(mensaje_empleado)
print(obtener_empleado_db("95981592"))
print(listar_empleados_db())
