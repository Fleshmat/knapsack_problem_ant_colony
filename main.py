import time
from collections import Counter
from data_loader import cargar_items
from ant_colony import ejecutar_aco
from utils import guardar_resultados_en_excel
from plotter import graficar_evolucion

print("Algoritmo de colonias de hormigas")
start_time = time.time()

items = cargar_items()
mejor_valor_global, mejor_solucion_global, mejores_valores_por_iteracion = ejecutar_aco(items)

finish_time = time.time()
duration = finish_time - start_time
indice_mejor_solucion = mejores_valores_por_iteracion.index(mejor_valor_global)

print(f"La mejor solución se alcanzó en la iteración número {indice_mejor_solucion + 1}.")
print(f"Tiempo de duración: {duration:.2f} segundos")
print(f"Mejor Valor Global: {mejor_valor_global}")
peso_total = sum(items[s, 1] for s in mejor_solucion_global)
print(f"Peso Total en gr: {peso_total}")

counter_solucion = Counter(mejor_solucion_global)
solucion_completa = [counter_solucion.get(i, 0) for i in range(len(items))]
print(f"Mejor Solución Global (Cantidad de Ítems seleccionados): {solucion_completa}")

guardar_resultados_en_excel(1, mejor_valor_global, duration, (indice_mejor_solucion + 1), peso_total, solucion_completa)

graficar_evolucion(mejores_valores_por_iteracion)
