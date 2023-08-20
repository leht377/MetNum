from .frame import frame
import numpy as np


class graph (frame):
    def __init__(self, f, historialA, historialB, historialRaiz) -> None:
        super().__init__()
        self.titulo = "Biseccion"
        self.frameAnimation = 0
        self.maximosFrames = len(historialRaiz) - 1

        self.f = f
        self.historialA = np.array(historialA)
        self.historialB = np.array(historialB)
        self.historialRaiz = np.array(historialRaiz)

    def _update(self, frame):
        if frame < self.maximosFrames:
            self.linea_A.set_xdata(
                [self.historialA[frame], self.historialA[frame]])
            self.linea_A.set_ydata([0, self.f(self.historialA[frame])])

            self.linea_B.set_xdata(
                [self.historialB[frame], self.historialB[frame]])
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
            self.ax.set_title(
                f"{self.titulo}\n Paso {frame+1}/{self.maximosFrames}")
            self.draw()

    def _configure_initial_graph(self):
        procentajeEspacio = 0.15

        self.ax.set_title(f"{self.titulo}\n Paso 1/{self.maximosFrames}")

        tempArray = np.concatenate((self.historialA, self.historialB), axis=0)

        minEjeX = min(tempArray)
        maxEjex = max(tempArray)

        diferenciaEjeX = abs(minEjeX - maxEjex)
        espaciamiento = diferenciaEjeX * procentajeEspacio

        x = np.arange((minEjeX - espaciamiento),
                      (maxEjex + espaciamiento), 0.1)
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
