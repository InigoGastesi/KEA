from solve_vc import solve_vc


def multisolve(graph, problem):    
    if problem ==   "VERTEX COVER":
        return solve_vc(graph)  
    else:
        if problem == "INDEPENDENT SET":
            result = solve_vc(graph)
            #independent set-en emaitza vertex cover-en emaitzaren alderantzizkoa da, beraz,
            #vertex cover-en emaitzaren listan 1 badago orain 0 izango da eta 0 denean 1 izango da.
            return [0 if result[i]==1 else 1 for i in range(len(result))]
        else:
            #cliqueren soluzioa independent set-aren grafo osagarriaren emaitza da, beraz,
            #cliquereen grafoaren osagarria kalkulatzen da eta gero independent set bat bezala eazten da.
            result = solve_vc(convert_clique(graph)) 
            return [0 if result[i]==1 else 1 for i in range(len(result))]
            
def convert_clique(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if(i!=j and graph[i][j]==1):
                graph[i][j]=0
            elif(i!=j and graph[i][j]==0):
                graph[i][j]=1

    return graph


def test():
   graph = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   sol_clique = multisolve(graph, "CLIQUE")
   
   assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
   assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
   assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]

test()
