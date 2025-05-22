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
    conn.commit()
    conn.close()

# ⚠️ Esta línea ejecuta realmente la función
crear_tabla()

print("Tabla creada correctamente en HIS25.db")
