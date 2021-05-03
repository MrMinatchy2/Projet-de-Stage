
import cplex
from cplex.exceptions import CplexError
import sys

# data common to all populateby functions
my_obj      = []
my_ub       = []
my_colnames = []
my_rhs      = []
my_rownames = []
my_sense    = "LLLLLLLLL"
for i in range(9):
    my_rhs.append(45.0)
    my_rownames.append("c"+str(i+1))
for i in range(81):
    my_colnames.append("x"+str(i+1))
    my_obj.append(1.0)
    my_ub.append(cplex.infinity)
    my_rhs.append(1.0)
    my_rownames.append("c"+str(9+i+1))
    my_sense=my_sense+"G"



def populatebyrow(prob):
    prob.objective.set_sense(prob.objective.sense.maximize)
    v_name=[]
    for i in range(648*2):
        v_name.append("i"+str(81+i+1))
    # since lower bounds are all 0.0 (the default), lb is omitted here
    prob.variables.add(obj = my_obj, ub = my_ub, names = my_colnames)
    prob.variables.add(names = v_name)

    rows = []
    for i in range(9):
        p1=[]
        p2=[]
        for j in range(9):
            p1.append("x"+str((i*9+j)+1))
            p2.append(1.0)
        rows.append([p1.copy() , p2.copy()])
    for i in range(81):
        rows.append([["x"+str(i+1)], [1.0]])
    prob.linear_constraints.add(lin_expr = rows, senses = my_sense,rhs = my_rhs, names = my_rownames)
    my_indvar=[]
    rows1=[]
    c=0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if((i*9+j)!=(i*9+k)):
                    rows1.append([["x"+str(i*9+j+1),"x"+str(i*9+k+1)], [1.0,-1.0]])
                    my_indvar.append("i"+str(81+c+1))
                    c+=1
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if((i*9+j)!=(i+((k*9))%81)):
                    rows1.append([["x"+str(i*9+j+1),"x"+str(i+((k*9))%81+1)], [1.0,-1.0]])
                    my_indvar.append("i"+str(81+c+1))
                    c+=1
    for i in range(648*2):
        prob.indicator_constraints.add(indvar=my_indvar[i],complemented=0,rhs=0.0,sense="E",lin_expr=rows1[i],name="ind"+str(i+1),indtype=1)


def lpex1():
    try:
        my_prob = cplex.Cplex()
        handle = populatebyrow(my_prob)
        my_prob.solve()
    except(CplexError):
        print(CplexError)
        return

    numrows = my_prob.linear_constraints.get_num()
    numcols = my_prob.variables.get_num()

    print
    # solution.get_status() returns an integer code
    print("Solution status = " , my_prob.solution.get_status(), ":")
    # the following line prints the corresponding string
    print(my_prob.solution.status[my_prob.solution.get_status()])
    print("Solution value  = ", my_prob.solution.get_objective_value())
    
    x     = my_prob.solution.get_values()
    
    for j in range(numcols):
        print("Column %d:  Value = %10f" % (j, x[j]))

    my_prob.write("lpex1.lp")

lpex1()
