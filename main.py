import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_FILE = "HIS25.db"
data = []

# 🧱 Crear tabla si no existe
def crear_tabla():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            dni TEXT,
            hb TEXT,
            regla TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 🔃 Operaciones de base de datos
def insertar_paciente(paciente):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pacientes (nombre, dni, hb, regla)
        VALUES (?, ?, ?, ?)
    ''', (paciente['nombre'], paciente['dni'], paciente['hb'], paciente['regla']))
    conn.commit()
    conn.close()

def actualizar_paciente(id_, paciente):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pacientes
        SET nombre = ?, dni = ?, hb = ?, regla = ?
        WHERE id = ?
    ''', (paciente['nombre'], paciente['dni'], paciente['hb'], paciente['regla'], id_))
    conn.commit()
    conn.close()

def eliminar_paciente(id_):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pacientes WHERE id = ?', (id_,))
    conn.commit()
    conn.close()

def obtener_pacientes():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, dni, hb, regla FROM pacientes')
    rows = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'nombre': row[1], 'dni': row[2], 'hb': row[3], 'regla': row[4]} for row in rows]

# 🚀 Lógica de la interfaz
def cargar_data_desde_sql():
    global data
    data = obtener_pacientes()

def actualizar_tabla():
    for i in tree.get_children():
        tree.delete(i)
    for index, row in enumerate(data):
        tree.insert('', 'end', iid=index, values=(row['nombre'], row['dni'], row['hb'], row['regla']))

def agregar_nuevo():
    def guardar():
        nuevo = {
            'nombre': entry_nombre.get(),
            'dni': entry_dni.get(),
            'hb': entry_hb.get(),
            'regla': entry_regla.get()
        }
        insertar_paciente(nuevo)
        cargar_data_desde_sql()
        actualizar_tabla()
        ventana.destroy()

    ventana = tk.Toplevel(root)
    ventana.title("Nuevo Paciente")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="DNI:").grid(row=1, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.grid(row=1, column=1)

    tk.Label(ventana, text="Fecha Hb:").grid(row=2, column=0)
    entry_hb = tk.Entry(ventana)
    entry_hb.grid(row=2, column=1)

    tk.Label(ventana, text="Fecha Regla:").grid(row=3, column=0)
    entry_regla = tk.Entry(ventana)
    entry_regla.grid(row=3, column=1)

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2)

def get_selected_index():
    selected = tree.selection()
    return int(selected[0]) if selected else None

def ver_paciente():
    index = get_selected_index()
    if index is None: return
    row = data[index]
    ventana = tk.Toplevel(root)
    ventana.title("Ver Paciente")
    for i, (k, v) in enumerate(row.items()):
        if k != "id":
            tk.Label(ventana, text=f"{k.capitalize()}: {v}").grid(row=i, column=0, sticky="w")

def editar_paciente():
    index = get_selected_index()
    if index is None: return
    row = data[index]

    def guardar():
        nuevo = {
            'nombre': entry_nombre.get(),
            'dni': entry_dni.get(),
            'hb': entry_hb.get(),
            'regla': entry_regla.get()
        }
        actualizar_paciente(row['id'], nuevo)
        cargar_data_desde_sql()
        actualizar_tabla()
        ventana.destroy()

    ventana = tk.Toplevel(root)
    ventana.title("Editar Paciente")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.insert(0, row['nombre'])
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="DNI:").grid(row=1, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.insert(0, row['dni'])
    entry_dni.grid(row=1, column=1)

    tk.Label(ventana, text="Fecha Hb:").grid(row=2, column=0)
    entry_hb = tk.Entry(ventana)
    entry_hb.insert(0, row['hb'])
    entry_hb.grid(row=2, column=1)

    tk.Label(ventana, text="Fecha Regla:").grid(row=3, column=0)
    entry_regla = tk.Entry(ventana)
    entry_regla.insert(0, row['regla'])
    entry_regla.grid(row=3, column=1)

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2)

def eliminar_paciente_gui():
    index = get_selected_index()
    if index is None: return
    if messagebox.askyesno("¿Eliminar?", "¿Seguro que deseas eliminar este registro?"):
        eliminar_paciente(data[index]['id'])
        cargar_data_desde_sql()
        actualizar_tabla()

# 🖼️ GUI
root = tk.Tk()
root.title("Registro HIS 2025")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Button(frame, text="+ Nuevo", command=agregar_nuevo).pack(anchor='e')

columns = ("nombre", "dni", "hb", "regla")
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col.capitalize())
tree.pack()

boton_frame = tk.Frame(root)
boton_frame.pack(pady=5)

tk.Button(boton_frame, text="Ver", command=ver_paciente).pack(side="left", padx=5)
tk.Button(boton_frame, text="Editar", command=editar_paciente).pack(side="left", padx=5)
tk.Button(boton_frame, text="Eliminar", command=eliminar_paciente_gui).pack(side="left", padx=5)

# Inicialización
crear_tabla()
cargar_data_desde_sql()
actualizar_tabla()

root.mainloop()
