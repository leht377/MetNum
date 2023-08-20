from .frame import frame
import numpy as np
# import matplotlib.pyplot as plt


class graph(frame):
    def __init__(self, f, historialRaiz) -> None:
        super().__init__()
        self.f = f
        self.historialRaiz = historialRaiz
        self.frameAnimation = 0
        self.maximosFrames = len(historialRaiz) - 1

    def _update(self, frame):
        if frame < self.maximosFrames:
            self.punto_x0.set_xdata([self.historialRaiz[frame]])
            self.punto_x0.set_ydata([0])

            self.punto_x1.set_xdata([self.historialRaiz[frame + 1]])
            self.punto_x1.set_ydata([0])

            self.fx_x0.set_xdata(
                [[self.historialRaiz[frame], self.historialRaiz[frame]]]
            )
            self.fx_x0.set_ydata([0, self.f(self.historialRaiz[frame])])

            self.recta.set_xdata(
                [self.historialRaiz[frame + 1], self.historialRaiz[frame]]
            )
            self.recta.set_ydata([0, self.f(self.historialRaiz[frame])])

            self.ax.legend(
                [
                    "f(x)",
                    f"X(i): {self.historialRaiz[frame]}",
                    f"X(i+1): {self.historialRaiz[frame +1]}",
                    f"f(xi): {self.f(self.historialRaiz[frame])}",
                ]
            )
            self.ax.set_title(
                f"Newton-Rapson\n Paso {frame+1}/{self.maximosFrames}")
            self.draw()

    def _configure_initial_graph(self):
        procentajeEspacio = 0.15

        self.ax.set_title(f"Newton-Rapson\n Paso 1/{self.maximosFrames}")

        minEjeX = min(self.historialRaiz)
        maxEjex = max(self.historialRaiz)

        diferenciaEjeX = abs(minEjeX - maxEjex)
        espaciamiento = diferenciaEjeX * procentajeEspacio

        x = np.arange((minEjeX - espaciamiento),
                      (maxEjex + espaciamiento), 0.1)
        y = [self.f(x) for x in x]

        x_punto_x0 = np.array(self.historialRaiz[0])
        y_punto_x0 = np.array([0])

        x_fx_x0 = np.array([self.historialRaiz[0], self.historialRaiz[0]])
        y_fx_x0 = np.array([0, self.f(self.historialRaiz[0])])

        x_punto_x1 = np.array(self.historialRaiz[1])
        y_punto_x1 = np.array([0])

        x_recta = np.array([self.historialRaiz[1], self.historialRaiz[0]])
        y_recta = np.array([0, self.f(self.historialRaiz[0])])

        (
            self.funcion,
            self.punto_x0,
            self.punto_x1,
            self.fx_x0,
            self.recta,
        ) = self.ax.plot(
            x,
            y,
            x_punto_x0,
            y_punto_x0,
            x_punto_x1,
            y_punto_x1,
            x_fx_x0,
            y_fx_x0,
            x_recta,
            y_recta,
        )

        self.punto_x0.set_marker(marker="o")
        self.punto_x1.set_marker(marker="o")
        self.fx_x0.set_linestyle("--")

        self.ax.legend(
            [
                "f(x)",
                f"X(i): {self.historialRaiz[0]}",
                f"X(i+1): {self.historialRaiz[1]}",
                f"f(xi): {self.f(self.historialRaiz[0])}",
            ]
        )
