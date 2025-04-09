import numpy as np
import matplotlib.pyplot as plt

def grid():
    x = np.linspace(0, 10, 40)
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    fig = plt.figure()
    fig.suptitle('Grilla con 4 funciones', fontsize=16)

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x, y1, color='darkred', label='y1 = x²')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(ls='dashed')
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.legend()

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(x, y2, color='green', label='y2 = x³')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls='dashed')
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.legend()

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(x, y3, color='orange', label='y3 = x⁴')
    ax3.set_facecolor('whitesmoke')
    ax3.grid(ls='dashed')
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    ax3.legend()

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(x, y4, color='purple', label='y4 = √x')
    ax4.set_facecolor('whitesmoke')
    ax4.grid(ls='dashed')
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")
    ax4.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot: Figura con múltiples gráficos")
    grid()
    print("terminamos")
