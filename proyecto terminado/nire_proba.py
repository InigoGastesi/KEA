from SubsetSum_to_SAT import reduce_subsetsum_to_SAT
import subprocess


def subset(list1, mysum):
    text = reduce_subsetsum_to_SAT(list1, mysum)
    with open('proba1.cnf', 'w') as f:
        f.write(text)

def all_subset(list1, mysum):
    filename = str(mysum) + ".txt"
    text = reduce_subsetsum_to_SAT(list1, mysum) #SAT kalkulatu
    with open(filename, 'w') as f:
        f.write(text)

    
    luzera = len(list1)
    #Irakurri minisat-en irteera daukan fitxategia
    output_file = filename + '_output.txt'
    last_line = ""
    while(last_line != "UNSAT"):
        subprocess.run(["minisat", filename, output_file]) #pythonen bidez linux-en bash-a erabili minisat erabiltzeko
        f_read = open(output_file, "r")
        last_line = f_read.readlines()[-1]
        f_read.close()
        if(last_line == "UNSAT\n"):
            break

        emaitza = last_line.split(" ")#last line " " karakterearen bidez banandu
        emaitza = emaitza[0:luzera]#lehenago kalkulatutako listaren luzera erabiliz lehenengo luzera aldagaiak aukeratu
        for i in range(len(emaitza)):
            emaitza[i] = int(emaitza[i]) # string-etik int ra pasa

        outcome=""
        for number in emaitza:
            outcome += str(-number) + " "# -aldagaia outcomeri gehitu

        outcome += '0\n' #0 a gehitu eta lerro jauzia ipini
        with open(filename, 'a') as f:
            f.write(outcome)

        pantaila_emaitza=[]
        # pantailan emaitza ipini
        for i in range(len(emaitza)):
            if emaitza[i] > 0:
                pantaila_emaitza.append(list1[i])

        print(pantaila_emaitza)

subset([8, 9, 14, 15, 16, 22, 26, 32], 53)