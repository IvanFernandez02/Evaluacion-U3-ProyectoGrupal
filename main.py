import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db, set_db_config
import crud_cliente
import crud_telefono
import crud_plan_entrenamiento
import crud_rutina
import crud_ejercicios

# ====================== FUNCIONES CRUD DEL CLIENTE ======================

def clear_client_fields():
    client_cedula_entry.delete(0, tk.END)
    client_nombres_entry.delete(0, tk.END)
    client_apellidos_entry.delete(0, tk.END)
    client_direccion_calle_entry.delete(0, tk.END)
    client_direccion_numero_entry.delete(0, tk.END)
    client_objetivo_entry.delete(0, tk.END)


def client_create():
    try:
        cedula = client_cedula_entry.get()
        nombres = client_nombres_entry.get()
        apellidos = client_apellidos_entry.get()
        direccion_calle = client_direccion_calle_entry.get()
        direccion_numero = int(client_direccion_numero_entry.get())
        objetivo = client_objetivo_entry.get()
        crud_cliente.create_cliente(cedula, nombres, apellidos, direccion_calle, direccion_numero, objetivo)
    except ValueError:
        messagebox.showerror("Error", "Dirección número debe ser un número.")


def client_update():
    try:
        cedula = client_cedula_entry.get()
        nombres = client_nombres_entry.get()
        apellidos = client_apellidos_entry.get()
        direccion_calle = client_direccion_calle_entry.get()
        direccion_numero = int(client_direccion_numero_entry.get())
        objetivo = client_objetivo_entry.get()
        crud_cliente.update_cliente(cedula, nombres, apellidos, direccion_calle, direccion_numero, objetivo)
    except ValueError:
        messagebox.showerror("Error", "Dirección número debe ser un número.")


def client_delete():
    cedula = client_cedula_entry.get()
    crud_cliente.delete_cliente(cedula)

# ====================== FUNCIONES CRUD DEL TELÉFONO ======================

def clear_telefono_fields():
    tel_id_entry.delete(0, tk.END)
    tel_telefono_entry.delete(0, tk.END)
    tel_cliente_entry.delete(0, tk.END)


def telefono_create():
    telefono = tel_telefono_entry.get()
    cliente = tel_cliente_entry.get()
    crud_telefono.create_telefono(telefono, cliente)


def telefono_update():
    try:
        idTelefono = int(tel_id_entry.get())
        telefono = tel_telefono_entry.get()
        cliente = tel_cliente_entry.get()
        crud_telefono.update_telefono(idTelefono, telefono, cliente)
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")


def telefono_delete():
    try:
        idTelefono = int(tel_id_entry.get())
        crud_telefono.delete_telefono(idTelefono)
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")

# ====================== FUNCIONES CRUD DEL PLAN ENTRENAMIENTO ======================

def clear_plan_fields():
    plan_id_entry.delete(0, tk.END)
    plan_dia_entry.delete(0, tk.END)
    plan_duracion_entry.delete(0, tk.END)
    plan_descripcion_entry.delete(0, tk.END)
    plan_cliente_entry.delete(0, tk.END)


def plan_create():
    dia = plan_dia_entry.get()
    duracion = plan_duracion_entry.get()
    descripcion = plan_descripcion_entry.get()
    cliente = plan_cliente_entry.get()
    crud_plan_entrenamiento.create_plan(dia, duracion, descripcion, cliente)


def plan_update():
    try:
        idPlan = int(plan_id_entry.get())
        dia = plan_dia_entry.get()
        duracion = plan_duracion_entry.get()
        descripcion = plan_descripcion_entry.get()
        cliente = plan_cliente_entry.get()
        crud_plan_entrenamiento.update_plan(idPlan, dia, duracion, descripcion, cliente)
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")


def plan_delete():
    try:
        idPlan = int(plan_id_entry.get())
        crud_plan_entrenamiento.delete_plan(idPlan)
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")

# ====================== FUNCIONES CRUD DE LA RUTINA ======================

def clear_rutina_fields():
    rutina_id_entry.delete(0, tk.END)
    rutina_descripcion_entry.delete(0, tk.END)
    rutina_nroEjercicios_entry.delete(0, tk.END)
    rutina_nombre_entry.delete(0, tk.END)
    rutina_plan_id_entry.delete(0, tk.END)


def rutina_create():
    descripcion = rutina_descripcion_entry.get()
    try:
        nroEjercicios = int(rutina_nroEjercicios_entry.get())
        nombreRutina = rutina_nombre_entry.get()
        idPlan = int(rutina_plan_id_entry.get())
        crud_rutina.create_rutina(descripcion, nroEjercicios, nombreRutina, idPlan)
    except ValueError:
        messagebox.showerror("Error", "Campos numéricos deben ser números.")


def rutina_update():
    try:
        idRutina = int(rutina_id_entry.get())
        descripcion = rutina_descripcion_entry.get()
        nroEjercicios = int(rutina_nroEjercicios_entry.get())
        nombreRutina = rutina_nombre_entry.get()
        idPlan = int(rutina_plan_id_entry.get())
        crud_rutina.update_rutina(idRutina, descripcion, nroEjercicios, nombreRutina, idPlan)
    except ValueError:
        messagebox.showerror("Error", "Campos numéricos deben ser números.")


def rutina_delete():
    try:
        idRutina = int(rutina_id_entry.get())
        crud_rutina.delete_rutina(idRutina)
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")

# ====================== FUNCIONES CRUD DE LOS EJERCICIOS ======================

def clear_ejercicio_fields():
    ejercicio_id_entry.delete(0, tk.END)
    ejercicio_nombre_entry.delete(0, tk.END)
    ejercicio_descripcion_entry.delete(0, tk.END)
    ejercicio_grupo_entry.delete(0, tk.END)
    ejercicio_tiempo_entry.delete(0, tk.END)
    ejercicio_nroSeries_entry.delete(0, tk.END)
    ejercicio_rutina_id_entry.delete(0, tk.END)


def ejercicio_create():
    nombreEjercicio = ejercicio_nombre_entry.get()
    descripcion = ejercicio_descripcion_entry.get()
    grupoMuscular = ejercicio_grupo_entry.get()
    tiempoDescanso = ejercicio_tiempo_entry.get()
    try:
        nroSeries = int(ejercicio_nroSeries_entry.get())
        idRutina = int(ejercicio_rutina_id_entry.get())
        crud_ejercicios.create_ejercicio(nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina)
    except ValueError:
        messagebox.showerror("Error", "Campos numéricos deben ser números.")


def ejercicio_update():
    try:
        idEjercicio = int(ejercicio_id_entry.get())
        nombreEjercicio = ejercicio_nombre_entry.get()
        descripcion = ejercicio_descripcion_entry.get()
        grupoMuscular = ejercicio_grupo_entry.get()
        tiempoDescanso = ejercicio_tiempo_entry.get()
        nroSeries = int(ejercicio_nroSeries_entry.get())
        idRutina = int(ejercicio_rutina_id_entry.get())
        crud_ejercicios.update_ejercicio(idEjercicio, nombreEjercicio, descripcion, grupoMuscular, tiempoDescanso, nroSeries, idRutina)
    except ValueError:
        messagebox.showerror("Error", "Campos numéricos deben ser números.")


def ejercicio_delete():
    try:
        idEjercicio = int(ejercicio_id_entry.get())
        crud_ejercicios.delete_ejercicio(idEjercicio)
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")

# ====================== FUNCIONES PARA MOSTRAR DATOS (REFRESCAR) ======================

def refresh_client_data():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CLIENTE")
    records = cursor.fetchall()
    for row in client_tree.get_children():
        client_tree.delete(row)
    for record in records:
        client_tree.insert("", "end", values=record)
    cursor.close()
    conn.close()


def refresh_telefono_data():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TELEFONO")
    records = cursor.fetchall()
    for row in tel_tree.get_children():
        tel_tree.delete(row)
    for record in records:
        tel_tree.insert("", "end", values=record)
    cursor.close()
    conn.close()


def refresh_plan_data():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PLAN_ENTRENAMIENTO")
    records = cursor.fetchall()
    for row in plan_tree.get_children():
        plan_tree.delete(row)
    for record in records:
        plan_tree.insert("", "end", values=record)
    cursor.close()
    conn.close()


def refresh_rutina_data():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RUTINA")
    records = cursor.fetchall()
    for row in rutina_tree.get_children():
        rutina_tree.delete(row)
    for record in records:
        rutina_tree.insert("", "end", values=record)
    cursor.close()
    conn.close()


def refresh_ejercicio_data():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EJERCICIOS")
    records = cursor.fetchall()
    for row in ejercicio_tree.get_children():
        ejercicio_tree.delete(row)
    for record in records:
        ejercicio_tree.insert("", "end", values=record)
    cursor.close()
    conn.close()

# ====================== FUNCIONES PARA OCULTAR DATOS (LIMPIAR TREEVIEW) ======================

def hide_client_data():
    for row in client_tree.get_children():
        client_tree.delete(row)


def hide_telefono_data():
    for row in tel_tree.get_children():
        tel_tree.delete(row)


def hide_plan_data():
    for row in plan_tree.get_children():
        plan_tree.delete(row)


def hide_rutina_data():
    for row in rutina_tree.get_children():
        rutina_tree.delete(row)


def hide_ejercicio_data():
    for row in ejercicio_tree.get_children():
        ejercicio_tree.delete(row)

# ====================== CONFIGURACIÓN PRINCIPAL (INTERFAZ) ======================

root = tk.Tk()
root.withdraw()  # Oculto la ventana principal inicialmente
root.title("Sistema CRUD MySQL")
root.geometry("900x700")
root.resizable(True, True)

def show_login():
    login_win = tk.Toplevel(root)
    login_win.title("Login de Base de Datos")

    tk.Label(login_win, text="Host:").grid(row=0, column=0, padx=5, pady=5)
    host_entry = tk.Entry(login_win)
    host_entry.insert(tk.END, "localhost")
    host_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(login_win, text="Usuario:").grid(row=1, column=0, padx=5, pady=5)
    user_entry = tk.Entry(login_win)
    user_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(login_win, text="Contraseña:").grid(row=2, column=0, padx=5, pady=5)
    password_entry = tk.Entry(login_win, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(login_win, text="Base de Datos:").grid(row=3, column=0, padx=5, pady=5)
    db_entry = tk.Entry(login_win)
    db_entry.grid(row=3, column=1, padx=5, pady=5)

    def attempt_login():
         host = host_entry.get()
         usuario = user_entry.get()
         contrasena = password_entry.get()
         db_name = db_entry.get()
         set_db_config(host, usuario, contrasena, db_name)
         conn = connect_db()
         if conn is not None:
             conn.close()
             login_win.destroy()
             root.deiconify()  # Muestra la ventana principal
         else:
             messagebox.showerror("Error", "Credenciales inválidas o error en la conexión. Intente nuevamente.")

    tk.Button(login_win, text="Login", command=attempt_login).grid(row=4, column=0, columnspan=2, pady=10)
    login_win.grab_set()
    root.wait_window(login_win)

show_login()

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# --- Pestaña CLIENTE ---
cliente_tab = ttk.Frame(notebook)
notebook.add(cliente_tab, text="Cliente")

client_labels = ["Cédula:", "Nombres:", "Apellidos:", "Dirección Calle:", "Dirección Número:", "Objetivo:"]

tk.Label(cliente_tab, text=client_labels[0]).grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
client_cedula_entry = tk.Entry(cliente_tab)
client_cedula_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(cliente_tab, text=client_labels[1]).grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
client_nombres_entry = tk.Entry(cliente_tab)
client_nombres_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(cliente_tab, text=client_labels[2]).grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
client_apellidos_entry = tk.Entry(cliente_tab)
client_apellidos_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(cliente_tab, text=client_labels[3]).grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
client_direccion_calle_entry = tk.Entry(cliente_tab)
client_direccion_calle_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(cliente_tab, text=client_labels[4]).grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
client_direccion_numero_entry = tk.Entry(cliente_tab)
client_direccion_numero_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(cliente_tab, text=client_labels[5]).grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
client_objetivo_entry = tk.Entry(cliente_tab)
client_objetivo_entry.grid(row=5, column=1, padx=5, pady=5)

client_btn_frame = tk.Frame(cliente_tab)
client_btn_frame.grid(row=6, column=0, columnspan=2, pady=10)

tk.Button(client_btn_frame, text="Crear", bg="green", fg="white", width=12, command=client_create).grid(row=0, column=0, padx=5)
tk.Button(client_btn_frame, text="Actualizar", bg="yellow", fg="black", width=12, command=client_update).grid(row=0, column=1, padx=5)
tk.Button(client_btn_frame, text="Eliminar", bg="red", fg="white", width=12, command=client_delete).grid(row=0, column=2, padx=5)
tk.Button(client_btn_frame, text="Limpiar Campos", bg="blue", fg="white", width=12, command=clear_client_fields).grid(row=0, column=3, padx=5)

# Frame para mostrar la tabla de CLIENTE
client_table_frame = tk.Frame(cliente_tab)
client_table_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
client_tree = ttk.Treeview(client_table_frame, columns=("cedula", "nombres", "apellidos", "direccion_calle", "direccion_numero", "objetivo"), show="headings")
client_tree.heading("cedula", text="Cédula")
client_tree.heading("nombres", text="Nombres")
client_tree.heading("apellidos", text="Apellidos")
client_tree.heading("direccion_calle", text="Calle")
client_tree.heading("direccion_numero", text="Número")
client_tree.heading("objetivo", text="Objetivo")
client_tree.pack(fill="both", expand=True)

tk.Button(cliente_tab, text="Mostrar Datos", bg="gray", fg="white", command=refresh_client_data).grid(row=8, column=0, columnspan=2, pady=5)
tk.Button(cliente_tab, text="Ocultar Datos", bg="black", fg="white", command=hide_client_data).grid(row=9, column=0, columnspan=2, pady=5)

# --- Pestaña TELEFONO ---
telefono_tab = ttk.Frame(notebook)
notebook.add(telefono_tab, text="Teléfono")

tk.Label(telefono_tab, text="ID (para actualizar/eliminar):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
tk.Label(telefono_tab, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
tk.Label(telefono_tab, text="Cliente:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

tel_id_entry = tk.Entry(telefono_tab)
tel_id_entry.grid(row=0, column=1, padx=5, pady=5)

tel_telefono_entry = tk.Entry(telefono_tab)
tel_telefono_entry.grid(row=1, column=1, padx=5, pady=5)

tel_cliente_entry = tk.Entry(telefono_tab)
tel_cliente_entry.grid(row=2, column=1, padx=5, pady=5)

tel_btn_frame = tk.Frame(telefono_tab)
tel_btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(tel_btn_frame, text="Crear", bg="green", fg="white", width=12, command=telefono_create).grid(row=0, column=0, padx=5)

tk.Button(tel_btn_frame, text="Actualizar", bg="yellow", fg="black", width=12, command=telefono_update).grid(row=0, column=1, padx=5)

tk.Button(tel_btn_frame, text="Eliminar", bg="red", fg="white", width=12, command=telefono_delete).grid(row=0, column=2, padx=5)

tk.Button(tel_btn_frame, text="Limpiar Campos", bg="blue", fg="white", width=12, command=clear_telefono_fields).grid(row=0, column=3, padx=5)

# Frame para mostrar la tabla de TELEFONO
tel_table_frame = tk.Frame(telefono_tab)
tel_table_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
tel_tree = ttk.Treeview(tel_table_frame, columns=("idTelefono", "telefono", "cliente"), show="headings")
tel_tree.heading("idTelefono", text="ID")
tel_tree.heading("telefono", text="Teléfono")
tel_tree.heading("cliente", text="Cliente")
tel_tree.pack(fill="both", expand=True)

tk.Button(telefono_tab, text="Mostrar Datos", bg="gray", fg="white", command=refresh_telefono_data).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(telefono_tab, text="Ocultar Datos", bg="black", fg="white", command=hide_telefono_data).grid(row=6, column=0, columnspan=2, pady=5)

# --- Pestaña PLAN ENTRENAMIENTO ---
plan_tab = ttk.Frame(notebook)
notebook.add(plan_tab, text="Plan Entrenamiento")

labels_plan = ["ID (para actualizar/eliminar):", "Día:", "Duración:", "Descripción:", "Cliente:"]

tk.Label(plan_tab, text=labels_plan[0]).grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
plan_id_entry = tk.Entry(plan_tab)
plan_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(plan_tab, text=labels_plan[1]).grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
plan_dia_entry = tk.Entry(plan_tab)
plan_dia_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(plan_tab, text=labels_plan[2]).grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
plan_duracion_entry = tk.Entry(plan_tab)
plan_duracion_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(plan_tab, text=labels_plan[3]).grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
plan_descripcion_entry = tk.Entry(plan_tab)
plan_descripcion_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(plan_tab, text=labels_plan[4]).grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
plan_cliente_entry = tk.Entry(plan_tab)
plan_cliente_entry.grid(row=4, column=1, padx=5, pady=5)

plan_btn_frame = tk.Frame(plan_tab)
plan_btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(plan_btn_frame, text="Crear", bg="green", fg="white", width=12, command=plan_create).grid(row=0, column=0, padx=5)

tk.Button(plan_btn_frame, text="Actualizar", bg="yellow", fg="black", width=12, command=plan_update).grid(row=0, column=1, padx=5)

tk.Button(plan_btn_frame, text="Eliminar", bg="red", fg="white", width=12, command=plan_delete).grid(row=0, column=2, padx=5)

tk.Button(plan_btn_frame, text="Limpiar Campos", bg="blue", fg="white", width=12, command=clear_plan_fields).grid(row=0, column=3, padx=5)

# Frame para mostrar la tabla de PLAN ENTRENAMIENTO
plan_table_frame = tk.Frame(plan_tab)
plan_table_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
plan_tree = ttk.Treeview(plan_table_frame, columns=("idPlan", "dia", "duracion", "descripcion", "cliente"), show="headings")
plan_tree.heading("idPlan", text="ID")
plan_tree.heading("dia", text="Día")
plan_tree.heading("duracion", text="Duración")
plan_tree.heading("descripcion", text="Descripción")
plan_tree.heading("cliente", text="Cliente")
plan_tree.pack(fill="both", expand=True)

tk.Button(plan_tab, text="Mostrar Datos", bg="gray", fg="white", command=refresh_plan_data).grid(row=7, column=0, columnspan=2, pady=5)
tk.Button(plan_tab, text="Ocultar Datos", bg="black", fg="white", command=hide_plan_data).grid(row=8, column=0, columnspan=2, pady=5)

# --- Pestaña RUTINA ---
rutina_tab = ttk.Frame(notebook)
notebook.add(rutina_tab, text="Rutina")

labels_rutina = ["ID (para actualizar/eliminar):", "Descripción:", "Nro Ejercicios:", "Nombre de Rutina:", "ID del Plan:"]

tk.Label(rutina_tab, text=labels_rutina[0]).grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
rutina_id_entry = tk.Entry(rutina_tab)
rutina_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(rutina_tab, text=labels_rutina[1]).grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
rutina_descripcion_entry = tk.Entry(rutina_tab)
rutina_descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(rutina_tab, text=labels_rutina[2]).grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
rutina_nroEjercicios_entry = tk.Entry(rutina_tab)
rutina_nroEjercicios_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(rutina_tab, text=labels_rutina[3]).grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
rutina_nombre_entry = tk.Entry(rutina_tab)
rutina_nombre_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(rutina_tab, text=labels_rutina[4]).grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
rutina_plan_id_entry = tk.Entry(rutina_tab)
rutina_plan_id_entry.grid(row=4, column=1, padx=5, pady=5)

rutina_btn_frame = tk.Frame(rutina_tab)
rutina_btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(rutina_btn_frame, text="Crear", bg="green", fg="white", width=12, command=rutina_create).grid(row=0, column=0, padx=5)

tk.Button(rutina_btn_frame, text="Actualizar", bg="yellow", fg="black", width=12, command=rutina_update).grid(row=0, column=1, padx=5)

tk.Button(rutina_btn_frame, text="Eliminar", bg="red", fg="white", width=12, command=rutina_delete).grid(row=0, column=2, padx=5)

tk.Button(rutina_btn_frame, text="Limpiar Campos", bg="blue", fg="white", width=12, command=clear_rutina_fields).grid(row=0, column=3, padx=5)

# Frame para mostrar la tabla de RUTINA
rutina_table_frame = tk.Frame(rutina_tab)
rutina_table_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
rutina_tree = ttk.Treeview(rutina_table_frame, columns=("idRutina", "descripcion", "nroEjercicios", "nombreRutina", "idPlan"), show="headings")
rutina_tree.heading("idRutina", text="ID")
rutina_tree.heading("descripcion", text="Descripción")
rutina_tree.heading("nroEjercicios", text="Ejercicios")
rutina_tree.heading("nombreRutina", text="Nombre")
rutina_tree.heading("idPlan", text="Plan")
rutina_tree.pack(fill="both", expand=True)

tk.Button(rutina_tab, text="Mostrar Datos", bg="gray", fg="white", command=refresh_rutina_data).grid(row=7, column=0, columnspan=2, pady=5)
tk.Button(rutina_tab, text="Ocultar Datos", bg="black", fg="white", command=hide_rutina_data).grid(row=8, column=0, columnspan=2, pady=5)

# --- Pestaña EJERCICIOS ---
ejercicio_tab = ttk.Frame(notebook)
notebook.add(ejercicio_tab, text="Ejercicios")

labels_ejercicio = ["ID (para actualizar/eliminar):", "Nombre del Ejercicio:", "Descripción:", "Grupo Muscular:", "Tiempo de Descanso:", "Nro de Series:", "ID de la Rutina:"]

tk.Label(ejercicio_tab, text=labels_ejercicio[0]).grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_id_entry = tk.Entry(ejercicio_tab)
ejercicio_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ejercicio_tab, text=labels_ejercicio[1]).grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_nombre_entry = tk.Entry(ejercicio_tab)
ejercicio_nombre_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ejercicio_tab, text=labels_ejercicio[2]).grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_descripcion_entry = tk.Entry(ejercicio_tab)
ejercicio_descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ejercicio_tab, text=labels_ejercicio[3]).grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_grupo_entry = tk.Entry(ejercicio_tab)
ejercicio_grupo_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ejercicio_tab, text=labels_ejercicio[4]).grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_tiempo_entry = tk.Entry(ejercicio_tab)
ejercicio_tiempo_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(ejercicio_tab, text=labels_ejercicio[5]).grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_nroSeries_entry = tk.Entry(ejercicio_tab)
ejercicio_nroSeries_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(ejercicio_tab, text=labels_ejercicio[6]).grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
ejercicio_rutina_id_entry = tk.Entry(ejercicio_tab)
ejercicio_rutina_id_entry.grid(row=6, column=1, padx=5, pady=5)

ejercicio_btn_frame = tk.Frame(ejercicio_tab)
ejercicio_btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

tk.Button(ejercicio_btn_frame, text="Crear", bg="green", fg="white", width=12, command=ejercicio_create).grid(row=0, column=0, padx=5)

tk.Button(ejercicio_btn_frame, text="Actualizar", bg="yellow", fg="black", width=12, command=ejercicio_update).grid(row=0, column=1, padx=5)

tk.Button(ejercicio_btn_frame, text="Eliminar", bg="red", fg="white", width=12, command=ejercicio_delete).grid(row=0, column=2, padx=5)

tk.Button(ejercicio_btn_frame, text="Limpiar Campos", bg="blue", fg="white", width=12, command=clear_ejercicio_fields).grid(row=0, column=3, padx=5)

# Frame para mostrar la tabla de EJERCICIOS
ejercicio_table_frame = tk.Frame(ejercicio_tab)
ejercicio_table_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
ejercicio_tree = ttk.Treeview(ejercicio_table_frame, columns=("idEjercicio", "nombreEjercicio", "descripcion", "grupoMuscular", "tiempoDescanso", "nroSeries", "idRutina"), show="headings")
ejercicio_tree.heading("idEjercicio", text="ID")
ejercicio_tree.heading("nombreEjercicio", text="Ejercicio")
ejercicio_tree.heading("descripcion", text="Descripción")
ejercicio_tree.heading("grupoMuscular", text="Grupo")
ejercicio_tree.heading("tiempoDescanso", text="Descanso")
ejercicio_tree.heading("nroSeries", text="Series")
ejercicio_tree.heading("idRutina", text="Rutina ID")
ejercicio_tree.pack(fill="both", expand=True)

tk.Button(ejercicio_tab, text="Mostrar Datos", bg="gray", fg="white", command=refresh_ejercicio_data).grid(row=9, column=0, columnspan=2, pady=5)
tk.Button(ejercicio_tab, text="Ocultar Datos", bg="black", fg="white", command=hide_ejercicio_data).grid(row=10, column=0, columnspan=2, pady=5)

root.mainloop() 