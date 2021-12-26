from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Components.TextField import TextField
from Logic import Submit
from functools import partial
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as lines


class plotX(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 1200, 800)
        self.setWindowTitle("plotX")
        self.layout = QVBoxLayout(self)

        self.text_label = QLabel()
        self.text_label.setText("")
        self.text_label.setFont(QFont("Arial", 20))

        self.F_X = TextField()
        self.minX = TextField()
        self.maxX = TextField()

        # self.canvas = canvas(self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.PlotButton = QPushButton("Plot X")
        self.PlotButton.setFont(QFont("Arial", 14))
        self.PlotButton.clicked.connect(
            lambda: Submit(
                ErrorMessageLabel=self.text_label,
                Function=self.F_X,
                minX=self.minX,
                maxX=self.maxX,
                plotGraph=self.canvas,
                plotFigure=self.figure,
            )
        )

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.layout.addWidget(self.F_X)
        self.layout.addWidget(self.minX)
        self.layout.addWidget(self.maxX)
        self.layout.addWidget(self.PlotButton)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)

    # def Submit(self):
    #     try:
    #         ValidationResult = Validate(
    #             self.F_X.text(), self.minX.text(), self.maxX.text()
    #         )
    #         if ValidationResult == "minX can't be greater than or equal to maxX":
    #             self.text_label.setText(ValidationResult + ".\nThey will be swaped")
    #             temp = self.minX.text()
    #             self.minX.setText(self.maxX.text())
    #             self.maxX.setText(temp)
    #         elif ValidationResult != "OK":
    #             self.text_label.setText(ValidationResult)
    #             return
    #         else:
    #             self.text_label.setText("")

    #         xAxis = np.linspace(float(self.minX.text()), float(self.maxX.text()), 100)
    #         yAxis = f(self.F_X.text(), xAxis)

    #         self.figure.clear()
    #         ax = self.figure.add_subplot(111)
    #         ax.plot(xAxis, yAxis)
    #         self.canvas.draw()
    #     except:
    #         print("error")
