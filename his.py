import fitz  # PyMuPDF

doc = fitz.open("his.pdf")
page = doc[0]

# Dibuja marcadores con coordenadas
for x in range(0, 600, 50):
    for y in range(0, 800, 50):
        coord_text = f"({x},{y})"
        page.insert_text((x, y), coord_text, fontsize=6, color=(1, 0, 0))

page.insert_text((150, 175), "Juan Pérez", fontsize=7)
page.insert_text((150, 225), "Juan Pérez", fontsize=7)
page.insert_text((150, 275), "Juan Pérez", fontsize=7)

doc.save("coordenadas_marcadas.pdf")
