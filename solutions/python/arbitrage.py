# Arbitrage.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import math
import random


# @include
def is_arbitrage_exist(G_in):
    G = []
    # Transforms each edge in G.
    for edge_list in G_in:
        G.append([-math.log10(edge) for edge in edge_list])

    # Uses Bellman-ford to find negative weight cycle.
    return bellman_ford(G, 0)


def bellman_ford(G, source):
    dis_to_source = [float('inf')] * len(G)
    dis_to_source[source] = 0

    for times in range(1, len(G)):
        have_update = False
        for i in range(len(G)):
            for j in range(len(G[i])):
                if (dis_to_source[i] != float('inf') and
                        dis_to_source[j] > dis_to_source[i] + G[i][j]):
                    have_update = True
                    dis_to_source[j] = dis_to_source[i] + G[i][j]

        # No update in this iteration means no negative cycle.
        if not have_update:
            return False

    # Detects cycle if there is any further update.
    for i in range(len(G)):
        for j in range(len(G[i])):
            if (dis_to_source[i] != float('inf') and
                    dis_to_source[j] > dis_to_source[i] + G[i][j]):
                return True
    return False
# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 100)
    G = [[0.0] * n for i in range(n)]
    # Assume the input is a complete graph.
    for i in range(len(G)):
        G[i][i] = 1
        for j in range(i + 1, len(G)):
            G[i][j] = random.random()
            G[j][i] = 1.0 / G[i][j]
    res = is_arbitrage_exist(G)
    print(res)
    g = [[1.0, 2.0,  1.0],
         [0.5, 1.0,  4.0],
         [1.0, 0.25, 1.0]]
    res = is_arbitrage_exist(g)
    assert res == True
    print(is_arbitrage_exist(g))


if __name__ == '__main__':
    main()
