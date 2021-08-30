import numpy as np
import pandas as pd
import networkx as nx
import scipy

from FuncoesUteis import dist, printGrafo

def TSP(instanciaTSP):
    # Computa a Árvore Geradora Mínima
    MST = nx.minimum_spanning_tree(instanciaTSP)

    # Seleciona o todos vértices de grau par
    listaDeGraus = [(v, g) for (v, g) in MST.degree()]
    grauImpar = [ v for (v, g) in listaDeGraus if g % 2 == 1 ]

    # Induz o grafo apenas com os vértices ímpares
    GrafoAuxiliar = instanciaTSP.subgraph(grauImpar)

    # Computa o Matching Perfeito para esse sub grafo (Blossom)
    Matching = nx.max_weight_matching(GrafoAuxiliar, weight='weight')

    # Instancia as arestas do Matching Perfeito na Árvore Geradora Mínima
    MST.add_edges_from(Matching)

    # Calcula o circuito euleriano
    euler = list(nx.eulerian_circuit(MST))
    conj = []
    for i in range(0, len(euler)):
        if not euler[i][0] in conj:
            conj.append(euler[i][0])
    conj.append(conj[0])

    # Computa o custo total
    custo = 0
    for i in range(0, len(conj)-1):
        custo += instanciaTSP[conj[i]][conj[i+1]]['weight']

    return int(custo)