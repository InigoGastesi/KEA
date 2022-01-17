from time import time
from tools import list_minisat2list_our_sat
import copy

# Write a function solve_nSAT using the search-tree technique outlined
# below that takes as its input a SAT instance (see Problem Set 2),
# applies pre-processing (see Problem Set 4), and then uses a search tree
# to find if the given instance has a satisfying assignment. Your function
# should return None if the given instance of SAT has no satisfying
# assignment and otherwise return a satisfying assignment.

# Take any clause that is not satisfied
# * If all variables have already been set, then there is no
#   possible solution anymore
# * Otherwise, branch into all possible cases where in each case a different
#   variable is set so that the clause becomes satisfied

# Note that any solution must fall into one of the above categories.
# Naturally, after having applied the pre-processing and also during the
# branching, some clauses will not contain three unassigned variables anymore
# and your program needs to account for that.

# You may write any additional functions you require to solve this problem.


def sat_preprocessing(num_variables, clauses, assig):
    # TODO:
    # Funtzio honen kodea programatu
    # Gomendagarria da funtzio lagungarriak definitzea
    validity = True
    # Validity true den bitartean, preprocessing aplikatu dela izango da, beraz iteratu preprocessing-a ezin denean egin artean
    while validity:
        validity = False
        # lehenengo begiratu ea r1 aplikatu daiteken eta asignazioa itzuli
        r1check, assig = check_r1(clauses, assig)
        if(r1check):
            clauses = r1_apply(clauses)
            validity = True
        # begiratu ea r2 aplikatu daiteke
        check, count = check_r2(clauses, num_variables)
        if(check):
            clauses, assig = r2_apply(clauses, count, assig)
            validity = True
        # klausulak ez badaude asignazioa eta klausula itzuli
        if(len(clauses) == 0):
            return clauses, assig
        # [] badago, sat unsatisfiable da asignazio honekin beraz errorea itzuli
        if([] in clauses):
            error = [[1], [-1]]
            return error, assig

    return clauses, assig


def check_r1(clauses, assig):
    for i in range(len(clauses)):
        # klausula bat bakarrik literal bat badu literala aurkitu dugu
        if(len(clauses[i]) == 1):
            if(clauses[i][0] < 0):  # literala negatiboa bada asignazioan 0 izango da, bestela 1
                assig[abs(clauses[i][0])] = 0
            else:
                assig[abs(clauses[i][0])] = 1
            return True, assig
    return False, assig


# funtzio honetan literalak zenbat aldiz agertzen diren aztertuko dugu
def check_r2(clauses, num_variables):
    count = [0]*(num_variables+1)
    # klausula guztiak iteratu eta aldagaiak kontatu eta count-en gorde
    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            count[abs(clauses[i][j])] = count[abs(clauses[i][j])] + 1
    # literal bat badago bakarrik behin agertzen dena true izuli
    if(1 in count):
        return True, count
    else:
        return False, count


def r1_apply(clauses):
    # aurkitu ze klausula duen luzera 1 eta literala gorde
    for i in range(len(clauses)):
        if(len(clauses[i]) == 1):
            var = clauses[i][0]
            break

    i = 0
    # literala duen klausulak ezabatu. -literala badago bakarrik literala ezabatu
    while i < len(clauses):
        if(var in clauses[i]):
            clauses.remove(clauses[i])
        elif(-var in clauses[i]):
            clauses[i].remove(-var)
        else:
            i += 1
    return clauses


def r2_apply(clauses, count, assig):
    # ze literala agertzen den bakarrik aldi batean
    variable = count.index(1)
    for i in range(len(clauses)):
        # literala badago asignazioa eguneratu eta klasula ezabatu
        if(variable in clauses[i]):
            index = clauses[i].index(variable)
            if(clauses[i][index] < 0):
                assig[variable] = 0
            else:
                assig[variable] = 1
            clauses.remove(clauses[i])
            return clauses, assig
        # -literala badago asignazioa eguneratu eta klasula ezabatu
        elif(-variable in clauses[i]):
            index = clauses[i].index(-variable)
            if(clauses[i][index] < 0):
                assig[variable] = 0
            else:
                assig[variable] = 1
            clauses.remove(clauses[i])
            return clauses, assig


def garbitu(clauses, index, assig):
    i = 0
    while i < len(clauses):
        if((assig[index] == 0 and -index in clauses[i]) or (assig[index] == 1 and index in clauses[i])):
            clauses.remove(clauses[i])
        elif(assig[index] == 0 and index in clauses[i]):
            clauses[i].remove(index)
        elif(assig[index] == 1 and -index in clauses[i]):
            clauses[i].remove(-index)
        else:
            i += 1
    return clauses


def solve_nSAT_recu(num_variables, clauses, assignment):
    # KASU NABARIA: klausula hutsa badago, emaitza aurkitu du. Batzuetan asignazioan
    # None aldagaiak daude, beraz None hauek 0 edo 1 bezala jarri ditzazkegu, ni 1 jartzea jarri dut
    if(len(clauses) == 0):
        if(None in assignment):
            for i in range(len(assignment)):
                if(assignment[i] == None):
                    assignment[i] = 1

        return assignment

    # BIGARREN KASU NABARIA: [] badago klasula batean, gure asignazioarako sat-a unsatisfiable da beraz [[]] itzuli
    elif([] in clauses):
        return [[]]
    else:
        # Asignazioan none ez badago errorea emango zuen, hau preprocessing egiterakoan gertatzen da,
        # batzuetan asignazio guztiak ipintzen dira, baina klausulak ez dira garbitzen beraz errorea ematen du
        try:
            index = assignment.index(None)
        except:
            # Klausulen luzera 0 ez bada, asignazio guztiak ipini dira, baina, klausulak ez dira garbitu beraz, unsatisfiable itzuli
            if(len(clauses) != 0):
                return [[]]

        # preprozesaketak egin
        clauses, assignment = sat_preprocessing(
            num_variables, copy.deepcopy(clauses), assignment.copy())
        # preprozesaketa itzulitako klausula [[1],[-1]] baldin bada unsat izango da, beraz [[]] itzuli
        if(clauses == [[1], [-1]]):
            return[[]]

        # bi asignazio kopiatu eta lehenengo None balioari 0 eta 1 esleitu
        assignment0 = assignment.copy()
        assignment1 = assignment.copy()
        assignment0[index] = 0
        assignment1[index] = 1

        # asignazioak egin ondoren klausulak garibtu
        clauses0 = garbitu(copy.deepcopy(clauses), index, assignment0)
        clauses1 = garbitu(copy.deepcopy(clauses), index, assignment1)
        # dei errekurtsiboak
        assig0 = solve_nSAT_recu(num_variables, clauses0, assignment0)
        assig1 = solve_nSAT_recu(num_variables, clauses1, assignment1)

        # asignazioak itzuli
        if([] not in assig0):
            return assig0
        if([] not in assig1):
            return assig1
        else:
            return [[]]


def solve_nSAT(num_variables, clauses):
    assig = [None]*(num_variables+1)
    assig[0] = 0
    assig = solve_nSAT_recu(num_variables, clauses.copy(), assig)
    if([] not in assig):
        return assig
    else:
        return "UNSATISFIABLE"


def test():

    print('Starting tests...')
    clauses = [[-2, -3, -1], [3, -2, 1], [-3, 2, 1],
               [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    solutions = [[0, 0, 0, 0],
                 [0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [1, 0, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0],
                 [None, 0, 0, 0],
                 [None, 0, 1, 1],
                 [None, 1, 0, 0],
                 [None, 1, 1, 0]]
    assert solve_nSAT(3, clauses) in solutions

    clauses = [[1, -2, -3], [2, -3, 1], [3, -2, 1],
               [2, 3, 1]]
    solutions = [[0, 1, 0, 0],
                 [0, 1, 0, 1],
                 [0, 1, 1, 0],
                 [0, 1, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 0, 1],
                 [1, 1, 1, 0],
                 [1, 1, 1, 1],
                 [None, 1, 0, 0],
                 [None, 1, 0, 1],
                 [None, 1, 1, 0],
                 [None, 1, 1, 1]]
    assert solve_nSAT(3, clauses) in solutions

    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    assert solve_nSAT(3, clauses) == "UNSATISFIABLE"

    clauses = [[4, -18, 19], [3, 18, -5], [-5, -8, -15], [-20, 7, -16], [10, -13, -7],
               [-12, -9, 17], [17, 19, 5], [-16, 9,
                                            15], [11, -5, -14], [18, -10, 13],
               [-3, 11, 12], [-6, -17, -8], [-18, 14,
                                             1], [-19, -15, 10], [12, 18, -19],
               [-8, 4, 7], [-8, -9, 4], [7, 17, -15], [12, -7, -14], [-10, -11, 8],
               [2, -15, -11], [9, 6, 1], [-11, 20, -
                                          17], [9, -15, 13], [12, -7, -17],
               [-18, -2, 20], [20, 12, 4], [19, 11,
                                            14], [-16, 18, -4], [-1, -17, -19],
               [-13, 15, 10], [-12, -14, -13], [12, -
                                                14, -7], [-7, 16, 10], [6, 10, 7],
               [20, 14, -16], [-19, 17, 11], [-7, 1, -
                                              20], [-5, 12, 15], [-4, -9, -13],
               [12, -11, -7], [-5, 19, -8], [-16], [20, -14, -15], [13, -4, 10],
               [14, 7, 10], [-5, 9, 20], [10, 1, -
                                          19], [-16, -15, -1], [16, 3, -11],
               [-15, -10, 4], [4, -15, -3], [-10, -
                                             16, 11], [-8, 12, -5], [14, -6, 12],
               [1, 6, 11], [-13, -5, -1], [-12], [1, -20, 19], [-2, -13, -8],
               [18], [-11, 14, 9], [-6, -15, -2], [-5], [-6, 17, 5],
               [-13, 5, -19], [20, -1, 14], [9, -17,
                                             15], [-5, 19, -18], [-12, 8, -10],
               [-18, 14, -4], [15, -9, 13], [9, -5, -1], [10, -19, -14], [20, 9, 4],
               [-9, -2, 19], [-5, 13, -17], [2, -
                                             10, -18], [-18, 3, 11], [7, -9, 17],
               [-15, -6, -3], [-2, 3, -13], [12, 3, -
                                             2], [2, -2, -3, 17], [20, -15, -16],
               [-5, -17, -19], [-20, -18, 11], [-9,
                                                1, -5], [-19, 9, 17], [17], [1],
               [4, -16, -5]]
    assert solve_nSAT(20, clauses) == "UNSATISFIABLE"

    print('Tests passed')


def test2():

    print('Starting Instances tests')
    # tupla = list_minisat2list_our_sat('instances/1-unsat.cnf')
    # print('1: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/2-sat.cnf')
    # print('2: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/3-sat.cnf')
    # print('3: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/4-sat.cnf')
    # print('4: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/6-sat.cnf')
    # print('6: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/7-unsat.cnf')
    # print('7: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/8-unsat.cnf')
    # print('8: ' + str(solve_nSAT(tupla[0], tupla[1])))
    # tupla = list_minisat2list_our_sat('instances/9-unsat.cnf')
    # print('9: ' + str(solve_nSAT(tupla[0], tupla[1])))

    # IRUZKIN HAUEK AURREKO GUZTIAK FUNTZIONATZERAKOAN KENDU...
    # tupla = list_minisat2list_our_sat('instances/5-unsat.cnf')
    # print('5: ' + str(solve_nSAT(tupla[0], tupla[1])))
    tupla = list_minisat2list_our_sat('instances/10-unsat.cnf')
    print('10: ' + str(solve_nSAT(tupla[0], tupla[1])))


start_time = time()
test()
elapsed_time = time() - start_time
print("Elapsed time for tests: %0.10f seconds." % elapsed_time)

start_time = time()
test2()
elapsed_time = time() - start_time
print("Elapsed time for instances tests: %0.10f seconds." % elapsed_time)
