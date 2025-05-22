import tkinter as tk
from tkinter import ttk, messagebox

data = []

def actualizar_tabla():
    for i in tree.get_children():
        tree.delete(i)
    for index, row in enumerate(data):
        tree.insert('', 'end', iid=index, values=(row['nombre'], row['dni'], row['hb'], row['regla']))

def agregar_nuevo():
    def guardar():
        data.append({
            'nombre': entry_nombre.get(),
            'dni': entry_dni.get(),
            'hb': entry_hb.get(),
            'regla': entry_regla.get()
        })
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
        tk.Label(ventana, text=f"{k.capitalize()}: {v}").grid(row=i, column=0, sticky="w")

def editar_paciente():
    index = get_selected_index()
    if index is None: return
    row = data[index]

    def guardar():
        row['nombre'] = entry_nombre.get()
        row['dni'] = entry_dni.get()
        row['hb'] = entry_hb.get()
        row['regla'] = entry_regla.get()
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

def eliminar_paciente():
    index = get_selected_index()
    if index is None: return
    if messagebox.askyesno("Confirmar", "¿Deseas eliminar este registro?"):
        data.pop(index)
        actualizar_tabla()

# GUI
root = tk.Tk()
root.title("Registro HIS")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Button(frame, text="+ Nuevo", command=agregar_nuevo).pack(anchor='e')

columns = ("nombre", "dni", "hb", "regla")
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col.capitalize())
tree.pack()

# Botones debajo de la tabla
boton_frame = tk.Frame(root)
boton_frame.pack(pady=5)

tk.Button(boton_frame, text="Ver", command=ver_paciente).pack(side="left", padx=5)
tk.Button(boton_frame, text="Editar", command=editar_paciente).pack(side="left", padx=5)
tk.Button(boton_frame, text="Eliminar", command=eliminar_paciente).pack(side="left", padx=5)

actualizar_tabla()
root.mainloop()
