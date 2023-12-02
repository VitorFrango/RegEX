"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 11: Desenvolvimento


# 11.1
def duplicados_3(lista):
    """
    Procura a existencia de pelo menos um par de numeros duplicados
    numa lista de inteiros positivos.
    """
    max_num = max(lista)
    tamanho = len(lista)
    aux = [0] * (max_num+1)
    print(aux)
    for i in range(tamanho):
        if aux[lista[i]] != 0:
            return True
        else:
            aux[lista[i]] = 1
    return False

# 11.2
import random
import time
import matplotlib.pyplot as plt

def profile(f):
    """Calcula informacao sobre o tempo gasto pela computacao de f(x)."""
    def inner(*x):
        tempo = time.time()
        res = f(*x)
        return time.time() - tempo
    return inner

def gera_lista(tamanho, inf,sup):
    return [random.randint(inf,sup) for i in range(tamanho)]

@profile
def duplicados_1(lista):
    """
    Procura a existencia de pelo menos um par de numeros duplicados
    numa lista de inteiros positivos.
    """
    tamanho = len(lista)
    for i in range(tamanho-1):
        for j in range(i+1,tamanho):
            if lista[i] == lista[j]:
                return True
            
    return False

@profile
def duplicados_2(lista):
    """
    Procura a existencia de pelo menos um par de numeros duplicados
    numa lista de inteiros positivos.Funciona no caso de os numeros constantes
    na lista forem inferiores ao valor do comprimento da lista.
    """
    tamanho = len(lista)
    aux = [0] * tamanho
    for i in range(tamanho):
        if aux[lista[i]] != 0:
            return True 
        else:
            aux[lista[i]] = 1
    return False


@profile
def duplicados_3(lista):
    """
    Procura a existencia de pelo menos um par de numeros duplicados
    numa lista de inteiros positivos.
    """
    max_num = max(lista)
    tamanho = len(lista)
    aux = [0] * (max_num+1)
    for i in range(tamanho):
        if aux[lista[i]] != 0:
            return True
        else:
            aux[lista[i]] = 1
    return False

@profile
def duplicados_4(lista):
    """Assume lista ordenada."""
    for index in range(len(lista)-1):
        if lista[index] == lista[index+1]:
            return index
    return -1

def main112():
    tempo_1 = []
    tempo_2 = []
    tempo_3 = []
    valores = [10,50,100,150, 250, 500,750,1000,1250,2500,5000,7500,10000,12500,15000, 20000,25000,30000,50000,100000]
    for tamanho in valores:
        max_num = int(10.0*tamanho-1)
        lista = gera_lista(tamanho,1,max_num)
        lista_2 = gera_lista(tamanho,1, tamanho-1)
        tempo_1.append(duplicados_1(lista))
        tempo_2.append(duplicados_2(lista_2))
        tempo_3.append(duplicados_3(lista))
        #lista_ord = sorted(lista[:])
        
        
    plt.title('Compara Tempos')
    plt.ylabel('Tempo Gasto')
    plt.plot(valores,tempo_1, label='Versão Normal')
    plt.plot(valores,tempo_2,label = 'Versão Lista')
    plt.plot(valores,tempo_3,label = 'Versão Lista Max')
    plt.legend(loc=2)
    plt.show()
   

# 11.3

import random
import time
import matplotlib.pyplot as plt

def profile(f):
    """Calcula informacao sobre o tempo gasto pela computacao de f(x)."""
    def inner(*x):
        tempo = time.time()
        res = f(*x)
        return time.time() - tempo
    return inner

def gera_lista(tamanho, inf,sup):
    return [random.randint(inf,sup) for i in range(tamanho)]


@profile
def duplicados_ord(lista):
    """ Pelo menos um duplicado?"""
    for index in range(len(lista)):
        if lista[index] == lista[index+1:]: # estando ordenado bastava fazer lista[index] == lista[index+1]
            return True
    return False
    
def main113():
    tempo = []
    valores = [10,50,100,150, 250, 500,750,1000,1250,2500,5000,7500,10000,12500,15000, 20000,25000,30000,50000,100000]
    for tamanho in valores:
        max_num = int(10.0*tamanho-1)
        lista = gera_lista(tamanho,1,max_num)
        tempo.append(duplicados_ord(lista))
    # visualiza    
    plt.title('Testa Duplicados')
    plt.ylabel('Tempo Gasto')
    plt.xlabel('Dimensão')
    plt.plot(valores,tempo)
    plt.show()


# 11.4

""" Recorrência no texto."""
def ovais(n):
    """
    Em quantas regiões distintas se divide o plano com n ovais
    sabendo que as ovais se interceptam duas a duas em exactamente dois pontos,
    e que três ovais nunca se encontram no mesmo ponto.
    """
    if n == 1:
        return 2
    else:
        return ovais(n-1) + 2* (n-1)
    
# 11.5
    
    """ Resolvido no texto."""

# 11.6

"""Resolvido no texto."""

# 11.7
import time
import matplotlib.pyplot as plt
from math import factorial

def profile(f):
    """Calcula informacao sobre o tempo gasto pela computacao de f(x)."""
    def inner(*x):
        tempo = time.time()
        res = f(*x)
        return time.time() - tempo
    return inner

@profile
def exp_e(x,k):
    pot = 1
    for i in range(k):
        pot += pow(x,i+1)/factorial(i+1)
    return pot
@profile
def exp_e_2(x,k):
    pot = 1 
    fact = 1
    res = 1
    for i in range(1,k):
        pot *= x
        fact *= i
        res += pot/fact
    return res

def main117(): 
    tempo_1 = []
    tempo_2 = []
    valores = list(range(10,1000))
    for tamanho in valores:
        tempo_1.append(exp_e(123,tamanho))
        tempo_2.append(exp_e_2(123,tamanho))
 
    plt.title('Compara Tempos')
    plt.ylabel('Tempo Gasto')
    plt.plot(valores,tempo_1, label='Versão Func')
    plt.plot(valores,tempo_2,label = 'Versão Simples')
    plt.legend(loc=2)
    plt.show()  
    
# 11.8
    
import doctest

def palindrome_1(objecto):
    """Determina se uma palavra é palindrtome
    >>> palindrome_1('AMA')
    True
    >>> palindrome_1('TOTO')
    False
    """
    if  not isinstance(objecto,list):
        objecto = str(objecto)
    return objecto == objecto[::-1]


def palindrome_2(s):
    """Determina se uma palavra é palindrtome
    >>> palindrome_1('AMA')
    True
    >>> palindrome_1('TOTO')
    False
    """
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and palindrome_2(s[1:-1])
	

if __name__ == '__main__':
    doctest.testmod()  
    
# 11.9
 """Resolvido no texto."""  
# 11.10
    
# 11.11
"""Resolvido no texto."""
# 11.12

"""Resolvido no texto."""

# 11.13
    
    
# 11.14
    
 """ Restante no texto."""
def tabuada_1(n):
    """Imprime uma tabuada: (1*1) (1*2) ... (1*n)\\(2*1) (2*2) ... (2*n) \\ ....(n*1) ... (n*n)"""
    for i in range(1,n+1):
        # imprime linha i
        pass


def tabuada_2(n):
    """Imprime uma tabuada: (1*1) (1*2) ... (1*n)\\(2*1) (2*2) ... (2*n) \\ ....(n*1) ... (n*n)"""
    for i in range(1,n+1):
        # imprime tabuada do i
        print('Tabuada do %d' % i)
        for j in range(1,11):
            #imprime valor (i*j)
            print('%d   X   %d  =  %d' % (i,j,i*j))
        print() # muda de linha     


# 11.15
"""Complexidade no texto."""
def insercao_1(seq):
    """Ordenamento por inserção."""
    for i in range(1,len(seq)):
        """Invariante: ordem relativa da posição 0 a (i-1)."""
        # Coloca elemento na posição i no lugar correcto entre 0 e i.
        pass
    
def insercao_2(seq):
    """Ordenamento por inserção."""
    for i in range(2,len(seq)):
        """Invariante: ordem relativa da posição 0 a (i-1)."""
        # Coloca elemento na posição i no lugar correcto entre 0 e i.
        # Compara seq[i] com os que estão à sua esquerda
        elem = seq[i]
        for j in range(i-1,-1,-1):
            # procura posição correcta para seq[i] e insere
            pass
    return seq
    
def insercao_3(seq):
    """Ordenamento por inserção."""
    for i in range(2,len(seq)):
        """Invariante: ordem relativa da posição 0 a (i-1)."""
        # Coloca elemento na posição i no lugar correcto entre 0 e i.
        # Compara seq[i] com os que estão à sua esquerda
        elem = seq[i]
        for j in range(i-1,-1,-1):
            if elem < seq[j]:
                # Enquanto for menor desloca os maiores uma posição para a direita
                seq[j+1] = seq[j]
            else:
                # Quando não houver nenhum insere e passa ao seguinta
                seq[j+1] = elem
                break
    return seq
    
def insercao_4(seq):
    """Ordenamento por inserção."""
    seq = [0] + seq[:]
    for i in range(2,len(seq)):
        """Invariante: ordem relativa da posição 0 a (i-1)."""
        # Coloca elemento na posição i no lugar correcto entre 0 e i.
        # Compara seq[i] com os que estão à sua esquerda
        elem = seq[i]
        for j in range(i-1,-1,-1):
            if elem < seq[j]:
                # Enquanto for menor desloca os maiores uma posição para a direita
                seq[j+1] = seq[j]
            else:
                # Quando não houver nenhum insere e passa ao seguinta
                seq[j+1] = elem
                break
    return seq[1:]
# 11.16
# 1 ---------------------
def quadrado_magico(quadrado):
	num_magico = nm(quadrado)
	# Verifica linhas
	# Verifica colunas
	# Verifica diagonais
	return resposta, num_magico
# 2 ----------------------
def quadrado_magico(quadrado):
	num_magico = nm(quadrado)
	# Verifica linhas
	if not linhas(quadrado,num_magico):
		return False, num_magico
	# Verifica colunas
	elif not colunas(quadrado, num_magico):
		return False, num_magico
	# Verifica diagonais
	else:
		return diagonals(quadrate,num_magico), num_magico
# 3 ----------------------
def linhas(quadrado,num_magic):
	for linha in lin(quadrado):
		if soma(linha) != num_magic:
			return False
	return True

def lin(quadrado):
	return []

def colunas(quadrado, num_magic):
	for coluna in col(quadrado):
		if soma(coluna) != num_magic:
			return False
	return True

def col(quadrado):
	return []
	
def diagonais(quadrado,num_magic):
	for diagonal in diag(quadrado):
		if soma(diagonal) != num_magic:
			return False
	return True

def diag(quadrado):
	return []

# 4 ----------------------

def lin(quadrado):
	return quadrado
	
def col(quadrado):
	mat = []
	for i in range(len(quadrado)):
		linha_i = []
		for j in range(len(quadrado[0])):
			linha_i.append(quadrado[j][i])
		mat.append(linha_i)
	return mat
	
def diag(quadrado):
	diag_1 = []
	diag_2 = []
	for i in range(len(quadrado)):
		for j in range(len(quadrado[0])):
			if i == j:
				diag_1.append(quadrado[i][j])
			if (i+j) == (len(quadrado) - 1):
				diag_2.append(quadrado[i][j])
	return [diag_1, diag_2]


def soma(lista):
	return sum(lista)
# 5 -------------------
def nm(quadrado):
	linhas = len(quadrado)
	colunas = len(quadrado[0])
	return (linhas ** 3 + colunas) / 2
 
# 11.17

# 11.18

def consensus(lseq):
	"""
	Constrói a sequência de consenso a partir de uma lista de sequências de ADN 
	de igual comprimento.
	"""
	# 1. inicializa sequência de consenso
	cons = '' # vai ser uma string
	# 2. por cada posição da sequência
	for pos in range(len(lseq[0])): # entrada uma lista
		# 2.1 calcula qual a base mais frequente para a posição corrente
		# inicializa contadores das bases
		dicio_bases={'A':0,'C':0,'T':0,'G':0} # uso um dicionário para contar
		# para cada sequência
		for seq in lseq: 
			# determina a base por cada sequência e actualiza o seu contador
			dicio_bases[seq[pos]]=dicio_bases[seq[pos]] + 1
		# determina a base que ocorre mais vezes
		base=max_ocorre(dicio_bases)
		# 2.2 actualiza a sequência de consenso na posição corrente
		cons = cons + base # a base será um caracter
	# 3. Devolve a sequência de consenso completa
	return cons


def max_ocorre(dicio):
	"""A chave cujo valor associado é o maior.
	A solução depende muito do que se sabe de Python!
	Vamos ver a solução mais 'ignorante'."""
	# Vamos buscar os pares (chave, valor)
	items=list(dicio.items())
	max_val=items[0][1]
	max_ch=items[0][0]
	for par in items:
		if par[1] > max_val:
			max_val=par[1]
			max_ch=par[0]
	return max_ch

# 11.19

# 11.20


if __name__ == '__main__':
    main113()

