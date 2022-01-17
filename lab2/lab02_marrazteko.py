import marrazteko as irudi

def test():
    #Sortu grafo bat (auzokidetasun matrizea)
    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    #Grafoa bistaratu
    grafoa = irudi.formatu_berri(g2)
    print(grafoa.edges)
    print(grafoa.nodes)
    irudi.marraztu(grafoa)

    #Grafo gehiagorekin frogatu, 10 tamaina gehienez
    
    
test()
