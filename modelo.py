import sqlite3
from datetime import datetime

DB_FILE = "HIS25.db"

def guardar_formulario_completo(
    nombres, apellidos, dni, fecha_nacimiento, sexo,
    perimetro_cefalico, perimetro_abdominal, peso, talla, hb,
    fecha_ultima_hb, establecimiento, servicio, unidad_productora_nombre
):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Insertar paciente
    cursor.execute('''
        INSERT INTO paciente (
            nombre, apellido, dni, fecha_nacimiento, sexo
        ) VALUES (?, ?, ?, ?, ?)
    ''', (nombres, apellidos, dni, fecha_nacimiento, sexo))
    paciente_id = cursor.lastrowid

    # Obtener ID de la unidad productora
    cursor.execute('''
        SELECT id FROM UnidadProductora WHERE nombre = ?
    ''', (unidad_productora_nombre,))
    unidad_result = cursor.fetchone()
    if not unidad_result:
        raise Exception("Unidad productora no encontrada")
    id_unidad = unidad_result[0]

    # Obtener o crear relación UnidadProductora_Diagnostico (usamos por ahora Diagnóstico 1)
    cursor.execute('''
        SELECT id FROM UnidadProductora_Diagnosticos 
        WHERE idUnidadProductora = ? AND idDiagnostico = ?
    ''', (id_unidad, 1))
    relacion = cursor.fetchone()
    if relacion:
        id_relacion = relacion[0]
    else:
        cursor.execute('''
            INSERT INTO UnidadProductora_Diagnosticos (idUnidadProductora, idDiagnostico)
            VALUES (?, ?)
        ''', (id_unidad, 1))
        id_relacion = cursor.lastrowid

    # Insertar en cabecera_his
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        INSERT INTO cabecera_his (idUnidadProductoraDiagnostico, fecha)
        VALUES (?, ?)
    ''', (id_relacion, fecha_actual))
    id_cabecera = cursor.lastrowid

    # Insertar en detalle_his
    cursor.execute('''
        INSERT INTO detalle_his (
            idPaciente, per_cefalico, per_abdominal, peso, talla, hb,
            establecimiento, servicio
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        paciente_id, perimetro_cefalico, perimetro_abdominal, peso,
        talla, hb, establecimiento, servicio
    ))

    conn.commit()
    conn.close()
