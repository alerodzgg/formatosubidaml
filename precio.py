import random

import pandas as pd

# Ruta del archivo Excel
ruta_excel = "C:\\Users\\rodri\\Downloads\\conca - Copy.xlsx"

# Diccionario de rangos y valores para actualizar la columna "Tabla2.precio"
rangos_valores = {
    (1, 35): 4410,
    (35, 44): 5384,
    (45, 49): 5825,
    (50, 54): 6375,
    (55, 59): 6705,
    (60, 69): 7036,
    (70, 79): 7477,
    (80, 89): 7919,
    (90, 99): 8360,
    (100, 109): 8801,
    (110, 119): 9243,
    (120, 129): 9684,
    (130, 139): 10125,
    (140, 149): 10567,
    (150, 159): 11008,
    (160, 169): 11450,
    (170, 179): 11891,
    (180, 189): 12332,
    (190, 199): 12774,
    (200, 249): 13215,
    (250, 299): 14545,
    (300, 349): 15874,
    (350, 399): 17203,
    (400, 449): 18533,
    (450, 499): 19862,
    (500, 549): 21192,
    (550, 599): 22521,
    (600, 649): 23850,
    (650, 699): 25180,
    (700, 799): 26509,
    (800, 999): 28949,
    (1000, 2000): 33608,
}

# Leer el archivo Excel Leer el archivo Excel
df = pd.read_excel(ruta_excel)

# Convertir la columna "Tabla2.precio" a numérica
df['Tabla2.precio'] = pd.to_numeric(df['Tabla2.precio'], errors='coerce')

# Actualizar la columna "Tabla2.precio" usando los rangos
for rango, valor in rangos_valores.items():
    inicio, fin = rango
    for i in df.index:
        if (df.loc[i, 'Tabla2.precio'] >= inicio) & (df.loc[i, 'Tabla2.precio'] <= fin):
            nuevo_valor = valor + random.randint(1, 500)
            while nuevo_valor == df.loc[i, 'Tabla2.precio']:
                nuevo_valor = valor + random.randint(1, 500)
            df.loc[i, 'Tabla2.precio'] = nuevo_valor

# Guardar los cambios en el archivo Excel original
df.to_excel(ruta_excel, index=False)

print("Los valores de la columna 'Tabla2.precio' se han actualizado correctamente.")
