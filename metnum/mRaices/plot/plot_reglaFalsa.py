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

    x_tanjete = np.array([historialA[0], historialB[0]])
    y_tanjete = np.array([f(historialA[0]), f(historialB[0])])

    x_puntoA = np.array([historialA[0], historialA[0]])
    y_puntoA = np.array([0, f(historialA[0])])

    x_puntoB = np.array([historialB[0], historialB[0]])
    y_puntoB = np.array([0, f(historialB[0])])

    (funcion, punto_medio, tanjente, linea_A, linea_B) = ax.plot(
        x,
        y,
        x_punto_medio,
        y_punto_medio,
        x_tanjete,
        y_tanjete,
        x_puntoA,
        y_puntoA,
        x_puntoB,
        y_puntoB,
    )

    punto_medio.set_marker(marker="o")
    ax.legend(
        [
            "f(x)",
            f"Raiz {historialRaiz[0]}",
            f"Tanjente [f(a), f(b)]",
            f"intevalo a: {historialA[0]} ",
            f"intevalo b: {historialB[0]} ",
        ]
    )

    linea_A.set_linestyle("--")
    linea_B.set_linestyle("--")
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")

    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])

    btnnext = Button(axnext, "Siguiente")
    btnprev = Button(axprev, "Atras")

    def update(frame):
        linea_A.set_xdata([historialA[frame], historialA[frame]])
        linea_A.set_ydata([0, f(historialA[frame])])

        linea_B.set_xdata([historialB[frame], historialB[frame]])
        linea_B.set_ydata([0, f(historialB[frame])])

        tanjente.set_xdata([historialA[frame], historialB[frame]])
        tanjente.set_ydata([f(historialA[frame]), f(historialB[frame])])

        punto_medio.set_xdata(historialRaiz[(frame)])
        ax.legend(
            [
                "f(x)",
                f"Raiz {historialRaiz[frame]}",
                f"Tanjente [f(a), f(b)]",
                f"intevalo a: {historialA[frame]} ",
                f"intevalo b: {historialB[frame]} ",
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
