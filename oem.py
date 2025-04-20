import pandas as pd
import re  # Biblioteca para expresiones regulares

# Ruta del archivo
file_path = r"C:\Users\rodri\Downloads\publicaciones.xlsx"

# Función para filtrar palabras según las condiciones
def filtrar_palabras(celda):
    if not isinstance(celda, str):
        return ""
    palabras_filtradas = []
    # Dividir la celda en palabras
    palabras = celda.split()
    for palabra in palabras:
        # Contar números y letras en la palabra
        numeros = sum(c.isdigit() for c in palabra)
        letras = sum(c.isalpha() for c in palabra)
        # Verificar si cumple las condiciones
        if numeros > 5 and letras <= 4:
            palabras_filtradas.append(palabra)
    return " ".join(palabras_filtradas)

# Leer todas las hojas del archivo Excel
hojas = pd.read_excel(file_path, sheet_name=None)

# Procesar cada hoja
for nombre_hoja, df in hojas.items():
    if 'OEM' in df.columns:
        # Crear una nueva columna OEM2 con los resultados filtrados
        df['OEM2'] = df['OEM'].apply(filtrar_palabras)
    hojas[nombre_hoja] = df

# Guardar los cambios en el archivo Excel
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    for nombre_hoja, df in hojas.items():
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)
