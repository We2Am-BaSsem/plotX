from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QLineEdit,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

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

        self.F_X_label = QLabel()
        self.F_X_label.setText("Function")
        self.F_X_label.setFont(QFont("Arial", 10))

        self.F_X = QLineEdit()
        self.F_X.setFixedSize(1000, 20)

        self.F_X_layout = QHBoxLayout()
        self.F_X_layout.addStretch(1)
        self.F_X_layout.addWidget(self.F_X_label)
        self.F_X_layout.addWidget(self.F_X)
        self.F_X_layout.alignment()

        self.minX_label = QLabel()
        self.minX_label.setText("min X")
        self.minX_label.setFont(QFont("Arial", 10))

        self.minX = QLineEdit()
        self.minX.setFixedSize(1000, 20)

        self.minX_layout = QHBoxLayout()
        self.minX_layout.addStretch(1)
        self.minX_layout.addWidget(self.minX_label)
        self.minX_layout.addWidget(self.minX)

        self.maxX_label = QLabel()
        self.maxX_label.setText("max X")
        self.maxX_label.setFont(QFont("Arial", 10))

        self.maxX = QLineEdit()
        self.maxX.setFixedSize(1000, 20)

        self.maxX_layout = QHBoxLayout()
        self.maxX_layout.addStretch(1)
        self.maxX_layout.addWidget(self.maxX_label)
        self.maxX_layout.addWidget(self.maxX)

        # self.canvas = canvas(self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.PlotButton = QPushButton("Plot X")
        self.PlotButton.setFont(QFont("Arial", 14))
        self.PlotButton.clicked.connect(
            lambda: Submit(
                ErrorMessageLabel=self.error_message_label,
                Function=self.F_X,
                minX=self.minX,
                maxX=self.maxX,
                plotGraph=self.canvas,
                plotFigure=self.figure,
            )
        )

        self.error_message_label = QLabel()
        self.error_message_label.setText("")
        self.error_message_label.setFont(QFont("Arial", 20))
        self.error_message_label.setStyleSheet("color: red")
        self.error_message_label.setAlignment(Qt.AlignCenter)

        self.logo = QLabel(self)
        logo = QPixmap("logo.png")
        self.logo.setPixmap(logo)
        self.logo.resize(200, 200)
        self.logo.setAlignment(Qt.AlignCenter)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.layout.addLayout(self.F_X_layout)
        self.layout.addLayout(self.minX_layout)
        self.layout.addLayout(self.maxX_layout)
        self.layout.addWidget(self.PlotButton)
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.error_message_label)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)
