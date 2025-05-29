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
    page.scroll = "auto"  # Permitir scroll automático vertical y horizontal

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

    def validar_fecha(fecha_str):
        """Valida que una fecha tenga el formato DD-MM-YYYY y sea válida.

        Args:
            fecha_str (str): Cadena de texto que representa la fecha.

        Returns:
            bool: True si la fecha es válida, False si no lo es.
        """
        if not fecha_str:  # Permitir campo vacío
            return True
        try:
            datetime.strptime(fecha_str, "%d-%m-%Y")
            return True
        except ValueError:
            return False

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

    def actualizar_listas_empleado(empleado):
        """Actualiza las listas globales con los datos del empleado.

        Args:
            empleado (dict): Diccionario con los datos del empleado.
        """
        global direcciones, telefonos, cargos, jornadas
        global direcciones_container, telefonos_container, cargos_container, jornadas_container

        # Depuración: Imprimir datos del empleado
        print(f"Actualizando listas para empleado: DNI={empleado.get('dni', 'N/A')}")
        print(f"Direcciones: {empleado.get('direcciones', [])}")
        print(f"Teléfonos: {empleado.get('telefonos', [])}")
        print(f"Cargos: {empleado.get('cargos', [])}")
        print(f"Jornadas: {empleado.get('jornadas', [])}")

        direcciones.clear()
        telefonos.clear()
        cargos.clear()
        jornadas.clear()
        direcciones_container.controls.clear()
        telefonos_container.controls.clear()
        cargos_container.controls.clear()
        jornadas_container.controls.clear()

        for d in empleado.get("direcciones", []):
            direcciones.append(d.copy())
            direcciones_container.controls.append(
                ft.Row([
                    ft.Text(f"Dirección: {d['calle']} {d['altura']}, {d['localidad']}"),
                    ft.ElevatedButton("Modificar",
                        on_click=lambda e, d_id=d['id']: mostrar_formulario_direccion(d_id)),
                    ft.ElevatedButton("Eliminar",
                        on_click=lambda e, d_id=d['id']: eliminar_direccion(d_id))
                ])
            )
        for t in empleado.get("telefonos", []):
            telefonos.append(t.copy())
            telefonos_container.controls.append(
                ft.Row([
                    ft.Text(f"Teléfono: {t['telefono']} ({t['tipo']})"),
                    ft.ElevatedButton("Modificar",
                        on_click=lambda e, t_id=t['id']: mostrar_formulario_telefono(t_id)),
                    ft.ElevatedButton("Eliminar",
                        on_click=lambda e, t_id=t['id']: eliminar_telefono(t_id))
                ])
            )
        for c in empleado.get("cargos", []):
            cargos.append(c.copy())
            cargos_container.controls.append(
                ft.Row([
                    ft.Text(f"Cargo: {c['cargo']}, Salario: {c['salario']}"),
                    ft.ElevatedButton("Modificar",
                        on_click=lambda e, c_id=c['id']: mostrar_formulario_cargo(c_id)),
                    ft.ElevatedButton("Eliminar",
                        on_click=lambda e, c_id=c['id']: eliminar_cargo(c_id))
                ])
            )
        for j in empleado.get("jornadas", []):
            jornadas.append(j.copy())
            jornadas_container.controls.append(
                ft.Row([
                    ft.Text(f"Jornada: {j['fecha']}, {j['hora_de_entrada']} - {j['hora_de_salida']}"),
                    ft.ElevatedButton("Modificar",
                        on_click=lambda e, j_id=j['id']: mostrar_formulario_jornada(j_id)),
                    ft.ElevatedButton("Eliminar",
                        on_click=lambda e, j_id=j['id']: eliminar_jornada(j_id))
                ])
            )
        page.update()

    def mostrar_formulario(modo="agregar", empleado=None):
        """Muestra el formulario para agregar o editar un empleado dentro de un modal.

        Args:
            modo (str): 'agregar' para nuevo empleado, 'editar' para modificar.
            empleado (dict, optional): Datos del empleado a editar.
        """
        global nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text
        global direcciones_container, telefonos_container, cargos_container, jornadas_container
        global direcciones, telefonos, cargos, jornadas

        # Si estamos en modo edición, asegurarnos de obtener los datos más recientes
        if modo == "editar" and empleado and empleado.get("dni"):
            empleado = controlador.obtener_empleado(empleado["dni"])
            print(f"Recuperado empleado para edición: {empleado}")

        # Inicializar campos del formulario
        nombre = ft.TextField(label="Nombre", width=200, value=empleado.get("nombre", "") if empleado else "")
        segundo_nombre = ft.TextField(label="Segundo Nombre", width=200, value=empleado.get("segundo_nombre", "") if empleado else "")
        apellido = ft.TextField(label="Apellido", width=200, value=empleado.get("apellido", "") if empleado else "")
        segundo_apellido = ft.TextField(label="Segundo Apellido", width=200, value=empleado.get("segundo_apellido", "") if empleado else "")
        dni = ft.TextField(label="DNI", width=200, value=empleado.get("dni", "") if empleado else "", read_only=modo == "editar")
        cuit = ft.TextField(label="CUIT", width=200, value=empleado.get("cuit", "") if empleado else "")
        sexo = ft.TextField(label="Sexo", width=100, value=empleado.get("sexo", "") if empleado else "")

        # Campos de texto para las fechas con validación
        fecha_nacimiento_text = ft.TextField(
            label="Fecha de Nacimiento (DD-MM-YYYY)",
            width=200,
            value=empleado.get("fecha_nacimiento", "") if empleado else "",
            hint_text="Ejemplo: 31-01-1990",
            on_change=lambda e: (
                mensaje.__setattr__("value", "Formato de fecha inválido. Use DD-MM-YYYY (ejemplo: 1990-01-01)")
                if e.control.value and not validar_fecha(e.control.value) else "",
                page.update()
            )
        )

        fecha_ingreso_text = ft.TextField(
            label="Fecha de Ingreso (DD-MM-YYYY)",
            width=200,
            value=empleado.get("fecha_ingreso", "") if empleado else "",
            hint_text="Ejemplo: 31-01-2020",
            on_change=lambda e: (
                mensaje.__setattr__("value", "Formato de fecha inválido. Use DD-MM-YYYY (ejemplo: 2020-05-26)")
                if e.control.value and not validar_fecha(e.control.value) else "",
                page.update()
            )
        )

        fecha_egreso_text = ft.TextField(
            label="Fecha de Egreso (DD-MM-YYYY)",
            width=200,
            value=empleado.get("fecha_egreso", "") if empleado else "",
            hint_text="Ejemplo: 31-12-2025",
            on_change=lambda e: (
                mensaje.__setattr__("value", "Formato de fecha inválido. Use DD-MM-YYYY (ejemplo: 2025-12-31)")
                if e.control.value and not validar_fecha(e.control.value) else "",
                page.update()
            )
        )

        # Contenedores para listas de datos múltiples
        direcciones_container = ft.Column([], scroll="auto")
        telefonos_container = ft.Column([], scroll="auto")
        cargos_container = ft.Column([], scroll="auto")
        jornadas_container = ft.Column([], scroll="auto")

        # Botones para agregar nuevas entradas
        btn_agregar_direccion = ft.ElevatedButton("Agregar Dirección", on_click=lambda e: mostrar_formulario_direccion())
        btn_agregar_telefono = ft.ElevatedButton("Agregar Teléfono", on_click=lambda e: mostrar_formulario_telefono())
        btn_agregar_cargo = ft.ElevatedButton("Agregar Cargo", on_click=lambda e: mostrar_formulario_cargo())
        btn_agregar_jornada = ft.ElevatedButton("Agregar Jornada", on_click=lambda e: mostrar_formulario_jornada())

        # Cargar datos existentes si es modo editar
        if modo == "editar" and empleado:
            actualizar_listas_empleado(empleado)

        # Botones del formulario
        if modo == "agregar":
            btn_guardar = ft.ElevatedButton("Guardar", on_click=lambda e: guardar_usuario())
        else:
            btn_guardar = ft.ElevatedButton("Guardar Cambios", on_click=lambda e: modificar_usuario())

        btn_cancelar = ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo())

        # Sección superior: Campos de ingreso de información
        campos_info = ft.Column([
            ft.Row([nombre, segundo_nombre, apellido, segundo_apellido], spacing=20, scroll="auto"),
            ft.Row([dni, cuit, sexo], spacing=20, scroll="auto"),
            ft.Row([fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text], spacing=20, scroll="auto")
        ], spacing=10, scroll="auto")

        # Sección inferior: Botones y contenedores para datos asociados
        datos_asociados = ft.Column([
            ft.Row([
                ft.Column([ft.Text("Direcciones"), btn_agregar_direccion, direcciones_container], spacing=10, scroll="auto"),
                ft.Column([ft.Text("Teléfonos"), btn_agregar_telefono, telefonos_container], spacing=10, scroll="auto")
            ], spacing=20, scroll="auto"),
            ft.Row([
                ft.Column([ft.Text("Cargos"), btn_agregar_cargo, cargos_container], spacing=10, scroll="auto"),
                ft.Column([ft.Text("Jornadas Laborales"), btn_agregar_jornada, jornadas_container], spacing=10, scroll="auto")
            ], spacing=20, scroll="auto"),
            ft.Row([btn_guardar, btn_cancelar], spacing=10)
        ], spacing=20, scroll="auto")

        # Contenido del modal
        contenido_formulario = ft.Column([
            ft.Text("Agregar Nuevo Empleado" if modo == "agregar" else "Editar Empleado", size=20),
            campos_info,
            datos_asociados
        ], spacing=10, scroll="auto")

        # Crear el modal
        dialogo = ft.AlertDialog(
            title=None,
            content=contenido_formulario,
            modal=True,
            shape=ft.RoundedRectangleBorder(radius=10),
            content_padding=ft.padding.all(20),
        )

        # Ajustar el tamaño del modal
        dialogo_width = min(page.window_width * 0.9, 1000)
        dialogo_height = min(page.window_height * 0.9, 600)
        contenido_formulario.width = dialogo_width - 40
        contenido_formulario.height = dialogo_height - 40

        page.overlay.append(dialogo)
        page.dialog = dialogo
        dialogo.open = True
        page.update()

    def cerrar_dialogo():
        """Cierra el diálogo actual."""
        if page.dialog:
            page.dialog.open = False
        limpiar_formulario()
        page.update()

    def cerrar_dialogo_secundario():
        """Cierra solo el diálogo secundario (para dirección, teléfono, etc.)."""
        if page.dialog and isinstance(page.dialog.content, ft.Column):
            page.dialog.open = False
        page.update()

    def guardar_usuario():
        """Guarda un nuevo empleado en la base de datos."""
        global direcciones, telefonos, cargos, jornadas
        global nombre, segundo_nombre, apellido, segundo_apellido, dni, cuit, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text

        try:
            # Validar fechas antes de guardar
            for fecha in [fecha_nacimiento_text.value, fecha_ingreso_text.value, fecha_egreso_text.value]:
                if fecha and not validar_fecha(fecha):
                    mensaje.value = "Una o más fechas tienen un formato inválido. Use DD-MM-YYYY."
                    page.update()
                    return

            datos = {
                "dni": dni.value or "",
                "cuit": cuit.value or "",
                "nombre": nombre.value or "",
                "segundo_nombre": segundo_nombre.value or "",
                "apellido": apellido.value or "",
                "segundo_apellido": segundo_apellido.value or "",
                "fecha_nacimiento": fecha_nacimiento_text.value or "",
                "edad": "0",  # Edad calculada o predeterminada
                "sexo": sexo.value or "",
                "fecha_ingreso": fecha_ingreso_text.value or "",
                "fecha_egreso": fecha_egreso_text.value or "",
                "direcciones": direcciones or [],
                "telefonos": telefonos or [],
                "cargos": cargos or [],
                "jornadas": jornadas or []
            }

            exito, msg, empleado_id = controlador.agregar_empleado(datos)
            mensaje.value = msg
            if exito:
                actualizar_tabla()
                cerrar_dialogo()
            page.update()
        except Exception as e:
            mensaje.value = f"Error al guardar empleado: {str(e)}"
            page.update()

    def modificar_usuario():
        """Modifica los datos de un empleado existente."""
        global dni, cuit, nombre, segundo_nombre, apellido, segundo_apellido, sexo
        global fecha_nacimiento_text, fecha_ingreso_text, fecha_egreso_text

        try:
            # Validar fechas antes de guardar
            for fecha in [fecha_nacimiento_text.value, fecha_ingreso_text.value, fecha_egreso_text.value]:
                if fecha and not validar_fecha(fecha):
                    mensaje.value = "Una o más fechas tienen un formato inválido. Use DD-MM-YYYY."
                    page.update()
                    return

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
                cerrar_dialogo()
            page.update()
        except Exception as e:
            mensaje.value = f"Error al modificar empleado: {str(e)}"
            page.update()

    def ver_detalles(empleado):
        """Muestra los detalles de un empleado en un modal."""
        # Obtener datos frescos del empleado
        empleado = controlador.obtener_empleado(empleado["dni"])
        print(f"Mostrando detalles para empleado: {empleado}")

        datos_personales = ft.Column([
            ft.Row([ft.Text(f"DNI: {empleado['dni']}", size=16), ft.Text(f"CUIT: {empleado['cuit']}", size=16)], spacing=20),
            ft.Row([ft.Text(f"Nombre: {empleado['nombre']} {empleado['segundo_nombre']}", size=16),
                    ft.Text(f"Apellido: {empleado['apellido']} {empleado['segundo_apellido']}", size=16)], spacing=20),
            ft.Row([ft.Text(f"Sexo: {empleado['sexo']}", size=16)], spacing=20),
            ft.Row([ft.Text(f"Fecha de Nacimiento: {empleado['fecha_nacimiento']}", size=16)], spacing=20),
            ft.Row([ft.Text(f"Fecha de Ingreso: {empleado['fecha_ingreso']}", size=16),
                    ft.Text(f"Fecha de Egreso: {empleado['fecha_egreso']}", size=16)], spacing=20),
        ], spacing=10, scroll="auto")

        direcciones_section = ft.Column([
            ft.Text("Direcciones:", size=16, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Text(f"- {d['calle']} {d['altura']}, {d['localidad']}, {d['provincia']}, CP: {d['codigo_postal']}")
                for d in empleado.get("direcciones", [])
            ], spacing=5) if empleado.get("direcciones") else ft.Text("Sin direcciones registradas")
        ], spacing=10, scroll="auto")

        telefonos_section = ft.Column([
            ft.Text("Teléfonos:", size=16, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Text(f"- {t['telefono']} ({t['tipo']})")
                for t in empleado.get("telefonos", [])
            ], spacing=5) if empleado.get("telefonos") else ft.Text("Sin teléfonos registrados")
        ], spacing=10, scroll="auto")

        cargos_section = ft.Column([
            ft.Text("Cargos:", size=16, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Text(f"- {c['cargo']}, Salario: {c['salario']}, Desde: {c['fecha_inicio']}, Hasta: {c['fecha_fin'] or 'N/A'}")
                for c in empleado.get("cargos", [])
            ], spacing=5) if empleado.get("cargos") else ft.Text("Sin cargos registrados")
        ], spacing=10, scroll="auto")

        jornadas_section = ft.Column([
            ft.Text("Jornadas Laborales:", size=16, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Text(f"- {j['fecha']}: {j['hora_de_entrada']} - {j['hora_de_salida']}")
                for j in empleado.get("jornadas", [])
            ], spacing=5) if empleado.get("jornadas") else ft.Text("Sin jornadas registradas")
        ], spacing=10, scroll="auto")

        contenido_detalles = ft.Column([
            ft.Text("Detalles del Empleado", size=20),
            datos_personales,
            direcciones_section,
            telefonos_section,
            cargos_section,
            jornadas_section,
            ft.ElevatedButton("Cerrar", on_click=lambda e: cerrar_dialogo())
        ], spacing=15, scroll="auto")

        dialogo = ft.AlertDialog(
            title=None,
            content=contenido_detalles,
            modal=True,
            shape=ft.RoundedRectangleBorder(radius=10),
            content_padding=ft.padding.all(20),
        )

        dialogo_width = min(page.window_width * 0.9, 800)
        dialogo_height = min(page.window_height * 0.9, 600)
        contenido_detalles.width = dialogo_width - 40
        contenido_detalles.height = dialogo_height - 40

        page.overlay.append(dialogo)
        page.dialog = dialogo
        dialogo.open = True
        page.update()

    def eliminar_direccion(direccion_id):
        """Elimina una dirección asociada a un empleado."""
        exito, msg = controlador.eliminar_direccion(direccion_id)
        mensaje.value = msg
        if exito and dni.value:
            empleado = controlador.obtener_empleado(dni.value)
            actualizar_listas_empleado(empleado)
        page.update()

    def eliminar_telefono(telefono_id):
        """Elimina un teléfono asociado a un empleado."""
        exito, msg = controlador.eliminar_telefono(telefono_id)
        mensaje.value = msg
        if exito and dni.value:
            empleado = controlador.obtener_empleado(dni.value)
            actualizar_listas_empleado(empleado)
        page.update()

    def eliminar_cargo(cargo_id):
        """Elimina un cargo asociado a un empleado."""
        exito, msg = controlador.eliminar_cargo(cargo_id)
        mensaje.value = msg
        if exito and dni.value:
            empleado = controlador.obtener_empleado(dni.value)
            actualizar_listas_empleado(empleado)
        page.update()

    def eliminar_jornada(jornada_id):
        """Elimina una jornada laboral asociada a un empleado."""
        exito, msg = controlador.eliminar_jornada(jornada_id)
        mensaje.value = msg
        if exito and dni.value:
            empleado = controlador.obtener_empleado(dni.value)
            actualizar_listas_empleado(empleado)
        page.update()

    def mostrar_formulario_direccion(direccion_id=None):
        """Muestra un diálogo para agregar o modificar una dirección."""
        global direcciones, direcciones_container
        try:
            direccion = next((d for d in direcciones if d['id'] == direccion_id), None) if direccion_id else None
            calle_input = ft.TextField(label="Calle", width=200, value=direccion["calle"] if direccion else "")
            altura_input = ft.TextField(label="Altura", width=200, value=direccion["altura"] if direccion else "")
            localidad_input = ft.TextField(label="Localidad", width=200, value=direccion["localidad"] if direccion else "")
            provincia_input = ft.TextField(label="Provincia", width=200, value=direccion["provincia"] if direccion else "")
            codigo_postal_input = ft.TextField(label="Código Postal", width=200, value=direccion["codigo_postal"] if direccion else "")

            def guardar_direccion(e):
                global direcciones
                nueva_direccion = {
                    "calle": calle_input.value or "",
                    "altura": altura_input.value or "",
                    "localidad": localidad_input.value or "",
                    "provincia": provincia_input.value or "",
                    "codigo_postal": codigo_postal_input.value or ""
                }
                if direccion_id:
                    nueva_direccion['id'] = direccion_id
                    exito, msg = controlador.modificar_direccion(direccion_id, nueva_direccion)
                    if exito:
                        direcciones[:] = [d for d in direcciones if d['id'] != direccion_id]
                        direcciones.append(nueva_direccion)
                        mensaje.value = msg
                    else:
                        mensaje.value = f"Error al modificar dirección: {msg}"
                else:
                    if dni.value and controlador.obtener_empleado(dni.value):
                        empleado_id = controlador.obtener_empleado(dni.value)['id']
                        exito, msg, nuevo_direccion_id = controlador.agregar_direccion(empleado_id, nueva_direccion)
                        if exito:
                            nueva_direccion['id'] = nuevo_direccion_id
                            direcciones.append(nueva_direccion)
                            mensaje.value = msg
                        else:
                            mensaje.value = f"Error al agregar dirección: {msg}"
                    else:
                        nueva_direccion['id'] = len(direcciones) + 1
                        direcciones.append(nueva_direccion)
                        mensaje.value = "Dirección agregada a la lista (se guardará al guardar el empleado)."
                cerrar_dialogo_secundario()
                if dni.value:
                    empleado = controlador.obtener_empleado(dni.value)
                    actualizar_listas_empleado(empleado)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Dirección" if not direccion_id else "Modificar Dirección"),
                content=ft.Column([calle_input, altura_input, localidad_input, provincia_input, codigo_postal_input], scroll="auto"),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_direccion),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo_secundario())
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
        """Muestra un diálogo para agregar o modificar un teléfono."""
        global telefonos, telefonos_container
        try:
            telefono_data = next((t for t in telefonos if t['id'] == telefono_id), None) if telefono_id else None
            telefono_input = ft.TextField(label="Teléfono", width=200, value=telefono_data["telefono"] if telefono_data else "")
            tipo_input = ft.TextField(label="Tipo", width=200, value=telefono_data["tipo"] if telefono_data else "")

            def guardar_telefono(e):
                global telefonos
                nuevo_telefono = {
                    "telefono": telefono_input.value or "",
                    "tipo": tipo_input.value or ""
                }
                if telefono_id:
                    nuevo_telefono['id'] = telefono_id
                    exito, msg = controlador.modificar_telefono(telefono_id, nuevo_telefono["telefono"], nuevo_telefono["tipo"])
                    if exito:
                        telefonos[:] = [t for t in telefonos if t['id'] != telefono_id]
                        telefonos.append(nuevo_telefono)
                        mensaje.value = msg
                    else:
                        mensaje.value = f"Error al modificar teléfono: {msg}"
                else:
                    if dni.value and controlador.obtener_empleado(dni.value):
                        empleado_id = controlador.obtener_empleado(dni.value)['id']
                        exito, msg, nuevo_telefono_id = controlador.agregar_telefono(empleado_id, nuevo_telefono["telefono"], nuevo_telefono["tipo"])
                        if exito:
                            nuevo_telefono['id'] = nuevo_telefono_id
                            telefonos.append(nuevo_telefono)
                            mensaje.value = msg
                        else:
                            mensaje.value = f"Error al agregar teléfono: {msg}"
                    else:
                        nuevo_telefono['id'] = len(telefonos) + 1
                        telefonos.append(nuevo_telefono)
                        mensaje.value = "Teléfono agregado a la lista (se guardará al guardar el empleado)."
                cerrar_dialogo_secundario()
                if dni.value:
                    empleado = controlador.obtener_empleado(dni.value)
                    actualizar_listas_empleado(empleado)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Teléfono" if not telefono_id else "Modificar Teléfono"),
                content=ft.Column([telefono_input, tipo_input], scroll="auto"),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_telefono),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo_secundario())
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
        """Muestra un diálogo para agregar o modificar un cargo."""
        global cargos, cargos_container
        try:
            cargo_data = next((c for c in cargos if c['id'] == cargo_id), None) if cargo_id else None
            cargo_input = ft.TextField(label="Cargo", width=200, value=cargo_data["cargo"] if cargo_data else "")
            salario_input = ft.TextField(label="Salario", width=200, value=cargo_data["salario"] if cargo_data else "")
            fecha_inicio_text = ft.TextField(
                label="Fecha Inicio (DD-MM-YYYY)",
                width=200,
                value=cargo_data["fecha_inicio"] if cargo_data and cargo_data["fecha_inicio"] else "",
                hint_text="Ejemplo: 2020-05-26",
                on_change=lambda e: (
                    mensaje.__setattr__("value", "Formato de fecha inválido. Use DD-MM-YYYY (ejemplo: 2020-05-26)")
                    if e.control.value and not validar_fecha(e.control.value) else "",
                    page.update()
                )
            )
            fecha_fin_text = ft.TextField(
                label="Fecha Fin (DD-MM-YYYY)",
                width=200,
                value=cargo_data["fecha_fin"] if cargo_data and cargo_data["fecha_fin"] else "",
                hint_text="Ejemplo: 2025-12-31",
                on_change=lambda e: (
                    mensaje.__setattr__("value", "Formato de fecha inválido. Use DD-MM-YYYY (ejemplo: 2025-12-31)")
                    if e.control.value and not validar_fecha(e.control.value) else "",
                    page.update()
                )
            )

            def guardar_cargo(e):
                global cargos
                nuevo_cargo = {
                    "cargo": cargo_input.value or "",
                    "salario": salario_input.value or "",
                    "fecha_inicio": fecha_inicio_text.value or "",
                    "fecha_fin": fecha_fin_text.value or ""
                }
                if cargo_id:
                    nuevo_cargo['id'] = cargo_id
                    exito, msg = controlador.modificar_cargo(cargo_id, nuevo_cargo["cargo"], nuevo_cargo["salario"],
                                                             nuevo_cargo["fecha_inicio"], nuevo_cargo["fecha_fin"])
                    if exito:
                        cargos[:] = [c for c in cargos if c['id'] != cargo_id]
                        cargos.append(nuevo_cargo)
                        mensaje.value = msg
                    else:
                        mensaje.value = f"Error al modificar cargo: {msg}"
                else:
                    if dni.value and controlador.obtener_empleado(dni.value):
                        empleado_id = controlador.obtener_empleado(dni.value)['id']
                        exito, msg, nuevo_cargo_id = controlador.agregar_cargo(empleado_id, nuevo_cargo["cargo"], nuevo_cargo["salario"],
                                                                               nuevo_cargo["fecha_inicio"], nuevo_cargo["fecha_fin"])
                        if exito:
                            nuevo_cargo['id'] = nuevo_cargo_id
                            cargos.append(nuevo_cargo)
                            mensaje.value = msg
                        else:
                            mensaje.value = f"Error al agregar cargo: {msg}"
                    else:
                        nuevo_cargo['id'] = len(cargos) + 1
                        cargos.append(nuevo_cargo)
                        mensaje.value = "Cargo agregado a la lista (se guardará al guardar el empleado)."
                cerrar_dialogo_secundario()
                if dni.value:
                    empleado = controlador.obtener_empleado(dni.value)
                    actualizar_listas_empleado(empleado)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Cargo" if not cargo_id else "Modificar Cargo"),
                content=ft.Column([cargo_input, salario_input, fecha_inicio_text, fecha_fin_text], scroll="auto"),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_cargo),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo_secundario())
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
        """Muestra un diálogo para agregar o modificar una jornada laboral."""
        global jornadas, jornadas_container
        try:
            jornada_data = next((j for j in jornadas if j['id'] == jornada_id), None) if jornada_id else None
            fecha_text = ft.TextField(
                label="Fecha (DD-MM-YYYY)",
                width=200,
                value=jornada_data["fecha"] if jornada_data and jornada_data["fecha"] else "",
                hint_text="Ejemplo: 2025-05-28",
                on_change=lambda e: (
                    mensaje.__setattr__("value", "Formato de fecha inválido. Use DD-MM-YYYY (ejemplo: 2025-05-28)")
                    if e.control.value and not validar_fecha(e.control.value) else "",
                    page.update()
                )
            )
            hora_entrada_input = ft.TextField(label="Hora de Entrada", width=200, value=jornada_data["hora_de_entrada"] if jornada_data else "")
            hora_salida_input = ft.TextField(label="Hora de Salida", width=200, value=jornada_data["hora_de_salida"] if jornada_data else "")

            def guardar_jornada(e):
                global jornadas
                nueva_jornada = {
                    "fecha": fecha_text.value or "",
                    "hora_de_entrada": hora_entrada_input.value or "",
                    "hora_de_salida": hora_salida_input.value or ""
                }
                if jornada_id:
                    nueva_jornada['id'] = jornada_id
                    exito, msg = controlador.modificar_jornada(jornada_id, nueva_jornada["fecha"],
                                                               nueva_jornada["hora_de_entrada"], nueva_jornada["hora_de_salida"])
                    if exito:
                        jornadas[:] = [j for j in jornadas if j['id'] != jornada_id]
                        jornadas.append(nueva_jornada)
                        mensaje.value = msg
                    else:
                        mensaje.value = f"Error al modificar jornada: {msg}"
                else:
                    if dni.value and controlador.obtener_empleado(dni.value):
                        empleado_id = controlador.obtener_empleado(dni.value)['id']
                        exito, msg, nueva_jornada_id = controlador.agregar_jornada(empleado_id, nueva_jornada["fecha"],
                                                                                   nueva_jornada["hora_de_entrada"], nueva_jornada["hora_de_salida"])
                        if exito:
                            nueva_jornada['id'] = nueva_jornada_id
                            jornadas.append(nueva_jornada)
                            mensaje.value = msg
                        else:
                            mensaje.value = f"Error al agregar jornada: {msg}"
                    else:
                        nueva_jornada['id'] = len(jornadas) + 1
                        jornadas.append(nueva_jornada)
                        mensaje.value = "Jornada agregada a la lista (se guardará al guardar el empleado)."
                cerrar_dialogo_secundario()
                if dni.value:
                    empleado = controlador.obtener_empleado(dni.value)
                    actualizar_listas_empleado(empleado)
                page.update()

            dialogo = ft.AlertDialog(
                title=ft.Text("Agregar Jornada" if not jornada_id else "Modificar Jornada"),
                content=ft.Column([fecha_text, hora_entrada_input, hora_salida_input], scroll="auto"),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=guardar_jornada),
                    ft.ElevatedButton("Cancelar", on_click=lambda e: cerrar_dialogo_secundario())
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

    def actualizar_tabla():
        """Actualiza la tabla con la lista de empleados registrados."""
        empleados = controlador.listar_empleados()
        tabla_empleados.rows.clear()

        def on_ver_detalles(e, empleado):
            ver_detalles(empleado)

        def on_editar(e, empleado):
            mostrar_formulario(modo="editar", empleado=empleado)

        def on_eliminar(e, dni):
            confirmar_eliminar(dni)

        for empleado in empleados:
            tabla_empleados.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(empleado["dni"])),
                        ft.DataCell(ft.Text(empleado["nombre"])),
                        ft.DataCell(ft.Text(empleado["apellido"])),
                        ft.DataCell(
                            ft.Row([
                                ft.ElevatedButton("Ver Detalles", on_click=lambda e, emp=empleado: on_ver_detalles(e, emp)),
                                ft.ElevatedButton("Editar", on_click=lambda e, emp=empleado: on_editar(e, emp)),
                                ft.ElevatedButton("Eliminar", on_click=lambda e, dni=empleado["dni"]: on_eliminar(e, dni))
                            ])
                        )
                    ]
                )
            )
        page.update()

    def confirmar_eliminar(dni):
        """Muestra una caja de confirmación para eliminar un empleado."""
        def on_confirmar(e):
            exito, msg = controlador.eliminar_empleado(dni)
            mensaje.value = msg
            if exito:
                actualizar_tabla()
                cerrar_dialogo()
            page.update()

        def on_cancelar(e):
            cerrar_dialogo()
            page.update()

        confirmar_container = ft.Column([
            ft.Text(f"¿Estás seguro de que deseas eliminar al empleado con DNI {dni}?", size=16),
            ft.Row([
                ft.ElevatedButton("Confirmar", on_click=on_confirmar),
                ft.ElevatedButton("Cancelar", on_click=on_cancelar)
            ])
        ])

        dialogo = ft.AlertDialog(
            title=ft.Text("Confirmar Eliminación"),
            content=confirmar_container,
            modal=True
        )
        page.overlay.append(dialogo)
        page.dialog = dialogo
        dialogo.open = True
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
        ], scroll="auto")
    )

    # Cargar la tabla al inicio
    actualizar_tabla()

if __name__ == "__main__":
    ft.app(target=main)