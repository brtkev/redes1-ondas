# Importaciones
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

figure, axes = plt.subplots(2, 1) 

#Variables de Onda
amplitud = 10
longitud_onda = 2
fase = np.pi
frecuencia = 0.2
tiempo = np.linspace(0, 10, 100)  # Vector de tiempo
#print(tiempo)

formula_onda = amplitud * np.sin(fase + tiempo * 2 * np.pi / longitud_onda + fase)

onda1 = axes[0].plot(tiempo, formula_onda)
onda2 = axes[1].plot(tiempo, formula_onda)

def animate(i):
    formula_onda1 = amplitud * np.sin(fase + tiempo * 2 * np.pi / longitud_onda + fase + i * 2 * np.pi * frecuencia)
    formula_onda2 = amplitud * np.sin(fase + tiempo * 2 * np.pi / longitud_onda + fase + i * 2 * np.pi * (frecuencia + 0.2))
    onda1[0].set_ydata(formula_onda1)
    onda2[0].set_ydata(formula_onda2)
    return onda1, onda2

a = animation.FuncAnimation(figure, animate, interval=100)
plt.show()