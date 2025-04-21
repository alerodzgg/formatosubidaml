import pandas as pd
import re  # Biblioteca para expresiones regulares

# Ruta del archivo
file_path = r"C:\Users\rodri\Downloads\publicaciones1.xlsx"

# Función para extraer secuencias de 4 o más números
def extraer_numeros(celda):
    if not isinstance(celda, str):
        return ""
    # Eliminar los guiones antes de buscar las secuencias
    celda = celda.replace("-", "")
    # Buscar secuencias de 4 o más números
    secuencias = re.findall(r'\d{4,}', celda)
    return " ".join(secuencias)  # Unir las secuencias encontradas con un espacio

# Leer todas las hojas del archivo Excel
hojas = pd.read_excel(file_path, sheet_name=None)

# Procesar cada hoja
for nombre_hoja, df in hojas.items():
    if 'OEM' in df.columns:
        # Crear una nueva columna OEM2 con los resultados extraídos
        df['OEM2'] = df['OEM'].apply(extraer_numeros)
    hojas[nombre_hoja] = df

# Guardar los cambios en el archivo Excel
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    for nombre_hoja, df in hojas.items():
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)

print("El archivo ha sido actualizado con la columna OEM2.")
