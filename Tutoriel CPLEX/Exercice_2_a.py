
import cplex
from cplex.exceptions import CplexError
import sys

# data common to all populateby functions
my_obj      = [2.0, 1.0]

my_colnames = ["x1", "x2"]
my_rhs      = [9.0, 3.0,12.0,0.0,0.0]
my_rownames = ["c1", "c2","c3","c4","c5"]
my_sense    = "GLLGG"


def populatebyrow(prob):
    prob.objective.set_sense(prob.objective.sense.maximize)

    # since lower bounds are all 0.0 (the default), lb is omitted here
    prob.variables.add(obj = my_obj, names = my_colnames)

    rows = [[["x1","x2"],[3.0, 2.0]],[["x1","x2"],[0.0,1.0]],[["x1","x2"],[ 3.0,-1.0 ]],[["x1","x2"],[ 1.0,0.0 ]],[["x1","x2"],[ 0.0,1.0 ]]]
    
    prob.linear_constraints.add(lin_expr = rows, senses = my_sense,rhs = my_rhs, names = my_rownames)


def lpex1(pop_method):
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
    slack = my_prob.solution.get_linear_slacks()
    pi    = my_prob.solution.get_dual_values()
    x     = my_prob.solution.get_values()
    dj    = my_prob.solution.get_reduced_costs()
    for i in range(numrows):
        print("Row %d:  Slack = %10f  Pi = %10f" % (i, slack[i], pi[i]))
    for j in range(numcols):
        print("Column %d:  Value = %10f Reduced cost = %10f" % (j, x[j], dj[j]))

    my_prob.write("lpex1.lp")

lpex1("r")
