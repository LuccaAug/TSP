import numpy as np
import pandas as pd
import networkx as nx
import scipy

import itertools
from scipy.spatial import distance

def GeradorDeTSP(i):
    Manhattan = nx.Graph()
    Euclidian = nx.Graph()
    no = dict()

    for i in range(pow(2, i)):
        x = np.random.randint(0, 13000)
        y = np.random.randint(0, 13000)
        no[i] = (x, y)

        Manhattan.add_node(i)
        Euclidian.add_node(i)

        for v in Manhattan.nodes():
            if v == i: continue
            man, euc = dist(no[v], (x, y))

            Manhattan.add_weighted_edges_from([(v, i, man)])
            Euclidian.add_weighted_edges_from([(v, i, euc)])
            
    return Manhattan, Euclidian


def dist(a, b):
    return distance.cityblock(a, b), distance.euclidean(a, b)


def printGrafo(g):
    for n, nbrs in g.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr['weight']
            try: print(f"({n}, {nbr}, {wt:.3})")
            except: print(f"({n}, {nbr}, {wt})")