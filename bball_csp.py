from cspbase import *
from player import *
from propagators import *
from player_data import *
import itertools

def get_cost_constraints(variable_array):
    constraints = []
    for position in variable_array:
        C = Constraint(str(position), [position])
        C.add_satisfying_tuples([tuple([player]) for player in position.domain() if (player.get_price() < 60000)])
        constraints.append(C)


    C = Constraint('Total Cost', variable_array)
    tuples = get_total_cost_tuples(variable_array) # need to compute any 5-tuple where the sum of assigned player costs is < 500k
    C.add_satisfying_tuples(tuples)
    constraints.append(C)
    return constraints 

def get_total_cost_tuples(variable_array):
    tuples = []
    max_cost = 500000
    min_cost = 200000
    for t in generate_tuples(variable_array[0].cur_domain()):
        total = sum([p.get_price() for p in t]) 
        if total <= max_cost and total >= min_cost:
            tuples.append(tuple(t))
    return tuples

def generate_tuples(variable_array):
    return itertools.permutations(variable_array, 5)
    

def get_all_diff_constraints(variable_array):
    """ Initialize da constraints """
    constraints = []
    # Each constraint takes two variable objects in its init. Then we add the satisfying tuples.
        #tuples = list of tuples of mutually exclusive variables.
    tuples = get_pairs_from_list(variable_array)
    for pair in tuples:
        constraints.append(get_constraint_from_pair(pair, variable_array))
    return constraints

def get_pairs_from_list(lst):
    """ Essentially just the cartesian product """
    tuples = []
    for i in range(0,len(lst)):
        for j in range(0,len(lst)):
            if i != j:
                tuples.append((lst[i], lst[j]))
    return tuples

def get_constraint_from_pair(tup, var_array):
    # tuple contains two variables.
    c = Constraint('C(' + str(tup[0]) + ',' + str(tup[1]) + ')', [tup[0], tup[1]])
    satisfying_tuples = get_pairs_from_list(var_array[0].domain()) # a tuple will satisfy these variables so long as no match.
    c.add_satisfying_tuples(satisfying_tuples)
    return c


def get_constraints(variable_array):
    """ Return an array of Constraint objects
        There are going to be various types of constraints.
        Eg: - All diff.
            - Affordable.
    """
    # Implement
    constraint_list = []


    # Need to add satisfying tuples!!!
    #all_diff = lambda v: (len(set([p for p in v])) == len([p for p in v])) 
    #all_diff_constraint = Constraint('All Diff', variable_array, all_diff)
    constraint_list += get_all_diff_constraints(variable_array)
    constraint_list += get_cost_constraints(variable_array)
    return constraint_list


def get_variables(initial_state):
    """ Return an array of Variable objects.
        Each variable has a domain.
        initial_state is an array of Player objects.
    """
    pos1 = Variable('position 1', list(initial_state.get_players()))
    pos2 = Variable('position 2', list(initial_state.get_players()))
    pos3 = Variable('position 3', list(initial_state.get_players()))
    pos4 = Variable('position 4', list(initial_state.get_players()))
    pos5 = Variable('position 5', list(initial_state.get_players()))
    return [pos1, pos2, pos3, pos4, pos5]


def bball_csp_model(initial_state):
    """
    Takes a Player Pool and converts it into the 
    proper CSP format (Variables and Constraints).
    """
    variable_array = get_variables(initial_state)
    constraint_list = get_constraints(variable_array)

    basketball_csp = CSP('basketball_csp')
    for v in variable_array:
        basketball_csp.add_var(v)

    for c in constraint_list:
        basketball_csp.add_constraint(c)

    return basketball_csp, variable_array

def print_soln(var_array):
    print([var.get_assigned_value() for var in var_array])
    print([var.get_assigned_value().get_price() for var in var_array if var.get_assigned_value()])



# basic form to interface with existing code.
if __name__ == "__main__":
    b = random_players()
    csp, var_array = bball_csp_model(b)
    solver = BT(csp)
    solver.bt_search(prop_GAC)
    print_soln(var_array)
    print(sum([p.get_assigned_value().get_price() for p in var_array if p.get_assigned_value()]))
