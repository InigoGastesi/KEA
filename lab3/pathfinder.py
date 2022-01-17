import marrazteko as irudi
import timeit
import matplotlib.pyplot as plt

# Grafo baten sakonerako zeharkatzea: DFS Depth-First Search
def find_path(graph, start, end):
    #hasierako nodoaren auzokideak iteratu
    for i in range(0,len(graph[start])):
        nodes = [start]
        #auzokidearekin bidea badago eta ez bada bisitatu
        if(graph[start][i]==1 and not i in nodes):
            #funtzio errekurtsiboa deitu
            nodes = recursive(nodes.copy(),graph, end, i)
            #funtzio errekurtsiboarekin lortutako bidearen azken nodoa end nodoaren berdina bada, egindako bidea itzuli
            if(nodes[-1]==end):
                return nodes

    
    return []


def recursive(nodes, graph, end, nodo):
    nodes.append(nodo)
    #aztertzen ari den nodoa, bukaerako noadoaren berdina bada, bidea itzuli
    if(nodo == end):
        return nodes

    elif(len(nodes)==len(graph)):
        return []
    else:
        #nodoarean auzkokideak aztertu
        for i in range(0,len(graph)):
            #auzokideak konektatuta badago eta ez bada bisistatu
            if(graph[nodo][i]==1 and not i in nodes):
                #azkeneko nodoa bukaerako nodoaren berdina bada, bidea itzuli
                return recursive(nodes.copy(), graph, end,i)

    return nodes


def sortu_test(graph_amount):
    grafoak=[]
    g1 = [[0,1,0,0],
        [1,0,1,0],
        [0,1,0,1],
        [0,0,1,0]]
    grafoak.append(g1)
    #for hau egin graph_amount grafo kopurua sortzeko
    for graph_count in range(graph_amount-1):
        #hemen zutabe bat gehitzen dut. Zutabe osoa zeroak izango ditu azkeneko errenkadan izan ezik
        g1 = [g1[i]+[1] if i==len(g1)-1 else g1[i]+[0] for i in range(len(g1))]
            #Gero zeroz osatutako errenkada sortu eta azken aurreko posizioan 1 ipini.
        row = [0]*(len(g1[0]))
        row[-2]=1
        g1.append(row)
        grafoak.append(g1)
    return grafoak                 



def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 0, 1],
          [0, 1, 0, 0, 1],
          [0, 0, 1, 1, 0]]
    
    assert find_path(g1, 0, 4) in [[0, 2, 4], [0, 2, 1, 3, 4], [0, 1, 2, 4], [0, 1, 3, 4]]
    
    g2 = [[0, 1, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 1, 0]]
    
    assert find_path(g2, 0, 1) in [[0,1]]    
    assert find_path(g2, 0, 2) == []
    
    g3 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1],
          [0, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert find_path(g3, 1, 0) in [[1, 3, 2, 0], [1, 3, 5, 4, 2, 0]]
    
    g4 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0]]
    
    assert find_path(g4, 0, 5) in [[0, 2, 5]]
    
    g5 = [[0, 1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0]]
    
    assert find_path(g5, 0, 5) in [[0, 4, 5]]
    
    g6 = [[0, 1, 0, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0]]
    
    assert find_path(g6, 0, 7) == [0, 4, 5, 6, 7]
    

def test2():
    
    g7 = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    
    #mar.dibujar(g7) 
    G7 = irudi.formatu_berri(g7)
    print(G7.edges)
    print(G7.nodes)
    irudi.marraztu(G7)
    
    print("0tik 20rako bidea:\n" + str(find_path(g7, 0, 20)))
        
                 
    
    
    g8 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
        
    
    G8 = irudi.formatu_berri(g8)
    print(G8.edges)
    print(G8.nodes)
    irudi.marraztu(G8)
    
    print("0tik 20rako bidea:\n" + str(find_path(g8, 1, 23)) + "\n\n")
    

test()
zenbat_kasu = 450
proba_kasuak = sortu_test(zenbat_kasu)
time = []
x = list(range(4,zenbat_kasu+4))
#proba kasu bakoitzerako find_path funtzioa deitu eta denbora gorde time listan.
for i in range(0,len(proba_kasuak)):
    starttime=timeit.default_timer()
    find_path(proba_kasuak[i],0,i+3)
    time.append(timeit.default_timer()-starttime)


plt.plot(x,time, 'b')
plt.xlabel("n kopurua")
plt.ylabel("denbora")
plt.show()
# Grafo handiagoak bistaratzeko iruzkina kendu
test2()
