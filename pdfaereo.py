import os

import fitz

ruta_carpeta_origen = r"C:\Users\rodri\Downloads\guiasaereas"
ruta_pdf_combinado = r"C:\Users\rodri\Downloads\combinado.pdf"  # Ruta del PDF final

def dibujar_rectangulo(pagina):
    ancho_pagina, alto_pagina = pagina.rect.width, pagina.rect.height
    centro_x, centro_y = ancho_pagina / 1.3, alto_pagina / 4.7
    ancho_rectangulo, alto_rectangulo = 100, 50
    rectangulo = fitz.Rect(
        centro_x - ancho_rectangulo / 2,
        centro_y - alto_rectangulo / 2,
        centro_x + ancho_rectangulo / 2,
        centro_y + alto_rectangulo / 2
    )
    pagina.draw_rect(rectangulo, color=(1, 1, 1), fill=(0, 0, 0, 0))

if __name__ == "__main__":
    documento_combinado = fitz.open()  # Crear un nuevo documento vacío
    for nombre_archivo in os.listdir(ruta_carpeta_origen):
        if nombre_archivo.endswith(".pdf"):
            ruta_pdf = os.path.join(ruta_carpeta_origen, nombre_archivo)
            documento_original = fitz.open(ruta_pdf)
            for pagina in documento_original:
                dibujar_rectangulo(pagina)
                documento_combinado.insert_pdf(documento_original, from_page=pagina.number, to_page=pagina.number)
    documento_combinado.save(ruta_pdf_combinado, garbage=4, deflate=True, clean=True)
    print("PDF combinado guardado en:", ruta_pdf_combinado)
