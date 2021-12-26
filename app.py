import sys
from plotX import plotX
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = plotX()
    program.show()
    sys.exit(app.exec_())