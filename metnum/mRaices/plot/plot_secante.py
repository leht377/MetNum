import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button


class grafica:
    def __init__(self, f, historialX, historialXmenos) -> None:

        self.titulo = "Secante"
        self.frameAnimation = 0
        self.maximosFrames = len(historialX) - 1

        self.f = f
        self.historialX = np.array(historialX)
        self.historialXmenos = np.array(historialXmenos)

        self.fig, self.ax = plt.subplots()

        self.funcion = None
        self.xn = None
        self.xmenos = None
        self.raiz = None
        self.secante = None

    def _update(self, frame):
        if frame < self.maximosFrames:

            self.xn.set_xdata([self.historialX[frame], self.historialX[frame]])
            self.xn.set_ydata([0, self.f(self.historialX[frame])])

            self.xmenos.set_xdata(
                [self.historialXmenos[frame], self.historialXmenos[frame]]
            )
            self.xmenos.set_ydata([0, self.f(self.historialXmenos[frame])])

            self.raiz.set_xdata([self.historialX[frame + 1]])
            self.raiz.set_ydata([0])

            self.secante.set_xdata(
                [
                    self.historialX[frame],
                    self.historialXmenos[frame],
                    self.historialX[frame + 1],
                ]
            )
            self.secante.set_ydata(
                [self.f(self.historialX[frame]), self.f(self.historialXmenos[frame]), 0]
            )

            self.ax.legend(
                [
                    "f(x)",
                    f"Xn {self.historialX[frame]}",
                    f"Xmenos {self.historialXmenos[frame]}",
                    f"Raiz {self.historialX[frame+1]}",
                    f"Secante",
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

        minEjeX = self.historialXmenos.min()
        maxEjex = self.historialXmenos.max()

        diferenciaEjeX = abs(minEjeX - maxEjex)
        espaciamiento = diferenciaEjeX * procentajeEspacio

        x = np.arange((minEjeX - espaciamiento), (maxEjex + espaciamiento), 0.1)
        y = [self.f(x) for x in x]

        x_xmenos = [self.historialXmenos[0], self.historialXmenos[0]]
        y_xmenos = [0, self.f(self.historialXmenos[0])]

        x_xn = [self.historialX[0], self.historialX[0]]
        y_xn = [0, self.f(self.historialX[0])]

        x_raiz = np.array([self.historialX[1]])
        y_raiz = np.array([0])

        x_secante = np.array(
            [self.historialX[0], self.historialXmenos[0], self.historialX[1]]
        )
        y_secante = np.array(
            [self.f(self.historialX[0]), self.f(self.historialXmenos[0]), 0]
        )

        (self.funcion, self.xn, self.xmenos, self.raiz, self.secante) = self.ax.plot(
            x, y, x_xn, y_xn, x_xmenos, y_xmenos, x_raiz, y_raiz, x_secante, y_secante
        )

        self.raiz.set_marker(marker="o")
        self.secante.set_linestyle("--")

        self.ax.legend(
            [
                "f(x)",
                f"Xn {self.historialX[0]}",
                f"Xmenos {self.historialXmenos[0]}",
                f"Raiz {self.historialX[1]}",
                f"Secante",
            ]
        )

    def pintarGrafica(self):
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
