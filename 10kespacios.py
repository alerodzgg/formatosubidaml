import openpyxl

# Ruta al archivo Excel (usando una cadena raw)
archivo_excel = r"C:\Users\rodri\Downloads\alan\labwork-230k.xlsx"

# Cargar el libro de trabajo de Excel
libro_trabajo = openpyxl.load_workbook(archivo_excel)

# Iterar sobre todas las hojas
for hoja in libro_trabajo.worksheets:
    # Obtener el número total de filas
    num_filas = hoja.max_row

    # Iterar sobre las filas, insertando un espacio cada 10000 filas
    for i in range(10000, num_filas + 1, 10000):
        hoja.insert_rows(i)

# Guardar el libro de trabajo actualizado
libro_trabajo.save(archivo_excel)

print("Espacios insertados correctamente en todas las hojas.")
