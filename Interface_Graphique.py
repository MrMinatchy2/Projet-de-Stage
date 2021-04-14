import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit
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
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Résolveur de Sudoku")
class Text(QTextEdit):
    def __init__(self):
        QTextEdit.__init__(self)
        self.setText("0")
        self.setFocusPolicy(Qt.StrongFocus)
    def keyPressEvent(self, event):
        print("oops")
        refresh(Grille,Grille1)
def Test(text):

        font = text.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, text.toPlainText())

        w = textSize.width() + 10
        h = textSize.height() + 10
        text.setMinimumSize(w, h)
        text.setMaximumSize(w, h)
        text.resize(w, h)


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)


def refresh(x,y):
    for i in range(9):
        for j in range(9):
            x[i*9+j].setText(y[i*9+j].toPlainText())
fen = Fenetre()
fen.resize(800,800)



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
        Grille1.append(Text())
        Test(Grille1[9*i+j])
        LigneLayout[i].addWidget(Grille[i*9+j])
        Ligne1Layout[i].addWidget(Grille1[i*9+j])
for i in range(9):
    WGridsLayout[0].addWidget(Lignes[i])
    WGridsLayout[1].addWidget(Lignes1[i])
fen.show()

app.exec_()
 
