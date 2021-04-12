import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Résolveur de Sudoku")
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
Panel = []
for i in range(3):
    Panel.append(QWidget())
fen.resize(800,800)
layout = QHBoxLayout()
for i in range(3):
    layout.addWidget(Panel[i])
fen.setLayout(layout)

fen.show()

app.exec_()
