
#importaciones
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Variables
periodo = 8
cantidad_de_ns = 12

# simbolos de sympy
time = smp.symbols("t", real=True)
n = smp.symbols("n", integer=True)


# necesitamos los coeficientes a_n, b_n y c

restricciones = [[0,0,np.pi],
      [1,np.pi,np.pi*2]]

a_n = [
    (2 / periodo) * smp.integrate(
        valor * smp.sin(2 * smp.pi * n * time / periodo), 
        (time, desde, hasta)
    ) for valor, desde, hasta in restricciones
]
a_n = sum(a_n)

b_n = [
    (2 / periodo) * smp.integrate(
        valor * smp.cos(2 * smp.pi * n * time / periodo), 
        (time, desde, hasta)
    ) for valor, desde, hasta in restricciones    
]
b_n = sum(b_n)

c_n = [
    (2 / periodo) * smp.integrate(valor, (time, desde, hasta)) for valor, desde, hasta in restricciones
]
c_n = sum(c_n)


# Computamos la serie de fourier
g_t = (
    c_n / 2
    + smp.Sum(
        a_n * smp.sin(2 * smp.pi * n * time / periodo),
        (n, 1, cantidad_de_ns),
    )
    + smp.Sum(
        b_n * smp.cos(2 * smp.pi * n * time / periodo),
        (n, 1, cantidad_de_ns),
    )
)

# Computamos los armonicos
arr_armonicos = np.arange(1, cantidad_de_ns + 1)
frecuencias_a_n = np.abs([a_n.subs(n, armonico) for armonico in arr_armonicos])
frecuencias_b_n = np.abs([b_n.subs(n, armonico) for armonico in arr_armonicos])

# Graficación de resultados

# Se convierte la función simbólica a una función numérica para poder evaluarla
g_t_numpy = smp.lambdify(time, g_t, modules="numpy")

# Esblecimiento de rango de tiempo
arr_tiempo = np.linspace(0, 10, 100)

# Evaluación la función sobre el rango de tiempo
arr_g_t = g_t_numpy(arr_tiempo)

# Graficación
figure = plt.figure(figsize=(15, 5))

# Dominio del tiempo

# Seleccionar el primer plot
plt.subplot(1, 3, 1)

# Configuración de la gráfica
plt.plot(arr_tiempo, arr_g_t)
plt.title("Onda en el Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Valor")

# Dominio de la frecuencia

# Seleccionar el segundo plot
plt.subplot(1, 3, 2)

# Configuración de la gráfica
plt.stem(arr_armonicos, frecuencias_a_n, label='Frecuencia de a_n')
plt.stem(arr_armonicos, frecuencias_b_n, label='Frecuencia de b_n', markerfmt='rx', linefmt='r-', basefmt=" ")
plt.title('Onda en Frecuencia')
plt.xlabel('Armónico')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)

ax = plt.subplot(1, 3, 3)
plt.title("Movimiento de la onda")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
onda = ax.plot(arr_tiempo, arr_g_t)

def animate(i):
    arr_g_t = g_t_numpy(arr_tiempo + i * 2)
    onda[0].set_ydata(arr_g_t )
    return onda

ani = animation.FuncAnimation(figure, animate, interval=100)
# Mostrar la gráfica
plt.show()