import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button


# frameAnimation = 0


class grafica:
    def __init__(self, f, historialRaiz) -> None:

        self.f = f
        self.historialRaiz = historialRaiz
        self.frameAnimation = 0
        self.maximosFrames = len(historialRaiz) - 1

        self.fig, self.ax = plt.subplots()

        self.funcion = None
        self.punto_x0 = None
        self.punto_x1 = None
        self.fx_x0 = None
        self.recta = None

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
            self.ax.set_title(f"Newton-Rapson\n Paso {frame+1}/{self.maximosFrames}")
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
        self.ax.set_title(f"Newton-Rapson\n Paso 1/{self.maximosFrames}")

        minEjeX = min(self.historialRaiz)
        maxEjex = max(self.historialRaiz)

        diferenciaEjeX = abs(minEjeX - maxEjex)
        espaciamiento = diferenciaEjeX * procentajeEspacio

        x = np.arange((minEjeX - espaciamiento), (maxEjex + espaciamiento), 0.1)
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


# def paint_plot(f, historialRaiz):

#     maximosFrames = len(historialRaiz) - 1
#     minEjeX = min(historialRaiz)
#     maxEjex = max(historialRaiz)

#     fig, ax = plt.subplots(figsize=(10, 8))
#     plt.subplots_adjust(bottom=0.2)

#     ax.set_title("Newton-Rapson")

#     dif = abs(minEjeX - maxEjex)
#     porcentajedif = dif * 0.15

#     x = np.arange((minEjeX - porcentajedif), (maxEjex + porcentajedif), 1)
#     y = [f(x) for x in x]

#     x_punto_x0 = np.array(historialRaiz[0])
#     y_punto_x0 = np.array([0])

#     x_fx_x0 = np.array([historialRaiz[0], historialRaiz[0]])
#     y_fx_x0 = np.array([0, f(historialRaiz[0])])

#     x_punto_x1 = np.array(historialRaiz[1])
#     y_punto_x1 = np.array([0])

#     x_recta = np.array([historialRaiz[1], historialRaiz[0]])
#     y_recta = np.array([0, f(historialRaiz[0])])

#     (funcion, punto_x0, punto_x1, fx_x0, recta) = ax.plot(
#         x,
#         y,
#         x_punto_x0,
#         y_punto_x0,
#         x_punto_x1,
#         y_punto_x1,
#         x_fx_x0,
#         y_fx_x0,
#         x_recta,
#         y_recta,
#     )

#     punto_x0.set_marker(marker="o")
#     punto_x1.set_marker(marker="o")
#     fx_x0.set_linestyle("--")

#     ax.legend(
#         [
#             "f(x)",
#             f"X(i): {historialRaiz[0]}",
#             f"X(i+1): {historialRaiz[1]}",
#             f"f(x0): {f(historialRaiz[0])}",
#         ]
#     )

#     plt.axhline(0, color="black")
#     plt.axvline(0, color="black")

#     axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
#     axnext = plt.axes([0.81, 0.05, 0.1, 0.075])

#     btnnext = Button(axnext, "Siguiente")
#     btnprev = Button(axprev, "Atras")

#     def update(frame):

#         punto_x0.set_xdata([historialRaiz[frame]])
#         punto_x0.set_ydata([0])

#         punto_x1.set_xdata([historialRaiz[frame + 1]])
#         punto_x1.set_ydata([0])

#         fx_x0.set_xdata([[historialRaiz[frame], historialRaiz[frame]]])
#         fx_x0.set_ydata([0, f(historialRaiz[frame])])

#         recta.set_xdata([historialRaiz[frame + 1], historialRaiz[frame]])
#         recta.set_ydata([0, f(historialRaiz[frame])])

#         ax.legend(
#             [
#                 "f(x)",
#                 f"X(i): {historialRaiz[frame]}",
#                 f"X(i+1): {historialRaiz[frame +1]}",
#                 f"f(x0): {f(historialRaiz[frame])}",
#             ]
#         )

#         plt.draw()

#     def next(event):
#         global frameAnimation
#         if frameAnimation < maximosFrames:
#             frameAnimation += 1
#             update(frameAnimation)

#     def prev(event):
#         global frameAnimation
#         if frameAnimation > 0:
#             frameAnimation -= 1
#             update(frameAnimation)

#     btnnext.on_clicked(next)
#     btnprev.on_clicked(prev)

#     ax.grid()
#     plt.show()
