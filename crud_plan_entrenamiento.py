from database import connect_db
import tkinter.messagebox as messagebox


def create_plan(dia, duracion, descripcion, cliente):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "INSERT INTO PLAN_ENTRENAMIENTO (dia, duracion, descripcion, cliente) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (dia, duracion, descripcion, cliente))
        conn.commit()
        messagebox.showinfo("Éxito", "Plan creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el plan: {e}")
    finally:
        cursor.close()
        conn.close()


def update_plan(idPlan, dia, duracion, descripcion, cliente):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "UPDATE PLAN_ENTRENAMIENTO SET dia=%s, duracion=%s, descripcion=%s, cliente=%s WHERE idPlan=%s"
    try:
        cursor.execute(sql, (dia, duracion, descripcion, cliente, idPlan))
        conn.commit()
        messagebox.showinfo("Éxito", "Plan actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el plan: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_plan(idPlan):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "DELETE FROM PLAN_ENTRENAMIENTO WHERE idPlan=%s"
    try:
        cursor.execute(sql, (idPlan,))
        conn.commit()
        messagebox.showinfo("Éxito", "Plan eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el plan: {e}")
    finally:
        cursor.close()
        conn.close() 