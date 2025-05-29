from modelo.database import Database
from modelo.empleado import Empleado

class Controlador:
    """Clase que implementa la lógica de negocio del ABM de empleados (patrón MVC)."""

    def __init__(self):
        """Inicializa el controlador con una conexión a la base de datos."""
        self.db = Database()

    def agregar_empleado(self, datos):
        """Agrega un nuevo empleado y sus datos asociados."""
        try:
            # Iniciar transacción
            self.db.create_connection()

            empleado = Empleado(
                datos["dni"], datos["cuit"], datos["nombre"], datos["segundo_nombre"],
                datos["apellido"], datos["segundo_apellido"], datos["fecha_nacimiento"],
                datos["edad"], datos["sexo"], datos["fecha_ingreso"], datos["fecha_egreso"]
            )
            empleado.validar()
            exito, msg, empleado_id = self.db.agregar_empleado(empleado.to_dict())
            if not exito:
                self.db.rollback()
                return exito, msg, None

            # Agregar direcciones
            for direccion in datos.get("direcciones", []):
                if any([direccion.get("calle"), direccion.get("altura"), direccion.get("localidad"),
                        direccion.get("provincia"), direccion.get("codigo_postal")]):
                    exito_d, msg_d, direccion_id = self.db.agregar_direccion(empleado_id, direccion)
                    if not exito_d:
                        self.db.rollback()
                        return False, msg_d, None
                    if direccion_id:
                        direccion['id'] = direccion_id

            # Agregar teléfonos
            for telefono in datos.get("telefonos", []):
                if telefono.get("telefono"):
                    exito_t, msg_t, telefono_id = self.db.agregar_telefono(empleado_id, telefono["telefono"],
                                                                           telefono["tipo"])
                    if not exito_t:
                        self.db.rollback()
                        return False, msg_t, None
                    if telefono_id:
                        telefono['id'] = telefono_id

            # Agregar cargos
            for cargo in datos.get("cargos", []):
                if cargo.get("cargo"):
                    exito_c, msg_c, cargo_id = self.db.agregar_cargo(empleado_id, cargo["cargo"], cargo["salario"],
                                                                     cargo["fecha_inicio"], cargo.get("fecha_fin"))
                    if not exito_c:
                        self.db.rollback()
                        return False, msg_c, None
                    if cargo_id:
                        cargo['id'] = cargo_id

            # Agregar jornadas
            for jornada in datos.get("jornadas", []):
                if any([jornada.get("fecha"), jornada.get("hora_de_entrada"), jornada.get("hora_de_salida")]):
                    exito_j, msg_j, jornada_id = self.db.agregar_jornada(empleado_id, jornada["fecha"],
                                                                         jornada["hora_de_entrada"],
                                                                         jornada["hora_de_salida"])
                    if not exito_j:
                        self.db.rollback()
                        return False, msg_j, None
                    if jornada_id:
                        jornada['id'] = jornada_id

            # Confirmar transacción
            self.db.commit()
            return True, "Empleado y datos asociados agregados con éxito.", empleado_id
        except Exception as e:
            self.db.rollback()
            return False, f"Error al agregar empleado: {str(e)}", None
        finally:
            self.db.close_connection()

    def modificar_empleado(self, dni, datos):
        """Modifica los datos de un empleado existente."""
        try:
            self.db.create_connection()
            empleado = Empleado(
                dni, datos["cuit"], datos["nombre"], datos["segundo_nombre"],
                datos["apellido"], datos["segundo_apellido"], datos["fecha_nacimiento"],
                datos["edad"], datos["sexo"], datos["fecha_ingreso"], datos["fecha_egreso"]
            )
            empleado.validar()
            exito, msg = self.db.modificar_empleado(dni, empleado.to_dict())
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def eliminar_empleado(self, dni):
        """Elimina un empleado."""
        try:
            self.db.create_connection()
            exito, msg = self.db.eliminar_empleado(dni)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def agregar_direccion(self, empleado_id, direccion):
        """Agrega una dirección a un empleado."""
        try:
            self.db.create_connection()
            exito, msg, direccion_id = self.db.agregar_direccion(empleado_id, direccion)
            self.db.commit()
            return exito, msg, direccion_id
        except Exception as e:
            self.db.rollback()
            return False, str(e), None
        finally:
            self.db.close_connection()

    def modificar_direccion(self, direccion_id, direccion):
        """Modifica una dirección existente."""
        try:
            self.db.create_connection()
            exito, msg = self.db.modificar_direccion(direccion_id, direccion)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def eliminar_direccion(self, direccion_id):
        """Elimina una dirección."""
        try:
            self.db.create_connection()
            exito, msg = self.db.eliminar_direccion(direccion_id)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def agregar_telefono(self, empleado_id, telefono, tipo):
        """Agrega un teléfono a un empleado."""
        try:
            self.db.create_connection()
            exito, msg, telefono_id = self.db.agregar_telefono(empleado_id, telefono, tipo)
            self.db.commit()
            return exito, msg, telefono_id
        except Exception as e:
            self.db.rollback()
            return False, str(e), None
        finally:
            self.db.close_connection()

    def modificar_telefono(self, telefono_id, telefono, tipo):
        """Modifica un teléfono existente."""
        try:
            self.db.create_connection()
            exito, msg = self.db.modificar_telefono(telefono_id, telefono, tipo)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def eliminar_telefono(self, telefono_id):
        """Elimina un teléfono."""
        try:
            self.db.create_connection()
            exito, msg = self.db.eliminar_telefono(telefono_id)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def agregar_cargo(self, empleado_id, cargo, salario, fecha_inicio, fecha_fin=None):
        """Agrega un cargo a un empleado."""
        try:
            self.db.create_connection()
            exito, msg, cargo_id = self.db.agregar_cargo(empleado_id, cargo, salario, fecha_inicio, fecha_fin)
            self.db.commit()
            return exito, msg, cargo_id
        except Exception as e:
            self.db.rollback()
            return False, str(e), None
        finally:
            self.db.close_connection()

    def modificar_cargo(self, cargo_id, cargo, salario, fecha_inicio, fecha_fin):
        """Modifica un cargo existente."""
        try:
            self.db.create_connection()
            exito, msg = self.db.modificar_cargo(cargo_id, cargo, salario, fecha_inicio, fecha_fin)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def eliminar_cargo(self, cargo_id):
        """Elimina un cargo."""
        try:
            self.db.create_connection()
            exito, msg = self.db.eliminar_cargo(cargo_id)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def agregar_jornada(self, empleado_id, fecha, hora_de_entrada, hora_de_salida):
        """Agrega una jornada laboral a un empleado."""
        try:
            self.db.create_connection()
            exito, msg, jornada_id = self.db.agregar_jornada(empleado_id, fecha, hora_de_entrada, hora_de_salida)
            self.db.commit()
            return exito, msg, jornada_id
        except Exception as e:
            self.db.rollback()
            return False, str(e), None
        finally:
            self.db.close_connection()

    def modificar_jornada(self, jornada_id, fecha, hora_de_entrada, hora_de_salida):
        """Modifica una jornada laboral existente."""
        try:
            self.db.create_connection()
            exito, msg = self.db.modificar_jornada(jornada_id, fecha, hora_de_entrada, hora_de_salida)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def eliminar_jornada(self, jornada_id):
        """Elimina una jornada laboral."""
        try:
            self.db.create_connection()
            exito, msg = self.db.eliminar_jornada(jornada_id)
            self.db.commit()
            return exito, msg
        except Exception as e:
            self.db.rollback()
            return False, str(e)
        finally:
            self.db.close_connection()

    def obtener_empleado(self, dni):
        """Obtiene un empleado por su DNI."""
        try:
            self.db.create_connection()
            empleado = self.db.obtener_empleado(dni)
            return empleado
        finally:
            self.db.close_connection()

    def listar_empleados(self):
        """Lista todos los empleados."""
        try:
            self.db.create_connection()
            empleados = self.db.listar_empleados()
            return empleados
        finally:
            self.db.close_connection()