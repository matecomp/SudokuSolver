import numpy as np
from HillClimbing import *

class AG(HC):

	#Construtor
	def __init__(self, n_individuals, cross_rate, mut_rate, hill_object):
		self.__n_individuals = n_individuals
		self.__cross_rate = cross_rate
		self.__mut_rate = mut_rate
		self.__hc = hill_object
		self.__individual = np.array([])
		self.__DNA = np.array([])
		self.__chromosome = np.array([])
		self.population_generation(n_individuals)

	def train(self, iter=50):
		individuals = self.get_individual()
		n_individuals = self.__n_individuals
		hc = self.__hc
		for i in xrange(iter):
			scores = np.array([])
			for idx, ind in enumerate(individuals):
				_, score = hc.climbing(ind)
				scores = np.append(scores, score)
			probs = scores*1.0/scores.sum()
			print  scores*1.0
			idxs = np.random.choice(n_individuals,n_individuals,p=probs)
			print idxs
			self.__individual = self.__individual[idxs]
			# self.crossover()
			# self.mutation()


	def crossover(self):
		pass
	def mutation(self):
		pass


	def get_individual(self, idx=None):
		if idx is None:
			return self.__individual
		return self.__individual[idx]

	def get_chromosome(self, idx=None):
		if idx is None:
			return self.__chromosome
		return self.__chromosome[idx]

	def set_individual(self, individual, idx):
		self.__individual[idx] = individual

	def set_choromosome(self, chromosome, idx):
		self.__chromosome[idx] = chromosome

	def append_individual(self, individual):
		individuals = self.get_individual()
		self.__individual = np.append(individuals,individual)

	def append_chromosome(self, chromosome):
		chromosomes = self.get_chromosome()
		self.__chromosome = np.append(chromosomes, chromosome)

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
		self.__individual = np.array([])
		self.__chromosome = np.array([])
		for ind in xrange(n_individuals):
			individual = self.create_individual() 
			self.append_individual(individual)
			chromosome = self.ind2chromo(individual)
			self.append_chromosome(chromosome)

