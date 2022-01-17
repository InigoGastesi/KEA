def is_satisfied(num_variables, clauses, assignment):
    # TODO: 
    # - Funtzio honen kodea programatu
    # - Beharrezkoa ikusten baduzu, funtzio lagungarriak defini ditzakezu
    #klausula guztiak iteratu
    for i in range(len(clauses)):
        #klausula bakoitzeko literala iteratu
        for j in range(len(clauses[0])-1):
            #iteratutako aldagaia ezeztatuta ez badago eta asignazioa bat bada
            if(clauses[0][j]>0 and assignment[clauses[0][j]]==1):
                clauses.remove(clauses[0])
                break
            #iteratutako aldagaia ezeztatuta badago eta asignazioa zero bada
            elif(clauses[0][j]<0 and assignment[abs(clauses[0][j])]==0):
                clauses.remove(clauses[0])
                break
            
    return clauses == []
 
   

def test():
    num_variables = 4
    clauses = [[1,2,-3],[2,-4],[-1,3,4]]
    assignment = [0,1,1,1,1]
    assert is_satisfied(num_variables, clauses.copy(), assignment)

    assignment = [0,1,0,1,1]
    assert not is_satisfied(num_variables, clauses.copy(), assignment)
    
    clauses = [[-3, -1], [2, -3, -4, -1], [-1, -4], [-3], [-1, -2], [-3, 4, -2], [-1, -4, 2]]
    assignment = [0,0,0,1,0]
    assert not is_satisfied(num_variables, clauses.copy(), assignment)
    
    num_variables = 5
    clauses = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4]]
    assignment = [0,0,0,1,0,1]
    assert not is_satisfied(num_variables, clauses.copy(), assignment)
test()    

