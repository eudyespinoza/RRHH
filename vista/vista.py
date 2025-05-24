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

    # Campos de entrada para el empleado
    nombre = ft.TextField(label="Nombre", width=200)
    segundo_nombre = ft.TextField(label="Segundo Nombre", width=200)
    apellido = ft.TextField(label="Apellido", width=200)
    segundo_apellido = ft.TextField(label="Segundo Apellido", width=200)
    dni = ft.TextField(label="DNI", width=200)
    cuit = ft.TextField(label="CUIT", width=200)
    fecha_nacimiento = ft.TextField(label="Fecha de Nacimiento", width=200)
    fecha_ingreso = ft.TextField(label="Fecha de Ingreso", width=200)
    fecha_egreso = ft.TextField(label="Fecha de Egreso", width=200)
    sexo = ft.TextField(label="Sexo", width=200)

    # Listas para manejar múltiples entradas
    direcciones = []
    telefonos = []
    cargos = []
    jornadas = []

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

    # Mensaje de retroalimentación
    mensaje = ft.Text("")

    def guardar_usuario(e):
        """Guarda un nuevo empleado en la base de datos."""
        datos = {
            "dni": dni.value,
            "cuit": cuit.value,
            "nombre": nombre.value,
            "segundo_nombre": segundo_nombre.value,
            "apellido": apellido.value,
            "segundo_apellido": segundo_apellido.value,
            "fecha_nacimiento": fecha_nacimiento.value,
            "edad": "0",  # Podrías calcular la edad aquí con datetime
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
            limpiar_formulario()
        page.update()

    def modificar_usuario(e):
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
        page.update()

    def eliminar_usuario(e):
        """Elimina un empleado de la base de datos."""
        if not dni.value:
            mensaje.value = "Por favor, seleccione un empleado para eliminar."
            page.update()
            return
        exito, msg = controlador.eliminar_empleado(dni.value)
        mensaje.value = msg
        if exito:
            actualizar_tabla()
            limpiar_formulario()
        page.update()

    def limpiar_formulario():
        """Limpia todos los campos del formulario."""
        nombre.value = segundo_nombre.value = apellido.value = segundo_apellido.value = ""
        dni.value = cuit.value = fecha_nacimiento.value = fecha_ingreso.value = fecha_egreso.value = sexo.value = ""
        calle.value = altura.value = localidad.value = provincia.value = codigo_postal.value = ""
        telefono.value = tipo.value = ""
        cargo.value = salario.value = fecha_inicio.value = fecha_fin.value = ""
        fecha.value = hora_de_entrada.value = hora_de_salida.value = ""
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

    def actualizar_tabla():
        """Actualiza la tabla con la lista de empleados registrados."""
        empleados = controlador.listar_empleados()
        tabla_empleados.rows.clear()

        def on_ver_empleado(e, empleado):
            """Manejador para el botón 'Ver'."""
            ver_empleado(empleado)

        def on_eliminar_empleado(e, dni):
            """Manejador para el botón 'Eliminar'."""
            eliminar_empleado(dni)

        for emp in empleados:
            tabla_empleados.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(emp["dni"])),
                        ft.DataCell(ft.Text(emp["nombre"])),
                        ft.DataCell(ft.Text(emp["apellido"])),
                        ft.DataCell(
                            ft.Row([
                                ft.ElevatedButton("Ver",
                                                  on_click=lambda e: on_ver_empleado(e, emp)),
                                ft.ElevatedButton("Eliminar",
                                                  on_click=lambda e: on_eliminar_empleado(e, emp["dni"]))
                            ])
                        )
                    ]
                )
            )
        page.update()

    def eliminar_empleado(dni):
        """Elimina un empleado desde la tabla.

        Args:
            dni (str): DNI del empleado a eliminar.
        """
        exito, msg = controlador.eliminar_empleado(dni)
        mensaje.value = msg
        if exito:
            actualizar_tabla()
        page.update()

    def ver_empleado(emp):
        """Muestra los datos de un empleado seleccionado en el formulario.

        Args:
            emp (dict): Diccionario con los datos del empleado.
        """
        nombre.value = emp["nombre"]
        segundo_nombre.value = emp["segundo_nombre"]
        apellido.value = emp["apellido"]
        segundo_apellido.value = emp["segundo_apellido"]
        dni.value = emp["dni"]
        cuit.value = emp["cuit"]
        fecha_nacimiento.value = emp["fecha_nacimiento"]
        fecha_ingreso.value = emp["fecha_ingreso"]
        fecha_egreso.value = emp["fecha_egreso"]
        sexo.value = emp["sexo"]

        direcciones.clear()
        direcciones_container.controls.clear()
        for d in emp["direcciones"]:
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

        telefonos.clear()
        telefonos_container.controls.clear()
        for t in emp["telefonos"]:
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

        cargos.clear()
        cargos_container.controls.clear()
        for c in emp["cargos"]:
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

        jornadas.clear()
        jornadas_container.controls.clear()
        for j in emp["jornadas"]:
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
                ver_empleado(empleado)
                calle.value = altura.value = localidad.value = provincia.value = codigo_postal.value = ""
            page.update()

        page.add(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )

    def eliminar_direccion(direccion_id):
        """Elimina una dirección asociada a un empleado.

        Args:
            direccion_id (int): ID de la dirección a eliminar.
        """
        exito, msg = controlador.eliminar_direccion(direccion_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            ver_empleado(empleado)
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
                ver_empleado(empleado)
                telefono.value = tipo.value = ""
            page.update()

        page.add(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )

    def eliminar_telefono(telefono_id):
        """Elimina un teléfono asociado a un empleado.

        Args:
            telefono_id (int): ID del teléfono a eliminar.
        """
        exito, msg = controlador.eliminar_telefono(telefono_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            ver_empleado(empleado)
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
                ver_empleado(empleado)
                cargo.value = salario.value = fecha_inicio.value = fecha_fin.value = ""
            page.update()

        page.add(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )

    def eliminar_cargo(cargo_id):
        """Elimina un cargo asociado a un empleado.

        Args:
            cargo_id (int): ID del cargo a eliminar.
        """
        exito, msg = controlador.eliminar_cargo(cargo_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            ver_empleado(empleado)
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
                ver_empleado(empleado)
                fecha.value = hora_de_entrada.value = hora_de_salida.value = ""
            page.update()

        page.add(
            ft.Row([
                ft.ElevatedButton("Guardar Modificación", on_click=guardar_modificacion)
            ])
        )

    def eliminar_jornada(jornada_id):
        """Elimina una jornada laboral asociada a un empleado.

        Args:
            jornada_id (int): ID de la jornada a eliminar.
        """
        exito, msg = controlador.eliminar_jornada(jornada_id)
        mensaje.value = msg
        if exito:
            empleado = controlador.obtener_empleado(dni.value)
            ver_empleado(empleado)
        page.update()

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

    # Botones de acción
    btn_guardar = ft.ElevatedButton("Guardar", on_click=guardar_usuario)
    btn_modificar = ft.ElevatedButton("Modificar", on_click=modificar_usuario)
    btn_eliminar = ft.ElevatedButton("Eliminar", on_click=eliminar_usuario)
    btn_limpiar = ft.ElevatedButton("Limpiar", on_click=lambda e: limpiar_formulario())

    # Organizar todo en la página
    page.add(
        ft.Column([
            ft.Row([
                columna1, columna2, columna3, columna4, columna5,
                ft.Column([btn_guardar, btn_modificar, btn_eliminar, btn_limpiar, mensaje], spacing=10)
            ], spacing=20),
            ft.Text("Lista de Empleados", size=20),
            tabla_empleados
        ])
    )

    # Cargar la tabla al inicio
    actualizar_tabla()

if __name__ == "__main__":
    ft.app(target=main)