import glob
import os
import pandas as pd

# Ruta a la carpeta con los archivos CSV
ruta_carpeta = r'C:\Users\rodri\Downloads\compilacion'

# Lista para almacenar los DataFrames de cada archivo
dfs = []

# Recorre todos los archivos CSV en la carpeta
for archivo in glob.glob(os.path.join(ruta_carpeta, "*.csv")):
    try:
        # Lee el archivo CSV, seleccionando las columnas desde 'A' hasta 'H'
        df = pd.read_csv(archivo, usecols=range(8))  # Selecciona las primeras 8 columnas (A-H)
        dfs.append(df)
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")

# Concatena todos los DataFrames en uno solo
df_combinado = pd.concat(dfs, ignore_index=True)

# Elimina filas con valores NaN en todas las columnas (opcional)
df_combinado.dropna(how='all', inplace=True)

# Guarda el DataFrame combinado en un nuevo archivo CSV
ruta_salida = os.path.join(ruta_carpeta, "terminado.csv")
try:
    df_combinado.to_csv(ruta_salida, index=False)
    print(f"Archivo 'terminado.csv' creado exitosamente en {ruta_carpeta}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
