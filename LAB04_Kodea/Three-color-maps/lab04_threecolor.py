from fourcolor import graph_is_4colorable

def graph_is_3colorable(g):
    # TODO: 
    # - Funtzio honen kodea programatu
    # - Beharrezkoa ikusten baduzu, funtzio lagungarriak defini ditzakezu
    # batez osatutako zutabe bat gehitu g matrizera
    g = [g[i]+[1] for i in range(len(g))]
    # batez osatutako errenkada sortu eta matrizera gehitu
    row =[1]*(len(g)+1)
    g.append(row)
    # matrizearen azkeneko elementuari 0 esleitu matrizearen diagonala 0 izateko
    g[-1][-1]=0

    return graph_is_4colorable(g)


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
