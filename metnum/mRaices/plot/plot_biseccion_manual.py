import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button


frameAnimation = 0


def paint_plot(f, historialA, historialB, historialRaiz):

    maximosFrames = len(historialRaiz) - 1

    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.2)

    rangoIzquierdo = (
        (historialA[0] - 10) if historialA[0] < 0 else ((historialA[0] * -1) - 10)
    )
    rangoDerecho = historialB[0] + 10

    x = np.arange(rangoIzquierdo, rangoDerecho, 1)
    y = [f(x) for x in x]

    x_punto_medio = np.array([historialRaiz[0]])
    y_punto_medio = np.array([0])

    x_lineaA = np.array([historialA[0], historialA[0]])
    y_lineaA = np.array([historialA[0], f(historialA[0])])

    x_lineaB = np.array([historialB[0], historialB[0]])
    y_lineaB = np.array([historialB[0], f(historialB[0])])

    # (funcion, punto_medio, linea_A, linea_B) = ax.plot(
    #     x, y, x_punto_medio, y_punto_medio, x_lineaA, y_lineaA, x_lineaB, y_lineaB
    # )

    (funcion, punto_medio) = ax.plot(x, y, x_punto_medio, y_punto_medio)

    linea_A = ax.axvline(x=historialA[0], ymin=0, ymax=1, color="r")
    linea_B = ax.axvline(x=historialB[0], ymin=0, ymax=1, color="b")
    punto_medio.set_marker(marker="o")
    linea_A.set_linestyle("--")
    linea_B.set_linestyle("--")

    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])

    btnnext = Button(axnext, "Siguiente")
    btnprev = Button(axprev, "Atras")

    def update(frame):
        # linea_A.set_xdata([historialA[frame], historialA[frame]])
        # linea_A.set_ydata([historialA[frame], f(historialA[frame])])

        # linea_B.set_xdata([historialB[frame], historialB[frame]])
        # linea_B.set_ydata([historialB[frame], f(historialB[frame])])

        linea_A.set_xdata(historialA[frame])
        linea_B.set_xdata(historialB[frame])

        punto_medio.set_xdata(historialRaiz[(frame)])
        ax.legend(
            [
                "f(x)",
                f"Raiz {historialRaiz[frame]}",
                f"a {historialA[frame]}",
                f"b {historialB[frame]}",
            ]
        )
        plt.draw()

    def next(event):
        global frameAnimation
        if frameAnimation < maximosFrames:
            frameAnimation += 1
            update(frameAnimation)

    def prev(event):
        global frameAnimation
        if frameAnimation > 0:
            frameAnimation -= 1
            update(frameAnimation)

    btnnext.on_clicked(next)
    btnprev.on_clicked(prev)

    ax.grid()
    plt.show()
