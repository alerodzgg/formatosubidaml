import random
import pandas as pd

# Ruta del archivo Excel
ruta_excel = "C:\\Users\\rodri\\Downloads\\publicaciones.xlsx"

# Diccionario de rangos y valores para actualizar la columna "Tabla2.precio"
rangos_valores = {
    (1, 14): 5749,
    (15, 19): 6472,
    (20, 24): 7021,
    (25, 29): 7252,
    (30, 39): 7483,
    (40, 44): 7882,
    (45, 49): 8113,
    (50, 54): 8344,
    (55, 59): 8575,
    (60, 64): 8806,
    (65, 69): 9037,
    (70, 74): 9268,
    (75, 79): 9500,
    (80, 84): 9731,
    (85, 89): 9962,
    (90, 94): 10193,
    (95, 99): 10424,
    (100, 109): 10719,
    (110, 119): 11181,
    (120, 129): 11643,
    (130, 139): 12296,
    (140, 149): 12949,
    (150, 159): 13919,
    (160, 164): 14889,
    (165, 169): 15692,
    (170, 174): 16495,
    (175, 179): 16980,
    (180, 184): 16195,
    (185, 189): 16680,
    (190, 199): 17165,
    (200, 224): 18136,
    (225, 249): 19291,
    (250, 274): 20447,
    (275, 299): 21603,
    (300, 324): 22758,
    (325, 349): 24232,
    (350, 374): 25705,
    (375, 399): 27178,
    (400, 424): 28651,
    (425, 449): 30759,
    (450, 474): 32868,
    (475, 499): 34976,
    (500, 524): 37084,
    (525, 549): 39192,
    (550, 574): 41300,
    (575, 599): 43409,
    (600, 624): 45517,
    (625, 649): 47625,
    (650, 699): 49733,
    (700, 724): 52680,
    (725, 749): 54788,
    (750, 799): 56896,
    (800, 824): 59842,
    (825, 849): 61316,
    (850, 874): 62789,
    (875, 899): 64262,
    (900, 924): 65735,
    (925, 949): 67843,
    (950, 999): 69317,
    (1000, 1025): 71628,
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
            # Generar un nuevo valor aleatorio sumando un número entre 100 y 199
            nuevo_valor = valor_nuevo_base + random.randint(100, 199)

            # Asegurarse de que el nuevo valor sea diferente al original
            while nuevo_valor == valor_original:
                nuevo_valor = valor_nuevo_base + random.randint(100, 199)

            # Actualizar el valor en el DataFrame
            df.loc[index, columna_a_actualizar] = nuevo_valor
            break  # Importante: salir del bucle interno una vez encontrado el rango

# Guardar los cambios en el archivo Excel original
df.to_excel(ruta_excel, index=False)

print("Los valores de la columna 'Tabla2.precio' se han actualizado correctamente.")
