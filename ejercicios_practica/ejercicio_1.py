import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    # Generamos la función y = x**2
    x = range(^2)
    y = [i**2 for i in x]

    fig = plt.figure()
    fig.suptitle('Gráfico Ejemplo 1 Y=X**2', fontsize=12)
    ax = fig.add_subplot()
    
    # Graficamos la función con color, marcador y etiqueta
    ax.plot(x, y, c='darkgreen', marker='^', label='función: y = x**2')
    ax.legend()
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")
    
    # Se calcula y se grafica la función
    line_plot()
    print("terminamos")
