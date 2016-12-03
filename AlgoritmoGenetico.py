import numpy as np
import copy
from HillClimbing import *

class AG(HC):

	#Construtor
	def __init__(self, n_individuals, cross_rate, mut_rate, hill_object, elitism=0, roubar=True):
		self.__n_individuals = n_individuals
		self.__cross_rate = cross_rate
		self.__mut_rate = mut_rate
		self.__hc = hill_object
		self.__individual = np.array([])
		self.__DNA = np.array([])
		self.__chromosome = np.array([])
		self.population_generation(n_individuals)
		self.__elitism = elitism
		self.__roubar = roubar
	
	def softmax(self, x):
		e_x = np.exp(x)/np.exp(x).sum()
		return e_x

	def train(self, iter=50):
		individuals = self.get_individual()
		n_individuals = self.__n_individuals
		hc = self.__hc
		elitism = self.__elitism
		solution = None
		maximum = 0
		for i in xrange(iter):
			scores = np.array([])
			for idx, ind in enumerate(individuals):
				if self.__roubar:
					_, score = hc.climbing(ind)
				else:
					score = hc.score(ind)
				scores = np.append(scores, score)
			print "Generation:", i+1
			print scores
			probs = self.softmax(scores*1.0)
			if elitism > 0:
				sols = np.argsort(scores)[-elitism:]
			else:
				sols = []
			
			sol = np.argmax(scores)
			if scores[sol] >= maximum:
				solution = copy.copy(self.__individual[sol])
				maximum = scores[sol]
			idxs = np.random.choice(n_individuals,n_individuals-elitism,p=probs)
			idxs = np.append(sols,idxs).astype(int)
			self.__individual = self.__individual[idxs]

			for idx in xrange(0,n_individuals,2):
				if self.__cross_rate < random.random(): continue
				ind1 = self.get_individual(idx)
				ind2 = self.get_individual(idx+1)
				ind1, ind2 = self.crossover(ind1, ind2)
				self.set_individual(ind1, idx)
				self.set_individual(ind2, idx+1)

			np.random.shuffle(self.__individual)
			for idx in xrange(0,n_individuals):
				if self.__mut_rate < random.random(): continue
				ind = self.get_individual(idx)
				ind.random_swap()
				self.set_individual(ind, idx)
			# self.crossover()
			# self.mutation()
		print maximum
		return solution


	def crossover(self, ind1, ind2):
		rate = random.random()
		rows, cols = ind1.get_dimensions()
		cut = int(rate * rows)
		i1 = ind1.get_board()
		i2 = ind2.get_board() 
		b1 = np.append(i1[:cut,:],i2[cut:,:])
		b2 = np.append(i2[:cut,:],i1[cut:,:])
		b1 = b1.reshape(rows,cols)
		b2 = b2.reshape(rows,cols)
		ind1.set_board(b1)
		ind2.set_board(b2)
		return ind1, ind2



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
			for j, element in enumerate(line):
				if not(individual.is_fixed(i,j)):
					basenit = np.where(dna==element)[0][i]
					dec = np.where(idxs < basenit)[0].shape[0]
					idxs = np.append(idxs, basenit)
					chromosome.append(basenit-dec)
		chromosome = np.array(chromosome)
		return chromosome
	
	def chromo2ind(self, individual, chromosome):
		dna = individual.get_dna()
		rows, cols = individual.get_dimensions()
		board = []
		for i, line in enumerate(chromosome):
			for j, element in enumerate(line):
				if not(individual.is_fixed(i,j)):
					up = np.where(line[:j] <= element)[0].shape[0]
					# print element, up
					value = dna[i,element+up]
					board.append(value)
				else:
					board.append(individual.get_position(i,j))
		board = np.array(board).reshape(rows,cols)
		individual.set_board(board) 
		return individual
		
	
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
#			chromosome = self.ind2chromo(individual)
#			self.append_chromosome(chromosome)

