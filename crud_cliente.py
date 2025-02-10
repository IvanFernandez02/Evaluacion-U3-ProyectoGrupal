from database import connect_db
import tkinter.messagebox as messagebox


def create_cliente(cedula, nombres, apellidos, direccion_calle, direccion_numero, objetivo):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = ("INSERT INTO CLIENTE (cedula, nombres, apellidos, direccion_calle, direccion_numero, objetivo) "
           "VALUES (%s, %s, %s, %s, %s, %s)")
    try:
        cursor.execute(sql, (cedula, nombres, apellidos, direccion_calle, direccion_numero, objetivo))
        conn.commit()
        messagebox.showinfo("Éxito", "Cliente creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el cliente: {e}")
    finally:
        cursor.close()
        conn.close()


def update_cliente(cedula, nombres, apellidos, direccion_calle, direccion_numero, objetivo):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = ("UPDATE CLIENTE SET nombres=%s, apellidos=%s, direccion_calle=%s, direccion_numero=%s, objetivo=%s "
           "WHERE cedula=%s")
    try:
        cursor.execute(sql, (nombres, apellidos, direccion_calle, direccion_numero, objetivo, cedula))
        conn.commit()
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el cliente: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_cliente(cedula):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "DELETE FROM CLIENTE WHERE cedula=%s"
    try:
        cursor.execute(sql, (cedula,))
        conn.commit()
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el cliente: {e}")
    finally:
        cursor.close()
        conn.close() 