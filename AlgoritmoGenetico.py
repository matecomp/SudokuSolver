import numpy as np
from HillClimbing import *

class AG(HC):

	#Construtor
	def __init__(self, n_individuals, cross_rate, mut_rate, hill_object):
		self.__n_individuals = n_individuals
		self.__cross_rate = cross_rate
		self.__mut_rate = mut_rate
		self.__hc = hill_object
		self.__individual = []
		self.__DNA = []
		self.__chromosome = []
		self.population_generation(n_individuals)

	def get_individual(self, idx=None):
		if idx is None:
			return self.__individual
		return self.__individual[idx]

	def get_individual(self, idx=None):
		if idx is None:
			return self.__chromosome
		return self.__chromosome[idx]

	def append_individual(self, individual):
		self.__individual.append(individual)
	def append_chromosome(self, chromosome):
		self.__individual.append(chromosome)

	def ind2chromo(self, individual):
		dna = individual.get_dna()
		board = individual.get_board()
		rows, cols = individual.get_dimensions()
		chromosome = []
		for i, line in enumerate(board):
			idxs = []
			for element in line:
				basenit = np.where(dna[i,:]==element)[0][0]
				dec = np.where(idxs < basenit)[0].shape[0]
				idxs = np.append(idxs, basenit)
				chromosome.append(basenit-dec)
		chromosome = np.array(chromosome).reshape(rows,cols)
		return chromosome
	
	def chromo2ind(self, individual, chromosome):
		dna = individual.get_dna()
		rows, cols = individual.get_dimensions()
		board = []
		for i, line in enumerate(chromosome):
			for j, element in enumerate(line):
				up = np.where(line[:j] <= element)[0].shape[0]
				value = dna[i,element+up]
				board.append(value)
		board = np.array(board).reshape(rows,cols)
		return board
		
	
	def create_individual(self):
		individual = self.__hc.create_board()
		individual.init_board()
		return individual

	def population_generation(self, n_individuals):
		for ind in xrange(n_individuals):
			individual = self.create_individual() 
			self.append_individual(individual)
			chromosome = self.ind2chromo(individual)
			self.append_chromosome(chromosome)

