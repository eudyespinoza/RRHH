import flet as ft
from datetime import datetime
from controlador.controlador import Controlador

# Definir variables globales para evitar el uso de nonlocal
nombre = None
segundo_nombre = None
apellido = None
segundo_apellido = None
dni = None
cuit = None
fecha_nacimiento_text = None
fecha_ingreso_text = None
fecha_egreso_text = None
sexo = None
direcciones_container = None
telefonos_container = None
cargos_container = None
jornadas_container = None
direcciones = []
telefonos = []
cargos = []
jornadas = []

def main(page: ft.Page):
    """Función principal que inicia la aplicación Flet para el ABM de empleados.

    Args:
        page (ft.Page): Página principal de la aplicación Flet.
    """
    global nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit, sexo
    global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text
    global direcciones_container, telefonos_container, cargos_container, jornadas_container
    global direcciones, telefonos, cargos, jornadas

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

    # Añadir los DatePickers a page.overlay al inicio
    fecha_nacimiento_picker = ft.DatePicker()
    fecha_ingreso_picker = ft.DatePicker()
    fecha_egreso_picker = ft.DatePicker()
    page.overlay.extend([fecha_nacimiento_picker, fecha_ingreso_picker, fecha_egreso_picker])

    # Control dummy para mover el foco
    dummy_focus_control = ft.TextField(visible=False)
    page.add(dummy_focus_control)

    def limpiar_formulario():
        """Limpia todos los campos del formulario y las listas."""
        global nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text
        global direcciones_container, telefonos_container, cargos_container, jornadas_container
        global direcciones, telefonos, cargos, jornadas

        if nombre is not None:
            nombre.value = ""
            segundo_nombre.value = ""
            apellido.value = ""
            segundo_apellido.value = ""
            dni.value = ""
            cuit.value = ""
            sexo.value = ""
            fecha_nacimiento_text.value = ""
            fecha_ingreso_text.value = ""
            fecha_egreso_text.value = ""
        direcciones.clear()
        telefonos.clear()
        cargos.clear()
        jornadas.clear()
        if direcciones_container is not None:
            direcciones_container.controls.clear()
            telefonos_container.controls.clear()
            cargos_container.controls.clear()
            jornadas_container.controls.clear()
        mensaje.value = ""
        page.update()

    def abrir_date_picker(picker, text_field):
        """Abre un DatePicker."""
        try:
            picker.open = True
            mensaje.value += f" Abriendo DatePicker... Estado open: {picker.open}"
            page.update()
        except Exception as e:
            mensaje.value += f" Error al abrir DatePicker: {str(e)}"
            page.update()

    def cerrar_date_picker(picker):
        """Cierra un DatePicker y mueve el foco a un control dummy."""
        try:
            picker.open = False
            mensaje.value += f" Cerrando DatePicker... Estado open: {picker.open}"
            # Mover el foco al control dummy para evitar que el TextField reciba el foco de nuevo
            dummy_focus_control.focus()
            page.update()
        except Exception as e:
            mensaje.value += f" Error al cerrar DatePicker: {str(e)}"
            page.update()

    def mostrar_formulario(modo="agregar", empleado=None):
        """Muestra el formulario para agregar o editar un empleado.

        Args:
            modo (str): 'agregar' para nuevo empleado, 'editar' para modificar.
            empleado (dict, optional): Datos del empleado a editar.
        """
        global nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text
        global direcciones_container, telefonos_container, cargos_container, jornadas_container

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
        sexo = ft.TextField(label="Sexo", width=200, value=empleado["sexo"] if empleado else "")

        # Campos de texto para mostrar las fechas seleccionadas
        fecha_nacimiento_text = ft.TextField(label="Fecha de Nacimiento (YYYY-MM-DD)", width=200,
                                             value=empleado["fecha_nacimiento"] if empleado and empleado["fecha_nacimiento"] else "")
        fecha_nacimiento_picker.on_change = lambda e: (
            fecha_nacimiento_text.__setattr__("value", e.control.value.strftime("%Y-%m-%d") if e.control.value else ""),
            cerrar_date_picker(fecha_nacimiento_picker)
        )
        fecha_nacimiento_picker.on_dismiss = lambda e: cerrar_date_picker(fecha_nacimiento_picker)
        fecha_nacimiento_text.on_focus = lambda e: abrir_date_picker(fecha_nacimiento_picker, fecha_nacimiento_text)

        fecha_ingreso_text = ft.TextField(label="Fecha de Ingreso (YYYY-MM-DD)", width=200,
                                          value=empleado["fecha_ingreso"] if empleado and empleado["fecha_ingreso"] else "")
        fecha_ingreso_picker.on_change = lambda e: (
            fecha_ingreso_text.__setattr__("value", e.control.value.strftime("%Y-%m-%d") if e.control.value else ""),
            cerrar_date_picker(fecha_ingreso_picker)
        )
        fecha_ingreso_picker.on_dismiss = lambda e: cerrar_date_picker(fecha_ingreso_picker)
        fecha_ingreso_text.on_focus = lambda e: abrir_date_picker(fecha_ingreso_picker, fecha_ingreso_text)

        fecha_egreso_text = ft.TextField(label="Fecha de Egreso (YYYY-MM-DD)", width=200,
                                         value=empleado["fecha_egreso"] if empleado and empleado["fecha_egreso"] else "")
        fecha_egreso_picker.on_change = lambda e: (
            fecha_egreso_text.__setattr__("value", e.control.value.strftime("%Y-%m-%d") if e.control.value else ""),
            cerrar_date_picker(fecha_egreso_picker)
        )
        fecha_egreso_picker.on_dismiss = lambda e: cerrar_date_picker(fecha_egreso_picker)
        fecha_egreso_text.on_focus = lambda e: abrir_date_picker(fecha_egreso_picker, fecha_egreso_text)

        # Contenedores para listas de datos múltiples
        direcciones_container = ft.Column([])
        telefonos_container = ft.Column([])
        cargos_container = ft.Column([])
        jornadas_container = ft.Column([])

        # Botones para agregar nuevas entradas
        btn_agregar_direccion = ft.ElevatedButton("Agregar Dirección", on_click=lambda e: mostrar_formulario_direccion())
        btn_agregar_telefono = ft.ElevatedButton("Agregar Teléfono", on_click=lambda e: mostrar_formulario_telefono())
        btn_agregar_cargo = ft.ElevatedButton("Agregar Cargo", on_click=lambda e: mostrar_formulario_cargo())
        btn_agregar_jornada = ft.ElevatedButton("Agregar Jornada", on_click=lambda e: mostrar_formulario_jornada())

        # Cargar datos existentes si es modo editar
        if modo == "editar" and empleado:
            for d in empleado["direcciones"]:
                direcciones.append(d)
                direcciones_container.controls.append(
                    ft.Row([
                        ft.Text(f"Dirección: {d['calle']} {d['altura']}, {d['localidad']}"),
                        ft.ElevatedButton("Modificar",
                            on_click=lambda e, d_id=d['id']: mostrar_formulario_direccion(d_id)),
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
                            on_click=lambda e, t_id=t['id']: mostrar_formulario_telefono(t_id)),
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
                            on_click=lambda e, c_id=c['id']: mostrar_formulario_cargo(c_id)),
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
                            on_click=lambda e, j_id=j['id']: mostrar_formulario_jornada(j_id)),
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
            fecha_nacimiento_text,
            fecha_ingreso_text,
            fecha_egreso_text,
            sexo
        ])
        columna2 = ft.Column([
            ft.Text("Direcciones"),
            btn_agregar_direccion,
            direcciones_container
        ])
        columna3 = ft.Column([
            ft.Text("Teléfonos"),
            btn_agregar_telefono,
            telefonos_container
        ])
        columna4 = ft.Column([
            ft.Text("Cargos"),
            btn_agregar_cargo,
            cargos_container
        ])
        columna5 = ft.Column([
            ft.Text("Jornadas Laborales"),
            btn_agregar_jornada,
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

    def mostrar_formulario_direccion(direccion_id=None):
        """Muestra un diálogo para agregar o modificar una dirección.

        Args:
            direccion_id (int, optional): ID de la dirección a modificar.
        """
        global direcciones, direcciones_container

        try:
            direccion = next((d for d in direcciones if d['id'] == direccion_id), None) if direccion_id else None

            calle_input = ft.TextField(label="Calle", value=direccion["calle"] if direccion else "")
            altura_input = ft.TextField(label="Altura", value=direccion["altura"] if direccion else "")
            localidad_input = ft.TextField(label="Localidad", value=direccion["localidad"] if direccion else "")
            provincia_input = ft.TextField(label="Provincia", value=direccion["provincia"] if direccion else "")
            codigo_postal_input = ft.TextField(label="Código Postal", value=direccion["codigo_postal"] if direccion else "")

            def guardar_direccion(e):
                global direcciones
                nueva_direccion = {
                    "id": direccion_id,
                    "calle": calle_input.value or "",
                    "altura": altura_input.value or "",
                    "localidad": localidad_input.value or "",
                    "provincia": provincia_input.value or "",
                    "codigo_postal": codigo_postal_input.value or ""
                }
                if direccion_id:
                    # Modificar dirección existente
                    if any(d['id'] == direccion_id for d in direcciones):
                        direcciones[:] = [d for d in direcciones if d['id'] != direccion_id]
                    direcciones.append(nueva_direccion)
                    exito, msg = controlador.modificar_direccion(direccion_id, nueva_direccion)
                    mensaje.value = msg
                else:
                    # Agregar nueva dirección (se guardará en la DB al guardar el empleado)
                    direcciones.append(nueva_direccion)
                cerrar_dialogo()
                mostrar_formulario(modo="editar" if dni.value else "agregar", empleado=controlador.obtener_empleado(dni.value) if dni.value else None)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Dirección" if not direccion_id else "Modificar Dirección"),
                content=ft.Column([
                    calle_input, altura_input, localidad_input, provincia_input, codigo_postal_input
                ]),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_direccion),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo())
                ],
                modal=True
            )
            page.overlay.append(dialogo)
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        except Exception as e:
            mensaje.value = f"Error al mostrar formulario de dirección: {str(e)}"
            page.update()

    def mostrar_formulario_telefono(telefono_id=None):
        """Muestra un diálogo para agregar o modificar un teléfono.

        Args:
            telefono_id (int, optional): ID del teléfono a modificar.
        """
        global telefonos, telefonos_container

        try:
            telefono_data = next((t for t in telefonos if t['id'] == telefono_id), None) if telefono_id else None

            telefono_input = ft.TextField(label="Teléfono", value=telefono_data["telefono"] if telefono_data else "")
            tipo_input = ft.TextField(label="Tipo", value=telefono_data["tipo"] if telefono_data else "")

            def guardar_telefono(e):
                global telefonos
                nuevo_telefono = {
                    "id": telefono_id,
                    "telefono": telefono_input.value or "",
                    "tipo": tipo_input.value or ""
                }
                if telefono_id:
                    # Modificar teléfono existente
                    if any(t['id'] == telefono_id for t in telefonos):
                        telefonos[:] = [t for t in telefonos if t['id'] != telefono_id]
                    telefonos.append(nuevo_telefono)
                    exito, msg = controlador.modificar_telefono(telefono_id, nuevo_telefono["telefono"], nuevo_telefono["tipo"])
                    mensaje.value = msg
                else:
                    # Agregar nuevo teléfono
                    telefonos.append(nuevo_telefono)
                cerrar_dialogo()
                mostrar_formulario(modo="editar" if dni.value else "agregar", empleado=controlador.obtener_empleado(dni.value) if dni.value else None)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Teléfono" if not telefono_id else "Modificar Teléfono"),
                content=ft.Column([telefono_input, tipo_input]),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_telefono),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo())
                ],
                modal=True
            )
            page.overlay.append(dialogo)
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        except Exception as e:
            mensaje.value = f"Error al mostrar formulario de teléfono: {str(e)}"
            page.update()

    def mostrar_formulario_cargo(cargo_id=None):
        """Muestra un diálogo para agregar o modificar un cargo.

        Args:
            cargo_id (int, optional): ID del cargo a modificar.
        """
        global cargos, cargos_container

        try:
            cargo_data = next((c for c in cargos if c['id'] == cargo_id), None) if cargo_id else None

            cargo_input = ft.TextField(label="Cargo", value=cargo_data["cargo"] if cargo_data else "")
            salario_input = ft.TextField(label="Salario", value=cargo_data["salario"] if cargo_data else "")
            fecha_inicio_text = ft.TextField(label="Fecha Inicio (YYYY-MM-DD)", width=200,
                                             value=cargo_data["fecha_inicio"] if cargo_data and cargo_data["fecha_inicio"] else "")
            fecha_fin_text = ft.TextField(label="Fecha Fin (YYYY-MM-DD)", width=200,
                                          value=cargo_data["fecha_fin"] if cargo_data and cargo_data["fecha_fin"] else "")

            fecha_inicio_picker = ft.DatePicker()
            fecha_fin_picker = ft.DatePicker()
            page.overlay.extend([fecha_inicio_picker, fecha_fin_picker])

            fecha_inicio_picker.on_change = lambda e: (
                fecha_inicio_text.__setattr__("value", e.control.value.strftime("%Y-%m-%d") if e.control.value else ""),
                cerrar_date_picker(fecha_inicio_picker)
            )
            fecha_inicio_picker.on_dismiss = lambda e: cerrar_date_picker(fecha_inicio_picker)
            fecha_inicio_text.on_focus = lambda e: abrir_date_picker(fecha_inicio_picker, fecha_inicio_text)

            fecha_fin_picker.on_change = lambda e: (
                fecha_fin_text.__setattr__("value", e.control.value.strftime("%Y-%m-%d") if e.control.value else ""),
                cerrar_date_picker(fecha_fin_picker)
            )
            fecha_fin_picker.on_dismiss = lambda e: cerrar_date_picker(fecha_fin_picker)
            fecha_fin_text.on_focus = lambda e: abrir_date_picker(fecha_fin_picker, fecha_fin_text)

            def guardar_cargo(e):
                global cargos
                nuevo_cargo = {
                    "id": cargo_id,
                    "cargo": cargo_input.value or "",
                    "salario": salario_input.value or "",
                    "fecha_inicio": fecha_inicio_text.value or "",
                    "fecha_fin": fecha_fin_text.value or ""
                }
                if cargo_id:
                    # Modificar cargo existente
                    if any(c['id'] == cargo_id for c in cargos):
                        cargos[:] = [c for c in cargos if c['id'] != cargo_id]
                    cargos.append(nuevo_cargo)
                    exito, msg = controlador.modificar_cargo(cargo_id, nuevo_cargo["cargo"], nuevo_cargo["salario"],
                                                             nuevo_cargo["fecha_inicio"], nuevo_cargo["fecha_fin"])
                    mensaje.value = msg
                else:
                    # Agregar nuevo cargo
                    cargos.append(nuevo_cargo)
                cerrar_dialogo()
                mostrar_formulario(modo="editar" if dni.value else "agregar", empleado=controlador.obtener_empleado(dni.value) if dni.value else None)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Cargo" if not cargo_id else "Modificar Cargo"),
                content=ft.Column([
                    cargo_input, salario_input,
                    fecha_inicio_text,
                    fecha_fin_text
                ]),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_cargo),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo())
                ],
                modal=True
            )
            page.overlay.append(dialogo)
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        except Exception as e:
            mensaje.value = f"Error al mostrar formulario de cargo: {str(e)}"
            page.update()

    def mostrar_formulario_jornada(jornada_id=None):
        """Muestra un diálogo para agregar o modificar una jornada laboral.

        Args:
            jornada_id (int, optional): ID de la jornada a modificar.
        """
        global jornadas, jornadas_container

        try:
            jornada_data = next((j for j in jornadas if j['id'] == jornada_id), None) if jornada_id else None

            fecha_text = ft.TextField(label="Fecha (YYYY-MM-DD)", width=200,
                                      value=jornada_data["fecha"] if jornada_data and jornada_data["fecha"] else "")
            fecha_picker = ft.DatePicker()
            page.overlay.append(fecha_picker)
            fecha_picker.on_change = lambda e: (
                fecha_text.__setattr__("value", e.control.value.strftime("%Y-%m-%d") if e.control.value else ""),
                cerrar_date_picker(fecha_picker)
            )
            fecha_picker.on_dismiss = lambda e: cerrar_date_picker(fecha_picker)
            fecha_text.on_focus = lambda e: abrir_date_picker(fecha_picker, fecha_text)

            hora_entrada_input = ft.TextField(label="Hora de Entrada", value=jornada_data["hora_de_entrada"] if jornada_data else "")
            hora_salida_input = ft.TextField(label="Hora de Salida", value=jornada_data["hora_de_salida"] if jornada_data else "")

            def guardar_jornada(e):
                global jornadas
                nueva_jornada = {
                    "id": jornada_id,
                    "fecha": fecha_text.value or "",
                    "hora_de_entrada": hora_entrada_input.value or "",
                    "hora_de_salida": hora_salida_input.value or ""
                }
                if jornada_id:
                    # Modificar jornada existente
                    if any(j['id'] == jornada_id for j in jornadas):
                        jornadas[:] = [j for j in jornadas if j['id'] != jornada_id]
                    jornadas.append(nueva_jornada)
                    exito, msg = controlador.modificar_jornada(jornada_id, nueva_jornada["fecha"],
                                                               nueva_jornada["hora_de_entrada"], nueva_jornada["hora_de_salida"])
                    mensaje.value = msg
                else:
                    # Agregar nueva jornada
                    jornadas.append(nueva_jornada)
                cerrar_dialogo()
                mostrar_formulario(modo="editar" if dni.value else "agregar", empleado=controlador.obtener_empleado(dni.value) if dni.value else None)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Jornada" if not jornada_id else "Modificar Jornada"),
                content=ft.Column([
                    fecha_text,
                    hora_entrada_input,
                    hora_salida_input
                ]),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_jornada),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo())
                ],
                modal=True
            )
            page.overlay.append(dialogo)
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        except Exception as e:
            mensaje.value = f"Error al mostrar formulario de jornada: {str(e)}"
            page.update()

    def cerrar_dialogo():
        """Cierra el diálogo actual."""
        if page.dialog:
            page.dialog.open = False
        page.update()

    def cerrar_formulario():
        """Cierra el formulario y limpia los datos."""
        limpiar_formulario()
        page.update()

    def guardar_usuario():
        """Guarda un nuevo empleado en la base de datos."""
        global direcciones, telefonos, cargos, jornadas
        global dni, cuit, nombre, segundo_nombre, apellido, segundo_apellido, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text

        try:
            # Depuración: Mostrar el contenido de las listas antes de guardar
            mensaje.value = (f"Guardando empleado... Direcciones: {direcciones}, "
                             f"Teléfonos: {telefonos}, Cargos: {cargos}, Jornadas: {jornadas}")
            page.update()

            datos = {
                "dni": dni.value or "",
                "cuit": cuit.value or "",
                "nombre": nombre.value or "",
                "segundo_nombre": segundo_nombre.value or "",
                "apellido": apellido.value or "",
                "segundo_apellido": segundo_apellido.value or "",
                "fecha_nacimiento": fecha_nacimiento_text.value or "",
                "edad": "0",
                "sexo": sexo.value or "",
                "fecha_ingreso": fecha_ingreso_text.value or "",
                "fecha_egreso": fecha_egreso_text.value or "",
                "direcciones": [],
                "telefonos": [],
                "cargos": [],
                "jornadas": []
            }
            exito, msg, empleado_id = controlador.agregar_empleado(datos)
            if exito:
                # Guardar direcciones
                for direccion in direcciones:
                    if any(direccion.values()):  # Verificar que la dirección no esté vacía
                        exito_d, msg_d = controlador.agregar_direccion(empleado_id, direccion)
                        if not exito_d:
                            mensaje.value += f" Error al guardar dirección: {msg_d}"
                        else:
                            mensaje.value += f" Dirección guardada: {direccion}"
                # Guardar teléfonos
                for telefono in telefonos:
                    if telefono["telefono"]:
                        exito_t, msg_t = controlador.agregar_telefono(empleado_id, telefono["telefono"], telefono["tipo"])
                        if not exito_t:
                            mensaje.value += f" Error al guardar teléfono: {msg_t}"
                        else:
                            mensaje.value += f" Teléfono guardado: {telefono}"
                # Guardar cargos
                for cargo in cargos:
                    if cargo["cargo"]:
                        exito_c, msg_c = controlador.agregar_cargo(empleado_id, cargo["cargo"], cargo["salario"],
                                                                   cargo["fecha_inicio"], cargo["fecha_fin"])
                        if not exito_c:
                            mensaje.value += f" Error al guardar cargo: {msg_c}"
                        else:
                            mensaje.value += f" Cargo guardado: {cargo}"
                # Guardar jornadas
                for jornada in jornadas:
                    if jornada["fecha"] or jornada["hora_de_entrada"] or jornada["hora_de_salida"]:
                        exito_j, msg_j = controlador.agregar_jornada(empleado_id, jornada["fecha"],
                                                                     jornada["hora_de_entrada"], jornada["hora_de_salida"])
                        if not exito_j:
                            mensaje.value += f" Error al guardar jornada: {msg_j}"
                        else:
                            mensaje.value += f" Jornada guardada: {jornada}"
                mensaje.value = "Empleado y datos asociados agregados con éxito."
                actualizar_tabla()
                cerrar_formulario()
            else:
                mensaje.value = msg
            page.update()
        except Exception as e:
            mensaje.value = f"Error al guardar empleado: {str(e)}"
            page.update()

    def modificar_usuario():
        """Modifica los datos de un empleado existente."""
        global dni, cuit, nombre, segundo_nombre, apellido, segundo_apellido, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text

        try:
            datos = {
                "dni": dni.value or "",
                "cuit": cuit.value or "",
                "nombre": nombre.value or "",
                "segundo_nombre": segundo_nombre.value or "",
                "apellido": apellido.value or "",
                "segundo_apellido": segundo_apellido.value or "",
                "fecha_nacimiento": fecha_nacimiento_text.value or "",
                "edad": "0",
                "sexo": sexo.value or "",
                "fecha_ingreso": fecha_ingreso_text.value or "",
                "fecha_egreso": fecha_egreso_text.value or ""
            }
            exito, msg = controlador.modificar_empleado(dni.value, datos)
            mensaje.value = msg
            if exito:
                actualizar_tabla()
                cerrar_formulario()
            page.update()
        except Exception as e:
            mensaje.value = f"Error al modificar empleado: {str(e)}"
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

    def eliminar_direccion(direccion_id):
        """Elimina una dirección asociada a un empleado.

        Args:
            direccion_id (int): ID de la dirección a eliminar.
        """
        global direcciones
        exito, msg = controlador.eliminar_direccion(direccion_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def eliminar_telefono(telefono_id):
        """Elimina un teléfono asociado a un empleado.

        Args:
            telefono_id (int): ID del teléfono a eliminar.
        """
        global telefonos
        exito, msg = controlador.eliminar_telefono(telefono_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def eliminar_cargo(cargo_id):
        """Elimina un cargo asociado a un empleado.

        Args:
            cargo_id (int): ID del cargo a eliminar.
        """
        global cargos
        exito, msg = controlador.eliminar_cargo(cargo_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            mostrar_formulario(modo="editar", empleado=empleado)
        page.update()

    def eliminar_jornada(jornada_id):
        """Elimina una jornada laboral asociada a un empleado.

        Args:
            jornada_id (int): ID de la jornada a eliminar.
        """
        global jornadas
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