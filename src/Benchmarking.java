import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento mOrdenamiento;

    public Benchmarking() {
        Long currentMillis = System.currentTimeMillis();
        long currentNano = System.nanoTime();
        System.out.println("Tiempo en milisegundos: " + currentMillis);
        System.out.println("Tiempo en nanosegundos: " + currentNano);
        mOrdenamiento = new MetodosOrdenamiento();
        int [] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea = () -> {
            mOrdenamiento.burbujaTradicional(arreglo);
        };
        double tiempoConCurrentTimeMillis = medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNano = medirConNanoTime(tarea);

        System.out.println("Tiempo en mili: " + tiempoConCurrentTimeMillis + " segundos");
        System.out.println("Tiempo en nano: " + tiempoDuracionNano + " segundos");
    }

    private int[] generarArregloAleatorio(int tamano){
        int [] array = new int[tamano];
        Random random = new Random();
        for (int i =0; i < tamano; i++){
            array[i] = (int) (Math.random() * 1000000.0);
        }
        return array;
    }
    public double medirConCurrentTimeMiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }
}
