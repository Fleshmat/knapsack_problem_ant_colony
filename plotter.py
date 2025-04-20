import matplotlib.pyplot as plt

def graficar_evolucion(mejores_valores_por_iteracion):
    plt.plot(mejores_valores_por_iteracion, '-o', label='Mejor Valor por Iteración')
    plt.title('Evolución del Mejor Valor por Iteración')
    plt.xlabel('Iteración')
    plt.ylabel('Fitness')
    plt.legend()
    plt.show()
