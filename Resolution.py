import docplex
from docplex.cp.model import CpoModel
import sys

def chargez(var,liste):
    for i in range(9):
        for j in range(9):
            if(liste[i][j]>0):
                var[i][j].set_domain((liste[i][j], liste[i][j]))
def lpex1(liste,taille):

    c=1
    M=CpoModel("Sudoku")
    GRNG = range(taille)

    var = [[M.integer_var(min=1, max=taille, name="x" + str(l*taille+c)) for l in range(taille)] for c in range(taille)]

    # Add alldiff constraints for lines
    for l in GRNG:
        M.add(M.all_diff([var[l][c] for c in GRNG]))

    # Add alldiff constraints for columns
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
    
    
    # Add alldiff constraints for sub-squares
    ssrng = range(0, taille, divy)
    for sl in ssrng:
        for sc in range(0, taille, divx):
            M.add(M.all_diff([var[l][c] for l in range(sl, sl + divy) for c in range(sc, sc + divx)]))
    chargez(var,liste)
    msol=M.solve(TimeLimit=10)
    sol=[[msol[var[l][c]] for c in GRNG] for l in GRNG]
    for i in range(taille):
        print(sol[i])
sudoku =[[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
lpex1(sudoku,10)
