# 1. `leer_fasta(ruta)`


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


# 2. `calcular_gc(secuencia)`


def calcular_gc(secuencia):
    g = secuencia.count("G")

    c = secuencia.count("C")

    gc = g + c

    porcentaje = gc / len(secuencia)

    return porcentaje


resultado = calcular_gc("ATGCGC")

print(resultado)


# 3. `calcular_estadisticas(encabezado, secuencia)`
def calcular_estadisticas(encabezado, secuencia):
    longitud = len(secuencia)

    gc = calcular_gc(secuencia)

    estadisticas = {"encabezado": encabezado, "longitud": longitud, "gc": gc}

    return estadisticas


stats = calcular_estadisticas(">seq1", "ATGCGC")

print(stats)


# 4. `pasa_filtros(stats, args)`


def pasa_filtros(stats, minimo_longitud):
    if stats["longitud"] >= minimo_longitud:
        return True

    return False


stats = {"encabezado": ">seq1", "longitud": 6, "gc": 0.66}

resultado = pasa_filtros(stats, 5)

print(resultado)


# 5. `escribir_resultados(stats, ruta)`


# 6. `parsear_argumentos()`


# 7. `main()`
