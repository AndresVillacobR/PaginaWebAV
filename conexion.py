import mysql.connector
from mysql.connector import Error

def create_connection():
    """Establece una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="lenguajedos",
            user="root",
            password=''
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
        else:
            print("No se pudo conectar a la base de datos")
            return None
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None