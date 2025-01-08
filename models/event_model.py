from database.connection import DatabaseConnection

class EventModel:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS events (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                date DATETIME NOT NULL
            )
        """
        try:
            self.db.execute_query(query)
            print("Tabla 'events' creada o ya existe.")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")

    def create_event(self, name, date):
        query = "INSERT INTO events (name, date) VALUES (%s, %s)"
        params = (name, date)
        try:
            self.db.execute_query(query, params)
            print("Evento creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el evento: {e}")

    def get_events(self):
        query = "SELECT * FROM events"
        try:
            cursor = self.db.execute_query(query)
            events = cursor.fetchall()
            return events
        except Exception as e:
            print(f"Error al obtener los eventos: {e}")
            return []

    def delete_event(self, event_id):
        query = "DELETE FROM events WHERE id = %s"
        params = (event_id,)
        try:
            self.db.execute_query(query, params)
            print("Evento eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el evento: {e}")
