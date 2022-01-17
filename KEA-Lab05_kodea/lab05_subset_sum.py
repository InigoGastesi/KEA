from time import time
import itertools
import matplotlib.pyplot as plt

# has_sum funtzioak zenbaki positiboen bilduma bat eta "value" balioa jasotzen ditu
# eta zenbaki positiboen azpibilduma baten baturak "value" ematen duen
# erabakitzen du.  
def has_sum(value, collection):
    #valioa 0 bada true bueltatu
    if value == 0:
        return True
    #listan zenbakirik ez badago, ez dago konbinaziorik beraz false itzuli
    elif len(collection) == 0:
        return False
    else:
        #listako lehenengo balioa value baino handiago bada, collection[0] ez da egongo konbinazioan
        #beraz, bakarrik bide bat egin
        if(value<collection[0]):
            return has_sum(value, collection[1:])
        else:
            #bi bideak egin, bat zenbakia sartuz eta bestea zenbakia sartu gabe
            return has_sum(value-collection[0], collection[1:]) or has_sum(value, collection[1:])
    

# subset, funtzioak zenbaki positiboen bilduma bat eta "value" balioa jasotzen ditu
# eta zenbaki positiboen azpibilduma baten baturak "value" ematen badu, azpibilduma hori
# itzultzen du. Horrelako azpibildumarik ez balego, [None] lista itzultzen du.
def subset(value, collection):
    #valioa 0 bada lista hutsa bueltatu
    if value == 0:
        return []
    #listan zenbakirik ez badago, ez dago konbinaziorik beraz [None] itzuli
    elif len(collection) == 0:
        return [None]
    else:
        #listako lehenengo balioa value baino handiago bada, collection[0] ez da egongo konbinazioan
        #beraz, bakarrik bide bat egin
        if(collection[0] > value):
            emaitza = subset(value, collection[1:])
            return emaitza
        else:
            
            emaitza1 = subset(value-collection[0], collection[1:])
            #emaitza1 != [None] bada emaitza1 konbinazio bat dauka beraz, emaitza1 bueltatu
            if(emaitza1 != [None]):
                return emaitza1 + [collection[0]]
            else:
                #zenbakia konbinazioan ez sartu
                emaitza2 = subset(value, collection[1:])
                #emaitza1 != [None] bada emaitza1 konbinazio bat dauka beraz, emaitza1 bueltatu
                if(emaitza2 != [None]):
                    return emaitza2

                else:
                    return [None]


# all_subsets funtzioak zenbaki positiboen bilduma bat eta "value" balio bat emanda, 
# "value" batzen duten azpimultzo guztiak itzultzen ditu. Soluziorik ez badago, [None] itzultzen du.                       
def all_subsets(value, collection): 
    #valioa 0 bada listen lista hutsa bueltatu 
    if value == 0:
        return [[]]
    #listan zenbakirik ez badago, ez dago konbinaziorik beraz [None] itzuli
    elif len(collection) == 0:
        return [None]
    else:
        emaitza = []
        emaitza2 = [None]

        #konbinazio guztiak aurkitu behar direnez, bi bideak egin
        emaitza2 = all_subsets(value, collection[1:])
        emaitza1 = all_subsets(value-collection[0], collection[1:])

        #emaitza2 !=[None] bada konbinazio bat du beraz, listen listara gehitu
        if(emaitza2 != [None]):
            for i in emaitza2:
                emaitza.append(i)
        #emaitza1 !=[None] bada konbinazio bat du beraz, listen listara gehitu
        if(emaitza1 != [None]):
            for i in emaitza1:
                emaitza.append([collection[0]]+i)
        #biak == [None] badira, ez dago konbinaziorik beraz, [None] itzuli
        elif(emaitza1 == [None] and emaitza2 == [None]):
            return [None]
            
        return emaitza
    
def test():
    
    #  0 bilduma
    collection0 = [3, 11, 8, 13, 16, 1, 6]
    value0 = 59
    
    # 1 bilduma
    collection1 = [3, 11, 8, 13, 16, 1, 6]
    value1 = 21
    

    sol11 = [3, 11, 1, 6]
    perm11 = [list(t) for t in itertools.permutations(sol11)]
    perm12 = [[13, 8], [8, 13]]
   
    # 2 bilduma
    collection2 = [518533, 1037066, 2074132, 1648264,
                   796528, 1593056, 686112, 1372224,
                   244448, 488896, 977792, 1955584,
                   1411168, 322336, 644672, 1289344,
                   78688, 157376, 314752, 629504, 1259008]
    value2 = 2463098
    
    sol21 = [1037066, 796528, 629504] 
    perm21 = [list(t) for t in itertools.permutations(sol21)]
    
    # 3 bilduma
    collection3 = [15, 22, 14, 26, 32, 9, 16, 8]
    value3 = 53
    
    
    sol31 = [15, 22, 16]
    perm31 = [list(t) for t in itertools.permutations(sol31)]
    
    # sol31ko balio guztien batura 53 denez, emaitza permutazio posible guztiak
    # Berdin azpiko bi aukerekin
    sol32 = [14, 15, 16, 8]
    perm32 = [list(t) for t in itertools.permutations(sol32)]
    sol33 = [9, 22, 14, 8]
    perm33 = [list(t) for t in itertools.permutations(sol33)]
    
    # 4. bilduma
    collection4 = [1,5,6]
    value4 = 6
    perm41 = [[6], [1, 5], [5, 1]] # Eskuz pentsatua
    
    # 5.bilduma
    collection5 = [4,5,1]
    value5 = 6
    perm51 = [[1, 5], [5, 1]]
    
#   HAS_SUM PROBATZEKO KOMENTARIOAK KENDU
#######################################################  
      
    assert not has_sum(value0, collection0)
    assert has_sum(value1, collection1)
    assert has_sum(value2, collection2)
    assert has_sum(value3, collection3)
    assert has_sum(value4, collection4)
    assert has_sum(value5, collection5)
    
    
#   SUBSET PROBATZEKO KOMENTARIOAK KENDU
###############################################################
    
    assert subset(value0, collection0) == [None]
    assert subset(value1, collection1) in perm11 + perm12 
    assert subset(value2, collection2) in perm21
    assert subset(value3, collection3) in perm31 + perm32 + perm33
    assert subset(value4, collection4) in perm41 
    assert subset(value5, collection5) in perm51 
    
    

##  ALL_SUBSETS PROBATZEKO KOMENTARIOAK KENDU   
##############################################################
    
    assert all_subsets(value0, collection0) == [None]

    all_solutions1 = all_subsets(value1, collection1)
    assert len(all_solutions1) == 2
    assert all_solutions1[0] in perm11 + perm12
    assert all_solutions1[1] in perm11 + perm12
    
    all_solutions2 = all_subsets(value2, collection2)
    assert len(all_solutions2) == 1
    assert all_solutions2[0] in perm21
    
        
    all_solutions3 = all_subsets(value3, collection3)
    assert len(all_solutions3) == 3
    assert all_solutions3[0] in perm31 + perm32 + perm33
    assert all_solutions3[1] in perm31 + perm32 + perm33
    assert all_solutions3[2] in perm31 + perm32 + perm33
    
    
    all_solutions4 = all_subsets(value4, collection4)       
    assert len(all_solutions4) == 2
    assert all_solutions4[0] in perm41
    assert all_solutions4[1] in perm41
    
    
### DENBORA NEURTZEKO VALUE BATZEN DUEN AZPIBILDUMARIK EZ DUEN 
### BILDUMA HAU ERABILTZEN DA
####################################################################    
    
    
    collection5 = list(range(1,25))
    value5 = 301
    assert subset(value5, collection5) == [None] 
    


'''
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)   
'''

denb=[]
n = []
test_cases=[]
values=[]
for i in range(3,25):
    test_cases.append(list(range(1,i)))
    values.append(301+i)

print("test done")

for i in range(len(test_cases)):
    start_time = time()
    all_subsets(values[i], test_cases[i])
    elapsed_time = time() - start_time
    denb.append(elapsed_time)
    n.append(i)
    print(str(i)+" iter")

plt.plot(n,denb, 'b')
plt.xlabel("n kopurua")
plt.ylabel("denbora")
plt.show()
