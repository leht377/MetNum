import matplotlib.pyplot as plt

from abc import ABC, abstractmethod
from matplotlib.widgets import Button


class frame(ABC):
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.frameAnimation = 0
        self.maximosFrames = 0
        self.fig.subplots_adjust(bottom=0.2)
        self.draw = plt.draw

    @abstractmethod
    def _update(self, frame):
        pass

    def _next(self, event):
        if self.frameAnimation < self.maximosFrames:
            self.frameAnimation += 1
            self._update(self.frameAnimation)

    def _prev(self, event):
        if self.frameAnimation > 0:
            self.frameAnimation -= 1
            self._update(self.frameAnimation)

    @abstractmethod
    def _configure_initial_graph(self):
        pass

    def paint(self):
        self._configure_initial_graph()

        plt.axhline(0, color="black")  # ejeX plano cartesiano
        plt.axvline(0, color="black")  # ejeY plano cartesiano

        axprev = plt.axes([0.7, 0.05, 0.1, 0.075])  # type: ignore
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])  # type: ignore

        btnnext = Button(axnext, "Next")
        btnprev = Button(axprev, "Back")

        btnnext.on_clicked(self._next)
        btnprev.on_clicked(self._prev)

        self.ax.grid()
        plt.show()
