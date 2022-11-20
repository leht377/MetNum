import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button


frameAnimation = 0


class grafica:
    def __init__(self, f, historialA, historialB, historialRaiz) -> None:

        self.titulo = "Biseccion"
        self.frameAnimation = 0
        self.maximosFrames = len(historialRaiz) - 1

        self.f = f
        self.historialA = np.array(historialA)
        self.historialB = np.array(historialB)
        self.historialRaiz = np.array(historialRaiz)

        self.fig, self.ax = plt.subplots()

        self.funcion = None
        self.punto_medio = None
        self.linea_A = None
        self.linea_B = None

    def _update(self, frame):
        if frame < self.maximosFrames:
            self.linea_A.set_xdata([self.historialA[frame], self.historialA[frame]])
            self.linea_A.set_ydata([0, self.f(self.historialA[frame])])

            self.linea_B.set_xdata([self.historialB[frame], self.historialB[frame]])
            self.linea_B.set_ydata([0, self.f(self.historialB[frame])])
            self.punto_medio.set_xdata(self.historialRaiz[(frame)])

            self.ax.legend(
                [
                    "f(x)",
                    f"Raiz {self.historialRaiz[frame]}",
                    f"a {self.historialA[frame]}",
                    f"b {self.historialB[frame]}",
                ]
            )
            self.ax.set_title(f"{self.titulo}\n Paso {frame+1}/{self.maximosFrames}")
            plt.draw()

    def _next(self, event):
        if self.frameAnimation < self.maximosFrames:
            self.frameAnimation += 1
            self._update(self.frameAnimation)

    def _prev(self, event):
        if self.frameAnimation > 0:
            self.frameAnimation -= 1
            self._update(self.frameAnimation)

    def _valores_iniciales(self):
        procentajeEspacio = 0.15

        plt.subplots_adjust(bottom=0.2)
        self.ax.set_title(f"{self.titulo}\n Paso 1/{self.maximosFrames}")

        tempArray = np.concatenate((self.historialA, self.historialB), axis=0)

        minEjeX = min(tempArray)
        maxEjex = max(tempArray)

        diferenciaEjeX = abs(minEjeX - maxEjex)
        espaciamiento = diferenciaEjeX * procentajeEspacio

        x = np.arange((minEjeX - espaciamiento), (maxEjex + espaciamiento), 0.1)
        y = [self.f(x) for x in x]

        x_punto_medio = np.array([self.historialRaiz[0]])
        y_punto_medio = np.array([0])

        x_lineaA = np.array([self.historialA[0], self.historialA[0]])
        y_lineaA = np.array([0, self.f(self.historialA[0])])

        x_lineaB = np.array([self.historialB[0], self.historialB[0]])
        y_lineaB = np.array([0, self.f(self.historialB[0])])

        (self.funcion, self.punto_medio, self.linea_A, self.linea_B,) = self.ax.plot(
            x,
            y,
            x_punto_medio,
            y_punto_medio,
            x_lineaA,
            y_lineaA,
            x_lineaB,
            y_lineaB,
        )
        self.punto_medio.set_marker(marker="o")
        self.linea_A.set_linestyle("--")
        self.linea_B.set_linestyle("--")
        self.ax.legend(
            [
                "f(x)",
                f"Raiz {self.historialRaiz[0]}",
                f"a {self.historialA[0]}",
                f"b {self.historialB[0]}",
            ]
        )

        self._valores_iniciales()

        plt.axhline(0, color="black")  # ejeX plano cartesiano
        plt.axvline(0, color="black")  # ejeY plano cartesiano

        axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])

        btnnext = Button(axnext, "Siguiente")
        btnprev = Button(axprev, "Atras")

        btnnext.on_clicked(self._next)
        btnprev.on_clicked(self._prev)

        self.ax.grid()
        plt.show()
