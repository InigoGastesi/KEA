from solve_vc import solve_vc


def multisolve(graph, problem):    
    if problem ==   "VERTEX COVER":
        return solve_vc(graph)  
    else:
        if problem == "INDEPENDENT SET":
            return solve_is(graph)
        else:
            return solve_cl(graph)

def solve_is(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if i!=j:
                if g[i][j]==1:
                    g[i][j]=0
                else:
                    g[i][j]=1
    return solve_vc(g)
    
    
    
def solve_cl(g):

    return solve_is(g)
    
    
    

def test():
   graph = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   
   assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
   assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
   assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]

test()
