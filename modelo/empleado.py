import re

class Empleado:
    """Clase que representa un empleado y sus datos asociados."""

    def __init__(self, dni, cuit, nombre, segundo_nombre, apellido, segundo_apellido, fecha_nacimiento,
                 edad, sexo, fecha_ingreso, fecha_egreso, direcciones=None, telefonos=None,
                 cargos=None, jornadas=None):
        """Inicializa un objeto Empleado.

        Args:
            dni (str): DNI del empleado.
            cuit (str): CUIT del empleado.
            nombre (str): Nombre del empleado.
            segundo_nombre (str, optional): Segundo nombre.
            apellido (str): Apellido del empleado.
            segundo_apellido (str, optional): Segundo apellido.
            fecha_nacimiento (str): Fecha de nacimiento.
            edad (str): Edad del empleado.
            sexo (str): Sexo del empleado.
            fecha_ingreso (str): Fecha de ingreso.
            fecha_egreso (str, optional): Fecha de egreso.
            direcciones (list, optional): Lista de direcciones.
            telefonos (list, optional): Lista de teléfonos.
            cargos (list, optional): Lista de cargos.
            jornadas (list, optional): Lista de jornadas laborales.
        """
        self.dni = dni
        self.cuit = cuit
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre or ''
        self.apellido = apellido
        self.segundo_apellido = segundo_apellido or ''
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.sexo = sexo
        self.fecha_ingreso = fecha_ingreso
        self.fecha_egreso = fecha_egreso or ''
        self.direcciones = direcciones or []
        self.telefonos = telefonos or []
        self.cargos = cargos or []
        self.jornadas = jornadas or []

    def validar(self):
        """Valida los datos del empleado.

        Raises:
            ValueError: Si faltan datos obligatorios o el nombre no cumple con el formato.
        """
        if not all([self.dni, self.cuit, self.nombre, self.apellido, self.fecha_nacimiento,
                    self.edad, self.sexo, self.fecha_ingreso]):
            raise ValueError("Todos los campos obligatorios deben estar completos.")

        patron = r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
        if not re.match(patron, self.nombre):
            raise ValueError("El nombre solo puede contener caracteres alfanuméricos y espacios/guiones.")

    def to_dict(self):
        """Convierte el empleado a un diccionario.

        Returns:
            dict: Diccionario con los datos del empleado.
        """
        return {
            "dni": self.dni,
            "cuit": self.cuit,
            "nombre": self.nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido": self.apellido,
            "segundo_apellido": self.segundo_apellido,
            "fecha_nacimiento": self.fecha_nacimiento,
            "edad": self.edad,
            "sexo": self.sexo,
            "fecha_ingreso": self.fecha_ingreso,
            "fecha_egreso": self.fecha_egreso
        }