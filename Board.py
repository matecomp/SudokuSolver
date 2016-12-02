import numpy as np
import random

class Board:
	#Construtor
	#marked is a triple (n_row,n_col,value)
	def __init__(self, n_rows, n_cols, markeds):
		self.__rows = n_rows
		self.__cols = n_cols
		self.__score = 0
		self.__board = np.zeros([n_rows,n_cols]).astype(int)
		self.__markeds = []
		#insert value on board and mark this place
		for i,j,n in markeds:
			self.__board[i,j] = int(n)
			self.__markeds.append((i,j))
		n_marks = len(markeds)
		self.__dna = np.zeros([n_rows*n_cols-n_marks]).astype(int)

	def __str__(self):
		return 'Board:\n{0}'.format(self.__board)

	def get_board(self):
		return self.__board

	def get_dna(self):
		return self.__dna

	def get_dimensions(self):
		return self.__rows, self.__cols
	
	def get_position(self, row, col):
		return self.__board[row,col]

	def get_submatrix(self,row,col,dimx,dimy):
		dx = row + dimx
		dy = col + dimy
		return self.__board[row:dx,col:dy]

	def set_board(self, board):
		if board.shape == self.__board.shape:
			self.__board = board
		else:
			print "Invalid size"
	#Return False if position is invalid and True otherwise
	def set_position(self, row, col, value):
		if value < 0 or value > 9:	return False
		if self.is_fixed(row, col): return False
		self.__board[row,col] = int(value)
		return True

	def is_fixed(self, row, col):
		if (row,col) in self.__markeds: return True
		return False
	#Insert random values on board
	def fill_allpositions(self):
		for row in xrange(self.__rows):
			for col in xrange(self.__cols):
				value = random.randint(1,9)
				self.set_position(row,col,value)
	
	def create_dna(self):
		count = 0
		for i, line in enumerate(self.__board):
			for j,  element in enumerate(line):
				if not(self.is_fixed(i,j)):
					self.__dna[count] = element
					count += 1

	def init_board(self):
		self.fill_allpositions()
		for i, line in enumerate(self.__board):
			#Make histogram of numbers on line
			hist = np.bincount(line)
			if len(hist) < 10:
				zeros = np.zeros(10-len(hist)).astype(int)
				hist = np.append(hist, zeros)
			hist[0] = 10
			for j, element in enumerate(line):
				if hist[element] > 1:
					#Principio da casa dos pombos... existe um elemnto nao usado
					new_element = np.argmin(hist)
					if self.set_position(i,j,new_element):
						hist[element] -= 1
						hist[new_element] += 1
			self.create_dna()

	def swap(self, coord1, coord2):
		i1, j1 = coord1
		i2, j2 = coord2
		if not(self.is_fixed(i1,j1) or self.is_fixed(i2,j2)):
			v1 = self.get_position(i1,j1)
			v2 = self.get_position(i2,j2)
			self.set_position(i1,j1,v2)
			self.set_position(i2,j2,v1)
