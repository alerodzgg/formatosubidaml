import os
from openpyxl import load_workbook
import pandas as pd

# Ruta de la carpeta con los archivos Excel
ruta_carpeta = r"C:\Users\rodri\Downloads\compilacion"

# Lista para almacenar los datos combinados
datos_combinados = []

# Columnas a extraer (basadas en índices de Excel: A=0, E=4, F=5, G=6, T=19, U=20)
columnas_a_extraer = [0, 4, 5, 6, 19, 20]

# Recorre todos los archivos .xlsx en la carpeta
for archivo in os.listdir(ruta_carpeta):
    if archivo.endswith(".xlsx"):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        try:
            wb = load_workbook(ruta_archivo, data_only=True)

            # Recorre todas las hojas del archivo
            for hoja in wb.sheetnames:
                if hoja == "MLM-CARS_AND_VANS":  # Saltar la hoja especificada
                    continue

                ws = wb[hoja]
                datos_hoja = []

                # Extraer datos de las columnas especificadas
                for fila in ws.iter_rows(min_row=2, values_only=True):  # Saltar la fila de encabezados
                    fila_extraida = [fila[i] for i in columnas_a_extraer if i < len(fila)]
                    datos_hoja.append(fila_extraida)

                # Agregar los datos de la hoja a la lista principal
                datos_combinados.extend(datos_hoja)

        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")

# Crear un DataFrame con los datos combinados
df_combinado = pd.DataFrame(datos_combinados, columns=["A", "E", "F", "G", "T", "U"])

# Dividir el DataFrame en partes de 500,000 filas y guardar en un archivo Excel
ruta_salida = os.path.join(ruta_carpeta, "combinado.xlsx")
with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
    for i in range(0, len(df_combinado), 500000):
        df_combinado.iloc[i:i+500000].to_excel(writer, sheet_name=f"Parte_{i//500000 + 1}", index=False)

print(f"Archivo combinado guardado en: {ruta_salida}")
