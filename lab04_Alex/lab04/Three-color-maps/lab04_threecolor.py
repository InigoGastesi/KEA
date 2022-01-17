from fourcolor import graph_is_4colorable

def graph_is_3colorable(g):
    # TODO: 
    # - Funtzio honen kodea programatu
    # - Beharrezkoa ikusten baduzu, funtzio lagungarriak defini ditzakezu
    for i in range(len(g)):
        g[i].append(1)
    berria=[1]*len(g)
    berria.append(0)
    g.append(berria)
    if graph_is_4colorable(g):
        return True
    else:
        return False

def test():
    g1 = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]
    assert graph_is_3colorable(g1)

    g2 = [[0, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 1, 1, 0]]
    assert graph_is_3colorable(g2)

    g3 = [[0, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 0]]
    assert not graph_is_3colorable(g3)


test()
