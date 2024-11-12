import mysql.connector
from mysql.connector import errorcode

class BaseDeDatos:
    def __init__(self, host="localhost", user="root", password="12345678", database="club_deportivo"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def crear_tablas(self):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(20) NOT NULL,
                    password VARCHAR(15) NOT NULL,
                    rol VARCHAR(20) NOT NULL
                  )''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS cuotas (
                    tipo VARCHAR(255) NOT NULL,
                    deporte VARCHAR(255),
                    monto FLOAT NOT NULL,
                    PRIMARY KEY (tipo, deporte)
                )''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
                    nombre VARCHAR(30) NOT NULL,
                    dni VARCHAR(8) NOT NULL,
                    PRIMARY KEY (dni)
                )''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS pagos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    socio_dni VARCHAR(8),
                    dni VARCHAR(8),
                    tipo VARCHAR(255) NOT NULL,
                    deporte VARCHAR(255) NOT NULL,
                    FOREIGN KEY (socio_dni) REFERENCES socios(dni) ON DELETE CASCADE,
                    FOREIGN KEY (tipo, deporte) REFERENCES cuotas(tipo, deporte) ON DELETE CASCADE
                )''')

                conn.commit()

    def insertar_usuario(self, nombre, password, rol):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO usuarios (nombre, password, rol) VALUES (%s, %s, %s)", (nombre, password, rol))
                conn.commit()

    def insertar_socio(self, nombre, dni):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO socios (nombre, dni) VALUES (%s, %s)", (nombre, dni))
                conn.commit()
            

    def obtener_usuario(self, nombre):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM usuarios WHERE nombre = %s", (nombre,))
                return cursor.fetchone()
            
    def obtener_socio(self, dni):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM socios WHERE dni = %s", (dni,))
                return cursor.fetchone()

    def insertar_cuota(self, tipo, deporte, monto):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO cuotas (tipo, deporte, monto) VALUES (%s, %s, %s)", 
                               (tipo, deporte, monto))
                conn.commit()

    def obtener_cuotas(self):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM cuotas")
                return cursor.fetchall()
    
    def obtener_cuota(self, tipo, deporte):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM cuotas WHERE tipo = %s AND deporte = %s", (tipo, deporte))
                return cursor.fetchone()

    def insertar_pago_socio(self, socio_dni, tipo, deporte):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO pagos (socio_dni, tipo, deporte) VALUES (%s, %s, %s)", (socio_dni, tipo, deporte))
                conn.commit()

    def insertar_pago_no_socio(self, dni, tipo, deporte):
        with self.conectar() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO pagos (dni, tipo, deporte) VALUES (%s, %s, %s)", (dni, tipo, deporte))
                conn.commit()
