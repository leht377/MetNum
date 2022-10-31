import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def paint_plot(f, historialA, historialB, historialRaiz):

    fig, ax = plt.subplots(figsize=(8, 8))

    rangoIzquierdo = (
        (historialA[0] - 10) if historialA[0] < 0 else ((historialA[0] * -1) - 10)
    )
    rangoDerecho = historialB[0] + 10

    x = np.arange(rangoIzquierdo, rangoDerecho, 1)
    y = [f(x) for x in x]
    lineY = np.arange(-50, 50, 1)

    (ln1, ln4, ln5, ln6) = ax.plot(
        x,
        y,
        np.repeat(historialA[0], 100),
        lineY,
        np.repeat(historialB[0], 100),
        lineY,
        np.repeat(historialRaiz[0], 100),
        lineY,
    )

    ax.legend(["f(x)", "a", "b", "Raiz"])

    def init():
        ax.set_xlim(historialA[0] - 10, historialB[0] + 10)
        ax.set_ylim(-60, 60)
        return (ln1, ln4, ln5, ln6)

    def update(frame):
        ln4.set_data(historialA[frame], lineY)
        ln5.set_data(historialB[frame], lineY)
        ln6.set_data(historialRaiz[frame], lineY)
        ax.legend(
            [
                "f(x)",
                f"a {historialA[frame]}",
                f"b {historialB[frame]}",
                f"Raiz {historialRaiz[frame]}",
            ]
        )
        return (ln1, ln4, ln5, ln6, ax.get_legend())

    ani = FuncAnimation(
        fig,
        update,
        frames=np.arange(0, len(historialRaiz) - 1),
        init_func=init,
        interval=600,
        blit=True,
    )
    plt.grid()
    plt.show()
