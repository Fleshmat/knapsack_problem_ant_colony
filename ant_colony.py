import numpy as np
from collections import Counter
from config import PESO_MAXIMO, NUM_HORMIGAS, NUM_ITERACIONES, EVAPORACION, FEROMONA_INICIAL, ALPHA, BETA

def seleccionar_item(items, feromonas, peso_actual, seleccionados):
    pesos_disponibles = items[:, 1] <= (PESO_MAXIMO - peso_actual)
    cantidades_disponibles = np.array([items[i, 3] - seleccionados.count(i) for i in range(len(items))]) > 0
    valor_heuristico = items[:, 2] ** BETA
    probabilidad = ((feromonas ** ALPHA) * valor_heuristico * pesos_disponibles * cantidades_disponibles)
    if probabilidad.sum() == 0:
        return None
    probabilidad /= probabilidad.sum()
    return np.random.choice(range(len(items)), p=probabilidad)

def ejecutar_aco(items):
    feromonas = np.ones(len(items)) * FEROMONA_INICIAL
    mejor_valor_global = 0
    mejor_solucion_global = []
    mejores_valores_por_iteracion = []

    for _ in range(NUM_ITERACIONES):
        mejor_valor_iteracion = 0
        mejor_solucion_iteracion = []

        for _ in range(NUM_HORMIGAS):
            seleccionados = []
            solucion_actual = []
            valor_actual = 0
            peso_actual = 0

            while True:
                item = seleccionar_item(items, feromonas, peso_actual, seleccionados)
                if item is None or peso_actual + items[item, 1] > PESO_MAXIMO:
                    break
                seleccionados.append(item)
                solucion_actual.append(item)
                valor_actual += items[item, 2]
                peso_actual += items[item, 1]

            if valor_actual > mejor_valor_iteracion:
                mejor_valor_iteracion = valor_actual
                mejor_solucion_iteracion = solucion_actual

        if mejor_valor_iteracion > mejor_valor_global:
            mejor_valor_global = mejor_valor_iteracion
            mejor_solucion_global = mejor_solucion_iteracion

        mejores_valores_por_iteracion.append(mejor_valor_iteracion)

        for item in range(len(items)):
            feromonas[item] = (1 - EVAPORACION) * feromonas[item] + sum(
                [items[item, 2] for s in mejor_solucion_iteracion if s == item]
            ) / (mejor_valor_iteracion if mejor_valor_iteracion > 0 else 1)

    return mejor_valor_global, mejor_solucion_global, mejores_valores_por_iteracion
