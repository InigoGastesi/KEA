
def graph_has_Hamiltonian_circuit(g):
    nodes = []
    #iterazio bakoitzean hasierako nodoa aldatzen da eta gero funtzio errekurtsiboa deitzen da
    for nodo in range(0,len(g)):
        if(recursive(nodes, g, nodo)):
            return True
    return False

#nodes: ze nodoetatik pasa den
#g: grafoa
#nodo: momentu hontan gauden nodoa
def recursive(nodes, g, nodo):
    nodes.append(nodo)

    #pasa garen nodo kopurua grafoan dauden nodo kopuruen berdina bada, lehenengo nodoa azkeneko nodarekin
    #konektatuta dagoen begiratzen dut. Hau betetzen bada grafo hamiltondarra izango da, bestela ez
    if(len(nodes)==len(g) and g[nodo][nodes[0]]==1):
        return True
    elif(len(nodes)==len(g) and g[nodo][nodes[0]]==0):
        return False

    #nodo bakoitzaren konexioak iteratzen dira
    for i in range(0,len(g[nodo])):

        #nodo bat beste batekin konektatuta badago eta lehenago ez bagara pasa no horretatik, funtzio recursiboa deitzen du
        if(g[nodo][i] == 1 and not i in nodes):
            if(recursive(nodes.copy(),g,i)):
                return True
    return False


def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert graph_has_Hamiltonian_circuit(g3)
    
    g4 = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
   
    

test()
