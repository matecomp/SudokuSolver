# SudokuSolver

### Instruções de uso

  - Na pasta do projeto, execute main.py

Três classes:
  - Board - Tabuleiro do Sudoku
  - HillClimbing - Otimizador do Board
  - AlgoritmoGenético - Encontra a solução baseado em seleção natural

(a ) - A função consiste em contar os algarismos de 1 a m que apareceu em cada linha, coluna e bloco. Isso resulta em um range de 0 a mxm para cada conjunto (linha, coluna e bloco). Esta função retorna um valor entre 0 (mínimo global) e 3xmxm (máximo global).

	ex: m = 4
			1 2 | 3 4
			1 2 | 2 3
			---------
			2 3 | 3 1
			4 4 | 1 2
    linhas:	
			1º -> 4
			2º -> 3
			3º -> 3
			4º -> 3
	coluna:
			1º -> 3
			2º -> 3
			3º -> 3
			4º -> 4
	bloco:
			1º -> 2
			2º -> 3
			3º -> 3
			4º -> 3 
		total : 13 + 13 + 11 = 37

(b ) - Mesmo sem nenhuma informação, podemos preencher o tabuleiro já com as linhas ou com as colunas na pontuação máxima. Basta inserir o valor que ainda não foi usado. Neste trabalho foi configurado o estado inicial com a pontuação máxima em linhas. Falta otimizar a pontuação para colunas e blocos. O próximo passo é definido pelo swap entre dois elementos de uma linha, esta operação não afeta a pontuação de linhas, mas afeta as pontuações restante. Logo o próximo passo é o swap de uma linha qualquer que melhor otimiza a pontuação de colunas e bloco. O novo máximo e mínimo global neste novo problema é 182 e 18 respectivamente. 

(c ) - O crossover entre dois tabuleiros é um corte horizontal numa linha escolhida aleatoriamente durante a execução, após cortar os "pedaços" são combinados.

    ex:     A             B                A/B
        1 2 | 3 4     2 3 | 1 4         2 3 | 1 4
    	1 2 | 2 3     2 3 | 1 4         2 3 | 1 4
    	--------- (x) ----------     = ----------
    	2 3 | 3 1     2 3 | 1 4         2 3 | 3 1
    	4 3 | 1 2     2 3 | 1 4         4 3 | 1 2

