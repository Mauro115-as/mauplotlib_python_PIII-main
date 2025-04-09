import numpy as np
import matplotlib.pyplot as plt

def scatter_plot():
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.tanh(x)

    fig = plt.figure()
    fig.suptitle('Gráfico Scatter de tanh(x)', fontsize=16)
    ax = fig.add_subplot()

    ax.scatter(x, y, c='darkcyan', marker='x', label='y = tanh(x)')
    ax.set_facecolor('whitesmoke')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.legend()

    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Scatter Plot")
    scatter_plot()
    print("terminamos")
