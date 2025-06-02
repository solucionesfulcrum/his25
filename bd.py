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
            nombre TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            codigo TEXT
        )
    ''')
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
    conn.commit()
    conn.close()

# ⚠️ Esta línea ejecuta realmente la función
crear_tabla()

print("Tabla creada correctamente en HIS25.db")
