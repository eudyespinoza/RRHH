import sqlite3
from sqlite3 import Error

class Database:
    """Clase para manejar la conexión y operaciones con la base de datos SQLite3."""

    def __init__(self, db_file="empleados.db"):
        """Inicializa la base de datos y crea las tablas necesarias."""
        self.db_file = db_file
        self.conn = None
        self.create_tables()

    def create_connection(self):
        """Crea o retorna una conexión a la base de datos SQLite3.

        Returns:
            sqlite3.Connection: Conexión a la base de datos.
        """
        try:
            if self.conn is None:
                self.conn = sqlite3.connect(self.db_file)
                self.conn.execute("PRAGMA foreign_keys = ON")  # Habilitar claves foráneas
            return self.conn
        except Error as e:
            raise Exception(f"Error al conectar a la base de datos: {e}")

    def commit(self):
        """Confirma los cambios en la base de datos."""
        if self.conn:
            self.conn.commit()

    def rollback(self):
        """Deshace los cambios en la base de datos."""
        if self.conn:
            self.conn.rollback()

    def create_tables(self):
        """Crea las tablas necesarias en la base de datos."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dni TEXT NOT NULL UNIQUE,
                    cuit TEXT NOT NULL,
                    nombre TEXT NOT NULL,
                    segundo_nombre TEXT,
                    apellido TEXT NOT NULL,
                    segundo_apellido TEXT,
                    fecha_nacimiento TEXT NOT NULL,
                    edad INTEGER NOT NULL,
                    sexo TEXT NOT NULL,
                    fecha_ingreso TEXT NOT NULL,
                    fecha_egreso TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS direcciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    empleado_id INTEGER NOT NULL,
                    calle TEXT,
                    altura TEXT,
                    localidad TEXT,
                    provincia TEXT,
                    codigo_postal TEXT,
                    FOREIGN KEY (empleado_id) REFERENCES empleados (id) ON DELETE CASCADE
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS telefonos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    empleado_id INTEGER NOT NULL,
                    telefono TEXT NOT NULL,
                    tipo TEXT,
                    FOREIGN KEY (empleado_id) REFERENCES empleados (id) ON DELETE CASCADE
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cargos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    empleado_id INTEGER NOT NULL,
                    cargo TEXT NOT NULL,
                    salario TEXT,
                    fecha_inicio TEXT NOT NULL,
                    fecha_fin TEXT,
                    FOREIGN KEY (empleado_id) REFERENCES empleados (id) ON DELETE CASCADE
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS jornadas_laborales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    empleado_id INTEGER NOT NULL,
                    fecha TEXT NOT NULL,
                    hora_de_entrada TEXT,
                    hora_de_salida TEXT,
                    FOREIGN KEY (empleado_id) REFERENCES empleados (id) ON DELETE CASCADE
                )
            ''')

            conn.commit()
        except Error as e:
            raise Exception(f"Error al crear las tablas: {e}")

    def close_connection(self):
        """Cierra la conexión a la base de datos."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def agregar_empleado(self, empleado):
        """Agrega un nuevo empleado a la base de datos."""
        sql = '''INSERT INTO empleados (dni, cuit, nombre, segundo_nombre, apellido, segundo_apellido, 
                 fecha_nacimiento, edad, sexo, fecha_ingreso, fecha_egreso) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (
                empleado['dni'], empleado['cuit'], empleado['nombre'], empleado['segundo_nombre'],
                empleado['apellido'], empleado['segundo_apellido'], empleado['fecha_nacimiento'],
                empleado['edad'], empleado['sexo'], empleado['fecha_ingreso'], empleado['fecha_egreso']
            ))
            empleado_id = cursor.lastrowid
            return True, "Empleado agregado con éxito.", empleado_id
        except Error as e:
            return False, f"Error al agregar empleado: {e}", None

    def modificar_empleado(self, dni, datos):
        """Modifica los datos de un empleado existente."""
        sql = '''UPDATE empleados SET cuit = ?, nombre = ?, segundo_nombre = ?, apellido = ?, 
                 segundo_apellido = ?, fecha_nacimiento = ?, edad = ?, sexo = ?, 
                 fecha_ingreso = ?, fecha_egreso = ? WHERE dni = ?'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (
                datos['cuit'], datos['nombre'], datos['segundo_nombre'], datos['apellido'],
                datos['segundo_apellido'], datos['fecha_nacimiento'], datos['edad'], datos['sexo'],
                datos['fecha_ingreso'], datos['fecha_egreso'], dni
            ))
            return True, "Empleado modificado con éxito."
        except Error as e:
            return False, f"Error al modificar empleado: {e}"
        finally:
            self.commit()

    def eliminar_empleado(self, dni):
        """Elimina un empleado de la base de datos."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM empleados WHERE dni = ?", (dni,))
            return True, "Empleado eliminado con éxito."
        except Error as e:
            return False, f"Error al eliminar empleado: {e}"
        finally:
            self.commit()

    def agregar_direccion(self, empleado_id, direccion):
        """Agrega una dirección asociada a un empleado."""
        sql = '''INSERT INTO direcciones (empleado_id, calle, altura, localidad, provincia, codigo_postal) 
                 VALUES (?, ?, ?, ?, ?, ?)'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (
                empleado_id, direccion['calle'], direccion['altura'], direccion['localidad'],
                direccion['provincia'], direccion['codigo_postal']
            ))
            direccion_id = cursor.lastrowid
            return True, "Dirección agregada con éxito.", direccion_id
        except Error as e:
            return False, f"Error al agregar dirección: {e}", None

    def modificar_direccion(self, direccion_id, direccion):
        """Modifica una dirección existente."""
        sql = '''UPDATE direcciones SET calle = ?, altura = ?, localidad = ?, provincia = ?, 
                 codigo_postal = ? WHERE id = ?'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (
                direccion['calle'], direccion['altura'], direccion['localidad'],
                direccion['provincia'], direccion['codigo_postal'], direccion_id
            ))
            return True, "Dirección modificada con éxito."
        except Error as e:
            return False, f"Error al modificar dirección: {e}"

    def eliminar_direccion(self, direccion_id):
        """Elimina una dirección de la base de datos."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM direcciones WHERE id = ?", (direccion_id,))
            return True, "Dirección eliminada con éxito."
        except Error as e:
            return False, f"Error al eliminar dirección: {e}"

    def agregar_telefono(self, empleado_id, telefono, tipo):
        """Agrega un teléfono asociado a un empleado."""
        sql = '''INSERT INTO telefonos (empleado_id, telefono, tipo) VALUES (?, ?, ?)'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (empleado_id, telefono, tipo))
            telefono_id = cursor.lastrowid
            return True, "Teléfono agregado con éxito.", telefono_id
        except Error as e:
            return False, f"Error al agregar teléfono: {e}", None

    def modificar_telefono(self, telefono_id, telefono, tipo):
        """Modifica un teléfono existente."""
        sql = '''UPDATE telefonos SET telefono = ?, tipo = ? WHERE id = ?'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (telefono, tipo, telefono_id))
            return True, "Teléfono modificado con éxito."
        except Error as e:
            return False, f"Error al modificar teléfono: {e}"

    def eliminar_telefono(self, telefono_id):
        """Elimina un teléfono de la base de datos."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM telefonos WHERE id = ?", (telefono_id,))
            return True, "Teléfono eliminado con éxito."
        except Error as e:
            return False, f"Error al eliminar teléfono: {e}"

    def agregar_cargo(self, empleado_id, cargo, salario, fecha_inicio, fecha_fin=None):
        """Agrega un cargo asociado a un empleado."""
        sql = '''INSERT INTO cargos (empleado_id, cargo, salario, fecha_inicio, fecha_fin) 
                 VALUES (?, ?, ?, ?, ?)'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (empleado_id, cargo, salario, fecha_inicio, fecha_fin))
            cargo_id = cursor.lastrowid
            return True, "Cargo agregado con éxito.", cargo_id
        except Error as e:
            return False, f"Error al agregar cargo: {e}", None

    def modificar_cargo(self, cargo_id, cargo, salario, fecha_inicio, fecha_fin):
        """Modifica un cargo existente."""
        sql = '''UPDATE cargos SET cargo = ?, salario = ?, fecha_inicio = ?, fecha_fin = ? WHERE id = ?'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (cargo, salario, fecha_inicio, fecha_fin, cargo_id))
            return True, "Cargo modificado con éxito."
        except Error as e:
            return False, f"Error al modificar cargo: {e}"

    def eliminar_cargo(self, cargo_id):
        """Elimina un cargo de la base de datos."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cargos WHERE id = ?", (cargo_id,))
            return True, "Cargo eliminado con éxito."
        except Error as e:
            return False, f"Error al eliminar cargo: {e}"

    def agregar_jornada(self, empleado_id, fecha, hora_de_entrada, hora_de_salida):
        """Agrega una jornada laboral asociada a un empleado."""
        sql = '''INSERT INTO jornadas_laborales (empleado_id, fecha, hora_de_entrada, hora_de_salida) 
                 VALUES (?, ?, ?, ?)'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (empleado_id, fecha, hora_de_entrada, hora_de_salida))
            jornada_id = cursor.lastrowid
            return True, "Jornada laboral agregada con éxito.", jornada_id
        except Error as e:
            return False, f"Error al agregar jornada laboral: {e}", None

    def modificar_jornada(self, jornada_id, fecha, hora_de_entrada, hora_de_salida):
        """Modifica una jornada laboral existente."""
        sql = '''UPDATE jornadas_laborales SET fecha = ?, hora_de_entrada = ?, hora_de_salida = ? 
                 WHERE id = ?'''
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (fecha, hora_de_entrada, hora_de_salida, jornada_id))
            return True, "Jornada laboral modificada con éxito."
        except Error as e:
            return False, f"Error al modificar jornada laboral: {e}"

    def eliminar_jornada(self, jornada_id):
        """Elimina una jornada laboral de la base de datos."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM jornadas_laborales WHERE id = ?", (jornada_id,))
            return True, "Jornada laboral eliminada con éxito."
        except Error as e:
            return False, f"Error al eliminar jornada laboral: {e}"

    def obtener_empleado(self, dni):
        """Obtiene los datos de un empleado por su DNI."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados WHERE dni = ?", (dni,))
            empleado = cursor.fetchone()
            if empleado:
                empleado_dict = dict(zip([column[0] for column in cursor.description], empleado))
                print(f"Empleado encontrado: {empleado_dict}")

                # Recuperar direcciones
                cursor.execute("SELECT * FROM direcciones WHERE empleado_id = ?", (empleado_dict['id'],))
                empleado_dict['direcciones'] = [dict(zip([column[0] for column in cursor.description], d)) for d in cursor.fetchall()]
                print(f"Direcciones recuperadas: {empleado_dict['direcciones']}")

                # Recuperar teléfonos
                cursor.execute("SELECT * FROM telefonos WHERE empleado_id = ?", (empleado_dict['id'],))
                empleado_dict['telefonos'] = [dict(zip([column[0] for column in cursor.description], t)) for t in cursor.fetchall()]
                print(f"Teléfonos recuperados: {empleado_dict['telefonos']}")

                # Recuperar cargos
                cursor.execute("SELECT * FROM cargos WHERE empleado_id = ?", (empleado_dict['id'],))
                empleado_dict['cargos'] = [dict(zip([column[0] for column in cursor.description], c)) for c in cursor.fetchall()]
                print(f"Cargos recuperados: {empleado_dict['cargos']}")

                # Recuperar jornadas
                cursor.execute("SELECT * FROM jornadas_laborales WHERE empleado_id = ?", (empleado_dict['id'],))
                empleado_dict['jornadas'] = [dict(zip([column[0] for column in cursor.description], j)) for j in cursor.fetchall()]
                print(f"Jornadas recuperadas: {empleado_dict['jornadas']}")

                return empleado_dict
            return None
        except Error as e:
            print(f"Error al obtener empleado: {e}")
            raise Exception(f"Error al obtener empleado: {e}")

    def listar_empleados(self):
        """Lista todos los empleados registrados."""
        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados")
            empleados = cursor.fetchall()
            result = []
            for emp in empleados:
                emp_dict = dict(zip([column[0] for column in cursor.description], emp))
                cursor.execute("SELECT * FROM direcciones WHERE empleado_id = ?", (emp_dict['id'],))
                emp_dict['direcciones'] = [dict(zip([column[0] for column in cursor.description], d)) for d in cursor.fetchall()]
                cursor.execute("SELECT * FROM telefonos WHERE empleado_id = ?", (emp_dict['id'],))
                emp_dict['telefonos'] = [dict(zip([column[0] for column in cursor.description], t)) for t in cursor.fetchall()]
                cursor.execute("SELECT * FROM cargos WHERE empleado_id = ?", (emp_dict['id'],))
                emp_dict['cargos'] = [dict(zip([column[0] for column in cursor.description], c)) for c in cursor.fetchall()]
                cursor.execute("SELECT * FROM jornadas_laborales WHERE empleado_id = ?", (emp_dict['id'],))
                emp_dict['jornadas'] = [dict(zip([column[0] for column in cursor.description], j)) for j in cursor.fetchall()]
                result.append(emp_dict)
            return result
        except Error as e:
            raise Exception(f"Error al listar empleados: {e}")