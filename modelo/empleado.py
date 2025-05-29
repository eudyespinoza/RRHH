import re

class Empleado:
    """Clase que representa un empleado y sus datos asociados."""

    def __init__(self, dni, cuit, nombre, segundo_nombre, apellido, segundo_apellido, fecha_nacimiento,
                 edad, sexo, fecha_ingreso, fecha_egreso, direcciones=None, telefonos=None,
                 cargos=None, jornadas=None):
        """Inicializa un objeto Empleado."""
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
        """Valida los datos del empleado."""
        if not all([self.dni, self.cuit, self.nombre, self.apellido, self.fecha_nacimiento,
                    self.edad, self.sexo, self.fecha_ingreso]):
            raise ValueError("Todos los campos obligatorios deben estar completos.")

        patron = r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
        if not re.match(patron, self.nombre):
            raise ValueError("El nombre solo puede contener caracteres alfanuméricos y espacios/guiones.")

    def to_dict(self):
        """Convierte el empleado a un diccionario."""
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