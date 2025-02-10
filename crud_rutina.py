from database import connect_db
import tkinter.messagebox as messagebox


def create_rutina(descripcion, nroEjercicios, nombreRutina, idPlan):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "INSERT INTO RUTINA (descripcion, nroEjercicios, nombreRutina, idPlan) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (descripcion, nroEjercicios, nombreRutina, idPlan))
        conn.commit()
        messagebox.showinfo("Éxito", "Rutina creada correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear la rutina: {e}")
    finally:
        cursor.close()
        conn.close()


def update_rutina(idRutina, descripcion, nroEjercicios, nombreRutina, idPlan):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "UPDATE RUTINA SET descripcion=%s, nroEjercicios=%s, nombreRutina=%s, idPlan=%s WHERE idRutina=%s"
    try:
        cursor.execute(sql, (descripcion, nroEjercicios, nombreRutina, idPlan, idRutina))
        conn.commit()
        messagebox.showinfo("Éxito", "Rutina actualizada correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar la rutina: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_rutina(idRutina):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "DELETE FROM RUTINA WHERE idRutina=%s"
    try:
        cursor.execute(sql, (idRutina,))
        conn.commit()
        messagebox.showinfo("Éxito", "Rutina eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar la rutina: {e}")
    finally:
        cursor.close()
        conn.close() 