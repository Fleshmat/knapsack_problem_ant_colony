# 🐜 Algoritmo de Colonia de Hormigas para el Problema de la Mochila (Knapsack ACO)

Este proyecto implementa una solución basada en el **Algoritmo de Colonia de Hormigas (ACO)** para resolver el clásico **problema de la mochila (Knapsack Problem)**. Los datos de los ítems a considerar son cargados desde un archivo Excel, y el algoritmo busca maximizar el valor total sin superar la capacidad máxima de la mochila.

## 📦 Estructura del Proyecto

├── main.py               # Script principal que ejecuta todo el proceso
├── config.py             # Parámetros y configuración global del algoritmo
├── data_loader.py        # Carga y procesamiento de datos desde Excel
├── ant_colony.py         # Lógica del algoritmo ACO
├── utils.py              # Funciones auxiliares (como guardar resultados)
└── plotter.py            # Gráficos de evolución de soluciones

## 🧠 ¿Qué es el Problema de la Mochila?

El problema de la mochila busca seleccionar un subconjunto de ítems con el mayor valor posible sin exceder la capacidad de la mochila. Cada ítem tiene:
- Un identificador
- Un peso
- Un valor
- Una cantidad máxima disponible

## 🐜 ¿Qué es ACO?

ACO (Ant Colony Optimization) es un algoritmo metaheurístico inspirado en el comportamiento de las hormigas reales, que encuentran caminos óptimos a través del uso de feromonas.

## 📊 Funcionalidades

- Carga dinámica de datos desde un archivo `.xlsx`
- Visualización gráfica de la evolución del valor óptimo por iteración
- Guardado automático de resultados en un archivo Excel de salida
- Totalmente parametrizable vía el archivo `config.py`

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas necesarias:

pip install numpy pandas matplotlib openpyxl


## 🚀 Ejecución
1. Coloca tu archivo de Excel con los ítems en la ruta especificada dentro de config.py.

2. Asegúrate de tener los nombres de columnas correctos en la hoja "Hoja1".

3. Ejecuta el programa:

python main.py

El algoritmo mostrará en consola la mejor solución encontrada, generará un gráfico y guardará los resultados en Resultados.xlsx.

## 📈 Ejemplo de Salida
Mejor solución encontrada en la iteración 73

Valor total: 5820

Peso total: 2445g

Ítems seleccionados: [2, 0, 0, 1, ...] (representa cuántas veces se seleccionó cada ítem)

## 📑 Créditos
Este proyecto es una implementación educativa y experimental del algoritmo ACO adaptado a un problema combinatorio clásico.