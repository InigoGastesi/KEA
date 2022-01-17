#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:45:41 2021

@author: juanmi
"""

from time import time

import os
import pickle

import sys

from subsetSum_backtracking import subset

from SubsetSum_to_SAT import generate_formula
from SubsetSum_to_SAT import solve_case_backtracking
from SubsetSum_to_SAT import solve_case_nSAT_solver
from SubsetSum_to_SAT import solve_case_minisat

# Metodo honetan, load_instances metodoak egiten duen berdina egin behar da, baina:
#   - soluzio guztiak atera nahi dira, ez bakarra
# Metodoa garatzeko load_instances  metodoan egindakoa hartu eta soluzio posible guztiak ateratzeko egokitu

def load_instances_all_solutions(folder, inst_folder):
    mydirname = './' + inst_folder + '_instances/'
    if not os.path.exists(mydirname):
        os.makedirs(os.path.dirname(mydirname), exist_ok=True)

    for file in os.listdir(mydirname):
        if file.endswith(".pkl"):
            #print(mydirname + file)
            #print(mydirname + file)
            #print(os.path.join("/mydir", file))
            clauses = pickle.load(open(mydirname + file, "rb"))
            # print(clauses)

            with open(mydirname + file.split('.')[0] + '.txt', "r") as f:
                contents = int(f.read())
                print(contents)

                results_dir = './myresults/' + folder + '/' + inst_folder + '/'
                plots_dir = './myplots/' + folder + '/' + inst_folder + '/'
                if not os.path.exists(results_dir):
                    os.makedirs(os.path.dirname(results_dir), exist_ok=True)
                if not os.path.exists(plots_dir):
                    os.makedirs(os.path.dirname(plots_dir), exist_ok=True)

                filename = './myresults/' + folder + '/subsetsum_' + folder + '_times.csv'
                plotfile = './myplots/' + folder + '/' + inst_folder + '/' + file + '.png'
                if folder == 'backtracking':
                    solve_case_backtracking(
                        filename, clauses, contents, plotfile)
                elif folder == 'nsatsolver':
                    # solve_case_nSAT_solver(filename, formula, list1, mysum, plotfile):
                    formula = generate_formula(filename, clauses, contents)
                    solve_case_nSAT_solver(
                        filename, formula, clauses, contents, plotfile)
                elif folder == 'minisat':
                    # solve_case_nSAT_solver(filename, formula, list1, mysum, plotfile):
                    formula = generate_formula(filename, clauses, contents)
                    solve_case_minisat(filename, formula,
                                       clauses, contents, plotfile)
                    
                    last_line=""
                    zenbat_erantzuna=1
                    while(last_line != "UNSAT"):
                        luzera = len(clauses)
                        output_file="./myresults/" + str(contents) + ".txt_output.txt"
                        f_read = open(output_file, "r")
                        last_line = f_read.readlines()[-1]
                        f_read.close()
                        if(last_line == "UNSAT\n"):
                            break
                        zenbat_erantzuna+=1
                        emaitza = last_line.split(" ")#last line " " karakterearen bidez banandu
                        emaitza = emaitza[0:luzera]#lehenago kalkulatutako listaren luzera erabiliz lehenengo luzera aldagaiak aukeratu
                        for i in range(len(emaitza)):
                            emaitza[i] = int(emaitza[i]) # string-etik int ra pasa

                        outcome=""
                        for number in emaitza:
                            outcome += str(-number) + " "# -aldagaia outcomeri gehitu

                        outcome += '0\n' #0 a gehitu eta lerro jauzia ipini
                        with open("./myresults/"+ str(contents)+ ".txt", 'a') as f:
                            f.write(outcome)

                        pantaila_emaitza=[]
                        # pantailan emaitza ipini
                        for i in range(len(emaitza)):
                            if emaitza[i] > 0:
                                pantaila_emaitza.append(clauses[i])

                        print(pantaila_emaitza)

                        #formulari klasula bat gehitzeko
                        with open("./myresults/"+ str(contents)+ ".txt", "r") as f:
                            formula = f.read()
                        
                        formula_split_enter = formula.split('\n') #formula '\n' bidez split egin bigarren lerroa lortzeko
                        formula_second_line = formula_split_enter[1]
                        formula_second_line = formula_second_line.split(" ")#bigarren lerroan ' ' split egin azkeneko blaioa lortzeko
                        formula_second_line[-1] = str(int(formula_second_line[-1])+1)#azkeneko balioari +1 egin
                        #bigarren lerroaren string-a berriz eraiki
                        formula_split_enter[1] = ""
                        for elem in formula_second_line:
                            formula_split_enter[1]+=elem+" "
                        formula_split_enter[1] = formula_split_enter[1][0:-1]
                        #formula osoa berriz eraiki
                        formula = ""
                        for elem in formula_split_enter:
                            formula += elem + "\n"

                        formula = formula[0:-1] #azkeneko '\n' ezabatu
                        solve_case_minisat(filename, formula,
                                       clauses, contents, plotfile)




                    

def load_instances(folder, inst_folder):

    mydirname = './' + inst_folder + '_instances/'
    if not os.path.exists(mydirname):
        os.makedirs(os.path.dirname(mydirname), exist_ok=True)

    for file in os.listdir(mydirname):
        if file.endswith(".pkl"):
            #print(mydirname + file)
            #print(mydirname + file)
            #print(os.path.join("/mydir", file))
            clauses = pickle.load(open(mydirname + file, "rb"))
            # print(clauses)

            with open(mydirname + file.split('.')[0] + '.txt', "r") as f:
                contents = int(f.read())
                print(contents)

                results_dir = './myresults/' + folder + '/' + inst_folder + '/'
                plots_dir = './myplots/' + folder + '/' + inst_folder + '/'
                if not os.path.exists(results_dir):
                    os.makedirs(os.path.dirname(results_dir), exist_ok=True)
                if not os.path.exists(plots_dir):
                    os.makedirs(os.path.dirname(plots_dir), exist_ok=True)

                filename = './myresults/' + folder + '/subsetsum_' + folder + '_times.csv'
                plotfile = './myplots/' + folder + '/' + inst_folder + '/' + file + '.png'
                if folder == 'backtracking':
                    solve_case_backtracking(
                        filename, clauses, contents, plotfile)
                elif folder == 'nsatsolver':
                    # solve_case_nSAT_solver(filename, formula, list1, mysum, plotfile):
                    formula = generate_formula(filename, clauses, contents)
                    solve_case_nSAT_solver(
                        filename, formula, clauses, contents, plotfile)
                elif folder == 'minisat':
                    # solve_case_nSAT_solver(filename, formula, list1, mysum, plotfile):
                    formula = generate_formula(filename, clauses, contents)
                    solve_case_minisat(filename, formula,
                                       clauses, contents, plotfile)


def test_backtracking():

    start_time = time()
    load_instances('backtracking', 'backtracking')
    elapsed_time = time() - start_time
    print("BACKTRACKING: backtracking_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    start_time = time()
    load_instances('backtracking', 'sample')
    elapsed_time = time() - start_time
    print("BACKTRACKING: sample_instances -> Elapsed time: %0.10f seconds." %
          elapsed_time)

    # start_time = time()
    # load_instances('backtracking', 'sample')
    # elapsed_time = time() - start_time
    # print("BACKTRACKING: larger_instances -> Elapsed time: %0.10f seconds." % elapsed_time)


def test_NSatSolver():

    # start_time = time()
    # load_instances('nsatsolver', 'backtracking')
    # elapsed_time = time() - start_time
    # print("NSATSOLVER: backtracking_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    start_time = time()
    load_instances('nsatsolver', 'read_satisfied_assignmentsample')
    elapsed_time = time() - start_time
    print("NSATSOLVER: sample_instances -> Elapsed time: %0.10f seconds." %
          elapsed_time)

    # start_time = time()
    # load_instances('nsatsolver', 'larger')
    # elapsed_time = time() - start_time
    # print("NSATSOLVER: larger_instances -> Elapsed time: %0.10f seconds." % elapsed_time)


def test_MinisatSolver():

    start_time = time()
    load_instances('minisat', 'backtracking')
    elapsed_time = time() - start_time
    print("MINISAT: backtracking_instances -> Elapsed time: %0.10f seconds." %
          elapsed_time)

    start_time = time()
    load_instances('minisat', 'sample')
    elapsed_time = time() - start_time
    print("MINISAT: sample_instances -> Elapsed time: %0.10f seconds." %
          elapsed_time)

    start_time = time()
    load_instances('minisat', 'larger')
    elapsed_time = time() - start_time
    print("MINISAT: larger_instances -> Elapsed time: %0.10f seconds." %
          elapsed_time)

# Hurrengo 3 metodoak funtzionatzeko, aurretik load_instances_all_solutions programatuta eduki behar duzu
# Begin programatuta edukita, orduan 3 metodoen iruzkinak kendu

# Metodo honetan, backtracking bidez soluzio guztiak topatu, ez bakar bat (all_subsets)
# def test_backtracking_all_solutions():
    # start_time = time()
    # load_instances_all_solutions('backtracking', 'backtracking')
    # elapsed_time = time() - start_time
    # print("BACKTRACKING: backtracking_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    # start_time = time()
    # load_instances_all_solutions('backtracking', 'sample')
    # elapsed_time = time() - start_time
    # print("BACKTRACKING: sample_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    # # start_time = time()
    # # load_instances_all_solutions('backtracking', 'sample')
    # # elapsed_time = time() - start_time
    # # print("BACKTRACKING: larger_instances -> Elapsed time: %0.10f seconds." % elapsed_time)


# Metodo honetan, zure nsatsolver-aren bidez soluzio guztiak topatu, ez bakar bat
# def test_NSatSolver_all_solutions():
    # # start_time = time()
    # # load_instances_all_solutions('nsatsolver', 'backtracking')
    # # elapsed_time = time() - start_time
    # # print("NSATSOLVER: backtracking_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    # start_time = time()
    # load_instances_all_solutions('nsatsolver', 'read_satisfied_assignmentsample')
    # elapsed_time = time() - start_time
    # print("NSATSOLVER: sample_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    # # start_time = time()
    # # load_instances_all_solutions('nsatsolver', 'larger')
    # # elapsed_time = time() - start_time
    # # print("NSATSOLVER: larger_instances -> Elapsed time: %0.10f seconds." % elapsed_time)


# Metodo honetan, minisat bidez soluzio guztiak topatu, ez bakar bat
def test_MinisatSolver_all_solutions():
    start_time = time()
    load_instances_all_solutions('minisat', 'backtracking')
    elapsed_time = time() - start_time
    print("MINISAT: backtracking_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    start_time = time()
    load_instances_all_solutions('minisat', 'sample')
    elapsed_time = time() - start_time
    print("MINISAT: sample_instances -> Elapsed time: %0.10f seconds." % elapsed_time)

    start_time = time()
    load_instances_all_solutions('minisat', 'larger')
    elapsed_time = time() - start_time
    print("MINISAT: larger_instances -> Elapsed time: %0.10f seconds." % elapsed_time)


# main metodoan soluzio guztiak topatzeko behar diren aldaketak egin
def main():
    original_stdout = sys.stdout

    with open('execution_log.txt', 'w') as f:
        sys.stdout = f

        test_backtracking()
        test_NSatSolver()
        test_MinisatSolver()


        # Aurrekoan programatuta dauzkazunean, ondorengo iruzkinak kendu
        # test_backtracking_all_solutions()
        # test_NSatSolver_all_solutions()
        # test_MinisatSolver_all_solutions()

        sys.stdout = original_stdout


if __name__ == "__main__":
    main()
