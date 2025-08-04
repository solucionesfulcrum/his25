import sqlite3

DB_FILE = "HIS25.db"

def crear_tabla():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Tabla pacientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paciente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres TEXT(200),
            apellidos TEXT(200),
            dni TEXT(20),
            fecha_nacimiento TEXT(100),
            sexo TEXT(20)
        )
    ''')

    # Tabla UnidadProductora
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UnidadProductora (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            agrupacion TEXT 
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO UnidadProductora (id, nombre, agrupacion)
        VALUES (?, ?, ?)
    ''', (1, 'ITS PG', '2'))

    # Tabla Diagnosticos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            codigo TEXT
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Diagnosticos (id, nombre, codigo)
        VALUES (?, ?, ?)
    ''', (1, 'CONSEJERIA PRE TEST VIH', '50978.46'))
    cursor.execute('''
        INSERT OR IGNORE INTO Diagnosticos (id, nombre, codigo)
        VALUES (?, ?, ?)
    ''', (2, 'TAMIZAJE VIH', '31403.58'))

    # Tabla Parametros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Parametros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            codigo TEXT,
            filtro TEXT
        )
    ''')

    # Tabla intermedia UnidadProductora_Diagnosticos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UnidadProductora_Diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idUnidadProductora INTEGER,
            idDiagnostico INTEGER,
            FOREIGN KEY (idUnidadProductora) REFERENCES UnidadProductora(id),
            FOREIGN KEY (idDiagnostico) REFERENCES Diagnosticos(id)
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO UnidadProductora_Diagnosticos (id, idUnidadProductora, idDiagnostico)
        VALUES (?, ?, ?)
    ''', (1, 1, 1))
    cursor.execute('''
        INSERT OR IGNORE INTO UnidadProductora_Diagnosticos (id, idUnidadProductora, idDiagnostico)
        VALUES (?, ?, ?)
    ''', (2, 1, 2))

    # Tabla cabecera_his relacionada a UnidadProductora_Diagnosticos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cabecera_his (
            id_cabecera_his INTEGER PRIMARY KEY AUTOINCREMENT,
            idUnidadProductoraDiagnostico INTEGER,
            fecha TEXT,
            FOREIGN KEY (idUnidadProductoraDiagnostico) REFERENCES UnidadProductora_Diagnosticos(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detalle_his (
            id_detalle_his INTEGER PRIMARY KEY AUTOINCREMENT,
            idPaciente INTEGER,
            per_cefalico TEXT,
            per_abdominal TEXT,
            peso TEXT,
            talla TEXT,
            hb TEXT,
            establecimiento TEXT,
            servicio TEXT,
            FOREIGN KEY (idPaciente) REFERENCES pacientes(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sub_detalle_his (
            id_sub_detalle_his INTEGER PRIMARY KEY AUTOINCREMENT,
            idUnidadProductoraDiagnostico INTEGER,
            tipo_diagnostico TEXT,
            valor_lab1 TEXT,
            valor_lab2 TEXT,
            valor_lab3 TEXT,
            FOREIGN KEY (idUnidadProductoraDiagnostico) REFERENCES UnidadProductora_Diagnosticos(id)
        )
    ''')

    conn.commit()
    conn.close()

# Ejecutar la función
crear_tabla()
print("Tablas creadas correctamente en HIS25.db")
