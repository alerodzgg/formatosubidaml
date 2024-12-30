import csv

def reemplazar_nbsp(archivo_entrada, archivo_salida):
    """Reemplaza los nbsp por espacios normales en un archivo CSV.

    Args:
        archivo_entrada: Ruta del archivo CSV de entrada.
        archivo_salida: Ruta del archivo CSV de salida.
    """

    with open(archivo_entrada, 'r', encoding='utf-8') as infile, \
            open(archivo_salida, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Reemplaza los nbsp por espacios en cada celda de la fila
            row = [celda.replace('\xa0', ' ') for celda in row]
            writer.writerow(row)

# Ruta del archivo de entrada
archivo_entrada = "C:\\Users\\rodri\\Downloads\\alan-db.csv"

# Ruta del archivo de salida
archivo_salida = "C:\\Users\\rodri\\Downloads\\almanuevo_procesado.csv"  # Añade el nombre del archivo

reemplazar_nbsp(archivo_entrada, archivo_salida)

print(f"Se ha procesado el archivo '{archivo_entrada}' y se ha guardado como '{archivo_salida}'.")
