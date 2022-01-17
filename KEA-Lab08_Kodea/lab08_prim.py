

def prim_algorithm(graph):
    # TODO
    markatuak = [0]
    emaitza = [[float("inf")]*len(graph) for i in range(len(graph))]

    while len(markatuak) != len(graph):

        minimo = float("inf")
        aurkitu = False
        for j in markatuak:
            for k in range(len(graph[j])):
                if graph[j][k] < minimo and not k in markatuak:
                    minimo = graph[j][k]
                    nodj = j
                    nodk = k
                    aurkitu = True

        if aurkitu:
            markatuak.append(nodk)
            emaitza[nodj][nodk] = minimo
            emaitza[nodk][nodj] = minimo

    return emaitza


def test():

    g1 = [[float("inf"), 2.0],
          [2.0, float("inf")]]

    assert prim_algorithm(g1) == g1

    g2 = [[float("inf"), 5.0, 3.0],
          [5.0, float("inf"), float("inf")],
          [3.0, float("inf"), float("inf")]]

    assert prim_algorithm(g2) == g2

    g3 = [[float("inf"), 1.0, 2.0, 3.0, 4.0],
          [1.0, float("inf"), float("inf"), float("inf"), 8.0],
          [2.0, float("inf"), float("inf"), 2.0, 3.0],
          [3.0, float("inf"), 2.0, float("inf"), 5.0],
          [4.0, 8.0, 3.0, 5.0, float("inf")]]

    assert prim_algorithm(g3) == [[float("inf"), 1.0, 2.0, float("inf"), float("inf")],
                                  [1.0, float("inf"), float("inf"),
                                   float("inf"), float("inf")],
                                  [2.0, float("inf"), float("inf"), 2.0, 3.0],
                                  [float("inf"), float("inf"), 2.0,
                                   float("inf"), float("inf")],
                                  [float("inf"), float("inf"), 3.0, float("inf"), float("inf")]]

    g4 = [[float("inf"), 6.0, 2.0, 5.0],
          [6.0, float("inf"), 4.0, float("inf")],
          [2.0, 4.0, float("inf"), 2.0],
          [5.0, float("inf"), 2.0, float("inf")]]

    assert prim_algorithm(g4) == [[float("inf"), float("inf"), 2.0, float("inf")],
                                  [float("inf"), float("inf"),
                                   4.0, float("inf")],
                                  [2.0, 4.0, float("inf"), 2.0],
                                  [float("inf"), float("inf"), 2.0, float("inf")]]

    g5 = [[float("inf"), 10.0, 1.0, float("inf"), float("inf"), float("inf")],
          [10.0, float("inf"), float("inf"), 5.0, 4.0, float("inf")],
          [1.0, float("inf"), float("inf"), 8.0, 2.0, 3.0],
          [float("inf"), 5.0, 8.0, float("inf"), float("inf"), 2.0],
          [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")],
          [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]

    assert prim_algorithm(g5) == [[float("inf"), float("inf"), 1.0, float("inf"), float("inf"), float("inf")],
                                  [float("inf"), float("inf"), float(
                                      "inf"), float("inf"), 4.0, float("inf")],
                                  [1.0, float("inf"), float("inf"),
                                   float("inf"), 2.0, 3.0],
                                  [float("inf"), float("inf"), float(
                                      "inf"), float("inf"), float("inf"), 2.0],
                                  [float("inf"), 4.0, 2.0, float("inf"),
                                   float("inf"), float("inf")],
                                  [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]

    g6 = [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")],
          [3.0, float("inf"), 8.0, 10.0, 5.0, float("inf"), float("inf")],
          [1.0, 8.0, float("inf"), float("inf"), float(
              "inf"), float("inf"), float("inf")],
          [float("inf"), 10.0, float("inf"), float(
              "inf"), 6.0, float("inf"), 9.0],
          [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0],
          [float("inf"), float("inf"), float("inf"),
           float("inf"), 1.0, float("inf"), 4.0],
          [float("inf"), float("inf"), float("inf"), 9.0, 2.0, 4.0, float("inf")]]

    assert prim_algorithm(g6) == [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")],
                                  [3.0, float("inf"), float("inf"), float(
                                      "inf"), 5.0, float("inf"), float("inf")],
                                  [1.0, float("inf"), float("inf"), float(
                                      "inf"), float("inf"), float("inf"), float("inf")],
                                  [float("inf"), float("inf"), float("inf"), float(
                                      "inf"), 6.0, float("inf"), float("inf")],
                                  [float("inf"), 5.0, float("inf"),
                                   6.0, float("inf"), 1.0, 2.0],
                                  [float("inf"), float("inf"), float("inf"), float(
                                      "inf"), 1.0, float("inf"), float("inf")],
                                  [float("inf"), float("inf"), float("inf"), float("inf"), 2.0, float("inf"), float("inf")]]


test()
