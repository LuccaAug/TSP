import numpy as np
import pandas as pd
import networkx as nx
import scipy

from FuncoesUteis import printGrafo

def TSP(instanciaTSP):

    # Computa a Árvore Geradora Mínima
    MST = nx.minimum_spanning_tree(instanciaTSP)

    # Cria uma cópia da MSF com apenas um filho cada nó orientado por profundidade
    DFS = nx.dfs_tree(MST)

    # Soma o peso de todas as arestas do grafo DFS
    custo = DFS.size(weight="weight")

    # Adiciona a aresta que interliga o último vértice no primeiro
    listaDeVertices = list(nx.topological_sort(DFS))
    try:    custo += instanciaTSP[listaDeVertices[0]][listaDeVertices[-1]]["weight"]
    except: custo += instanciaTSP[listaDeVertices[-1]][listaDeVertices[0]]["weight"]

    return int(custo)