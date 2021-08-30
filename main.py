import numpy as np
import pandas as pd
import networkx as nx
import scipy

import TwiceAroundTheTree, BranchAndBound, Christofides
from FuncoesUteis import GeradorDeTSP, printGrafo

import signal
import time

def TimeLimit(func, instanciaTSP):
	start = time.time()
	custo = func(instanciaTSP)
	end = time.time()
	duracao = end-start
	return f"{custo} em {duracao} segundos"

def main():
	for i in range(4, 11):
		print(f"Dificuldade {i}")
		instanciaTSP_Manhattan, instanciaTSP_Euclidian = GeradorDeTSP(i)

		print("\t Manhattan:")
		print("\t\t TATT  -> ", TimeLimit(TwiceAroundTheTree.TSP, instanciaTSP_Manhattan))
		print("\t\t Chris -> ", TimeLimit(Christofides.TSP, instanciaTSP_Manhattan))
	
		print("\t Euclidiana:")
		print("\t\t TATT  -> ", TimeLimit(TwiceAroundTheTree.TSP, instanciaTSP_Euclidian))
		print("\t\t Chris -> ", TimeLimit(Christofides.TSP, instanciaTSP_Euclidian))
		

if __name__ == '__main__':
	main()
	