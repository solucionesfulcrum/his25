import fitz  # PyMuPDF
from datetime import date
import locale
import sqlite3

DB_FILE = "HIS25.db"

locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

hoy = date.today()

datos = [
  {
    "nombre": "KARINA PUJAY CLAUDIO",
    "H. CL.": "281302",
    "DNI": "76795677",
    "FN": "16/06/1995",
    "EDAD": 30
  },
  {
    "nombre": "AYME JHAHAIRA ESTREMADOYRO JAUREGUI",
    "H. CL.": "24947",
    "DNI": "74730076",
    "FN": "9/02/1995",
    "EDAD": 30
  },
  {
    "nombre": "SISLY BRENDA MARTINEZ GUERRA",
    "H. CL.": "47181",
    "DNI": "60235681",
    "FN": "2/03/2000",
    "EDAD": 25
  },
  {
    "nombre": "SOLEDAD MILAGROS ALCANTARA CONDORI",
    "H. CL.": "43053",
    "DNI": "43602838",
    "FN": "27/06/1986",
    "EDAD": 39
  },
  {
    "nombre": "MARIASABETH GINA GOMEZ LIZANA",
    "H. CL.": "162577",
    "DNI": "72957842",
    "FN": "3/07/1999",
    "EDAD": 25
  },
  {
    "nombre": "CATNHERINE MAVILA CASTRO CARIJANO",
    "H. CL.": "41773",
    "DNI": "73936090",
    "FN": "30/11/1996",
    "EDAD": 28
  },
  {
    "nombre": "ELVITA FLOR ZAVALETA AGUILAR",
    "H. CL.": "281675",
    "DNI": "48623291",
    "FN": "29/08/1995",
    "EDAD": 29
  },
  {
    "nombre": "ROXANA Marisol ALIAGA LADERA",
    "H. CL.": "162997",
    "DNI": "47038535",
    "FN": "25/12/1991",
    "EDAD": 33
  },
  {
    "nombre": "GABRIELA HERRERA GERONIMO",
    "H. CL.": "281705",
    "DNI": "60244256",
    "FN": "18/03/2004",
    "EDAD": 22
  },
  {
    "nombre": "MARISOL Soleyn RODRIGUEZ ARIAS",
    "H. CL.": "118800",
    "DNI": "48052783",
    "FN": "31/01/1993",
    "EDAD": 32
  },
  {
    "nombre": "JOHANA CRISS ORTIZ COLOME",
    "H. CL.": "278754",
    "DNI": "61006154",
    "FN": "13/12/1994",
    "EDAD": 30
  },
  {
    "nombre": "JANETH MARIBEL PACHECO PIO",
    "H. CL.": "43543",
    "DNI": "61943474",
    "FN": "15/07/1999",
    "EDAD": 25
  }]

def llenadoPdf(cantidad_registro, page, rango_ini_hori, nombre, tamano_fuente, distancia_vert, rango_ini_vert, siguiente):    


    #for x in range(cantidad_registro):
        page.insert_text((rango_ini_hori, rango_ini_vert), nombre, fontsize=tamano_fuente)

def llenadoPdf1(cantidad_registro, page, rango_ini_hori, nombre, tamano_fuente, distancia_vert, rango_ini_vert, siguiente):    

    for x in range(cantidad_registro):
        page.insert_text((rango_ini_hori, rango_ini_vert), nombre, fontsize=tamano_fuente)
        rango_ini_vert += distancia_vert * siguiente

def obtener_UnidadProductora_Diagnosticos():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""SELECT UPD.id, UPD.idUnidadProductora, UPD.idDiagnostico, UP.id, 
UP.nombre, UP.agrupacion, D.id, D.nombre, D.codigo  
FROM UnidadProductora_Diagnosticos UPD
INNER JOIN UnidadProductora UP ON UP.id = UPD.idUnidadProductora
INNER JOIN Diagnosticos D ON D.id = UPD.idDiagnostico;""")
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    return [{'id_upd': row[0], 'idUnidadProductora': row[1], 'nombre_up': row[2], 
             'agrupacion_up': row[3], 'id_d': row[4], 'id_d': row[5], 'nombre_d': row[6], 
             'codigo_d': row[6]} for row in rows]


def logicaGeneral():
    #doc = fitz.open("coordenadas_marcadas.pdf")
    doc = fitz.open("his.pdf")
    page = doc[0]

    # Dibuja marcadores con coordenadas
    """for x in range(0, 600, 25):
        for y in range(0, 800, 2):
            coord_text = f"({x},{y})"
            page.insert_text((x, y), coord_text, fontsize=2, fontname="Times-Bold", color=(1, 0, 0))"""

    #AÑO
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 25
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = str(hoy.year)
    siguiente = 0
    llenadoPdf1(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, 
               siguiente = siguiente)

    #MES
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 60
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = str(hoy.strftime("%B").upper())
    siguiente = 0
    llenadoPdf1(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
               siguiente = siguiente)
    
    #NOMBRE IPRESS
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 150
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "HOSPITAL HUAYCAN"
    siguiente = 0
    llenadoPdf1(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
               siguiente = siguiente)

    unidadProductora_diagnostico = obtener_UnidadProductora_Diagnosticos()
    #print(unidadProductora_diagnostico)

    #UNIDAD
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 330
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = ""
    siguiente = 0
    llenadoPdf1(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
               siguiente = siguiente)

    #DNI
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 450
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "20883195"
    siguiente = 0
    llenadoPdf1(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
               siguiente = siguiente)

    #NOMBRE
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 502
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "L. CANCHIHUAMAN V. "
    siguiente = 0
    llenadoPdf1(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
               siguiente = siguiente)
    for x in range(len(datos)):
        #NOMBRES PACIENTE
        rango_ini_vert = 183
        distancia_vert = 46.4
        rango_ini_hori = 117
        tamano_fuente = 4
        cantidad_registro = 12
        nombre = datos[x]["nombre"]
        siguiente = x
        rango_ini_vert += distancia_vert * siguiente

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert, 
                siguiente = siguiente)
            
        #FECHA HEMOGLOBINA
        rango_ini_vert = 183
        distancia_vert = 46.4
        rango_ini_hori = 337
        tamano_fuente = 6
        cantidad_registro = 3
        nombre = ""
        siguiente = x
        rango_ini_vert += distancia_vert * siguiente
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
    
        #FECHA NACIMIENTO
        rango_ini_vert = 183
        distancia_vert = 46.4
        rango_ini_hori = 522
        tamano_fuente = 6
        cantidad_registro = 12
        nombre = datos[x]["FN"]
        siguiente = x
        rango_ini_vert += distancia_vert * siguiente
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)

        #DIA
        rango_ini_vert = 205
        distancia_vert = 46.4
        rango_ini_hori = 28
        tamano_fuente = 6
        cantidad_registro = 12
        nombre = "28"
        siguiente = x
        rango_ini_vert += distancia_vert * siguiente
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #DNI
        rango_ini_vert = 193
        distancia_vert = 46.4
        rango_ini_hori = 58
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = datos[x]["DNI"]
        siguiente = x
        rango_ini_vert += distancia_vert * siguiente
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #HISTORIA CLINICA
        rango_ini_vert = 205
        distancia_vert = 46.4
        rango_ini_hori = 58
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = datos[x]["H. CL."]
        siguiente = x
        rango_ini_vert += distancia_vert * siguiente
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #FICHA FAMILIAR
        rango_ini_vert = 217
        distancia_vert = 46.4
        rango_ini_hori = 58
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = ""
        siguiente = 2
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #FINANCIAMIENTO
        rango_ini_vert = 197
        distancia_vert = 46.4
        rango_ini_hori = 111
        tamano_fuente = 6
        cantidad_registro = 12
        nombre = "2"
        siguiente = 1
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ETNIA
        rango_ini_vert = 214
        distancia_vert = 46.4
        rango_ini_hori = 110
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "80"
        siguiente = 1
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #DISTRITO
        rango_ini_vert = 197
        distancia_vert = 46.4
        rango_ini_hori = 130
        tamano_fuente = 6
        cantidad_registro = 12
        nombre = "ATE"
        siguiente = 1
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #CENTRO POBLADO
        rango_ini_vert = 214
        distancia_vert = 46.4
        rango_ini_hori = 130
        tamano_fuente = 6
        cantidad_registro = 12
        nombre = "HUAYCAN"
        siguiente = 1
        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #EDAD
        rango_ini_vert = 205
        distancia_vert = 46.4
        rango_ini_hori = 193
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "21"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #EDADAÑO
        rango_ini_vert = 197
        distancia_vert = 46.4
        rango_ini_hori = 206
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #EDADMES
        rango_ini_vert = 209
        distancia_vert = 46.4
        rango_ini_hori = 206
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #EDADDIA
        rango_ini_vert = 221
        distancia_vert = 46.4
        rango_ini_hori = 206
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #SEXOMAS
        rango_ini_vert = 200
        distancia_vert = 46.4
        rango_ini_hori = 220
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #SEXOFEM
        rango_ini_vert = 219
        distancia_vert = 46.4
        rango_ini_hori = 220
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #PC
        rango_ini_vert = 197
        distancia_vert = 46.4
        rango_ini_hori = 252
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "50"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #PB
        rango_ini_vert = 215
        distancia_vert = 46.4
        rango_ini_hori = 252
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "22"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #PESO
        rango_ini_vert = 193
        distancia_vert = 46.4
        rango_ini_hori = 290
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "75"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TALLA
        rango_ini_vert = 205
        distancia_vert = 46.4
        rango_ini_hori = 289
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "156"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #HB
        rango_ini_vert = 217
        distancia_vert = 46.4
        rango_ini_hori = 290
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "14"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ESTABLECIMIENTO N
        rango_ini_vert = 197
        distancia_vert = 46.4
        rango_ini_hori = 310
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ESTABLECIMIENTO C
        rango_ini_vert = 209
        distancia_vert = 46.4
        rango_ini_hori = 310
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ESTABLECIMIENTO R
        rango_ini_vert = 221
        distancia_vert = 46.4
        rango_ini_hori = 310
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #SERVICIO N
        rango_ini_vert = 197
        distancia_vert = 46.4
        rango_ini_hori = 326
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #SERVICIO C
        rango_ini_vert = 209
        distancia_vert = 46.4
        rango_ini_hori = 326
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #SERVICIO R
        rango_ini_vert = 221
        distancia_vert = 46.4
        rango_ini_hori = 326
        tamano_fuente = 14
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ACTIVIDAD 1
        rango_ini_vert = 194
        distancia_vert = 46.4
        rango_ini_hori = 344
        tamano_fuente = 5
        cantidad_registro = 6
        nombre = "CONSEJERIA PRE TEST VIH"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ACTIVIDAD 2
        rango_ini_vert = 206
        distancia_vert = 46.4
        rango_ini_hori = 344
        tamano_fuente = 5
        cantidad_registro = 6
        nombre = "TAMIZAJE VIH"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #ACTIVIDAD 3
        rango_ini_vert = 218
        distancia_vert = 46.4
        rango_ini_hori = 344
        tamano_fuente = 5
        cantidad_registro = 6
        nombre = "CONSEJERIA POST TEST VIH"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO P 1
        rango_ini_vert = 196
        distancia_vert = 46.4
        rango_ini_hori = 502
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO P 2
        rango_ini_vert = 208
        distancia_vert = 46.4
        rango_ini_hori = 502
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO P 3
        rango_ini_vert = 220
        distancia_vert = 46.4
        rango_ini_hori = 502
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO D 1
        rango_ini_vert = 196
        distancia_vert = 46.4
        rango_ini_hori = 514    
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO D 2
        rango_ini_vert = 208
        distancia_vert = 46.4
        rango_ini_hori = 514
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO D 3
        rango_ini_vert = 220
        distancia_vert = 46.4
        rango_ini_hori = 514
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO R 1
        rango_ini_vert = 196
        distancia_vert = 46.4
        rango_ini_hori = 526 
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO R 2
        rango_ini_vert = 208
        distancia_vert = 46.4
        rango_ini_hori = 526
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #TIPO DIAGNOSTICO R 3
        rango_ini_vert = 220
        distancia_vert = 46.4
        rango_ini_hori = 526
        tamano_fuente = 12
        cantidad_registro = 6
        nombre = "X"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #LABORATORIO 1
        rango_ini_vert = 194
        distancia_vert = 46.4
        rango_ini_hori = 542
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "50"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #LABORATORIO 2
        rango_ini_vert = 206
        distancia_vert = 46.4
        rango_ini_hori = 542
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "30"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #LABORATORIO 3
        rango_ini_vert = 218
        distancia_vert = 46.4
        rango_ini_hori = 542
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "40"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #CODIGO CIE CPT 1
        rango_ini_vert = 194
        distancia_vert = 46.4
        rango_ini_hori = 565
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "50978.46"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #CODIGO CIE CPT 2
        rango_ini_vert = 206
        distancia_vert = 46.4
        rango_ini_hori = 565
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "31403.58"
        siguiente = 2

        llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
                tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
                siguiente = siguiente)
        
        #CODIGO CIE CPT 3
        rango_ini_vert = 218
        distancia_vert = 46.4
        rango_ini_hori = 565
        tamano_fuente = 6
        cantidad_registro = 6
        nombre = "40474.54"
        siguiente = 2

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert,
               siguiente = siguiente)
    
    # Guardar sobrescribiendo
    #doc.save("coordenadas_marcadas.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.save("coordenadas_marcadas.pdf")
    # Cerrar documento
    doc.close()

logicaGeneral()