#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:59:57 2020

@author: juanmi
"""

# TODO:
#
# Optimize Data types in formula to optimize space (memory)
#
# SAT -> All solutions
#   https://dwheeler.com/essays/minisat-user-guide.html
#   Getting more solutions
#   If you want to get another solution, the "obvious" way is to add, as a new clause, the negated form of the previous solution.
#


from itertools import combinations
from itertools import product

from time import time
from copy import copy, deepcopy
import os

from capstone_tools import calculate_formula_clause_amount

from capstone_tools import backtracking_display
from capstone_tools import minisat_display
from capstone_tools import nSAT_solver_display

#import gzip

import sys


def list_of_lists_to_string(matrix, result, list1, mysum):

    result = [x + [0] for x in result]  # 0 gehitu klausula bakoitzari
    output = ""
    number_of_variables = max(result)[0]  # emaitzaren zenbaki maximoa aurkitu
    # zenbakien multzoa stringra pasa
    strlist = ", ".join(str(e) for e in list1)
    output = "c [" + strlist + "] -> sums " + \
        str(mysum) + "\n"  # lehenengo lerrora
    output += "p cnf " + str(number_of_variables) + \
        " " + str(len(result)) + "\n"  # bigarren lerroa
    # klausula guztiak
    for i in range(len(result)):
        output += " ".join(str(e) for e in result[i])
        output += "\n"
    return output


def elkartrukaketa(A1, A2):
    elkar = []
    elkar.append([-A1, A2])
    elkar.append([A1, -A2])
    return elkar


def batuteka_2x2(A1, A2, indizea):
    batuketa = []
    batuketa.append([-indizea, A1, A2])
    batuketa.append([indizea, -A1, A2])
    batuketa.append([indizea, A1, -A2])
    batuketa.append([-indizea, -A1, -A2])
    return batuketa


def bururakoa_2x2(A1, A2, indizea):
    bururakoa = []
    bururakoa.append([-indizea, A1, A2])
    bururakoa.append([-indizea, -A1, A2])
    bururakoa.append([-indizea, A1, -A2])
    bururakoa.append([indizea, -A1, -A2])
    return bururakoa


def batuketa_4x4(A1, A2, A3, indizea):
    balioak = [A1, A2, A3]
    batuketa = []
    perms = list(product([0, 1], repeat=3))  # konbinazio guztiak sortu
    for perm in perms:
        lag = []  # ilara bat
        for i in range(len(perm)):
            # permutazioan 0 badago balioa - izango da bestela, +
            if(perm[i] == 0):
                lag.append(-balioak[i])
            else:
                lag.append(balioak[i])
        # permutazioaren 1 kopuruaren arabera, indizea + edo - izango da
        if(perm.count(1) == 1 or perm.count(1) == 3):
            lag.insert(0, -indizea)
        else:
            lag.insert(0, indizea)
        batuketa.append(lag)
    return batuketa


def bururakoa_4x4(A1, A2, A3, indizea):
    balioak = [A1, A2, A3]
    bururakoa = []
    perms = list(product([0, 1], repeat=3))  # konbinazio guztiak sortu
    for perm in perms:
        lag = []
        for i in range(len(perm)):
            # permutazioan 0 badago balioa - izango da bestela, +
            if(perm[i] == 0):
                lag.append(-balioak[i])
            else:
                lag.append(balioak[i])
        # permutazioaren 1 kopuruaren arabera, indizea + edo - izango da
        if(perm.count(1) == 2 or perm.count(1) == 3):
            lag.insert(0, -indizea)
        else:
            lag.insert(0, indizea)
        bururakoa.append(lag)
    return bururakoa


# Programatu beharreko metodoa
# Behar dituzun metodo lagungarri guztiak aurretik jarri


def preprocess(list1, mysum):
    index = 0
    while(index < len(list1)):
        if(list1[index] < 0):
            return 0
        if(list1[index] > mysum):
            list1.remove(list1[index])
        else:
            index += 1
    list1.sort()
    return list1


def reduce_subsetsum_to_SAT(list1, mysum):
    list1 = preprocess(list1, mysum)
    if(list1 == 0):
        print("balioren bat negatiboa da")
        return 0
    binary = []  # matrize honetan zenbaki guztiak gordeko dira binarioan
    ema = []  # hemen klausulak guztiak gordeko dira, hau da, emaitza
    for zenb in list1:
        binary.append(bin(zenb)[2:])

    for i in range(len(list1)):
        if(binary[i].count('1') == len(binary[i])):
            binary[i] = "0" + binary[i]

    # lehenengo taulen kalkulua matrix-en egongo dira, aldaketak aplikatu ondoren matrix-en dauden balioak
    # prematrix-en gordeko dira. Bukaeran, preamtrix balioen marizea izango da eta matrix, batuketen matrizea
    matrix = []
    prematrix = []

    indizea = len(binary)
    binzenb = bin(mysum)[2:]
    # balioak hasieratu
    for i in range(len(binary)):
        matrix.append([])
        for j in reversed(range(len(binary[i]))):
            indizea += 1
            if(binary[i][j] == '0'):
                matrix[i].append(-indizea)
                ema.append([-indizea])
            else:
                matrix[i].append(indizea)
                ema.append([indizea])

    prematrix = deepcopy(matrix)

    # tabla eguneratu, balioak egon ala ez egongo diren
    for i in range(len(matrix)):
        for j in (range(len(matrix[i]))):
            indizea += 1
            matrix[i][j] = indizea

    for j in (range(len(matrix))):
        for k in (range(len(matrix[j]))):
            ema.append([-matrix[j][k], j+1, abs(prematrix[j][k])])
            ema.append([-matrix[j][k], -(j+1), abs(prematrix[j][k])])
            ema.append([-matrix[j][k], j+1, -abs(prematrix[j][k])])
            ema.append([matrix[j][k], -(j+1), -abs(prematrix[j][k])])

    prematrix = deepcopy(matrix)
    # bururakoen matrizea izango da.
    burukoakMatrix = deepcopy(matrix)

    # tabla berriz eguneratu, hemen optimizazio bat egiten da, bururakoentzako balioak jartzen joaten dira, baina
    # emaitzaren luzeera ez da inoiz pasako
    for i in range(len(matrix)):
        # lehenengo batuketen matrizea eguneratu
        for j in (range(len(matrix[i]))):
            indizea += 1
            matrix[i][j] = indizea
        # lehenengo ilara ez bada, bururakoen matrizea eguneratu
        if(i != 0):
            gelditu = True
            # batuketen matrizean i ilara aurreko ilara baino txikiagoa bada, aldagiak gehitu i ilararen tamaina aurreko ilararen luzera+1 denean arte
            while(len(matrix[i]) <= len(matrix[i-1]) and gelditu):
                # hau optimizazioarako da, i ilararen luzera emaitzaren luzeera baino txikiago bada, balio bat gehitu daiteke, bestela, gelditu
                if(len(matrix[i]) < len(binzenb)):
                    indizea += 1
                    matrix[i].append(indizea)
                else:
                    gelditu = False

            # horain bururakoen matrizea osatzen da.
            for k in (range(len(matrix[i]))):
                if(k < len(binzenb)):
                    indizea += 1
                    try:
                        burukoakMatrix[i][k] = indizea
                    except:
                        burukoakMatrix[i].append(indizea)

    # lehenengo ilararen batuketa
    for i in (range(len(matrix[0]))):
        elkar = elkartrukaketa(matrix[0][i], prematrix[0][i])
        for row in elkar:
            ema.append(row)

    # taula guztiak 0 betetzen ditut, hau errazteko baturen kalkulua, aldagai bat badago i j posizioan aldagaia != 0 izango da
    # tabla zeroekin
    luzera = len(matrix[-1])
    for i in range(len(matrix)):
        for j in range(luzera-len(matrix[i])):
            matrix[i].append(0)

    # pretabla zeroekin
    for i in range(len(prematrix)):
        for j in range(luzera-len(prematrix[i])):
            prematrix[i].append(0)

    # bururakoen matrizea zeroekin
    luzera = len(burukoakMatrix[-1])
    for i in range(len(burukoakMatrix)):
        for j in range(luzera-len(burukoakMatrix[i])):
            burukoakMatrix[i].append(0)

    # bururakoen lehenengo ilaran 0 jarriz ez daudelako bururakorik, hau erroreak ez agertzeko egiten da
    for i in range(len(burukoakMatrix[0])):
        burukoakMatrix[0][i] = 0
    # 2. ilaratik aurrera
    for i in range(1, len(matrix)):
        for j in (range(len(matrix[i]))):
            # eskubiko zutabeko balioetarako
            if(j == 0):
                batuketaRes = batuteka_2x2(matrix[i-1][j], prematrix[i]
                                           [j], matrix[i][j])
                for row in batuketaRes:
                    ema.append(row)
                bururakoaRes = bururakoa_2x2(matrix[i-1][j], prematrix[i]
                                             [j], burukoakMatrix[i][j])
                for row in bururakoaRes:
                    ema.append(row)

            else:
                # batuketen matrizea == 0 bada, ez dago baliorik posizio horretan hau da, ez da kalkulurik egin behar
                if(matrix[i][j] != 0):
                    # 1. kasua: balioen matrizea == 0 eta batuketen matrizean goian ez dago aldagaiarik, hau da matrizea[i][j] == 0
                    if(prematrix[i][j] == 0 and matrix[i-1][j] == 0):
                        elkar = elkartrukaketa(
                            matrix[i][j], burukoakMatrix[i][j-1])
                        for row in elkar:
                            ema.append(row)
                    # 2. kasua: eskubiko bururakoa balioa du, goiko batuketa balioa du, baina posizioa hori balioen matrizean ez du aldagaiarik
                    elif((burukoakMatrix[i][j-1] != 0 and matrix[i-1][j] != 0 and prematrix[i][j] == 0)):
                        batuketaRes = batuteka_2x2(
                            matrix[i-1][j], burukoakMatrix[i][j-1], matrix[i][j])
                        for row in batuketaRes:
                            ema.append(row)
                        bururakoaRes = bururakoa_2x2(
                            matrix[i-1][j], burukoakMatrix[i][j-1], burukoakMatrix[i][j])

                        for row in bururakoaRes:
                            ema.append(row)
                    # 3. kasua: goiko batuketa ez du balirik eta balioen matrizean balioa du
                    elif(prematrix[i][j] != 0 and matrix[i-1][j] == 0):
                        batuketaRes = batuteka_2x2(
                            prematrix[i][j], burukoakMatrix[i][j-1], matrix[i][j])
                        for row in batuketaRes:
                            ema.append(row)
                        bururakoaRes = bururakoa_2x2(
                            prematrix[i][j], burukoakMatrix[i][j-1], burukoakMatrix[i][j])

                        for row in bururakoaRes:
                            ema.append(row)
                    # 4. kasua: aldagai guztiak balioa dute
                    else:
                        batuketaRes = batuketa_4x4(matrix[i-1][j], prematrix[i]
                                                   [j], burukoakMatrix[i][j-1], matrix[i][j])
                        for row in batuketaRes:
                            ema.append(row)

                        bururakoaRes = bururakoa_4x4(matrix[i-1][j], prematrix[i]
                                                     [j], burukoakMatrix[i][j-1], burukoakMatrix[i][j])
                        for row in bururakoaRes:
                            ema.append(row)

    # optimizazioa egiterakoan azkeneko zutabean, bururakoek ez dute baliorik izango, beraz klausulak gehitu -bururako balioarekin 0 izateko
    for i in range(len(burukoakMatrix)):
        if(burukoakMatrix[i][-1] != 0):
            ema.append([-burukoakMatrix[i][-1]])

    # azkeneko ilara emaitzan ipini
    for i in (range(len(matrix[-1]))):
        ema.append([matrix[-1][i]])

    # azkeneko ilararen zinuak aldatu
    luzera = len(matrix[-1])
    for i in reversed(range(len(binzenb))):
        if(binzenb[i] == '0'):
            ema[-luzera][0] = -ema[-luzera][0]
        luzera -= 1

    while luzera > 0:
        ema[-luzera][0] = -ema[-luzera][0]
        luzera -= 1

    # emaitza string moduan jarri
    output = list_of_lists_to_string(burukoakMatrix, ema, list1, mysum)
    return output


def generate_formula(filename, list1, mysum):
    myfilename = 'myresults/' + str(mysum) + '_subsetsum.cnf'

    if not os.path.exists(myfilename):
        start_time = time()
        formula = reduce_subsetsum_to_SAT(list1, mysum)
        elapsed_time = time() - start_time
        print("Elapsed time for formula generation: %0.10f seconds." %
              (elapsed_time))
        with open(filename, 'a') as f:
            f.write("formula,%s\n" % (elapsed_time))
        return formula


def solve_case_backtracking(filename, list1, mysum, plotfile):
    start_time = time()
    backtracking_display(list1, mysum, plotfile)
    elapsed_time = time() - start_time
    print("Elapsed time for test n=%s with backtracking: %0.10f" %
          (mysum, elapsed_time))
    with open(filename, 'a') as f:
        f.write("%s,backtracking,%s\n" % (mysum, elapsed_time))


def solve_case_minisat(filename, formula, list1, mysum, plotfile):
    start_time = time()
    minisat_display(formula, list1, mysum, plotfile)
    elapsed_time = time() - start_time
    print("Elapsed time for test n=%s with minisat: %0.10f" %
          (mysum, elapsed_time))
    with open(filename, 'a') as f:
        f.write("%s,minisat,%s\n" % (mysum, elapsed_time))


def solve_case_nSAT_solver(filename, formula, list1, mysum, plotfile):
    start_time = time()
    nSAT_solver_display(formula, list1, mysum, plotfile)
    elapsed_time = time() - start_time
    print("Elapsed time for test n=%s with SATSolver: %0.10f" %
          (mysum, elapsed_time))
    with open(filename, 'a') as f:
        f.write("%s,SATSolver,%s\n" % (mysum, elapsed_time))
