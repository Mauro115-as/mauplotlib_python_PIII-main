import numpy as np
import matplotlib.pyplot as plt

def multi_plot():
    x = list(np.linspace(-4, 4, 20))
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, color='green', marker='^', label='y1 = x²')
    ax.plot(x, y2, color='red', marker='+', label='y2 = x³')

    ax.set_facecolor('whitesmoke')
    ax.set_title("Dos funciones juntas")
    ax.set_xlabel("X [rads]")
    ax.set_ylabel("Y [amplitud]")
    ax.set_xlim([-4, 4])
    ax.set_ylim([-70, 70])
    ax.legend()
    ax.grid(True)

    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")
    multi_plot()
    print("terminamos")
