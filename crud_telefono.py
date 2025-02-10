from database import connect_db
import tkinter.messagebox as messagebox


def create_telefono(telefono, cliente):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "INSERT INTO TELEFONO (telefono, cliente) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (telefono, cliente))
        conn.commit()
        messagebox.showinfo("Éxito", "Teléfono creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el teléfono: {e}")
    finally:
        cursor.close()
        conn.close()


def update_telefono(idTelefono, telefono, cliente):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "UPDATE TELEFONO SET telefono=%s, cliente=%s WHERE idTelefono=%s"
    try:
        cursor.execute(sql, (telefono, cliente, idTelefono))
        conn.commit()
        messagebox.showinfo("Éxito", "Teléfono actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el teléfono: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_telefono(idTelefono):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "DELETE FROM TELEFONO WHERE idTelefono=%s"
    try:
        cursor.execute(sql, (idTelefono,))
        conn.commit()
        messagebox.showinfo("Éxito", "Teléfono eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el teléfono: {e}")
    finally:
        cursor.close()
        conn.close() 