import fitz  # PyMuPDF

def llenadoPdf(cantidad_registro, page, rango_ini_hori, nombre, tamano_fuente, distancia_vert, rango_ini_vert):    
    for x in range(cantidad_registro):
        page.insert_text((rango_ini_hori, rango_ini_vert), nombre, fontsize=tamano_fuente)
        rango_ini_vert += distancia_vert


def logicaGeneral():
    #doc = fitz.open("coordenadas_marcadas.pdf")
    doc = fitz.open("his.pdf")
    page = doc[0]

    # Dibuja marcadores con coordenadas
    """for x in range(0, 600, 25):
        for y in range(0, 800, 2):
            coord_text = f"({x},{y})"
            page.insert_text((x, y), coord_text, fontsize=2, fontname="Times-Bold", color=(1, 0, 0))"""

    #NOMBRES PACIENTE
    rango_ini_vert = 183
    distancia_vert = 46.4
    rango_ini_hori = 117
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "Juan Pérez"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #AÑO
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 25
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "2025"
    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)

    #MES
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 60
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "MAYO"
    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #NOMBRE IPRESS
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 150
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "HOSPITAL HUAYCAN"
    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)

    #UNIDAD
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 330
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "ITS PG"
    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)

    #DNI
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 450
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "20883195"
    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)

    #NOMBRE
    rango_ini_vert = 145
    distancia_vert = 0
    rango_ini_hori = 502
    distancia_vert = 0
    tamano_fuente = 6
    cantidad_registro = 1
    nombre = "CANCHIHUAMAN VILLEGAS LIRMA"
    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
        
    #FECHA HEMOGLOBINA
    rango_ini_vert = 183
    distancia_vert = 46.4
    rango_ini_hori = 337
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "01     06     2025"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
   
    #FECHA NACIMIENTO
    rango_ini_vert = 183
    distancia_vert = 46.4
    rango_ini_hori = 522
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "01     06     2025"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)

    #DIA
    rango_ini_vert = 205
    distancia_vert = 46.4
    rango_ini_hori = 28
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "28"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #DNI
    rango_ini_vert = 193
    distancia_vert = 46.4
    rango_ini_hori = 58
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "72412676"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #HISTORIA CLINICA
    rango_ini_vert = 205
    distancia_vert = 46.4
    rango_ini_hori = 58
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "72412676"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #FICHA FAMILIAR
    rango_ini_vert = 217
    distancia_vert = 46.4
    rango_ini_hori = 58
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "72412676"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #FINANCIAMIENTO
    rango_ini_vert = 197
    distancia_vert = 46.4
    rango_ini_hori = 111
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "2"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ETNIA
    rango_ini_vert = 214
    distancia_vert = 46.4
    rango_ini_hori = 110
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "80"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #DISTRITO
    rango_ini_vert = 197
    distancia_vert = 46.4
    rango_ini_hori = 130
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "ATE"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #CENTRO POBLADO
    rango_ini_vert = 214
    distancia_vert = 46.4
    rango_ini_hori = 130
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "HUAYCAN"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #EDAD
    rango_ini_vert = 205
    distancia_vert = 46.4
    rango_ini_hori = 193
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "21"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #EDADAÑO
    rango_ini_vert = 197
    distancia_vert = 46.4
    rango_ini_hori = 206
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #EDADMES
    rango_ini_vert = 209
    distancia_vert = 46.4
    rango_ini_hori = 206
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #EDADDIA
    rango_ini_vert = 221
    distancia_vert = 46.4
    rango_ini_hori = 206
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #SEXOMAS
    rango_ini_vert = 200
    distancia_vert = 46.4
    rango_ini_hori = 220
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #SEXOFEM
    rango_ini_vert = 219
    distancia_vert = 46.4
    rango_ini_hori = 220
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #PC
    rango_ini_vert = 197
    distancia_vert = 46.4
    rango_ini_hori = 252
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "50"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #PB
    rango_ini_vert = 215
    distancia_vert = 46.4
    rango_ini_hori = 252
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "22"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #PESO
    rango_ini_vert = 193
    distancia_vert = 46.4
    rango_ini_hori = 290
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "75"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TALLA
    rango_ini_vert = 205
    distancia_vert = 46.4
    rango_ini_hori = 289
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "156"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #HB
    rango_ini_vert = 217
    distancia_vert = 46.4
    rango_ini_hori = 290
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "14"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ESTABLECIMIENTO N
    rango_ini_vert = 197
    distancia_vert = 46.4
    rango_ini_hori = 310
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ESTABLECIMIENTO C
    rango_ini_vert = 209
    distancia_vert = 46.4
    rango_ini_hori = 310
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ESTABLECIMIENTO R
    rango_ini_vert = 221
    distancia_vert = 46.4
    rango_ini_hori = 310
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #SERVICIO N
    rango_ini_vert = 197
    distancia_vert = 46.4
    rango_ini_hori = 326
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #SERVICIO C
    rango_ini_vert = 209
    distancia_vert = 46.4
    rango_ini_hori = 326
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #SERVICIO R
    rango_ini_vert = 221
    distancia_vert = 46.4
    rango_ini_hori = 326
    tamano_fuente = 14
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ACTIVIDAD 1
    rango_ini_vert = 194
    distancia_vert = 46.4
    rango_ini_hori = 344
    tamano_fuente = 5
    cantidad_registro = 12
    nombre = "CONSEJERIA PRE TEST VIH"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ACTIVIDAD 2
    rango_ini_vert = 206
    distancia_vert = 46.4
    rango_ini_hori = 344
    tamano_fuente = 5
    cantidad_registro = 12
    nombre = "TAMIZAJE VIH"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #ACTIVIDAD 3
    rango_ini_vert = 218
    distancia_vert = 46.4
    rango_ini_hori = 344
    tamano_fuente = 5
    cantidad_registro = 12
    nombre = "CONSEJERIA POST TEST VIH"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO P 1
    rango_ini_vert = 196
    distancia_vert = 46.4
    rango_ini_hori = 502
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO P 2
    rango_ini_vert = 208
    distancia_vert = 46.4
    rango_ini_hori = 502
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO P 3
    rango_ini_vert = 220
    distancia_vert = 46.4
    rango_ini_hori = 502
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO D 1
    rango_ini_vert = 196
    distancia_vert = 46.4
    rango_ini_hori = 514    
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO D 2
    rango_ini_vert = 208
    distancia_vert = 46.4
    rango_ini_hori = 514
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO D 3
    rango_ini_vert = 220
    distancia_vert = 46.4
    rango_ini_hori = 514
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO R 1
    rango_ini_vert = 196
    distancia_vert = 46.4
    rango_ini_hori = 526 
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO R 2
    rango_ini_vert = 208
    distancia_vert = 46.4
    rango_ini_hori = 526
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #TIPO DIAGNOSTICO R 3
    rango_ini_vert = 220
    distancia_vert = 46.4
    rango_ini_hori = 526
    tamano_fuente = 12
    cantidad_registro = 12
    nombre = "X"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #LABORATORIO 1
    rango_ini_vert = 194
    distancia_vert = 46.4
    rango_ini_hori = 542
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "50"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #LABORATORIO 2
    rango_ini_vert = 206
    distancia_vert = 46.4
    rango_ini_hori = 542
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "30"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #LABORATORIO 3
    rango_ini_vert = 218
    distancia_vert = 46.4
    rango_ini_hori = 542
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "40"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #CODIGO CIE CPT 1
    rango_ini_vert = 194
    distancia_vert = 46.4
    rango_ini_hori = 565
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "50978.46"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #CODIGO CIE CPT 2
    rango_ini_vert = 206
    distancia_vert = 46.4
    rango_ini_hori = 565
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "31403.58"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    #CODIGO CIE CPT 3
    rango_ini_vert = 218
    distancia_vert = 46.4
    rango_ini_hori = 565
    tamano_fuente = 6
    cantidad_registro = 12
    nombre = "40474.54"

    llenadoPdf(cantidad_registro=cantidad_registro, page=page, rango_ini_hori=rango_ini_hori, nombre=nombre, 
               tamano_fuente=tamano_fuente, distancia_vert=distancia_vert, rango_ini_vert=rango_ini_vert)
    
    # Guardar sobrescribiendo
    #doc.save("coordenadas_marcadas.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.save("coordenadas_marcadas.pdf")
    # Cerrar documento
    doc.close()

logicaGeneral()