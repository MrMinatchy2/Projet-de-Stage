import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit
class Text(QTextEdit):
    def __init__(self):
        QTextEdit.__init__(self)
        self.setText("0")
        self.setFocusPolicy(Qt.StrongFocus)
        font = self.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, self.toPlainText())
        
        w = textSize.width() + 10
        h = textSize.height() + 10
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        self.resize(w, h)
    def Test(self):
        font = self.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, self.toPlainText())
        
        w = textSize.width() + 10
        h = textSize.height() + 10
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        self.resize(w, h)
    def keyPressEvent(self, event):
        QTextEdit.keyPressEvent(self,event)
        refresh(fen.Grille,fen.Grille1)

class Fenetre(QWidget):
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

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Résolveur de Sudoku")
        self.resize(800,800)
        for i in range(9):
            self.Lignes.append(QWidget())
            self.Lignes1.append(QWidget())
            self.LigneLayout.append(QHBoxLayout())
            self.Ligne1Layout.append(QHBoxLayout())
            self.Lignes[i].setLayout(self.LigneLayout[i])
            self.Lignes1[i].setLayout(self.Ligne1Layout[i])
        for i in range(2):
            self.WGrids.append(QWidget())
            self.WGridsLayout.append(QVBoxLayout())
        for i in range(3):
            self.Panel.append(QWidget())
        self.layouts.append(QVBoxLayout())
        for i in range(3):
            self.layout.addWidget(self.Panel[i])
        self.setLayout(self.layout)
        self.Panel[1].setLayout(self.layouts[0])
        self.layouts[0].addWidget(self.WGrids[0])
        self.layouts[0].addWidget(self.WGrids[1])
        self.WGrids[0].setLayout(self.WGridsLayout[0])
        self.WGrids[1].setLayout(self.WGridsLayout[1])
        for i in range(9):
            for j in range(9):
                self.Grille.append(QLabel("0"))
                self.Grille1.append(Text())
                self.LigneLayout[i].addWidget(self.Grille[i*9+j])
                self.Ligne1Layout[i].addWidget(self.Grille1[i*9+j])
        for i in range(9):
            self.WGridsLayout[0].addWidget(self.Lignes[i])
            self.WGridsLayout[1].addWidget(self.Lignes1[i])
        for i in range(9):
            self.LigneLayout[i].setContentsMargins(68,9,9,9)
            
    def toListeInt(self):
        liste=[]
        for i in range(9):
            liste.append([])
            for j in range(9):
                liste[i].append(int(self.Grille[i*9+j].text()))
        return liste
    
    def toListe(self):
        liste=[]
        for i in range(9):
            liste.append([])
            for j in range(9):
                liste[i].append(self.Grille[i*9+j].text())
        return liste
    
    def toGrille(self,liste):
        for i in range(9):
            for j in range(9):
                self.Grille[9*i+j].setText(liste[i][j])

    def reInput(self):
        for i in range(9):
            for j in range(9):
                self.Grille1[9*i+j].setText(self.Grille[9*i+j].text())
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
def valide(sudoku):
    valide= True
    for i in range(9):
        l=sudoku[i]
        for j in range(10):
            if l.count(str(j))>1 and j!=0:
                valide=False

    for i in range(9):
        l=[]
        for j in range(9):
            l.append(sudoku[j][i])
        for j in range(10):
            if l.count(str(j))>1 and j!=0:
                valide=False

    for i in range(9):
        l=[]
        for j in range(9):
            l.append(sudoku[int(j/3)+(int(i/3)*3)][(j%3)+((i%3)*3)])
        for j in range(10):
            if l.count(str(j))>1 and j!=0:
                valide=False

    return valide

def valideint(sudoku):
    valide= True
    for i in range(9):
        l=sudoku[i]
        for j in range(10):
            if l.count(j)>1 and j!=0:
                valide=False

    for i in range(9):
        l=[]
        for j in range(9):
            l.append(sudoku[j][i])
        for j in range(10):
            if l.count(j)>1 and j!=0:
                valide=False

    for i in range(9):
        l=[]
        for j in range(9):
            l.append(sudoku[int(j/3)+(int(i/3)*3)][(j%3)+((i%3)*3)])
        for j in range(10):
            if l.count(j)>1 and j!=0:
                valide=False

    return valide


def Remplie(liste):
    plein = True
    for i in range(9):
        for j in range(9):
            if (liste[i][j]==0):
                plein=False
    return plein

def Copie(liste,y,x,val):
    l=liste.copy()
    l[y][x]=val
    return l

def ResoudreArbre(liste,num):
    c=num
    i=0
    j=0
    x=0
    y=0
    while x<9:
        y=0
        while y<9:
            if(liste[x][y]==0):
                i=x
                j=y
                x=9
                y=9
            y+=1
        x+=1
    print(i,j)
    while not Remplie(liste):
        while not valideint(Copie(liste,i,j,c)):
            c+=1
        if valide(Copie(liste,i,j,c)):
            if valideint(ResoudreArbre(Copie(liste,i,j,c),1)):
                return ResoudreArbre(Copie(liste,i,j,c),1)

    print("plz no")
    return liste
        
def refresh(x,y):
    for i in range(9):
        for j in range(9):
            x[i*9+j].setText(y[i*9+j].toPlainText())
fen = Fenetre()
l=[]
for i in range(9):
    l.append([])
    for j in range(9):
        l[i].append(str(random.randint(0,9)))
l=[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
print(l)
print(valide(l))
sys.setrecursionlimit(15000)
l2=[[5,3,4,0,7,0,9,1,2],[6,7,2,1,0,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,0,7,6,0,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
print(ResoudreArbre(l2,1))
print(valide(ResoudreArbre(l2,1)))
while not valide(l):
    l=[]
    for i in range(9):
        l.append([])
        for j in range(9):
            l[i].append(str(random.randint(0,9)))
fen.toGrille(l)
fen.reInput()
print(fen.toListe())
print(len([]))
fen.show()

app.exec_()
 
