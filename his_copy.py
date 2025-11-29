import fitz  # PyMuPDF
from datetime import date
import locale
import sqlite3
import json

DB_FILE = "HIS25.db"

# Locale para el mes en español (ajusta según tu SO si da error)
try:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')
except locale.Error:
    # En Linux suele ser:
    # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    pass

hoy = date.today()

# 1. Leer el archivo JSON
with open("data.json", "r", encoding="utf-8") as f:
    datos = json.load(f)   # aquí datos es una lista de dicts


# 2. Función para dividir en bloques de n elementos
def dividir_en_bloques(lista, tam=12):
    for i in range(0, len(lista), tam):
        yield lista[i:i + tam]


# 3. Obtener los bloques de 12
bloques = list(dividir_en_bloques(datos, 12))

print("Total de bloques:", len(bloques))


def llenadoPdf(cantidad_registro, page, rango_ini_hori, nombre, tamano_fuente, distancia_vert, rango_ini_vert, siguiente):
    # En tu código original, el for estaba comentado,
    # así que solo se escribe una vez en la posición indicada.
    page.insert_text((rango_ini_hori, rango_ini_vert), nombre, fontsize=tamano_fuente)


def llenadoPdf1(cantidad_registro, page, rango_ini_hori, nombre, tamano_fuente, distancia_vert, rango_ini_vert, siguiente):
    for x in range(cantidad_registro):
        page.insert_text((rango_ini_hori, rango_ini_vert), nombre, fontsize=tamano_fuente)
        rango_ini_vert += distancia_vert * siguiente


def obtener_UnidadProductora_Diagnosticos():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT UPD.id, UPD.idUnidadProductora, UPD.idDiagnostico, UP.id, 
               UP.nombre, UP.agrupacion, D.id, D.nombre, D.codigo  
        FROM UnidadProductora_Diagnosticos UPD
        INNER JOIN UnidadProductora UP ON UP.id = UPD.idUnidadProductora
        INNER JOIN Diagnosticos D ON D.id = UPD.idDiagnostico;
    """)
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    # Nota: tu dict tenía claves repetidas ('id_d') y 'codigo_d' mal posicionado.
    return [
        {
            'id_upd': row[0],
            'idUnidadProductora': row[1],
            'idDiagnostico': row[2],
            'id_up': row[3],
            'nombre_up': row[4],
            'agrupacion_up': row[5],
            'id_d': row[6],
            'nombre_d': row[7],
            'codigo_d': row[8],
        }
        for row in rows
    ]


def logicaGeneral():
    # his.pdf será la PLANTILLA
    plantilla = fitz.open("his.pdf")
    doc = fitz.open()

    unidadProductora_diagnostico = obtener_UnidadProductora_Diagnosticos()
    # print(unidadProductora_diagnostico)  # si lo quieres usar después

    for num_bloque, bloque in enumerate(bloques):
        # Insertamos una copia de la página 0 de la plantilla en el doc de salida
        doc.insert_pdf(plantilla, from_page=0, to_page=0)
        page = doc[-1]  # última página insertada

        # ==================================================
        # CABECERA (se repite en cada página / bloque)
        # ==================================================

        # AÑO
        rango_ini_vert = 145
        distancia_vert = 0
        rango_ini_hori = 25
        tamano_fuente = 6
        cantidad_registro = 1
        nombre = str(hoy.year)
        siguiente = 0
        llenadoPdf1(
            cantidad_registro=cantidad_registro,
            page=page,
            rango_ini_hori=rango_ini_hori,
            nombre=nombre,
            tamano_fuente=tamano_fuente,
            distancia_vert=distancia_vert,
            rango_ini_vert=rango_ini_vert,
            siguiente=siguiente,
        )

        # MES
        rango_ini_vert = 145
        rango_ini_hori = 60
        tamano_fuente = 6
        cantidad_registro = 1
        nombre = str(hoy.strftime("%B").upper())
        siguiente = 0
        llenadoPdf1(
            cantidad_registro=cantidad_registro,
            page=page,
            rango_ini_hori=rango_ini_hori,
            nombre=nombre,
            tamano_fuente=tamano_fuente,
            distancia_vert=0,
            rango_ini_vert=rango_ini_vert,
            siguiente=siguiente,
        )

        # NOMBRE IPRESS
        rango_ini_vert = 145
        rango_ini_hori = 150
        tamano_fuente = 6
        cantidad_registro = 1
        nombre = "HOSPITAL HUAYCAN"
        siguiente = 0
        llenadoPdf1(
            cantidad_registro=cantidad_registro,
            page=page,
            rango_ini_hori=rango_ini_hori,
            nombre=nombre,
            tamano_fuente=tamano_fuente,
            distancia_vert=0,
            rango_ini_vert=rango_ini_vert,
            siguiente=siguiente,
        )

        # UNIDAD
        rango_ini_vert = 145
        rango_ini_hori = 280
        tamano_fuente = 6
        cantidad_registro = 1
        nombre = "TELESALUD / SMPN UNIDAD PRODUCTORA"
        siguiente = 0
        llenadoPdf1(
            cantidad_registro=cantidad_registro,
            page=page,
            rango_ini_hori=rango_ini_hori,
            nombre=nombre,
            tamano_fuente=tamano_fuente,
            distancia_vert=0,
            rango_ini_vert=rango_ini_vert,
            siguiente=siguiente,
        )

        # DNI PROFESIONAL
        rango_ini_vert = 145
        rango_ini_hori = 450
        tamano_fuente = 6
        cantidad_registro = 1
        nombre = "20883195"
        siguiente = 0
        llenadoPdf1(
            cantidad_registro=cantidad_registro,
            page=page,
            rango_ini_hori=rango_ini_hori,
            nombre=nombre,
            tamano_fuente=tamano_fuente,
            distancia_vert=0,
            rango_ini_vert=rango_ini_vert,
            siguiente=siguiente,
        )

        # NOMBRE PROFESIONAL
        rango_ini_vert = 145
        rango_ini_hori = 502
        tamano_fuente = 6
        cantidad_registro = 1
        nombre = "L. CANCHIHUAMAN V. "
        siguiente = 0
        llenadoPdf1(
            cantidad_registro=cantidad_registro,
            page=page,
            rango_ini_hori=rango_ini_hori,
            nombre=nombre,
            tamano_fuente=tamano_fuente,
            distancia_vert=0,
            rango_ini_vert=rango_ini_vert,
            siguiente=siguiente,
        )

        # ==================================================
        # DETALLE (PACIENTES) – máx 12 por página
        # ==================================================

        for x, fila in enumerate(bloque):
            # x va de 0 a 11 dentro de este bloque
            distancia_vert = 46.4

            # NOMBRE PACIENTE
            rango_ini_vert = 183 + distancia_vert * x
            rango_ini_hori = 117
            tamano_fuente = 4
            cantidad_registro = 12
            nombre = fila["nombre"]
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # FECHA HEMOGLOBINA (vacío)
            rango_ini_vert = 183 + distancia_vert * x
            rango_ini_hori = 337
            tamano_fuente = 6
            cantidad_registro = 3
            nombre = ""
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # FECHA NACIMIENTO
            rango_ini_vert = 183 + distancia_vert * x
            rango_ini_hori = 522
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = fila["fecha_nacimiento"]
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # DIA (ejemplo fijo "28")
            rango_ini_vert = 205 + distancia_vert * x
            rango_ini_hori = 28
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = "28"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # DNI
            rango_ini_vert = 193 + distancia_vert * x
            rango_ini_hori = 58
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = fila["dni"]
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # HISTORIA CLINICA
            rango_ini_vert = 205 + distancia_vert * x
            rango_ini_hori = 58
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = fila["h_clinica"]
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # FICHA FAMILIAR (vacío, ejemplo)
            rango_ini_vert = 217 + distancia_vert * x
            rango_ini_hori = 58
            tamano_fuente = 6
            cantidad_registro = 6
            nombre = ""
            siguiente = 2
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # FINANCIAMIENTO
            rango_ini_vert = 197 + distancia_vert * x
            rango_ini_hori = 111
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = "2"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # ETNIA
            rango_ini_vert = 214 + distancia_vert * x
            rango_ini_hori = 110
            tamano_fuente = 6
            cantidad_registro = 6
            nombre = "80"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # DISTRITO
            rango_ini_vert = 197 + distancia_vert * x
            rango_ini_hori = 130
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = "ATE"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # CENTRO POBLADO
            rango_ini_vert = 214 + distancia_vert * x
            rango_ini_hori = 130
            tamano_fuente = 6
            cantidad_registro = 12
            nombre = "HUAYCAN"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # EDAD
            rango_ini_vert = 205 + distancia_vert * x
            rango_ini_hori = 193
            tamano_fuente = 6
            cantidad_registro = 6
            nombre = str(fila["edad"])
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # EDAD AÑO (marca X fija)
            rango_ini_vert = 197 + distancia_vert * x
            rango_ini_hori = 206
            tamano_fuente = 14
            cantidad_registro = 12
            nombre = "X"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # EDAD MES (vacío)
            rango_ini_vert = 209 + distancia_vert * x
            rango_ini_hori = 206
            tamano_fuente = 14
            cantidad_registro = 6
            nombre = ""
            siguiente = 2
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # EDAD DIA (vacío)
            rango_ini_vert = 221 + distancia_vert * x
            rango_ini_hori = 206
            tamano_fuente = 14
            cantidad_registro = 6
            nombre = ""
            siguiente = 2
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # SEXO MASCULINO (vacío)
            rango_ini_vert = 200 + distancia_vert * x
            rango_ini_hori = 220
            tamano_fuente = 14
            cantidad_registro = 6
            nombre = ""
            siguiente = 2
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # SEXO FEMENINO (X fija)
            rango_ini_vert = 219 + distancia_vert * x
            rango_ini_hori = 220
            tamano_fuente = 14
            cantidad_registro = 12
            nombre = "X"
            siguiente = x
            llenadoPdf(
                cantidad_registro=cantidad_registro,
                page=page,
                rango_ini_hori=rango_ini_hori,
                nombre=nombre,
                tamano_fuente=tamano_fuente,
                distancia_vert=distancia_vert,
                rango_ini_vert=rango_ini_vert,
                siguiente=siguiente,
            )

            # PC, PB, PESO, TALLA, HB, ESTABLECIMIENTO, SERVICIO, LAB, TIPO DX, etc.
            # Aquí puedes seguir copiando el resto de tus bloques exactamente igual
            # cambiando solo las variables que dependan del paciente si las hubiera.
            # Para no hacer esto infinito, mantengo la estructura de ejemplo que ya tenías:

            # PC
            rango_ini_vert = 197 + distancia_vert * x
            rango_ini_hori = 252
            tamano_fuente = 6
            nombre = ""
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=2)

            # PB
            rango_ini_vert = 215 + distancia_vert * x
            rango_ini_hori = 252
            tamano_fuente = 6
            nombre = ""
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=2)

            # PESO
            rango_ini_vert = 193 + distancia_vert * x
            rango_ini_hori = 290
            tamano_fuente = 6
            nombre = ""
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=2)

            # TALLA
            rango_ini_vert = 205 + distancia_vert * x
            rango_ini_hori = 289
            tamano_fuente = 6
            nombre = ""
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=2)

            # HB
            rango_ini_vert = 217 + distancia_vert * x
            rango_ini_hori = 290
            tamano_fuente = 6
            nombre = ""
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=2)

            # ACTIVIDAD 1
            rango_ini_vert = 194 + distancia_vert * x
            rango_ini_hori = 344
            tamano_fuente = 5
            nombre = "CONSEJERIA EN SALUD SEXUAL Y REPRODUCTIVA"
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=x)

            # ACTIVIDAD 2
            rango_ini_vert = 206 + distancia_vert * x
            rango_ini_hori = 344
            tamano_fuente = 5
            nombre = "TELEORIENTACION SINCRONA"
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=x)

            # ACTIVIDAD 3
            rango_ini_vert = 218 + distancia_vert * x
            rango_ini_hori = 344
            tamano_fuente = 5
            nombre = "SEGUIMIENTO TELEFONICO"
            llenadoPdf(cantidad_registro=6, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=x)

            # Códigos CIE CPT (ejemplo fijo)
            # CPT 1
            rango_ini_vert = 194 + distancia_vert * x
            rango_ini_hori = 565
            tamano_fuente = 6
            nombre = "99402.03"
            llenadoPdf(cantidad_registro=12, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=x)

            # CPT 2
            rango_ini_vert = 206 + distancia_vert * x
            rango_ini_hori = 565
            tamano_fuente = 6
            nombre = "99499.08"
            llenadoPdf(cantidad_registro=12, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=x)

            # CPT 3
            rango_ini_vert = 218 + distancia_vert * x
            rango_ini_hori = 565
            tamano_fuente = 6
            nombre = "98967"
            llenadoPdf(cantidad_registro=12, page=page, rango_ini_hori=rango_ini_hori,
                       nombre=nombre, tamano_fuente=tamano_fuente,
                       distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, siguiente=x)

    # Guardar resultado
    doc.save("coordenadas_marcadas.pdf")
    doc.close()
    plantilla.close()


logicaGeneral()
