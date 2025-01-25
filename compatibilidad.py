import pandas as pd

def buscar_y_combinar_valores(ruta_archivo_excel):
    """
    Busca una o más coincidencias de la columna 'Combinada' de Tabla1 en la columna 'Combinada' de Tabla2
    y concatena los valores correspondientes de la columna 'Producto_Id' de Tabla2 en la columna H de Tabla1.

    Args:
        ruta_archivo_excel (str): Ruta al archivo Excel que contiene las tablas.

    Returns:
        pandas.DataFrame: El DataFrame de Tabla1 con la nueva columna 'H'.
    """

    try:
        # Cargar el archivo Excel, especificando los nombres de hojas
        excel_file = pd.ExcelFile(ruta_archivo_excel)
        try:
          tabla1 = excel_file.parse("tabla1", header=0)
        except ValueError as e:
          print(f"Error al cargar la hoja 'tabla1': {e}")
          return None
        try:
          tabla2 = excel_file.parse("tabla2", header=0)
        except ValueError as e:
          print(f"Error al cargar la hoja 'tabla2': {e}")
          return None

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo_excel}")
        return None
    except ValueError as e:
       print(f"Error al cargar las hojas del excel: {e}")
       return None


    # Mostrar nombres de columnas
    print("Columnas de tabla1:", tabla1.columns.tolist())
    print("Columnas de tabla2:", tabla2.columns.tolist())

    if 'Combinada' not in tabla2.columns:
        print("Error: La columna 'Combinada' no se encuentra en la tabla2")
        return None
    if 'Producto_Id' not in tabla2.columns:
        print("Error: La columna 'Producto_Id' no se encuentra en la tabla2")
        return None
    if 'Combinada' not in tabla1.columns:
        print("Error: La columna 'Combinada' no se encuentra en la tabla1")
        return None

    # Convertir columna 'Combinada' a string, rellena NaN y elimina espacios adicionales
    tabla1['Combinada'] = tabla1['Combinada'].fillna('').astype(str).str.strip()
    tabla2['Combinada'] = tabla2['Combinada'].fillna('').astype(str).str.strip()

    # Función para buscar todas las coincidencias
    def buscar_todas_las_coincidencias(valor_a_buscar):
        print(f"Buscando coincidencias para: '{valor_a_buscar}'")
        coincidencias = tabla2[tabla2['Combinada'] == valor_a_buscar]['Producto_Id'].tolist()
        print(f"Coincidencias encontradas: {coincidencias}")
        return ', '.join(map(str, coincidencias)) if coincidencias else None

    # Aplicar la función a la columna 'Combinada' de tabla1 para crear la columna H
    tabla1['H'] = tabla1['Combinada'].apply(buscar_todas_las_coincidencias)

    return tabla1


if __name__ == "__main__":
    ruta_excel = r"C:\Users\rodri\Downloads\xml1.xlsx"  # Ruta del archivo Excel
    tabla1_con_h = buscar_y_combinar_valores(ruta_excel)

    if tabla1_con_h is not None:
        print(tabla1_con_h)
        # Opcional: Guardar el resultado en un nuevo archivo Excel o sobreescribir el mismo
        try:
            with pd.ExcelWriter(ruta_excel, engine='xlsxwriter', mode='w') as writer:
                tabla1_con_h.to_excel(writer, sheet_name="tabla1", startcol=0, header=True, index=False)
        except Exception as e:
            print(f"Error al guardar los cambios en el archivo excel: {e}")
        else:
           print("Proceso completado.")
