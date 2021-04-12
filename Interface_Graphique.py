import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Résolveur de Sudoku")
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)


fen = Fenetre()
fen.resize(800,800)
WGrids= []
WGridsLayout= []
Lignes= []
Grille= []
LigneLayout= []
Lignes1 = []
Grille1= []
Ligne1Layout= []
layout = QHBoxLayout()
layouts= []
Panel = []


for i in range(9):
    Lignes.append(QWidget())
    Lignes1.append(QWidget())
    LigneLayout.append(QHBoxLayout())
    Ligne1Layout.append(QHBoxLayout())
    Lignes[i].setLayout(LigneLayout[i])
    Lignes1[i].setLayout(Ligne1Layout[i])
for i in range(2):
    WGrids.append(QWidget())
    WGridsLayout.append(QVBoxLayout())
for i in range(3):
    Panel.append(QWidget())
layouts.append(QVBoxLayout())
for i in range(3):
    layout.addWidget(Panel[i])
fen.setLayout(layout)
Panel[1].setLayout(layouts[0])
layouts[0].addWidget(WGrids[0])
layouts[0].addWidget(WGrids[1])
WGrids[0].setLayout(WGridsLayout[0])
WGrids[1].setLayout(WGridsLayout[1])
for i in range(9):
    for j in range(9):
        Grille.append(QLabel("0"))
        Grille1.append(QTextEdit())
        Grille1[i*9+j].resize(1,1)
        LigneLayout[i].addWidget(Grille[i*9+j])
        Ligne1Layout[i].addWidget(Grille1[i*9+j])
for i in range(9):
    WGridsLayout[0].addWidget(Lignes[i])
    WGridsLayout[1].addWidget(Lignes1[i])

fen.show()

app.exec_()
 
