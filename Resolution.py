import docplex
from docplex.cp.model import CpoModel
import sys

def set 
def lpex1(liste):
    myInput =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    c=1
    M=CpoModel("Sudoku")
    GRNG = range(9)

    var = [[M.integer_var(min=1, max=9, name="x" + str(l*9+c)) for l in range(9)] for c in range(9)]
    
    # Add alldiff constraints for lines
    for l in GRNG:
        M.add(M.all_diff([var[l][c] for c in GRNG]))

    # Add alldiff constraints for columns
    for c in GRNG:
        M.add(M.all_diff([var[l][c] for l in GRNG]))

    # Add alldiff constraints for sub-squares
    ssrng = range(0, 9, 3)
    for sl in ssrng:
        for sc in ssrng:
            M.add(M.all_diff([var[l][c] for l in range(sl, sl + 3) for c in range(sc, sc + 3)]))
            
    msol=M.solve(TimeLimit=10)
    sol=[[msol[var[l][c]] for c in GRNG] for l in GRNG]
    for i in range(9):
        print(sol[i])
    
lpex1()
