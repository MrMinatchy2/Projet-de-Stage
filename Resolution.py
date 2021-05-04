import docplex
from docplex.mp.model import Model
import sys

def lpex1():
    c=1
    M=Model("Sudoku")
    var=[]
    for i in range(81):
        var.append(M.integer_var(name="x"+str(i)))
        M.add_constraint(var[i] >= 1, "c"+str(c))
        c+=1
    for i in range(9):
        M.add_constraint(sum(var[i*9:i*9+9]) == 45, "c"+str(c))
        c+=1
    
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if((i*9+j)!=(i*9+k)):
                    M.add_constraint(var[i*9+j] != var[i*9+k], "c"+str(c))
                    c+=1
    
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if((i*9+j)!=(j+((k*9))%81)):
                    M.add_constraint(var[i*9+j] != var[j+((k*9))%81], "c"+str(c))
                    c+=1

    M2=[]
    
    M.maximize(sum(var))
    M.solve()
    for i in range(81):
        print(var[i].solution_value,end=" ")
        if (i+1)%9==0:
            print(" ")
lpex1()
