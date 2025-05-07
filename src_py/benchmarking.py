from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:
    def _init_(self):
        print("Benchmarking")
        # self.mO = MetodosOrdenamiento()

        # arreglo = self.build_arreglo(50000)
        # metodos=[
        #     ("Burbuja", self.mO.sort_bubble),
        #     ("Burbuja Mejorado", self.mO.sort_bubble_mejorado),
        #     ("Seleccion", self.mO.sort_selection)   
        # ]
        # for nombre, metodo in metodos:
        #     self.tarea = lambda: metodo(arreglo)
        #     print(f"Tiempo en milisegundos {nombre}: {self.contar_con_current_time_millis(self.tarea)} ")
        #     print(f"Tiempo en nanosegundos {nombre}: {self.contar_on_current_time_nano(self.tarea)} ")

    def medir_tiempo(self,funcion,arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio

    
    def build_arreglo(self, tamano):  
        arreglo = []
        for i in range(tamano):
            numero =random.randint(0, 999)
            arreglo.append(numero)
        return arreglo
    
    
    def contar_con_current_time_millis(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio

    def contar_on_current_time_nano(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio)/1000000.0




