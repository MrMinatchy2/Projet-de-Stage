import docplex
from docplex.mp.model import Model
import sys

def carre(M,carre,c):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if((k*3+l)!=(i*3+j)):
                        M.add_constraint(carre[i*3+j] != carre[k*3+l], "c"+str(c))
                        c+=1
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

    var2=[]
    for i in range(3):
        for j in range(3):
            var2=[]
            for k in range(3):
                for l in range(3):
                    var2.append(var[i*9*3+k*9+j*3+l])
            if(j==2 or j==1):
                carre(M,var2,c)
                var2.clear()
    M.maximize(sum(var))
    M.solve()
    for i in range(81):
        print(var[i].solution_value,end=" ")
        if (i+1)%9==0:
            print(" ")
lpex1()
