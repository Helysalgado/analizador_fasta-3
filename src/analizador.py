# --------------------------------------------------
# 1. leer_fasta(ruta)
# --------------------------------------------------

# ¿Qué recibe?
# La ruta de un archivo FASTA.

# ¿Qué hace?
# Lee el encabezado y la secuencia.

# ¿Qué devuelve?
# El encabezado y la secuencia.

# Pseudocódigo:
# abrir archivo
# leer líneas
# guardar encabezado
# guardar secuencia
# devolver encabezado y secuencia


def leer_fasta(ruta):
    try:
        archivo = open(ruta, "r")

    except FileNotFoundError:
        print("Error: archivo no encontrado")
        return None, None

    lineas = archivo.readlines()

    encabezado = lineas[0].strip()

    secuencia = ""

    for linea in lineas[1:]:
        secuencia += linea.strip()

    archivo.close()

    return encabezado, secuencia


# encabezado, secuencia = leer_fasta("prueba.fasta")

# print(encabezado)
# print(secuencia)


# --------------------------------------------------
# 2. calcular_gc(secuencia)
# --------------------------------------------------

# ¿Qué recibe?
# Una secuencia de ADN.

# ¿Qué hace?
# Cuenta las bases G y C.

# ¿Qué devuelve?
# El porcentaje GC.

# Pseudocódigo:
# contar G
# contar C
# sumarlas
# dividir entre la longitud total


def calcular_gc(secuencia):
    g = secuencia.count("G")

    c = secuencia.count("C")

    gc = g + c

    porcentaje = gc / len(secuencia)

    return porcentaje


# resultado = calcular_gc("ATGCGC")

# print(resultado)


# --------------------------------------------------
# 3. calcular_estadisticas(encabezado, secuencia)
# --------------------------------------------------

# ¿Qué recibe?
# El encabezado y la secuencia.

# ¿Qué hace?
# Calcula estadísticas de la secuencia.

# ¿Qué devuelve?
# Un diccionario con estadísticas.

# Pseudocódigo:
# calcular longitud
# calcular GC
# guardar datos en diccionario
# devolver diccionario


def calcular_estadisticas(encabezado, secuencia):
    longitud = len(secuencia)

    gc = calcular_gc(secuencia)

    estadisticas = {"encabezado": encabezado, "longitud": longitud, "gc": gc}

    return estadisticas


# stats = calcular_estadisticas(">seq1", "ATGCGC")

# print(stats)


# --------------------------------------------------
# 4. pasa_filtros(stats, minimo_longitud)
# --------------------------------------------------

# ¿Qué recibe?
# Estadísticas y una longitud mínima.

# ¿Qué hace?
# Verifica si la secuencia cumple el filtro.

# ¿Qué devuelve?
# True o False.

# Pseudocódigo:
# revisar longitud
# si cumple devolver True
# si no cumple devolver False


def pasa_filtros(stats, minimo_longitud):
    if stats["longitud"] >= minimo_longitud:
        return True

    return False


# stats = {"encabezado": ">seq1", "longitud": 6, "gc": 0.66}

# resultado = pasa_filtros(stats, 5)

# print(resultado)


# --------------------------------------------------
# 5. escribir_resultados(stats, ruta)
# --------------------------------------------------

# ¿Qué recibe?
# Estadísticas y una ruta de salida.

# ¿Qué hace?
# Guarda resultados en un archivo.

# ¿Qué devuelve?
# Nada.

# Pseudocódigo:
# abrir archivo
# escribir encabezado
# escribir longitud
# escribir GC
# cerrar archivo


def escribir_resultados(stats, ruta):
    archivo = open(ruta, "w")

    archivo.write("Encabezado: " + stats["encabezado"] + "\n")

    archivo.write("Longitud: " + str(stats["longitud"]) + "\n")

    archivo.write("GC: " + str(stats["gc"]) + "\n")

    archivo.close()


# stats = {"encabezado": ">seq1", "longitud": 6, "gc": 0.66}

# escribir_resultados(stats, "resultado.txt")


# --------------------------------------------------
# 6. parsear_argumentos()
# --------------------------------------------------

# ¿Qué recibe?
# Nada directamente.

# ¿Qué hace?
# Lee argumentos desde terminal.

# ¿Qué devuelve?
# Los argumentos del programa.

# Pseudocódigo:
# crear parser
# agregar argumento entrada
# agregar argumento salida
# leer argumentos
# devolver argumentos

import argparse


def parsear_argumentos():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True)

    parser.add_argument("-o", "--output", required=True)

    args = parser.parse_args()

    return args


# args = parsear_argumentos()

# print(args.entrada)

# print(args.salida)


# --------------------------------------------------
# 7. main()
# --------------------------------------------------

# ¿Qué recibe?
# Los argumentos del programa.

# ¿Qué hace?
# Coordina todas las funciones.

# ¿Qué devuelve?
# Nada.

# Pseudocódigo:
# leer argumentos
# leer FASTA
# calcular estadísticas
# aplicar filtros
# escribir resultados
# mostrar resumen


def main():
    args = parsear_argumentos()

    encabezado, secuencia = leer_fasta(args.input)

    if encabezado is None:
        return

    stats = calcular_estadisticas(encabezado, secuencia)

    cumple = pasa_filtros(stats, 5)

    if cumple:
        escribir_resultados(stats, args.output)

        print("Secuencia aceptada")

    else:
        print("Secuencia rechazada")


if __name__ == "__main__":
    main()

# Por accidente hice dos commits con docs, el segundo commit de docs debía ser el
# último feat, usaré este comentario para ese feat.
