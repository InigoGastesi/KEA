def sat_preprocessing(num_variables, clauses):
    # TODO:
    # Funtzio honen kodea programatu
    # Gomendagarria da funtzio lagungarriak definitzea
    assig = [None]*(num_variables+1)
    assig[0] = 0
    validity = True
    while validity:
        validity = False
        r1check, assig = check_r1(clauses, assig)
        if(r1check):
            clauses = r1_apply(clauses)
            validity = True
        check, count = check_r2(clauses, num_variables)
        if(check):
            clauses, assig = r2_apply(clauses, count, assig)
            validity = True
        if(len(clauses) == 0):
            return clauses
        if([] in clauses):
            error = [[1], [-1]]
            return error

    return clauses


def check_r1(clauses, assig):
    for i in range(len(clauses)):
        if(len(clauses[i]) == 1):

            if(clauses[i][0] < 0):
                assig[abs(clauses[i][0])] = 0
            else:
                assig[abs(clauses[i][0])] = 1
            return True, assig
    return False, assig


def check_r2(clauses, num_variables):
    count = [0]*(num_variables+1)
    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            count[abs(clauses[i][j])] = count[abs(clauses[i][j])] + 1

    if(1 in count):
        return True, count
    else:
        return False, count


def r1_apply(clauses):

    var = 0

    for i in range(len(clauses)):
        if(len(clauses[i]) == 1):
            var = clauses[i][0]
            break

    i = 0
    while i < len(clauses):
        if(var in clauses[i]):
            clauses.remove(clauses[i])
            i -= 1
        elif(-var in clauses[i]):
            clauses[i].remove(-var)
        i += 1
    return clauses


def r2_apply(clauses, count, assig):
    variable = count.index(1)
    for i in range(len(clauses)):
        if(variable in clauses[i]):
            index = clauses[i].index(variable)
            if(clauses[i][index] < 0):
                assig[variable] = 0
            else:
                assig[variable] = 1
        elif(-variable in clauses[i]):
            index = clauses[i].index(-variable)
            if(clauses[i][index] < 0):
                assig[variable] = 0
            else:
                assig[variable] = 1

        clauses.remove(clauses[i])
        return clauses, assig


def test():
    assert [] == sat_preprocessing(1, [[1]])
    assert [[1], [-1]] == sat_preprocessing(1, [[1], [-1]])
    assert [] == sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                       [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                       [1, 3, -4], [3, -4, 1], [-1]])
    assert [[1], [-1]] == sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                                [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                                [-3, -1], [-4], [4, -1, 2]])

    ans = [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans == sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], [-3, 2, -5, 6, -4]])
    # Espreski 2. erregela frogatzeko
    assert [] == sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                       [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                       [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]])


test()
