from benchmarking import Benchmarking 
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
if __name__ == "__main__":  
    print("Funciona")
    bench = Benchmarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [5000, 10000, 15000, 20000]

    metodos_dic = {
        "Burbuja": metodosO.sort_bubble,
        "Burbuja Mejorado": metodosO.sort_bubble_mejorado,
        "Seleccion": metodosO.sort_selection,
        "Shell": metodosO.sort_shell,
    }

    resultados = []
    
    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)
        for nombre, metodo in metodos_dic.items():
            tiempo_resultado= bench.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
    for tam,nombre,tiempo in resultados:
            print(f"tamaño: {tam}, Nombre metodo: {nombre}, tiempo: {tiempo:6f}")
            
    #Preparar datos para ser graficados
     # 1   Crear un diccionario o mapa para almacenar resultados por metodos
     
    tiempos_by_metodos = {
        "Burbuja": [],
        "Burbuja Mejorado": [],
        "Seleccion": [],
        "Shell": [],
    }
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodos[nombre].append((tam, tiempo))
    plt.figure(figsize=(10, 6))
    #graficar los tiempos para cada metodo
    for nombre, tiempos in tiempos_by_metodos.items():
        tamanios_plot = [tam for tam, _ in tiempos]
        tiempos_plot = [tiempo for _, tiempo in tiempos]
        plt.plot(tamanios_plot, tiempos_plot, label=nombre, marker="o")
    
    #agregar parametros
    
    plt.title("Comparacion de tiempos para cada metodo de ordenamiento")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.legend()
    plt.grid()
    plt.show()

