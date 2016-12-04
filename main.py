from Board import *
from HillClimbing import *
from AlgoritmoGenetico import *

#Definir numeros de linhas e colunas do tabuleiro
n_rows = 9
n_cols = 9
#Definir as posicoes marcadas no tabuleiro (linha, coluna, valor)
markeds = [(1,0,1),(0,3,7),(2,3,4),(2,4,3),(2,6,2),(3,8,6),(4,3,5),(4,5,9),(5,6,4),(5,7,1),(5,8,8),(6,4,8),(6,5,1),(7,2,2),(7,7,5),(8,1,4),(8,6,3)]
#Cria o objeto hillclimbing que otimiza o tabuleiro 
h = HC(n_rows,n_cols,markeds)
#Cria o objeto algoritmo genetico (n_individuos, crossover_rate, mutation, hillclimbing.object, elitism_number, roubar_flag)
#Roubar utiliza hillclimbing + genetico, com roubar=True, utilize um n_individuos pequeno
#Utilizar n_individuos par
ag = AG(10,0.99,1.0,h,elitism=4,roubar=False)
#Treina com o N geracoes
#Caso nao encontre solucao, retorna None
solution = ag.train(1000)
print solution
print "pontuacao linha:",h.count_scoreline(solution)
print "pontuacao coluna:",h.count_scoreline(solution, trans=True)
print "pontuacao bloco:",h.count_scoresquad(solution)
print h.score(solution)
#O objeto do algoritmo genetico possui os individuos otimizados
#individuals = ag.get_individual()
