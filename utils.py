import pandas as pd
import os
from config import EXCEL_RESULT_PATH

def guardar_resultados_en_excel(nueva_corrida, valor_optimo, tiempo_empleado, mejor_iteracion, mejor_peso, mejor_solucion):
    if os.path.isfile(EXCEL_RESULT_PATH):
        resultados = pd.read_excel(EXCEL_RESULT_PATH)
    else:
        resultados = pd.DataFrame(columns=['Corrida', 'Valor', 'Tiempo', 'Iteración', 'Peso', 'Mejor Solución'])

    nuevo_registro = pd.DataFrame({
        'Corrida': [nueva_corrida],
        'Valor': [valor_optimo],
        'Tiempo': [tiempo_empleado],
        'Iteración': [mejor_iteracion],
        'Peso': [mejor_peso],
        'Mejor Solución': [str(mejor_solucion)]
    })

    resultados = pd.concat([resultados, nuevo_registro], ignore_index=True)
    resultados.to_excel(EXCEL_RESULT_PATH, index=False)
