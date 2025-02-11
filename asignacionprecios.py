import random
import pandas as pd

# Ruta del archivo Excel
ruta_excel = "C:\\Users\\rodri\\Downloads\publicaciones.xlsx"

# Diccionario de rangos y valores para actualizar la columna "Tabla2.precio"
rangos_valores = {
    (1, 34): 5879,
    (35, 44): 7178,
    (45, 49): 7767,
    (50, 54): 8500,
    (55, 59): 8940,
    (60, 69): 9381,
    (70, 79): 9969,
    (80, 89): 10558,
    (90, 99): 11146,
    (100, 109): 11735,
    (110, 119): 12323,
    (120, 129): 12912,
    (130, 139): 13500,
    (140, 149): 14089,
    (150, 159): 14677,
    (160, 169): 15266,
    (170, 179): 15854,
    (180, 189): 16443,
    (190, 199): 17031,
    (200, 249): 17620,
    (250, 299): 19392,
    (300, 349): 21165,
    (350, 399): 22937,
    (400, 449): 24710,
    (450, 499): 26482,
    (500, 549): 28255,
    (550, 599): 30028,
    (600, 649): 31800,
    (650, 699): 33573,
    (700, 799): 35345,
    (800, 999): 38598,
    (1000, 2000): 44811,
}

# Leer el archivo Excel
df = pd.read_excel(ruta_excel)

# Columna a actualizar
columna_a_actualizar = 'Tabla2.precio'

# Iterar sobre las filas del DataFrame
for index, row in df.iterrows():
    valor_original = row[columna_a_actualizar]

    # Buscar el rango correspondiente al valor original
    for rango, valor_nuevo_base in rangos_valores.items():
        inicio, fin = rango
        if inicio <= valor_original <= fin:
            # Generar un nuevo valor aleatorio dentro de un rango (-500 a +500)
            nuevo_valor = valor_nuevo_base + random.randint(-500, 500)

            # Asegurarse de que el nuevo valor sea diferente al original
            while nuevo_valor == valor_original:
                nuevo_valor = valor_nuevo_base + random.randint(-500, 500)

            # Actualizar el valor en el DataFrame
            df.loc[index, columna_a_actualizar] = nuevo_valor
            break  # Importante: salir del bucle interno una vez encontrado el rango

# Guardar los cambios en el archivo Excel original
df.to_excel(ruta_excel, index=False)

print("Los valores de la columna 'Tabla2.precio' se han actualizado correctamente.")
