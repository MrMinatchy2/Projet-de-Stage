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
        if event.key() != Qt.Key_Enter:
            QTextEdit.keyPressEvent(self,event)
        refresh(fen.Grille,fen.Grille1,fen.taille)
        if event.key() == Qt.Key_Enter:
            fen.toGrille(myMap(ResoudreArbre(fen.toListeIntAff(),fen.taille),fen.taille))
        

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
    taille=0

    def __init__(self,taille):
        QWidget.__init__(self)
        self.setWindowTitle("Résolveur de Sudoku")
        self.resize(800,800)
        self.taille=taille
        for i in range(taille):
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
        for i in range(taille):
            for j in range(taille):
                self.Grille.append(QLabel("0"))
                self.Grille1.append(Text())
                self.LigneLayout[i].addWidget(self.Grille[i*taille+j])
                self.Ligne1Layout[i].addWidget(self.Grille1[i*taille+j])
        for i in range(taille):
            self.WGridsLayout[0].addWidget(self.Lignes[i])
            self.WGridsLayout[1].addWidget(self.Lignes1[i])
        for i in range(taille):
            self.LigneLayout[i].setContentsMargins(68,9,9,9)
            
    def toListeInt(self):
        liste=[]
        for i in range(self.taille):
            liste.append([])
            for j in range(self.taille):
                liste[i].append(int(self.Grille[i*self.taille+j].text()))
        return liste
    
    def toListeIntAff(self):
        liste=[]
        for i in range(self.taille):
            liste.append([])
            for j in range(self.taille):
                liste[i].append(int(self.Grille1[i*self.taille+j].toPlainText()))
        return liste
    
    def toListe(self):
        liste=[]
        for i in range(self.taille):
            liste.append([])
            for j in range(self.taille):
                liste[i].append(self.Grille[i*self.taille+j].text())
        return liste
    
    def toGrille(self,liste):
        for i in range(self.taille):
            for j in range(self.taille):
                self.Grille[self.taille*i+j].setText(liste[i][j])

    def reInput(self):
        for i in range(self.taille):
            for j in range(self.taille):
                self.Grille1[self.taille*i+j].setText(self.Grille[self.taille*i+j].text())
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

def valideint(sudoku,taille):
    valide= True
    for i in range(taille):
        for j in range(taille):
            if sudoku[i][j]<0 or sudoku[i][j]>taille:
                valide=False
                
    for i in range(taille):
        l=sudoku[i]
        for j in range(taille+1):
            if l.count(j)>1 and j!=0:
                valide=False

    for i in range(taille):
        l=[]
        for j in range(taille):
            l.append(sudoku[j][i])
        for j in range(taille+1):
            if l.count(j)>1 and j!=0:
                valide=False

    divx=0
    divy=0
    for i in range(2,taille):
        if(taille%i==0 and i*i==taille):
            divx=i
    divy=divx
    if divx==0 and divy==0:
        for i in range(2,taille):
            if(taille%i==0 and divx==0):
                divx=i
        for i in range(2,taille):
            if(taille%i==0 and (divx*i)==taille and divy==0):
                divy=i
    for i in range(taille):
        l=[]
        for j in range(taille):
            l.append(sudoku[int(j/divx)+(int(i/divy)*divy)][(j%divx)+((i%divy)*divx)])
        for j in range(taille+1):
            if l.count(j)>1 and j!=0:
                valide=False
                
    return valide

def myMap(l,taille):
    l1=l.copy()
    for i in range(taille):
        for j in range(taille):
            l1[i][j]=str(l1[i][j])
    return l1
    
def Remplie(liste,taille):
    plein = True
    for i in range(taille):
        for j in range(taille):
            if (liste[i][j]==0):
                plein=False
    return plein

def Copie(liste,y,x,val):
    l=liste.copy()
    l[y][x]=val
    return l

def ResoudreArbre(liste,taille):
    c=1
    i=0
    j=0
    x=0
    y=0
    while x<taille:
        y=0
        while y<taille:
            if(liste[x][y]==0):
                i=x
                j=y
                x=taille
                y=taille
            y+=1
        x+=1
    while not Remplie(liste,taille):
        while c<taille and not valideint(Copie(liste,i,j,c),taille):
            c+=1
        if valideint(Copie(liste,i,j,c),taille):
            liste= ResoudreArbre(Copie(liste,i,j,c),taille)
            c+=1
        if c>=taille and not (Remplie(liste,taille) and valideint(liste,taille)):
            liste[i][j]=0
            return liste
    return liste

def countIndices(liste,taille,nombre,x,y):
    compt=0
    compt+=sum(z!=0 for z in i)
    for j in range(taille):
        if liste[j][x]!=0:
            compt+=1
    divx=0
    divy=0
    for i in range(2,taille):
        if(taille%i==0 and i*i==taille):
            divx=i
    divy=divx
    if divx==0 and divy==0:
        for i in range(2,taille):
            if(taille%i==0 and divx==0):
                divx=i
        for i in range(2,taille):
            if(taille%i==0 and (divx*i)==taille and divy==0):
                divy=i
    
    ssrng=range(0, taille, divy)
    for j in range(taille):
        
    
    return compt
        
def calculProba(liste,taille,probs):
    
    
def ResoudreProba(liste,taille):
    probs=9*[(100/9)]
    c=1
    i=0
    j=0
    x=0
    y=0
    while x<taille:
        y=0
        while y<taille:
            if(liste[x][y]==0):
                i=x
                j=y
                x=taille
                y=taille
            y+=1
        x+=1
    while not Remplie(liste,taille):
        while c<taille and not valideint(Copie(liste,i,j,c),taille):
            c+=1
        if valideint(Copie(liste,i,j,c),taille):
            liste= ResoudreArbre(Copie(liste,i,j,c),taille)
            c+=1
        if c>=taille and not (Remplie(liste,taille) and valideint(liste,taille)):
            liste[i][j]=0
            return liste
    return liste


def refresh(x,y,taille):
    for i in range(taille):
        for j in range(taille):
            x[i*taille+j].setText(y[i*taille+j].toPlainText())
fen = Fenetre(16)

l=[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

l1=[[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
l2=[[5,3,4,0,7,0,9,1,2],[6,7,2,1,0,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,0,7,6,0,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
l3=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


fen.reInput()


fen.show()

app.exec_()
 
