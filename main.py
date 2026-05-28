# 1. `leer_fasta(ruta)`
# 2. `calcular_gc(secuencia)`
# 3. `calcular_estadisticas(encabezado, secuencia)`
# 4. `pasa_filtros(stats, args)`
# 5. `escribir_resultados(stats, ruta)`
# 6. `parsear_argumentos()`
# 7. `main()`


def leer_fasta(ruta):
    archivo = open(ruta, "r")

    lineas = archivo.readlines()

    encabezado = lineas[0].strip()

    secuencia = ""

    for linea in lineas[1:]:
        secuencia += linea.strip()

    archivo.close()

    return encabezado, secuencia


encabezado, secuencia = leer_fasta("prueba.fasta")

print(encabezado)
print(secuencia)
