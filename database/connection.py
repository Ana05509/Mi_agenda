import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host='localhost', database='MiAgenda', user='root', password='088266619Da.di'):
        self.db_config = {
            'host': host,
            'database': database,
            'user': user,
            'password': password
        }
        self.connection = None
        self.connect()

    def connect(self):
        """
        Establece una conexión con la base de datos MySQL.
        """
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos MySQL.")
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            self.connection = None

    def get_connection(self):
        """
        Devuelve la conexión a la base de datos.
        """
        if self.connection is None or not self.connection.is_connected():
            self.connect()
        return self.connection

    def close_connection(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta en la base de datos.
        """
        conn = self.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
            finally:
                cursor.close()
        return None
