import mysql.connector
from mysql.connector import Error
from models.event_model import EventModel

class EventController:
    def __init__(self, host='localhost', user='root', password='', database='calendario'):
        # Configurar la conexión a la base de datos MySQL
        self.db_config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def _connect_db(self):
        """
        Establece una conexión con la base de datos MySQL.
        """
        try:
            conn = mysql.connector.connect(**self.db_config)
            if conn.is_connected():
                return conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        return None

    def add_event(self, name, date):
        """
        Agrega un evento a la base de datos MySQL.
        """
        conn = self._connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                event = EventModel(name=name, date=date)
                query = "INSERT INTO events (name, date) VALUES (%s, %s)"
                cursor.execute(query, (event.name, event.date))
                conn.commit()
            except Error as e:
                print(f"Error al agregar el evento: {e}")
            finally:
                cursor.close()
                conn.close()

    def get_events(self):
        """
        Obtiene todos los eventos de la base de datos MySQL.
        """
        conn = self._connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM events"
                cursor.execute(query)
                events = cursor.fetchall()
                return [EventModel(name=row[1], date=row[2]) for row in events]
            except Error as e:
                print(f"Error al obtener los eventos: {e}")
            finally:
                cursor.close()
                conn.close()
        return []

    def remove_event(self, event_id):
        """
        Elimina un evento de la base de datos MySQL.
        """
        conn = self._connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM events WHERE id = %s"
                cursor.execute(query, (event_id,))
                conn.commit()
            except Error as e:
                print(f"Error al eliminar el evento: {e}")
            finally:
                cursor.close()
                conn.close()

    def update_event(self, event_id, new_name, new_date):
        """
        Actualiza los detalles de un evento en la base de datos.
        """
        try:
            conn = self._connect_db()
            cursor = conn.cursor()

            # Actualizar evento por ID
            cursor.execute("UPDATE eventos SET name=%s, date=%s WHERE id=%s", (new_name, new_date, event_id))
            conn.commit()

            print(f"Evento con ID {event_id} actualizado con éxito.")
        except Exception as e:
            print(f"Error al actualizar evento: {e}")
        finally:
            cursor.close()
            conn.close()
