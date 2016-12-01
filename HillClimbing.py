import numpy as np
from Board import *

class HC:
	#Construtor
	def __init__(self, n_rows, n_cols, markeds):
		self.__rows = n_rows
		self.__cols = n_cols
		self.__markeds = markeds

	def create_board(self):
		rows = self.__rows
		cols = self.__cols
		markeds = self.__markeds
		return Board(rows, cols, markeds)

	def train(self, n_cases):
		sum_difs = 1
		boards = []
		values = []
		solution = None
		for i in xrange(n_cases):
			b = self.create_board()
			b.init_board()
			boards.append(b)
			values.append(0)
		epoch = 0
		while sum_difs != 0:
			sum_difs = 0
			epoch += 1
			print "Epoch:",epoch
			for i in xrange(n_cases):
				new_board, new_value = self.climbing(boards[i])
				sum_difs += abs(values[i] - new_value)
				values[i] = new_value
				boards[i] = new_board
				if new_value == 162: solution = new_board
			print "Progress", sum_difs
			print values
		return values, boards, solution

	def climbing(self, board):
		coord1 = (0,0)
		coord2 = (0,0)
		rows, cols = board.get_dimensions()
		temp_score = self.score(board)
		
		for i in xrange(rows):
			for j in xrange(cols):
				if board.is_fixed(i,j): continue
				for k in xrange(j+1, cols):
					if board.is_fixed(i,k): continue
					board.swap((i,j),(i,k))
					if self.score(board) >= temp_score:
						coord1 = (i,j)
						coord2 = (i,k)
						big = self.score(board)
					board.swap((i,j),(i,k))
					
		board.swap(coord1,coord2)
		return board, self.score(board)

	def count_errorline(self, board, trans=False):
		b = board.get_board()
		if trans:  b = b.T
		score = 0
		for line in b:
			hist = np.bincount(line)
			score += np.count_nonzero(hist)
		return score

	def count_errorsquad(self, board):
		score = 0 
		rows, cols = board.get_dimensions()
		b = board.get_board()
		for i in xrange(0,rows,3):
			for j in xrange(0,cols,3):
				aux = board.get_submatrix(i,j,3,3).flatten()
				hist = np.bincount(aux)
				score += np.count_nonzero(hist)
		return score


	#Here !! Board is a numpy array n_rows x n_cols dimensions
	def score(self, board):
		score1 = self.count_errorline(board, trans=True)
		score2 = self.count_errorsquad(board)
		return score1 + score2