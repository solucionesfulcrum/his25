import sqlite3

DB_FILE = "HIS25.db"

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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UnidadProductora (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            agrupacion TEXT 
        )
    ''')

    cursor.execute('''
        INSERT INTO UnidadProductora (id, nombre, agrupacion)
        VALUES (?, ?, ?, ?)
     ('1','ITS PG', '2')''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            codigo TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO Diagnosticos (id, nombre, codigo)
        VALUES (?, ?, ?, ?)
     ('1','CONSEJERIA PRE TEST VIH', '50978.46')''')

    cursor.execute('''
        INSERT INTO Diagnosticos (id, nombre, codigo)
        VALUES (?, ?, ?, ?)
     ('2','TAMIZAJE VIH', '31403.58')''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Parametros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            codigo TEXT,
            filtro TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UnidadProductora_Diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idUnidadProductora TEXT,
            idDiagnostico TEXT,
            FOREIGN KEY (idUnidadProductora) REFERENCES UnidadProductora(id),
            FOREIGN KEY (idDiagnostico) REFERENCES Diagnosticos(id)
        )
    ''')

    cursor.execute('''
        INSERT INTO UnidadProductora_Diagnosticos (id, idUnidadProductora, idDiagnostico)
        VALUES (?, ?, ?, ?)
     ('1','1', '1')''')

    cursor.execute('''
        INSERT INTO UnidadProductora_Diagnosticos (id, idUnidadProductora, idDiagnostico)
        VALUES (?, ?, ?, ?)
     ('2','1', '2')''')
    
    conn.commit()
    conn.close()

# ⚠️ Esta línea ejecuta realmente la función
crear_tabla()

print("Tabla creada correctamente en HIS25.db")
