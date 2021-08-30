import numpy as np
import pandas as pd
import networkx as nx
import scipy

from FuncoesUteis import dist

class FilaDePrioridade():
    
    fila = np.array([])

    def Insere(element):
        index = numpy.searchsorted(self.fila, element)
        self.fila = numpy.insert(self.fila, index, element)

    def PrimeiroItem():
        return self.fila.pop(0)

def TSP(instanciaTSP):

    # Instancia a fila de prioridade
    fila = FilaDePrioridade()

    # Percorrre o grafo
    for n, nbrs in instanciaTSP.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr['weight']
            try: print(f"({n}, {nbr}, {wt:.3})")
            except: print(f"({n}, {nbr}, {wt})")