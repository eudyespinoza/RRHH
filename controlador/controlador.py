from modelo.database import Database
from modelo.empleado import Empleado

class Controlador:
    """Clase que implementa la lógica de negocio del ABM de empleados (patrón MVC)."""

    def __init__(self):
        """Inicializa el controlador con una conexión a la base de datos."""
        self.db = Database()

    def agregar_empleado(self, datos):
        """Agrega un nuevo empleado y sus datos asociados.

        Args:
            datos (dict): Diccionario con los datos del empleado y sus listas asociadas.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        try:
            empleado = Empleado(
                datos["dni"], datos["cuit"], datos["nombre"], datos["segundo_nombre"],
                datos["apellido"], datos["segundo_apellido"], datos["fecha_nacimiento"],
                datos["edad"], datos["sexo"], datos["fecha_ingreso"], datos["fecha_egreso"]
            )
            empleado.validar()
            exito, msg, empleado_id = self.db.agregar_empleado(empleado.to_dict())
            if not exito:
                return exito, msg

            for direccion in datos["direcciones"]:
                if any([direccion["calle"], direccion["altura"], direccion["localidad"],
                        direccion["provincia"], direccion["codigo_postal"]]):
                    self.db.agregar_direccion(empleado_id, direccion)

            for telefono in datos["telefonos"]:
                if telefono["telefono"]:
                    self.db.agregar_telefono(empleado_id, telefono["telefono"], telefono["tipo"])

            for cargo in datos["cargos"]:
                if cargo["cargo"]:
                    self.db.agregar_cargo(empleado_id, cargo["cargo"], cargo["salario"],
                                          cargo["fecha_inicio"], cargo.get("fecha_fin"))

            for jornada in datos["jornadas"]:
                if jornada["fecha"] or jornada["hora_de_entrada"] or jornada["hora_de_salida"]:
                    self.db.agregar_jornada(empleado_id, jornada["fecha"], jornada["hora_de_entrada"],
                                            jornada["hora_de_salida"])

            return True, "Empleado y datos asociados agregados con éxito."
        except Exception as e:
            return False, str(e)

    def modificar_empleado(self, dni, datos):
        """Modifica los datos de un empleado existente.

        Args:
            dni (str): DNI del empleado a modificar.
            datos (dict): Nuevos datos del empleado.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        try:
            empleado = Empleado(
                dni, datos["cuit"], datos["nombre"], datos["segundo_nombre"],
                datos["apellido"], datos["segundo_apellido"], datos["fecha_nacimiento"],
                datos["edad"], datos["sexo"], datos["fecha_ingreso"], datos["fecha_egreso"]
            )
            empleado.validar()
            exito, msg = self.db.modificar_empleado(dni, empleado.to_dict())
            return exito, msg
        except Exception as e:
            return False, str(e)

    def eliminar_empleado(self, dni):
        """Elimina un empleado.

        Args:
            dni (str): DNI del empleado a eliminar.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.eliminar_empleado(dni)

    def agregar_direccion(self, empleado_id, direccion):
        """Agrega una dirección a un empleado.

        Args:
            empleado_id (int): ID del empleado.
            direccion (dict): Datos de la dirección.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.agregar_direccion(empleado_id, direccion)

    def modificar_direccion(self, direccion_id, direccion):
        """Modifica una dirección existente.

        Args:
            direccion_id (int): ID de la dirección.
            direccion (dict): Nuevos datos de la dirección.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.modificar_direccion(direccion_id, direccion)

    def eliminar_direccion(self, direccion_id):
        """Elimina una dirección.

        Args:
            direccion_id (int): ID de la dirección.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.eliminar_direccion(direccion_id)

    def agregar_telefono(self, empleado_id, telefono, tipo):
        """Agrega un teléfono a un empleado.

        Args:
            empleado_id (int): ID del empleado.
            telefono (str): Número de teléfono.
            tipo (str): Tipo de teléfono.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.agregar_telefono(empleado_id, telefono, tipo)

    def modificar_telefono(self, telefono_id, telefono, tipo):
        """Modifica un teléfono existente.

        Args:
            telefono_id (int): ID del teléfono.
            telefono (str): Nuevo número de teléfono.
            tipo (str): Nuevo tipo de teléfono.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.modificar_telefono(telefono_id, telefono, tipo)

    def eliminar_telefono(self, telefono_id):
        """Elimina un teléfono.

        Args:
            telefono_id (int): ID del teléfono.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.eliminar_telefono(telefono_id)

    def agregar_cargo(self, empleado_id, cargo, salario, fecha_inicio, fecha_fin=None):
        """Agrega un cargo a un empleado.

        Args:
            empleado_id (int): ID del empleado.
            cargo (str): Nombre del cargo.
            salario (str): Salario.
            fecha_inicio (str): Fecha de inicio.
            fecha_fin (str, optional): Fecha de fin.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.agregar_cargo(empleado_id, cargo, salario, fecha_inicio, fecha_fin)

    def modificar_cargo(self, cargo_id, cargo, salario, fecha_inicio, fecha_fin):
        """Modifica un cargo existente.

        Args:
            cargo_id (int): ID del cargo.
            cargo (str): Nuevo nombre del cargo.
            salario (str): Nuevo salario.
            fecha_inicio (str): Nueva fecha de inicio.
            fecha_fin (str): Nueva fecha de fin.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.modificar_cargo(cargo_id, cargo, salario, fecha_inicio, fecha_fin)

    def eliminar_cargo(self, cargo_id):
        """Elimina un cargo.

        Args:
            cargo_id (int): ID del cargo.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.eliminar_cargo(cargo_id)

    def agregar_jornada(self, empleado_id, fecha, hora_de_entrada, hora_de_salida):
        """Agrega una jornada laboral a un empleado.

        Args:
            empleado_id (int): ID del empleado.
            fecha (str): Fecha de la jornada.
            hora_de_entrada (str): Hora de entrada.
            hora_de_salida (str): Hora de salida.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.agregar_jornada(empleado_id, fecha, hora_de_entrada, hora_de_salida)

    def modificar_jornada(self, jornada_id, fecha, hora_de_entrada, hora_de_salida):
        """Modifica una jornada laboral existente.

        Args:
            jornada_id (int): ID de la jornada.
            fecha (str): Nueva fecha.
            hora_de_entrada (str): Nueva hora de entrada.
            hora_de_salida (str): Nueva hora de salida.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.modificar_jornada(jornada_id, fecha, hora_de_entrada, hora_de_salida)

    def eliminar_jornada(self, jornada_id):
        """Elimina una jornada laboral.

        Args:
            jornada_id (int): ID de la jornada.

        Returns:
            tuple: (bool, str) Éxito y mensaje.
        """
        return self.db.eliminar_jornada(jornada_id)

    def obtener_empleado(self, dni):
        """Obtiene un empleado por su DNI.

        Args:
            dni (str): DNI del empleado.

        Returns:
            dict: Datos del empleado.
        """
        return self.db.obtener_empleado(dni)

    def listar_empleados(self):
        """Lista todos los empleados.

        Returns:
            list: Lista de empleados.
        """
        return self.db.listar_empleados()
