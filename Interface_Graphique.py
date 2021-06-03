import sys
import docplex
from docplex.cp.model import CpoModel
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit
#Varible indiquand la méthode de resolution choisie
Res=2

#La classe de nos zones de saisi de texte
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
            if Res==1:
                fen.toGrille(myMap(lpexl(fen.toListeIntAff(),fen.taille),fen.taille))
            if Res==2:
                fen.toGrille(myMap(ResoudreArbre(fen.toListeIntAff(),fen.taille),fen.taille))
        
#La classe de notre interface Graphique
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
    
#Fonction indiquant si un Sudoku est valide
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

#Fonction permettant d'avoir une liste représentant un sudoku d'entier sous la forme de liste de caractère
def myMap(l,taille):
    l1=l.copy()
    for i in range(taille):
        for j in range(taille):
            l1[i][j]=str(l1[i][j])
    return l1

#Fonction indiquand si un sudoku contient des cases vides    
def Remplie(liste,taille):
    plein = True
    for i in range(taille):
        for j in range(taille):
            if (liste[i][j]==0):
                plein=False
    return plein

#Fonction permettant la copie de notre sudoku
def Copie(liste,y,x,val):
    l=liste.copy()
    l[y][x]=val
    return l

#Fonction de résolution utilisant le backtracking
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

#Fonction pour actualiser notre affichage
def refresh(x,y,taille):
    for i in range(taille):
        for j in range(taille):
            x[i*taille+j].setText(y[i*taille+j].toPlainText())

#Fonction permettant de charger les case déjà rempli de notre sudoku parmi nos contraintes
def chargez(var,liste,taille):
    for i in range(taille):
        for j in range(taille):
            if(liste[i][j]>0):
                var[i][j].set_domain((liste[i][j], liste[i][j]))

#Fonction de resolution utilisant Cplex
def lpexl(liste,taille):

    c=1
    M=CpoModel("Sudoku")
    GRNG = range(taille)

    var = [[M.integer_var(min=1, max=taille, name="x" + str(l*taille+c)) for l in range(taille)] for c in range(taille)]

    # Ajout des contraintes sur les lignes
    for l in GRNG:
        M.add(M.all_diff([var[l][c] for c in GRNG]))

    # Ajout des contraintes sur les colonnes
    for c in GRNG:
        M.add(M.all_diff([var[l][c] for l in GRNG]))

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
    
    
    # Ajout des contraintes sur les sous grilles
    ssrng = range(0, taille, divy)
    for sl in ssrng:
        for sc in range(0, taille, divx):
            M.add(M.all_diff([var[l][c] for l in range(sl, sl + divy) for c in range(sc, sc + divx)]))
    chargez(var,liste,taille)
    msol=M.solve(TimeLimit=10)
    sol=[[msol[var[l][c]] for c in GRNG] for l in GRNG]
    return sol
        
fen = Fenetre(16)

fen.show()

app.exec_()
 
