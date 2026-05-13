from datos import *
import math
from functools import reduce

# =============================================================================
# ACTIVIDAD — Listas por Comprensión y Funciones Lambda
# Dataset: AI Impact on Job Market 2024-2030
# Algoritmos y Estructuras de Datos I — UADE
# =============================================================================
# Cada ejercicio tiene:
#   - Una descripción del problema
#   - El resultado esperado como comentario
#   - Un espacio para que escribas tu solución
# =============================================================================


def main():

    # Recordemos la estructura del dataset
    print("=" * 60)
    print("Dataset: primeros 5 registros")
    print("=" * 60)
    print(tabulate(datos[:5], headers="keys", tablefmt="grid"))
    print()

    # Nota: el campo "salary" viene como string desde el CSV.
    # Lo convertimos a float para poder operar con él.
    for d in datos:
        d["salary"] = float(d["salary"])

    # -------------------------------------------------------------------------
    # PARTE 1 — Listas por Comprensión
    # -------------------------------------------------------------------------

    print("=" * 60)
    print("PARTE 1 — Listas por Comprensión")
    print("=" * 60)

    # Ejercicio 1.1 — TRANSFORMACIÓN
    # Obtené una nueva lista con solo los títulos de trabajo (job_title)
    # de todos los registros del dataset.
    # Resultado esperado: una lista de strings con los nombres de los puestos.
    # Ejemplo: ['Data Scientist', 'Software Engineer', ...]

    job_titles = [d["job_title"] for d in datos]  # ← reemplazá esto con una lista por comprensión
    job_titles_unique = sorted(set(job_titles))
    print("1.1 Títulos de trabajo:")
    print(job_titles_unique)
    print()

    # Ejercicio 1.2 — TRANSFORMACIÓN con cálculo
    # Obtené una nueva lista de diccionarios donde cada elemento tenga:
    #   - "job_title": el título del puesto
    #   - "salary_ars": el salario convertido a pesos argentinos (multiplicá por 1200)
    # Resultado esperado: lista de dicts con job_title y salary_ars

    salarios_ars = [
        {"job_title": d["job_title"], "salary_ars": d["salary"] * 1500} for d in datos
    ]  # ← reemplazá esto con una lista por comprensión
    print("1.2 Salarios convertidos a ARS:")
    print(tabulate(salarios_ars[:5], headers="keys", tablefmt="grid"))
    print()

    # Ejercicio 1.3 — FILTRADO
    # Obtené una lista con solo los puestos que tienen impacto de IA "High"
    # (campo ai_impact == "High")
    # Resultado esperado: lista de diccionarios filtrada

    alto_impacto = [
        {"job_title_High": d["job_title"]} for d in datos if d["ai_impact"].lower() == "high"
    ]  # ← reemplazá esto con una lista por comprensión
    print("1.3 Puestos con alto impacto de IA:")
    print(tabulate(alto_impacto, headers="keys", tablefmt="grid"))
    print()

    # Ejercicio 1.4 — FILTRADO con condición numérica
    # Obtené una lista con los puestos cuyo salario supera los 100.000 USD
    # Resultado esperado: lista de diccionarios filtrada

    bien_pagados = [
        {"salary_>100K": d["salary"]} for d in datos if d["salary"] > 100000
    ]  # ← reemplazá esto con una lista por comprensión
    print("1.4 Puestos con salario > 100.000 USD:")
    print(tabulate(bien_pagados, headers="keys", tablefmt="grid"))
    print()

    # -------------------------------------------------------------------------
    # PARTE 2 — Lambda con map y filter
    # -------------------------------------------------------------------------

    print("=" * 60)
    print("PARTE 2 — Lambda con map y filter")
    print("=" * 60)

    # Ejercicio 2.1 — map + lambda
    # Usando map y lambda, obtené una lista con solo los job_title de cada registro.
    # Es el mismo resultado que 1.1 pero usando map + lambda en lugar de
    # lista por comprensión.

    job_titles_map = list(
        map(lambda d: d["job_title"], datos)
    )  # ← reemplazá esto con list(map(lambda ..., datos))
    print("2.1 Títulos con map + lambda:")
    print(job_titles_map)
    print()

    # Ejercicio 2.2 — map + lambda con transformación
    # Usando map y lambda, convertí cada salario a ARS (x 1200) y
    # redondealo hacia arriba con math.ceil.
    # Resultado esperado: lista de enteros

    salarios_ars_map = list(
        map(lambda d: math.ceil(d["salary"] * 1500), datos)
    )  # ← reemplazá esto con list(map(lambda ..., datos))
    print("2.2 Salarios en ARS redondeados con map + lambda:")
    print(salarios_ars_map)
    print()

    # Ejercicio 2.3 — filter + lambda
    # Usando filter y lambda, obtené los puestos con ai_impact == "High"
    # Es el mismo resultado que 1.3 pero con filter + lambda.

    alto_impacto_filter = list(
        filter(lambda d: d["salary"] > 100000, datos)
    )  # ← reemplazá esto con list(filter(lambda ..., datos))
    print("2.3 Alto impacto con filter + lambda:")
    print(tabulate(alto_impacto_filter, headers="keys", tablefmt="grid"))
    print()

    # -------------------------------------------------------------------------
    # PARTE 3 — Lambda con sorted y reduce
    # -------------------------------------------------------------------------

    print("=" * 60)
    print("PARTE 3 — Lambda con sorted y reduce")
    print("=" * 60)

    # Ejercicio 3.1 — sorted + lambda (ascendente)
    # Ordená el dataset por salario de menor a mayor.
    # Resultado esperado: lista de diccionarios ordenada

    ordenados_asc = sorted(
        datos, key=lambda d: d["salary"], reverse=False
    )  # ← reemplazá esto con sorted(..., key=lambda ...)
    print("3.1 Ordenados por salario (menor a mayor):")
    print(tabulate(ordenados_asc, headers="keys", tablefmt="grid"))
    print()

    # Ejercicio 3.2 — sorted + lambda (descendente)
    # Ordená el dataset por salario de mayor a menor.

    ordenados_desc = []  # ← reemplazá esto con sorted(..., key=lambda ..., reverse=True)
    print("3.2 Ordenados por salario (mayor a menor):")
    print(tabulate(ordenados_desc, headers="keys", tablefmt="grid"))
    print()

    # Ejercicio 3.3 — sorted + lambda por string
    # Ordená el dataset alfabéticamente por job_title (A → Z).

    ordenados_alfa = sorted(
        datos, key=lambda d: d["job_title"]
    )  # ← reemplazá esto con sorted(..., key=lambda ...)
    print("3.3 Ordenados alfabéticamente por job_title:")
    print(tabulate(ordenados_alfa, headers="keys", tablefmt="grid"))
    print()

    # Ejercicio 3.4 — reduce + lambda (suma)
    # Usá reduce y lambda para calcular la suma total de todos los salarios.
    # Recordá usar 0 como valor inicial.
    # Resultado esperado: un número float

    suma_salarios = reduce(
        lambda acc, d: acc + d["salary"], datos, 0
    )  # ← reemplazá esto con reduce(lambda ..., datos, 0)
    print(f"3.4 Suma total de salarios: ${suma_salarios:,.2f}")
    print()

    # Ejercicio 3.5 — reduce + lambda (promedio)
    # A partir de la suma del ejercicio anterior, calculá el salario promedio.

    promedio_salario = suma_salarios /len(datos)  # ← calculá el promedio usando suma_salarios y len(datos)
    print(f"3.5 Salario promedio: ${promedio_salario:,.2f}")
    print()

    # -------------------------------------------------------------------------
    # DESAFÍO FINAL — Integrá todo lo aprendido
    # -------------------------------------------------------------------------

    print("=" * 60)
    print("🏆 DESAFÍO FINAL")
    print("=" * 60)

    # En un solo bloque de código, sin usar bucles for explícitos:
    #
    # 1. Filtrá los puestos con ai_impact == "High"
    # 2. De esos puestos, calculá el salario promedio usando reduce
    # 3. Mostrá el resultado con el mensaje:
    #    "Salario promedio de puestos con alto impacto de IA: $XXX,XXX.XX"
    #
    # Pista: podés combinar filter + reduce en dos líneas.

    # Tu solución acá 👇


if __name__ == "__main__":
    main()
