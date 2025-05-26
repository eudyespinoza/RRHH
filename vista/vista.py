import flet as ft
from controlador.controlador import Controlador

def main(page: ft.Page):
    """Función principal que inicia la aplicación Flet para el ABM de empleados.

    Args:
        page (ft.Page): Página principal de la aplicación Flet.
    """
    controlador = Controlador()
    page.title = "ABM de Empleados"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 20
    page.spacing = 10

    # Tabla para mostrar empleados
    tabla_empleados = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("DNI")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("Acciones"))
        ],
        rows=[]
    )

    # Mensaje de retroalimentación
    mensaje = ft.Text("")

    # Contenedor para el formulario (inicialmente vacío)
    formulario_container = ft.Column([])

    # Contenedor para los detalles (inicialmente vacío)
    detalles_container = ft.Column([])

    # Listas para manejar múltiples entradas
    direcciones = []
    telefonos = []
    cargos = []
    jornadas = []

    # Campos del formulario (se definirán cuando se muestre el formulario)
    nombre = None
    segundo_nombre = None
    apellido = None
    segundo_apellido = None
    dni = None
    cuit = None
    fecha_nacimiento = None
    fecha_ingreso = None
    fecha_egreso = None
    sexo = None
    calle = None
    altura = None
    localidad = None
    provincia = None
    codigo_postal = None
    telefono = None
    tipo = None
    cargo = None
    salario = None
    fecha_inicio = None
    fecha_fin = None
    fecha = None
    hora_de_entrada = None
    hora_de_salida = None
    direcciones_container = None
    telefonos_container = None
    cargos_container = None
    jornadas_container = None

    def limpiar_formulario():
        """Limpia todos los campos del formulario y las listas."""
        if nombre is not None:
            nombre.value = ""
            segundo_nombre.value = ""
            apellido.value = ""
            segundo_apellido.value = ""
            dni.value = ""
            cuit.value = ""
            fecha_nacimiento.value = ""
            fecha_ingreso.value = ""
            fecha_egreso.value = ""
            sexo.value = ""
            calle.value = ""
            altura.value = ""
            localidad.value = ""
            provincia.value = ""
            codigo_postal.value = ""
            telefono.value = ""
            tipo.value = ""
            cargo.value = ""
            salario.value = ""
            fecha_inicio.value = ""
            fecha_fin.value = ""
            fecha.value = ""
            hora_de_entrada.value = ""
            hora_de_salida.value = ""
            direcciones.clear()
            telefonos.clear()
            cargos.clear()
            jornadas.clear()
            direcciones_container.controls.clear()
            telefonos_container.controls.clear()
            cargos_container.controls.clear()
            jornadas_container.controls.clear()
        mensaje.value = ""
        page.update()

    def mostrar_formulario(modo="agregar", empleado=None):
        """Muestra el formulario para agregar o editar un empleado.

        Args:
            modo (str): 'agregar' para nuevo empleado, 'editar' para modificar.
            empleado (dict, optional): Datos del empleado a editar.
        """
        nonlocal nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit, fecha_nacimiento, fecha_ingreso, fecha_egreso, sexo
        nonlocal calle, altura, localidad, provincia, codigo_postal, telefono, tipo, cargo, salario, fecha_inicio, fecha_fin
        nonlocal fecha, hora_de_entrada, hora_de_salida, direcciones_container, telefonos_container, cargos_container, jornadas_container

        # Limpiar contenedores
        formulario_container.controls.clear()
        detalles_container.controls.clear()

        # Inicializar campos del formulario
        nombre = ft.TextField(label="Nombre", width=200, value=empleado["nombre"] if empleado else "")
        segundo_nombre = ft.TextField(label="Segundo Nombre", width=200, value=empleado["segundo_nombre"] if empleado else "")
        apellido = ft.TextField(label="Apellido", width=200, value=empleado["apellido"] if empleado else "")
        segundo_apellido = ft.TextField(label="Segundo Apellido", width=200, value=empleado["segundo_apellido"] if empleado else "")
        dni = ft.TextField(label="DNI", width=200, value=empleado["dni"] if empleado else "", read_only=modo == "editar")
        cuit = ft.TextField(label="CUIT", width=200, value=empleado["cuit"] if empleado else "")
        fecha_nacimiento = ft.TextField(label="Fecha de Nacimiento", width=200, value=empleado["fecha_nacimiento"] if empleado else "")
        fecha_ingreso = ft.TextField(label="Fecha de Ingreso", width=200, value=empleado["fecha_ingreso"] if empleado else "")
        fecha_egreso = ft.TextField(label="Fecha de Egreso", width=200, value=empleado["fecha_egreso"] if empleado else "")
        sexo = ft.TextField(label="Sexo", width=200, value=empleado["sexo"] if empleado else "")

        # Campos para agregar dirección
        calle = ft.TextField(label="Calle", width=200)
        altura = ft.TextField(label="Altura", width=200)
        localidad = ft.TextField(label="Localidad", width=200)
        provincia = ft.TextField(label="Provincia", width=200)
        codigo_postal = ft.TextField(label="Código Postal", width=200)
        direcciones_container = ft.Column([])

        def agregar_direccion_input(e):
            """Agrega una dirección a la lista temporal y la muestra en la interfaz."""
            direccion = {
                "calle": calle.value,
                "altura": altura.value,
                "localidad": localidad.value,
                "provincia": provincia.value,
                "codigo_postal": codigo_postal.value
            }
            direcciones.append(direccion)
            direcciones_container.controls.append(
                ft.Text(f"Dirección: {calle.value} {altura.value}, {localidad.value}")
            )
            calle.value = altura.value = localidad.value = provincia.value = codigo_postal.value = ""
            page.update()

        # Campos para agregar teléfono
        telefono = ft.TextField(label="Teléfono", width=200)
        tipo = ft.TextField(label="Tipo", width=200)
        telefonos_container = ft.Column([])

        def agregar_telefono_input(e):
            """Agrega un teléfono a la lista temporal y lo muestra en la interfaz."""
            tel = {
                "telefono": telefono.value,
                "tipo": tipo.value
            }
            telefonos.append(tel)
            telefonos_container.controls.append(
                ft.Text(f"Teléfono: {telefono.value} ({tipo.value})")
            )
            telefono.value = tipo.value = ""
            page.update()

        # Campos para agregar cargo
        cargo = ft.TextField(label="Cargo", width=200)
        salario = ft.TextField(label="Salario", width=200)
        fecha_inicio = ft.TextField(label="Fecha Inicio", width=200)
        fecha_fin = ft.TextField(label="Fecha Fin", width=200)
        cargos_container = ft.Column([])

        def agregar_cargo_input(e):
            """Agrega un cargo a la lista temporal y lo muestra en la interfaz."""
            carg = {
                "cargo": cargo.value,
                "salario": salario.value,
                "fecha_inicio": fecha_inicio.value,
                "fecha_fin": fecha_fin.value
            }
            cargos.append(carg)
            cargos_container.controls.append(
                ft.Text(f"Cargo: {cargo.value}, Salario: {salario.value}")
            )
            cargo.value = salario.value = fecha_inicio.value = fecha_fin.value = ""
            page.update()

        # Campos para agregar jornada laboral
        fecha = ft.TextField(label="Fecha", width=200)
        hora_de_entrada = ft.TextField(label="Hora de Entrada", width=200)
        hora_de_salida = ft.TextField(label="Hora de Salida", width=200)
        jornadas_container = ft.Column([])

        def agregar_jornada_input(e):
            """Agrega una jornada laboral a la lista temporal y la muestra en la interfaz."""
            jornada = {
                "fecha": fecha.value,
                "hora_de_entrada": hora_de_entrada.value,
                "hora_de_salida": hora_de_salida.value
            }
            jornadas.append(jornada)
            jornadas_container.controls.append(
                ft.Text(f"Jornada: {fecha.value}, {hora_de_entrada.value} - {hora_de_salida.value}")
            )
            fecha.value = hora_de_entrada.value = hora_de_salida.value = ""
            page.update()

        # Cargar datos existentes si es modo editar
        if modo == "editar" and empleado:
            for d in empleado["direcciones"]:
                direcciones.append(d)
                direcciones_container.controls.append(
                    ft.Row([
                        ft.Text(f"Dirección: {d['calle']} {d['altura']}, {d['localidad']}"),
                        ft.ElevatedButton("Modificar",
                            on_click=lambda e, d_id=d['id']: modificar_direccion_form(d_id)),
                        ft.ElevatedButton("Eliminar",
                            on_click=lambda e, d_id=d['id']: eliminar_direccion(d_id))
                    ])
                )
            for t in empleado["telefonos"]:
                telefonos.append(t)
                telefonos_container.controls.append(
                    ft.Row([
                        ft.Text(f"Teléfono: {t['telefono']} ({t['tipo']})"),
                        ft.ElevatedButton("Modificar",
                            on_click=lambda e, t_id=t['id']: modificar_telefono_form(t_id)),
                        ft.ElevatedButton("Eliminar",
                            on_click=lambda e, t_id=t['id']: eliminar_telefono(t_id))
                    ])
                )
            for c in empleado["cargos"]:
                cargos.append(c)
                cargos_container.controls.append(
                    ft.Row([
                        ft.Text(f"Cargo: {c['cargo']}, Salario: {c['salario']}"),
                        ft.ElevatedButton("Modificar",
                            on_click=lambda e, c_id=c['id']: modificar_cargo_form(c_id)),
                        ft.ElevatedButton("Eliminar",
                            on_click=lambda e, c_id=c['id']: eliminar_cargo(c_id))
                    ])
                )
            for j in empleado["jornadas"]:
                jornadas.append(j)
                jornadas_container.controls.append(
                    ft.Row([
                        ft.Text(f"Jornada: {j['fecha']}, {j['hora_de_entrada']} - {j['hora_de_salida']}"),
                        ft.ElevatedButton("Modificar",
                            on_click=lambda e, j_id=j['id']: modificar_jornada_form(j_id)),
                        ft.ElevatedButton("Eliminar",
                            on_click=lambda e, j_id=j['id']: eliminar_jornada(j_id))
                    ])
                )

        # Botones del formulario
        if modo == "agregar":
            btn_guardar = ft.ElevatedButton("Guardar", on_click=lambda e: guardar_usuario())
        else:
            btn_guardar = ft.ElevatedButton("Guardar Cambios", on_click=lambda e: modificar_usuario())

        btn_cancelar = ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_formulario())

        # Organizar los campos en columnas
        columna1 = ft.Column([
            nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit,
            fecha_nacimiento, fecha_ingreso, fecha_egreso, sexo
        ])
        columna2 = ft.Column([
            calle, altura, localidad, provincia, codigo_postal,
            ft.ElevatedButton("Agregar Dirección", on_click=agregar_direccion_input),
            direcciones_container
        ])
        columna3 = ft.Column([
            telefono, tipo,
            ft.ElevatedButton("Agregar Teléfono", on_click=agregar_telefono_input),
            telefonos_container
        ])
        columna4 = ft.Column([
            cargo, salario, fecha_inicio, fecha_fin,
            ft.ElevatedButton("Agregar Cargo", on_click=agregar_cargo_input),
            cargos_container
        ])
        columna5 = ft.Column([
            fecha, hora_de_entrada, hora_de_salida,
            ft.ElevatedButton("Agregar Jornada", on_click=agregar_jornada_input),
            jornadas_container
        ])

        # Mostrar el formulario
        formulario_container.controls = [
            ft.Text("Agregar Nuevo Empleado" if modo == "agregar" else "Editar Empleado", size=20),
            ft.Row([
                columna1, columna2, columna3, columna4, columna5,
                ft.Column([btn_guardar, btn_cancelar], spacing=10)
            ], spacing=20)
        ]
        page.update()

    def cerrar_formulario():
        """Cierra el formulario y limpia los datos."""
        formulario_container.controls.clear()
        detalles_container.controls.clear()
        limpiar_formulario()
        page.update()

    def guardar_usuario():
        """Guarda un nuevo empleado en la base de datos."""
        datos = {
            "dni": dni.value,
            "cuit": cuit.value,
            "nombre": nombre.value,
            "segundo_nombre": segundo_nombre.value,
            "apellido": apellido.value,
            "segundo_apellido": segundo_apellido.value,
            "fecha_nacimiento": fecha_nacimiento.value,
            "edad": "0",
            "sexo": sexo.value,
            "fecha_ingreso": fecha_ingreso.value,
            "fecha_egreso": fecha_egreso.value,
            "direcciones": direcciones,
            "telefonos": telefonos,
            "cargos": cargos,
            "jornadas": jornadas
        }
        exito, msg = controlador.agregar_empleado(datos)
        mensaje.value = msg
        if exito:
            actualizar_tabla()
            cerrar_formulario()
        page.update()

    def modificar_usuario():
        """Modifica los datos de un empleado existente."""
        datos = {
            "dni": dni.value,
            "cuit": cuit.value,
            "nombre": nombre.value,
            "segundo_nombre": segundo_nombre.value,
            "apellido": apellido.value,
            "segundo_apellido": segundo_apellido.value,
            "fecha_nacimiento": fecha_nacimiento.value,
            "edad": "0",
            "sexo": sexo.value,
            "fecha_ingreso": fecha_ingreso.value,
            "fecha_egreso": fecha_egreso.value
        }
        exito, msg = controlador.modificar_empleado(dni.value, datos)
        mensaje.value = msg
        if exito:
            actualizar_tabla()
            cerrar_formulario()
        page.update()

    def ver_detalles(empleado):
        """Muestra los detalles de un empleado en modo solo lectura.

        Args:
            empleado (dict): Diccionario con los datos del empleado.
        """
        formulario_container.controls.clear()
        detalles_container.controls.clear()

        detalles = [
            ft.Text(f"DNI: {empleado['dni']}", size=16),
            ft.Text(f"Nombre: {empleado['nombre']} {empleado['segundo_nombre']}", size=16),
            ft.Text(f"Apellido: {empleado['apellido']} {empleado['segundo_apellido']}", size=16),
            ft.Text(f"CUIT: {empleado['cuit']}", size=16),
            ft.Text(f"Fecha de Nacimiento: {empleado['fecha_nacimiento']}", size=16),
            ft.Text(f"Sexo: {empleado['sexo']}", size=16),
            ft.Text(f"Fecha de Ingreso: {empleado['fecha_ingreso']}", size=16),
            ft.Text(f"Fecha de Egreso: {empleado['fecha_egreso']}", size=16),
            ft.Text("Direcciones:", size=16),
        ]
        for d in empleado["direcciones"]:
            detalles.append(ft.Text(f"- {d['calle']} {d['altura']}, {d['localidad']}, {d['provincia']}, CP: {d['codigo_postal']}"))
        detalles.append(ft.Text("Teléfonos:", size=16))
        for t in empleado["telefonos"]:
            detalles.append(ft.Text(f"- {t['telefono']} ({t['tipo']})"))
        detalles.append(ft.Text("Cargos:", size=16))
        for c in empleado["cargos"]:
            detalles.append(ft.Text(f"- {c['cargo']}, Salario: {c['salario']}, Desde: {c['fecha_inicio']}, Hasta: {c['fecha_fin']}"))
        detalles.append(ft.Text("Jornadas Laborales:", size=16))
        for j in empleado["jornadas"]:
            detalles.append(ft.Text(f"- {j['fecha']}: {j['hora_de_entrada']} - {j['hora_de_salida']}"))

        btn_cerrar = ft.ElevatedButton("Cerrar", on_click=lambda e: cerrar_detalles())

        detalles_container.controls = [
            ft.Text("Detalles del Empleado", size=20),
            ft.Column(detalles),
            btn_cerrar
        ]
        page.update()

    def cerrar_detalles():
        """Cierra la vista de detalles."""
        detalles_container.controls.clear()
        page.update()

    def confirmar_eliminar(dni):
        """Muestra una caja de confirmación para eliminar un empleado.

        Args:
            dni (str): DNI del empleado a eliminar.
        """
        formulario_container.controls.clear()
        detalles_container.controls.clear()

        def on_confirmar(e):
            exito, msg = controlador.eliminar_empleado(dni)
            mensaje.value = msg
            if exito:
                actualizar_tabla()
                cerrar_confirmacion()
            page.update()

        def on_cancelar(e):
            cerrar_confirmacion()
            page.update()

        confirmar_container = ft.Column([
            ft.Text(f"¿Está seguro de que desea eliminar al empleado con DNI {dni}?", size=16),
            ft.Row([
                ft.ElevatedButton("Confirmar", on_click=on_confirmar),
                ft.ElevatedButton("Cancelar", on_click=on_cancelar)
            ])
        ])

        formulario_container.controls = [confirmar_container]
        page.update()

    def cerrar_confirmacion():
        """Cierra la caja de confirmación."""
        formulario_container.controls.clear()
        page.update()

    def modificar_direccion_form(direccion_id):
        """Abre un formulario para modificar una dirección.

        Args:
            direccion_id (int): ID de la dirección a modificar.
        """
        for d in direcciones:
            if d['id'] == direccion_id:
                calle.value = d['calle']
                altura.value = d['altura']
                localidad.value = d['localidad']
                provincia.value = d['provincia']
                codigo_postal.value = d['codigo_postal']
                break

        def guardar_modificacion(e):
            direccion = {
                "calle": calle.value,
                "altura": altura.value,
                "localidad": localidad.value,
                "provincia": provincia.value,
                "codigo_postal": codigo_postal.value
            }
            exito, msg = controlador.modificar_direccion(direccion_id, direccion)
            mensaje.value = msg
            if exito:
                empleado = controlador.obtener_empleado(dni.value)
                mostrar_formulario(modo="editar", empleado=empleado)
                calle.value = altura.value = localidad.value = provincia.value = codigo_postal.value = ""
            page.update()

        formulario_container.controls.append(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )
        page.update()

    def eliminar_direccion(direccion_id):
        """Elimina una dirección asociada a un empleado.

        Args:
            direccion_id (int): ID de la dirección a eliminar.
        """
        exito, msg = controlador.eliminar_direccion(direccion_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def modificar_telefono_form(telefono_id):
        """Abre un formulario para modificar un teléfono.

        Args:
            telefono_id (int): ID del teléfono a modificar.
        """
        for t in telefonos:
            if t['id'] == telefono_id:
                telefono.value = t['telefono']
                tipo.value = t['tipo']
                break

        def guardar_modificacion(e):
            exito, msg = controlador.modificar_telefono(telefono_id, telefono.value, tipo.value)
            mensaje.value = msg
            if exito:
                empleado = controlador.obtener_empleado(dni.value)
                mostrar_formulario(modo="editar", empleado=empleado)
                telefono.value = tipo.value = ""
            page.update()

        formulario_container.controls.append(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )
        page.update()

    def eliminar_telefono(telefono_id):
        """Elimina un teléfono asociado a un empleado.

        Args:
            telefono_id (int): ID del teléfono a eliminar.
        """
        exito, msg = controlador.eliminar_telefono(telefono_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def modificar_cargo_form(cargo_id):
        """Abre un formulario para modificar un cargo.

        Args:
            cargo_id (int): ID del cargo a modificar.
        """
        for c in cargos:
            if c['id'] == cargo_id:
                cargo.value = c['cargo']
                salario.value = c['salario']
                fecha_inicio.value = c['fecha_inicio']
                fecha_fin.value = c['fecha_fin']
                break

        def guardar_modificacion(e):
            exito, msg = controlador.modificar_cargo(cargo_id, cargo.value, salario.value,
                                                    fecha_inicio.value, fecha_fin.value)
            mensaje.value = msg
            if exito:
                empleado = controlador.obtener_empleado(dni.value)
                mostrar_formulario(modo="editar", empleado=empleado)
                cargo.value = salario.value = fecha_inicio.value = fecha_fin.value = ""
            page.update()

        formulario_container.controls.append(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )
        page.update()

    def eliminar_cargo(cargo_id):
        """Elimina un cargo asociado a un empleado.

        Args:
            cargo_id (int): ID del cargo a eliminar.
        """
        exito, msg = controlador.eliminar_cargo(cargo_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def modificar_jornada_form(jornada_id):
        """Abre un formulario para modificar una jornada laboral.

        Args:
            jornada_id (int): ID de la jornada a modificar.
        """
        for j in jornadas:
            if j['id'] == jornada_id:
                fecha.value = j['fecha']
                hora_de_entrada.value = j['hora_de_entrada']
                hora_de_salida.value = j['hora_de_salida']
                break

        def guardar_modificacion(e):
            exito, msg = controlador.modificar_jornada(jornada_id, fecha.value,
                                                      hora_de_entrada.value, hora_de_salida.value)
            mensaje.value = msg
            if exito:
                empleado = controlador.obtener_empleado(dni.value)
                mostrar_formulario(modo="editar", empleado=empleado)
                fecha.value = hora_de_entrada.value = hora_de_salida.value = ""
            page.update()

        formulario_container.controls.append(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )
        page.update()

    def eliminar_jornada(jornada_id):
        """Elimina una jornada laboral asociada a un empleado.

        Args:
            jornada_id (int): ID de la jornada a eliminar.
        """
        exito, msg = controlador.eliminar_jornada(jornada_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def actualizar_tabla():
        """Actualiza la tabla con la lista de empleados registrados."""
        empleados = controlador.listar_empleados()
        tabla_empleados.rows.clear()

        def on_ver_detalles(e, empleado):
            """Manejador para el botón 'Ver Detalles'."""
            ver_detalles(empleado)

        def on_editar(e, empleado):
            """Manejador para el botón 'Editar'."""
            mostrar_formulario(modo="editar", empleado=empleado)

        def on_eliminar(e, dni):
            """Manejador para el botón 'Eliminar'."""
            confirmar_eliminar(dni)

        for emp in empleados:
            tabla_empleados.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(emp["dni"])),
                        ft.DataCell(ft.Text(emp["nombre"])),
                        ft.DataCell(ft.Text(emp["apellido"])),
                        ft.DataCell(
                            ft.Row([
                                ft.ElevatedButton("Ver Detalles",
                                    on_click=lambda e: on_ver_detalles(e, emp)),
                                ft.ElevatedButton("Editar",
                                    on_click=lambda e: on_editar(e, emp)),
                                ft.ElevatedButton("Eliminar",
                                    on_click=lambda e: on_eliminar(e, emp["dni"]))
                            ])
                        )
                    ]
                )
            )
        page.update()

    # Botón para agregar nuevo empleado
    btn_agregar_nuevo = ft.ElevatedButton("Agregar Nuevo", on_click=lambda e: mostrar_formulario(modo="agregar"))

    # Organizar la interfaz
    page.add(
        ft.Column([
            ft.Text("Lista de Empleados", size=20),
            btn_agregar_nuevo,
            tabla_empleados,
            mensaje,
            detalles_container,
            formulario_container
        ])
    )

    # Cargar la tabla al inicio
    actualizar_tabla()

if __name__ == "__main__":
    ft.app(target=main)