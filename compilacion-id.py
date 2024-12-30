import glob
import os

import openpyxl
import pandas as pd

# Ruta a la carpeta con los archivos xlsx
ruta_carpeta = r'C:\Users\rodri\Downloads\compilacion'

# Lista para almacenar los DataFrames de cada hoja
dfs = []

# Recorre todos los archivos xlsx en la carpeta
for archivo in glob.glob(os.path.join(ruta_carpeta, "*.xlsx")):
    try:
        # Carga el archivo Excel con openpyxl para acceder a las hojas
        wb = openpyxl.load_workbook(archivo, read_only=True) # read_only para optimizar si son archivos grandes

        # Itera sobre cada hoja del libro
        for nombre_hoja in wb.sheetnames:
            try:
                # Lee la hoja especificada, solo la columna 'A' y la nombra 'Id'
                df = pd.read_excel(archivo, sheet_name=nombre_hoja, usecols="A", names=['Id'])
                dfs.append(df)
            except Exception as e:
                print(f"Error al leer la hoja '{nombre_hoja}' en {archivo}: {e}")

        wb.close() # Cierra el archivo para liberar recursos

    except Exception as e:
        print(f"Error al leer {archivo}: {e}")

# Concatena todos los DataFrames en uno solo
df_combinado = pd.concat(dfs, ignore_index=True)

# Elimina filas con valores NaN en la columna 'Id' (opcional)
df_combinado.dropna(subset=['Id'], inplace=True)


# Guarda el DataFrame combinado en un nuevo archivo xlsx
ruta_salida = os.path.join(ruta_carpeta, "terminado.xlsx")
try:
    df_combinado.to_excel(ruta_salida, index=False)
    print(f"Archivo 'terminado.xlsx' creado exitosamente en {ruta_carpeta}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
