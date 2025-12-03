import fitz  # PyMuPDF
from datetime import date, datetime
import locale
import sqlite3
import json  

# ========================= CONFIGURACIÓN INICIAL =========================

DB_FILE = "HIS25.db"
TEMPLATE_FILE = "his.pdf"              # plantilla
REGISTROS_POR_PAGINA = 12              # máximo por hoja
ROW_HEIGHT = 46.4                      # distancia vertical entre filas

# Locale para nombre de mes en español (Windows)
locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

hoy = date.today()

# Datos que quieres imprimir en el PDF (vienen de data.json)
with open("data.json", "r", encoding="utf-8") as f:
    datos = json.load(f)


# ============================ FUNCIONES AUXILIARES ============================

def formato_fecha_dd_mm_aaaa(fecha_str: str) -> str:
    """
    Acepta:
      - '1995-06-16' (YYYY-MM-DD)
      - '16/06/1995' (DD/MM/YYYY)
    y devuelve: '16     06     1995'
    """
    fecha_str = fecha_str.strip()

    dt = None
    # 1) intenta ISO: 1995-06-16
    try:
        dt = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        pass

    # 2) si no, intenta formato Excel/Perú: 16/06/1995
    if dt is None:
        dt = datetime.strptime(fecha_str, "%d/%m/%Y").date()

    return f"{dt.day:02d}     {dt.month:02d}     {dt.year}"


def obtener_UnidadProductora_Diagnosticos():
    """
    Función que lee la tabla UnidadProductora_Diagnosticos (por ahora no se usa
    en el llenado del PDF, pero la dejo tal cual la tenías, corregida).
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            UPD.id, UPD.idUnidadProductora, UPD.idDiagnostico,
            UP.id, UP.nombre, UP.agrupacion,
            D.id, D.nombre, D.codigo
        FROM UnidadProductora_Diagnosticos UPD
        INNER JOIN UnidadProductora UP ON UP.id = UPD.idUnidadProductora
        INNER JOIN Diagnosticos D ON D.id = UPD.idDiagnostico;
    """)
    rows = cursor.fetchall()
    conn.close()

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
            'codigo_d': row[8]
        }
        for row in rows
    ]


def dibujar_cabecera(page):
    """
    Dibuja la cabecera (año, mes, IPRESS, DNI responsable, etc.) en una página.
    """
    rango_ini_vert = 145

    # AÑO
    rango_ini_hori = 25
    page.insert_text((rango_ini_hori, rango_ini_vert), str(hoy.year), fontsize=6)

    # MES (nombre en mayúsculas)
    rango_ini_hori = 60
    page.insert_text((rango_ini_hori, rango_ini_vert), hoy.strftime("%B").upper(), fontsize=6)

    # NOMBRE IPRESS
    rango_ini_hori = 150
    page.insert_text((rango_ini_hori, rango_ini_vert), "HOSPITAL HUAYCAN", fontsize=6)

    # UNIDAD (por ahora vacío)
    rango_ini_hori = 330
    page.insert_text((rango_ini_hori, rango_ini_vert), "", fontsize=6)

    # DNI RESPONSABLE
    rango_ini_hori = 450
    page.insert_text((rango_ini_hori, rango_ini_vert), "20883195", fontsize=6)

    # NOMBRE RESPONSABLE
    rango_ini_hori = 502
    page.insert_text((rango_ini_hori, rango_ini_vert), "L. CANCHIHUAMAN V.", fontsize=6)


# ============================ LÓGICA PRINCIPAL ============================

def logicaGeneral():
    # Abrimos la plantilla
    plantilla = fitz.open(TEMPLATE_FILE)

    # Creamos documento de salida vacío
    doc = fitz.open()

    # Calculamos cuántas páginas se necesitan
    if len(datos) == 0:
        print("No hay datos en data.json")
        return

    num_paginas = (len(datos) + REGISTROS_POR_PAGINA - 1) // REGISTROS_POR_PAGINA

    # Insertamos una copia de la página 0 de la plantilla por cada página necesaria
    for _ in range(num_paginas):
        doc.insert_pdf(plantilla, from_page=0, to_page=0)

    plantilla.close()

    # Dibujamos la cabecera en cada página
    for i in range(num_paginas):
        page = doc[i]
        dibujar_cabecera(page)

    # --------------------- DETALLE POR PACIENTE ---------------------

    for idx, paciente in enumerate(datos):
        # Página y fila en esa página
        page_index = idx // REGISTROS_POR_PAGINA          # 0, 1, 2, ...
        row_index = idx % REGISTROS_POR_PAGINA            # 0..11
        offset = row_index * ROW_HEIGHT                   # desplazamiento vertical

        page = doc[page_index]

        nombre_pac = paciente["nombre"]
        dni_pac = paciente["dni"]
        hc_pac = paciente["h_clinica"]
        edad_pac = str(paciente["edad"])
        fn_pac = formato_fecha_dd_mm_aaaa(paciente["fecha_nacimiento"])

        # 1) NOMBRES PACIENTE
        page.insert_text((117, 183 + offset), nombre_pac, fontsize=6)

        # 2) FECHA HEMOGLOBINA (ejemplo fijo como tenías antes)
        #    Si quieres usar hoy:   f"{hoy.day:02d}     {hoy.month:02d}     {hoy.year}"
        page.insert_text((337, 183 + offset), "01     06     2025", fontsize=6)

        # 3) FECHA NACIMIENTO (del JSON)
        page.insert_text((522, 183 + offset), fn_pac, fontsize=6)

        # 4) DÍA (columna izquierda)
        page.insert_text((28, 205 + offset), str(hoy.day), fontsize=6)

        # 5) DNI PACIENTE
        page.insert_text((58, 193 + offset), dni_pac, fontsize=6)

        # 6) HISTORIA CLÍNICA
        page.insert_text((58, 205 + offset), hc_pac, fontsize=6)

        # 7) FICHA FAMILIAR (por ahora vacío)
        page.insert_text((58, 217 + offset), "", fontsize=6)

        # 8) FINANCIAMIENTO (fijo)
        page.insert_text((111, 197 + offset), "2", fontsize=6)

        # 9) ETNIA (fijo)
        page.insert_text((110, 214 + offset), "80", fontsize=6)

        # 10) DISTRITO (fijo)
        page.insert_text((130, 197 + offset), "ATE", fontsize=6)

        # 11) CENTRO POBLADO (fijo)
        page.insert_text((130, 214 + offset), "HUAYCAN", fontsize=6)

        # 12) EDAD (del JSON)
        page.insert_text((193, 205 + offset), edad_pac, fontsize=6)

        # 13) EDAD AÑO / MES / DÍA (marco años con X como ejemplo)
        page.insert_text((206, 197 + offset), "X", fontsize=14)  # años
        # page.insert_text((206, 209 + offset), "X", fontsize=14)  # meses
        # page.insert_text((206, 221 + offset), "X", fontsize=14)  # días

        # 14) SEXO (fijo en femenino; si añades 'sexo' al JSON, lo cambiamos)
        page.insert_text((220, 219 + offset), "X", fontsize=14)  # Femenino

        # 15) PC / PB / PESO / TALLA / HB (valores de ejemplo)
        page.insert_text((252, 197 + offset), "50", fontsize=6)   # PC
        page.insert_text((252, 215 + offset), "22", fontsize=6)   # PB
        page.insert_text((290, 193 + offset), "75", fontsize=6)   # Peso
        page.insert_text((289, 205 + offset), "156", fontsize=6)  # Talla
        page.insert_text((290, 217 + offset), "14", fontsize=6)   # Hb

        # 16) ESTABLECIMIENTO (N/C/R) – aquí solo marco N como ejemplo
        page.insert_text((310, 197 + offset), "X", fontsize=14)  # Establecimiento N
        # page.insert_text((310, 209 + offset), "X", fontsize=14)  # C
        # page.insert_text((310, 221 + offset), "X", fontsize=14)  # R

        # 17) SERVICIO (N/C/R) – aquí solo marco N
        page.insert_text((326, 197 + offset), "X", fontsize=14)  # Servicio N
        # page.insert_text((326, 209 + offset), "X", fontsize=14)  # C
        # page.insert_text((326, 221 + offset), "X", fontsize=14)  # R

        # 18) ACTIVIDADES
        page.insert_text((344, 194 + offset), "CONSEJERIA PRE TEST VIH", fontsize=5)
        page.insert_text((344, 206 + offset), "TAMIZAJE VIH", fontsize=5)
        page.insert_text((344, 218 + offset), "CONSEJERIA POST TEST VIH", fontsize=5)

        # 19) TIPO DIAGNÓSTICO P/D/R – solo ejemplo, todo en P1/D1/R1
        page.insert_text((502, 196 + offset), "X", fontsize=12)  # P1
        page.insert_text((514, 196 + offset), "X", fontsize=12)  # D1
        page.insert_text((526, 196 + offset), "X", fontsize=12)  # R1

        # 20) LABORATORIO 1/2/3
        page.insert_text((542, 194 + offset), "50", fontsize=6)
        page.insert_text((542, 206 + offset), "30", fontsize=6)
        page.insert_text((542, 218 + offset), "40", fontsize=6)

        # 21) CÓDIGO CIE CPT 1/2/3
        page.insert_text((565, 194 + offset), "50978.46", fontsize=6)
        page.insert_text((565, 206 + offset), "31403.58", fontsize=6)
        page.insert_text((565, 218 + offset), "40474.54", fontsize=6)

    # Guardar PDF generado
    doc.save("coordenadas_marcadasv2.pdf")
    doc.close()


# ============================ EJECUCIÓN ============================

if __name__ == "__main__":
    logicaGeneral()
