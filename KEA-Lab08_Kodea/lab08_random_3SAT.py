import random
from time import time
# Aurretik egindakoak hartu


def is_satisfied_clause(clause, assig):
    for j in range(len(clause)):
        if(clause[j] > 0 and assig[clause[j]] == 1):
            return True
        elif(clause[j] < 0 and assig[abs(clause[j])] == 0):
            return True
        return False


def is_satisfied(num_variables, clauses, assignment):
    for i in range(len(clauses)):
        # klausula bakoitzeko literala iteratu
        for j in range(len(clauses[0])-1):
            # iteratutako aldagaia ezeztatuta ez badago eta asignazioa bat bada
            if(clauses[0][j] > 0 and assignment[clauses[0][j]] == 1):
                clauses.remove(clauses[0])
                break
            # iteratutako aldagaia ezeztatuta badago eta asignazioa zero bada
            elif(clauses[0][j] < 0 and assignment[abs(clauses[0][j])] == 0):
                clauses.remove(clauses[0])
                break

    return clauses == []

# Programatu beharreko funtzioa
# Ausaz asignazio bat sortu
# False egiten duen klausula bat topatuta, ausaz literal bati dagokion aldagaiaren balioa aldatu
# Errepikatu prozesua sarrera formularen aldagai kopuruaren balioa adina aldiz


def random_3SAT(clauses, num_variables):
    assig = [random.randint(0, 1) for i in range(num_variables+1)]
    assig[0] = 0
    aldi_kop = int(10/((2/3)**num_variables))
    for i in range(0, aldi_kop):
        if(not is_satisfied(num_variables, clauses, assig)):
            for j in range(len(clauses)):
                if(not is_satisfied_clause(clauses[j], assig)):
                    index = random.choice(clauses[j])
                    if assig[abs(index)] == 1:
                        assig[abs(index)] = 0
                    else:
                        assig[abs(index)] = 1
        else:
            return "Iteration:" + str(i) + " of " + str(aldi_kop) + " assig:" + str(assig)
    return "Error"


def test():

    clauses = [[1, -2, -4], [1, 4, 2], [2, -1, -4],
               [2, 4, -1], [-3, -1, 4], [-3, 1, -2], [-3, -4, 2]]
    print(random_3SAT(clauses, 4))

    clauses = [[3, 1, 2], [1, 2, -3], [-3, 1, -2], [1, 3, -2],
               [3, -1, 2], [-1, 2, -3], [-3, -1, -2], [-1, 4, -2]]
    print(random_3SAT(clauses, 4))

    clauses = [[-18, 4, 23], [14, 18, -13], [-13, -14], [-14, -3, 1], [6, 5, -4], [20, 10], [11, 13, -18], [26, 22, -28], [27, -17, 13], [10, 30, -8], [7, -26, 25], [-25, -1], [8, -5, -24], [-19, -4, 22], [3, 16, 1], [2, 3, -9], [-24, 28, -29], [16, -13, 12], [-12, 4, -3], [-18, 14, -23], [-19, -22, 29], [-25, 19, -14], [11, -18, -25], [-9, 20, -15], [-7, 1, 11], [-19, 20, -29], [1, -12], [4, -13, 27], [2, 23, -3], [11, -1, -22], [-14, -3, 13], [-13, 24, 17], [23, -16, -28], [-2, -30, 14], [-14, 17, 9], [-20, -26, 29], [13, -28, 12], [22, -9, 15], [-17, 11, 7], [27, -14], [-6, 28, -25], [-27, 4, 2], [-13, 14, 29], [-18, -11, 16], [21, -2, 15],
               [-9, -1, 28], [-2, 1, -3], [-6, 13, -3], [10, -7, -21], [22, -9, -21], [-4, 5, -2], [16, 15, 13], [-9, 11, -30], [-15, -30, 3], [-10, -3, -9], [15, 26, -3], [-18, -8, -5], [22, -27, 21], [26, 23, -16], [-21, -12, 8], [-14, 27, 28], [-24, 11, 10], [-24, 8, -21], [-14, -21, -19], [5, 4, -23], [5, -6, 11], [-5, -13, 18], [30, 12, -15], [-5, -8, -9], [-9, 16], [-27, 21, 24], [-26, -5, -16], [2, -7, 14], [5, -15, 8], [10, 19, -27], [9, -23, 19], [-28, -18, 29], [20, -28, -29], [-21, 30, 14], [20, -16, -8], [-9, -24, 30], [25, 7, 11], [-9, 30, -25], [10, -18, -2], [7, 23, 1], [24, 30, -21], [-22, -16, 19], [29, -20, -27], [-5, -23], [22, 30, -24]]
    print(random_3SAT(clauses, 30))

    clauses = [[10, 7, 23], [-7, -2, -36], [-21, -35, 13], [21, 33, -37], [37, -28, 27], [15, 16, 35], [-36, -15, -34], [1, 29, -35], [-17, -23, 10], [3, 18, -9], [-40, 38, -28], [11, 6], [17, -28, 36], [26, -4, -23], [15, 16, 23], [40, 2, 21], [27, 6, 20], [35, -30, 26], [-15, -4, -28], [22, -26, 38], [-6, 13], [2, 21, -23], [-2, 1, -9], [5, 29, 28], [21, 27, -24], [-17, 5, 18], [8, 10, 13], [21, -22], [36, 8, -39], [-12, 14, -22], [1, -5, 31], [7, -20, 16], [-1, -9, -12], [-9, 13, 27], [-34, 38, 4], [-37, 27, 13], [-15, 29, 28], [-33, 37, 4], [-24, 40, -31], [40, -36, -35], [40, -39, 24], [27, 36, -5], [-38, 17, -32], [-23, -11, -31], [1, 33, -34], [-11, 16, -40], [21, -8, 39], [-7, -37, 6], [6, -18, -35], [32, 31, 11], [11, 21, -39], [-14, 35, -4], [15, 35, -21], [-18, -8, 15], [-38, 15, -2], [25, 22, 37], [-20, -31, 17], [6, -7, 3], [-33, -27, -17], [-1, -25], [23, 27, 21], [-6, -34, -25], [-10, -4, 21], [-16, 9, -10], [-28, 1, 7], [15, -12], [23, -39, -20], [13, -8, -29], [9, -19, -15], [-23, -5, 36], [10, -21, -27], [34, -12, -23], [21, -27, -40], [21, -16, 18],
               [5, -11, -32], [-7, -28, 33], [40, 24, 2], [-32, -1, 6], [-3, -40, -1], [19, 29, 11], [-29, 22, 32], [-9, -12, -7], [8, -6, 15], [32, -21, -29], [13, -28, 6], [22, 25], [9, -13], [-1, -17], [-14, -31, 9], [2, 34, -16], [-18, 35, 34], [-30, 16, -29], [26, 6, -8], [-2, 31, 22], [38, -18, 3], [-21, -34, -13], [25, 38, -31], [9, -21, 19], [29, -22, -36], [27, -15, 38], [26, -3], [-17, 1, -31], [24, -5, 25], [-23, 2, 37], [38, 20, -6], [29, -11, 8], [-16, 27, 3], [-3, -1, -20], [23, -14, 9], [26, -16], [23, -18, 28], [-22, -36, -28], [3, 19, 40], [21, 3, -39], [36, -40, -37], [-14, -35, -6], [-37, -40, 39], [-15, -30, -4], [32, 21, -23], [-14, 15, -25], [36, 4, -32], [2, 21], [13, 37, -25], [4, -17, -7], [-24, -4, 19], [18, 32, -10], [17, 21, -23], [22, -1, 21], [-22, -16, -40], [18, 35, 4], [12, -9, -26], [-11, -25, -19], [18, 1, -2], [-16, 28, 34], [38, 40, 28], [-38, 11, 40], [16, 21, -26], [1, -3, 5], [-28, 14, -2], [37, 25, -40], [34, 38, 26], [-30, 12, 22], [-1, 16, 29], [-12, 15, -25], [15, -30, 2], [35, 1, -40], [-17, -3], [13, -12, -8], [36, 26, 10], [2, 39, 26]]
    print(random_3SAT(clauses, 40))

    clauses = [[29, -34, -44], [7, -39, -13], [12, -37, 47], [-2, -49, -26], [44, 2, 1], [-41, 43, 12], [34, -14, -24], [-44, 12, 19], [-24, -41, -49], [-15, 14, -40], [-34, 30], [39, 44, 36], [-23, 3, -12], [46, 47, 44], [-14, -37, 13], [-37, -14, 12], [40, -1, -3], [21, 18, -40], [-14, 4, 16], [-23, 48, 50], [38, 12, 37], [30, -22, -19], [-9, -20, 41], [35, 39, -6], [8, 49, -33], [-8, -43, 9], [31, -36, -46], [-44, -4, 24], [-22, -10, 2], [28, 20, 13], [10, 38, 8], [-10, -37, -3], [26, 1, 12], [-7, 2, 33], [-35, 26, -1], [10, -29, 1], [-19, -33, -15], [19, -44, -21], [-50, -30, -38], [7, -34, 45], [27, -48, 47], [24, -5, 33], [41, 26, -48], [29, 36, -19], [24, -43, 49], [-17, -26, 45], [40, 23, -38], [30, -29, -9], [2, -49, -36], [46, -38, 12], [-26, 15, 43], [37, -11, 42], [35, -50, 7], [7, -4, 16], [49, -14, -9], [9, 41, -43], [-19, -45, 9], [19, 30, -43], [47, -36, -22], [-46, 25, -15], [33, 46, 12], [-13, 2, 43], [-9, 14, -29], [-22, 39, 28], [3, -25, -12], [-44, -42, -11], [34, 15, -25], [-39, 50, -45], [-9, -22, -1], [-2, -39, -37], [-45, -4, 6], [8, 11, 37], [11, -45, 14], [-25, 49, -50], [18, -19, -22], [49, 11], [-14, 23, 13], [-6, 30, 32], [33, -38, -29], [-2, -8, 39], [20, -23, 24], [-1, 37, 14], [38, 16, -4], [-19, 23], [32, 10, 30], [3, 8, -7], [16, 21, -32], [-31, -23, 40], [15, -8, 21], [26, 20, -8], [-27, -20, -43], [-31, -16, 39], [1, -12, 30], [-1, -8, 9], [-49, 45, -17], [43, -5, -36], [-1, -16, 35], [-10, 42, 19], [-6, -49, 27], [-29, -9, -47],
               [-8, 6, 50], [-4, 42, 6], [-24, 22, -8], [-25, -32, -11], [30, 9, -50], [-22, 30, 26], [14, -27, 35], [2, 28, 7], [1, 44, -31], [15, -18], [-32, 7, 44], [-14, -12, -49], [-27, 45, -3], [-33, 7, 4], [29, -28, -19], [30, -17, -21], [37, 28, -2], [37, -18, -2], [44, -39, 17], [-39, -35, -22], [33, 16, -24], [17, 50, -12], [-50, 41, -32], [16, -47, 41], [-16, -40, -25], [-3, 6, -32], [-12, -38, 27], [39, 28, -18], [-12, -35, 15], [17, -43, 30], [-40, -26, -48], [-33, -25, 49], [-29, 23, 15], [-34, 19, 42], [33, 10, -26], [-22, 35, 43], [-11, -42, 29], [43, 22, -15], [-17, -8, -20], [10, -14, -12], [-43, 3, -12], [1, 30, -15], [7, 15, -18], [-23, 25, -43], [6, -33, 34], [15, -11, 12], [-31, 39, 21], [46, -24, -7], [-47, -49, -23], [49, -35, -23], [-3, 29, -40], [-5, -13, 23], [24, 23, 3], [-43, 31, -39], [-44, -26, -47], [50, 1], [38, -33, -35], [45, -12, 6], [36, 32, -16], [42, 10], [-9, 29, 32], [-37, 21, -2], [4, -39, -47], [28, -13, 19], [-45, -11, 19], [-16, 28, 34], [45, 40, -21], [39, 7, -38], [18, 47, 33], [-39, -12, 6], [22, -12, 30], [44, 3, 15], [5, 47, 25], [-25, -28, 41], [33, 45, 26], [41, 8, 7], [-9, -17, -32], [21, 47, -26], [-48, -16, 32], [-32, -41, -10], [-8, -36, -31], [-25, 22, -1], [-45, -49, -11], [50, 18, 6], [39, -43, -12], [-8, 11, 17], [-39, -44, 13], [35, 27, -34], [-50, 42, -23], [-6, 12, 11], [-15, -41, -33], [45, -33, -2], [-13, -32, -8], [-22, 17, 12], [11, 7, 31], [-46, 3, -47], [10, -15, 16], [43, 11, -28], [-43, 23, -25], [26, -19, -31]]
    print(random_3SAT(clauses, 50))


start_time = time()
test()
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)