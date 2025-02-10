import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as messagebox

# AGREGADO: Configuración global para la base de datos
db_host = None
DB_USER = None
DB_PASSWORD = None
DB_DATABASE = None

def set_db_config(host, user, password, database):
    global db_host, DB_USER, DB_PASSWORD, DB_DATABASE
    db_host = host
    DB_USER = user
    DB_PASSWORD = password
    DB_DATABASE = database

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        return conn
    except Error as err:
        messagebox.showerror("Error", f"Error al conectar a la base de datos: {err}")
        return None 