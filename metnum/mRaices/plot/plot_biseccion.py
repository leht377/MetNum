import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def paint_plot(f, historialA, historialB, historialRaiz):

    fig, ax = plt.subplots(figsize=(10, 8))

    rangoIzquierdo = (
        (historialA[0] - 10) if historialA[0] < 0 else ((historialA[0] * -1) - 10)
    )
    rangoDerecho = historialB[0] + 10

    x = np.arange(rangoIzquierdo, rangoDerecho, 1)
    y = [f(x) for x in x]

    x_punto_medio = np.array([historialRaiz[0]])
    y_punto_medio = np.array([0])

    (funcion, punto_medio) = ax.plot(x, y, x_punto_medio, y_punto_medio)

    linea_A = ax.axvline(x=historialA[0], ymin=0, ymax=1, color="r")
    linea_B = ax.axvline(x=historialB[0], ymin=0, ymax=1, color="b")
    punto_medio.set_marker(marker="o")

    def init():
        ax.set_xlim(historialA[0] - 10, historialB[0] + 10)
        ax.set_ylim(f(historialA[0]), f(historialB[0]))
        return (funcion,)

    def update(frame):
        linea_A.set_xdata(historialA[frame])
        linea_B.set_xdata(historialB[frame])
        punto_medio.set_xdata(historialRaiz[frame])
        ax.legend(
            [
                "f(x)",
                f"Raiz {historialRaiz[frame]}",
                f"a {historialA[frame]}",
                f"b {historialB[frame]}",
            ]
        )
        return (funcion, linea_A, linea_B, punto_medio, ax.get_legend())

    ani = FuncAnimation(
        fig,
        update,
        frames=np.arange(0, len(historialRaiz) - 1),
        init_func=init,
        interval=2000,
        blit=False,
        repeat=False,
    )

    plt.grid()
    plt.show()
