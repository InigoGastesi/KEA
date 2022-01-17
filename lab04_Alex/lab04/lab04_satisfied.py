def is_satisfied(num_variables, clauses, assignment):
     # TODO: 
     # - Funtzio honen kodea programatu
     # - Beharrezkoa ikusten baduzu, funtzio lagungarriak defini ditzakezu
     for i in range(len(clauses)):
         for j in range(len(clauses[i])):
             if not emaitza(clauses[i], assignment):
                 return False
     return True
   

def emaitza(clauses, assignment):
    for i in range(len(clauses)):
        oraingo=clauses[i]
        if oraingo>0 and assignment[oraingo]==1:
            return True
        if oraingo<0:
            oraingo=oraingo*-1
            if assignment[oraingo]==0:
                return True
    return False
            
    

def test():
    num_variables = 4
    clauses = [[1,2,-3],[2,-4],[-1,3,4]]
    assignment = [0,1,1,1,1]
    assert is_satisfied(num_variables, clauses, assignment)

    assignment = [0,1,0,1,1]
    assert not is_satisfied(num_variables, clauses, assignment)
    
    clauses = [[-3, -1], [2, -3, -4, -1], [-1, -4], [-3], [-1, -2], [-3, 4, -2], [-1, -4, 2]]
    assignment = [0,0,0,1,0]
    assert not is_satisfied(num_variables, clauses, assignment)
    
    num_variables = 5
    clauses = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4]]
    assignment = [0,0,0,1,0,1]
    assert not is_satisfied(num_variables, clauses, assignment)
test()    

