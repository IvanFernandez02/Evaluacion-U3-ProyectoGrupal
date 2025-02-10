from database import connect_db
import tkinter.messagebox as messagebox


def create_ejercicio(nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "INSERT INTO EJERCICIOS (nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina) VALUES (%s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, (nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina))
        conn.commit()
        messagebox.showinfo("Éxito", "Ejercicio creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el ejercicio: {e}")
    finally:
        cursor.close()
        conn.close()


def update_ejercicio(idEjercicio, nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "UPDATE EJERCICIOS SET nombreEjercicio=%s, descripcion=%s, grupoMuscular=%s, tiempoDescanso=%s, nroSeries=%s, idRutina=%s WHERE idEjercicio=%s"
    try:
        cursor.execute(sql, (nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina, idEjercicio))
        conn.commit()
        messagebox.showinfo("Éxito", "Ejercicio actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el ejercicio: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_ejercicio(idEjercicio):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "DELETE FROM EJERCICIOS WHERE idEjercicio=%s"
    try:
        cursor.execute(sql, (idEjercicio,))
        conn.commit()
        messagebox.showinfo("Éxito", "Ejercicio eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el ejercicio: {e}")
    finally:
        cursor.close()
        conn.close() 