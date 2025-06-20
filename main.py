import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkcalendar import DateEntry
import customtkinter as ctk

ctk.set_appearance_mode("light")  # o "dark"
ctk.set_default_color_theme("blue")  # o "green", "dark-blue", etc.

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
        tag = "evenrow" if index % 2 == 0 else "oddrow"
        tree.insert('', 'end', iid=index, values=(row['nombre'], row['dni'], row['hb'], row['regla']), tags=(tag,))

def obtener_unidades_productoras():
    conn = sqlite3.connect(DB_FILE)  # ajusta el nombre de tu archivo .db
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM unidadProductora")
    resultados = [fila[0] for fila in cursor.fetchall()]
    conn.close()
    return resultados

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

    # Obtener tamaño de pantalla
    ancho_total = root.winfo_screenwidth()
    alto_total = root.winfo_screenheight()

    # Calcular tamaño de ventana (1/4 del total)
    ancho_ventana = ancho_total // 2
    alto_ventana = alto_total // 2

    # Calcular posición para centrar
    x_pos = (ancho_total - ancho_ventana) // 2
    y_pos = (alto_total - alto_ventana) // 2

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    ventana.columnconfigure(0, weight=0)
    ventana.columnconfigure(1, weight=1)
    ventana.columnconfigure(2, weight=0)
    ventana.columnconfigure(3, weight=1)

    fuente = ("Arial", 12)

    ctk.CTkLabel(ventana, text="DNI:", font=fuente).grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_dni = tk.Entry(ventana, font=fuente)
    entry_dni.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="NOMBRE:", font=fuente).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_nombre = tk.Entry(ventana, font=fuente)
    entry_nombre.grid(row=1, column=1, columnspan=3, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="APELLIDO:", font=fuente).grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_apellido = tk.Entry(ventana, font=fuente)
    entry_apellido.grid(row=2, column=1, columnspan=3, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="HISTORIA CLINICA:", font=fuente).grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_historiaClinica = tk.Entry(ventana, font=fuente)
    entry_historiaClinica.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="FICHA FAMILIAR:", font=fuente).grid(row=3, column=2, sticky="e", padx=10, pady=5)
    entry_fichaFamiliar = tk.Entry(ventana, font=fuente)
    entry_fichaFamiliar.grid(row=3, column=3, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="FICHA FAMILIAR:", font=fuente).grid(row=3, column=2, sticky="e", padx=10, pady=5)
    entry_fichaFamiliar = tk.Entry(ventana, font=fuente)
    entry_fichaFamiliar.grid(row=3, column=3, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="FECHA NACIMIENTO:", font=fuente).grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_fechaNacimiento = DateEntry(ventana, font=fuente, date_pattern="dd/mm/yyyy", locale="es_PE", width=18)
    entry_fechaNacimiento.grid(row=4, column=1,sticky="ew", padx=10, pady=5)
    
    sexo_var = ctk.StringVar(value="")

    ctk.CTkLabel(ventana, text="SEXO:", font=fuente).grid(row=4, column=2, sticky="e", padx=10, pady=5)

    frame_sexo = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_sexo.grid(row=4, column=3, columnspan=1, sticky="w", padx=10, pady=5)

    ctk.CTkRadioButton(frame_sexo, text="Masculino", variable=sexo_var, value="M", font=fuente).pack(side="left", padx=5)
    ctk.CTkRadioButton(frame_sexo, text="Femenino", variable=sexo_var, value="F", font=fuente).pack(side="left", padx=5)


    ctk.CTkLabel(ventana, text="PERIMETRO CEFALICO:", font=fuente).grid(row=5, column=0, sticky="e", padx=10, pady=5)
    entry_perimetroCefalico = tk.Entry(ventana, font=fuente)
    entry_perimetroCefalico.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="PERIMETRO ABDOMINAL:", font=fuente).grid(row=6, column=0, sticky="e", padx=10, pady=5)
    entry_perimetroAdominal = tk.Entry(ventana, font=fuente)
    entry_perimetroAdominal.grid(row=6, column=1, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="PESO:", font=fuente).grid(row=7, column=0, sticky="e", padx=10, pady=5)
    entry_peso = tk.Entry(ventana, font=fuente)
    entry_peso.grid(row=7, column=1, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="TALLA:", font=fuente).grid(row=7, column=2, sticky="e", padx=10, pady=5)
    entry_talla = tk.Entry(ventana, font=fuente)
    entry_talla.grid(row=7, column=3, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="HB:", font=fuente).grid(row=8, column=0, sticky="e", padx=10, pady=5)
    entry_hb = tk.Entry(ventana, font=fuente)
    entry_hb.grid(row=8, column=1, sticky="ew", padx=10, pady=5)

    ctk.CTkLabel(ventana, text="FECHA ULTIMA HB:", font=fuente).grid(row=8, column=2, sticky="e", padx=10, pady=5)
    entry_fechaUltimaHb = DateEntry(ventana, font=fuente, date_pattern="dd/mm/yyyy", locale="es_PE", width=18)
    entry_fechaUltimaHb.grid(row=8, column=3, sticky="ew", padx=10, pady=5)

    # Variable para guardar la opción seleccionada
    ci_establecimiento_var = tk.StringVar(value="")  # puedes poner "Nuevo" si quieres preseleccionar

    ci_establecimiento_var = ctk.StringVar(value="")

    ctk.CTkLabel(ventana, text="CI - ESTABLECIMIENTO:", font=fuente).grid(row=9, column=0, sticky="e", padx=10, pady=5)

    frame_establecimiento = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_establecimiento.grid(row=9, column=1, columnspan=3, sticky="w", padx=10, pady=5)

    ctk.CTkRadioButton(frame_establecimiento, text="Nuevo", variable=ci_establecimiento_var, value="Nuevo", font=fuente).pack(side="left", padx=5)
    ctk.CTkRadioButton(frame_establecimiento, text="Continuador", variable=ci_establecimiento_var, value="Continuador", font=fuente).pack(side="left", padx=5)
    ctk.CTkRadioButton(frame_establecimiento, text="Reingresante", variable=ci_establecimiento_var, value="Reingresante", font=fuente).pack(side="left", padx=5)

    # Variable para almacenar la selección del servicio
    ci_servicio_var = tk.StringVar(value="")  # o "Nuevo" si quieres un valor preseleccionado

    ci_servicio_var = ctk.StringVar(value="")  # o "Nuevo" para valor por defecto

    ctk.CTkLabel(ventana, text="CI - SERVICIO:", font=fuente).grid(row=10, column=0, sticky="e", padx=10, pady=5)

    frame_servicio = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_servicio.grid(row=10, column=1, columnspan=3, sticky="w", padx=10, pady=5)

    ctk.CTkRadioButton(frame_servicio, text="Nuevo", variable=ci_servicio_var, value="Nuevo", font=fuente).pack(side="left", padx=5)
    ctk.CTkRadioButton(frame_servicio, text="Continuador", variable=ci_servicio_var, value="Continuador", font=fuente).pack(side="left", padx=5)
    ctk.CTkRadioButton(frame_servicio, text="Reingresante", variable=ci_servicio_var, value="Reingresante", font=fuente).pack(side="left", padx=5)

    lista_unidades = obtener_unidades_productoras()

    ctk.CTkLabel(ventana, text="UNIDAD PRODUCTORA:", font=fuente).grid(row=15, column=0, sticky="e", padx=10, pady=5)

    combo_unidadProductora = ctk.CTkComboBox(
        ventana,
        font=fuente,
        values=lista_unidades,
        width=200,
        state="readonly"  # Opcional, para que solo seleccione y no escriba libremente
    )
    combo_unidadProductora.grid(row=15, column=1, sticky="ew", padx=10, pady=5)


    tk.Button(ventana, text="Guardar", command=guardar, font=fuente, bg="#2ecc71", fg="white").grid(row=17, column=1, columnspan=2, pady=15)

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
            ctk.CTkLabel(ventana, text=f"{k.capitalize()}: {v}").grid(row=i, column=0, sticky="w")

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

    ctk.CTkLabel(ventana, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.insert(0, row['nombre'])
    entry_nombre.grid(row=0, column=1)

    ctk.CTkLabel(ventana, text="DNI:").grid(row=1, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.insert(0, row['dni'])
    entry_dni.grid(row=1, column=1)

    ctk.CTkLabel(ventana, text="Fecha Hb:").grid(row=2, column=0)
    entry_hb = tk.Entry(ventana)
    entry_hb.insert(0, row['hb'])
    entry_hb.grid(row=2, column=1)

    ctk.CTkLabel(ventana, text="Fecha Regla:").grid(row=3, column=0)
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

# Estilo de fuente para la tabla
style = ttk.Style()
style.configure("Treeview", font=("Arial", 11), rowheight=35)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# Obtener dimensiones de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

alto_tabla = int(alto_pantalla * 0.85)

# Aplicar como tamaño de ventana
root.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Frame superior con botón "+ Nuevo"
frame = tk.Frame(root)
frame.pack(fill="x", padx=10, pady=10)

# Subframe para el botón "+ Nuevo" a la izquierda
frame_izquierdo = tk.Frame(frame)
frame_izquierdo.pack(side="left", fill="x", expand=True)

tk.Button(
    frame_izquierdo,
    text="+ Nuevo",
    command=agregar_nuevo,
    font=("Arial", 11, "bold"),
    bg="#2ecc71",               # Verde brillante
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    relief="solid",
    bd=1,
    highlightbackground="black",
    highlightthickness=1,
    width=12
).pack(anchor="w", padx=5, pady=5)

# Frame para tabla y botones de acción juntos
tabla_botones_frame = tk.Frame(root, height=alto_tabla)
tabla_botones_frame.pack(fill="x", padx=10, pady=5)
tabla_botones_frame.pack_propagate(False)

# Frame de la tabla
tabla_frame = tk.Frame(tabla_botones_frame)
tabla_frame.pack(fill="both", expand=True, side="left")

columns = ("nombre", "dni", "hb", "regla")

scroll_y = ttk.Scrollbar(tabla_frame, orient="vertical")
scroll_y.pack(side="right", fill="y")

tree = ttk.Treeview(tabla_frame, columns=columns, show="headings", yscrollcommand=scroll_y.set)
tree.tag_configure("evenrow", background="#f2f2f2")  # Gris claro
tree.tag_configure("oddrow", background="white")     # Blanco

scroll_y.config(command=tree.yview)

tree.column("nombre", width=300, anchor="w")
tree.column("dni", width=150, anchor="center")
tree.column("hb", width=100, anchor="center")
tree.column("regla", width=150, anchor="center")

for col in columns:
    tree.heading(col, text=col.capitalize())

tree.pack(fill="both", expand=True)

# Subframe para los botones Ver, Editar, Eliminar agrupados a la derecha
frame_derecho = tk.Frame(frame)
frame_derecho.pack(side="right", padx=10)

# Botón "Ver"
tk.Button(
    frame_derecho,
    text="Ver",
    command=ver_paciente,
    font=("Arial", 11, "bold"),
    bg="#3498db",              # Azul vivo
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    relief="solid",
    bd=1,
    highlightbackground="black",
    highlightthickness=1,
    width=12
).pack(side="left", padx=5, pady=5)

# Botón "Editar"
tk.Button(
    frame_derecho,
    text="Editar",
    command=editar_paciente,
    font=("Arial", 11, "bold"),
    bg="#f39c12",              # Naranja brillante
    fg="white",
    activebackground="#d68910",
    activeforeground="white",
    relief="solid",
    bd=1,
    highlightbackground="black",
    highlightthickness=1,
    width=12
).pack(side="left", padx=5, pady=5)

# Botón "Eliminar"
tk.Button(
    frame_derecho,
    text="Eliminar",
    command=eliminar_paciente_gui,
    font=("Arial", 11, "bold"),
    bg="#e74c3c",              # Rojo intenso
    fg="white",
    activebackground="#c0392b",
    activeforeground="white",
    relief="solid",
    bd=1,
    highlightbackground="black",
    highlightthickness=1,
    width=12
).pack(side="left", padx=5, pady=5)

# Inicialización
crear_tabla()
cargar_data_desde_sql()
actualizar_tabla()

root.mainloop()
