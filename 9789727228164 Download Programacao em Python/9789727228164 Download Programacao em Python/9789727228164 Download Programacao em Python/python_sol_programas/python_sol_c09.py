"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 9: Recursividade

# 9.1
def mod(n,m):
    if n < m:
        return n
    else:
        return mod(n-m,m)

# 9.2
def prod_escalar(v,w):
    if len(v) == 0:
        return 0
    else:
        return (v[0] * w[0]) + prod_escalar(v[1:],w[1:])

# 9.3
def pot_op(x,n): 
    if n==0:
	return 1 
    else:
	factor=pot_op(x,n/2) 
	if (n%2 == 0):
	    return factor * factor 
	else:
	    return factor * factor * x

# 9.4
def remove_dup(cad): 
    if len(cad) == 1:
	return cad
    elif cad[0]== cad[1]:
	return cad[0] + remove_dup(cad[2:]) 
    else:
	return cad[0] + remove_dup(cad[1:])

# 9.5
def incluido(conj_1,conj_2):
    """conjuntos representados como listas."""
    if conj_1 == []:
        return True
    elif conj_1[0] not in conj_2:
        return False
    else:
        return incluido(conj_1[1:], conj_2)
	

# 9.6
def intersecta(conj_1, conj_2):
    """Determina a intersecção de dois conjuntos.""" 
    if conj_1 == []:
	return []
    elif conj_1[0] in conj_2:
	return [conj_1[0]] + intersecta(conj_1[1:], conj_2) 
    else:
	return intersecta(conj_1[1:], conj_2)

# 9.7
def horner_rec(x, poli):
    if len(poli) == 1:
        return poli[0]
    else:
        return poli[0] + x * horner_rec(x,poli[1:])

# 9.8
def power_set(conj):
	if conj == []:
		return [[]]
	else:
		temp = power_set(conj[1:])
		return temp + [[conj[0]] + elem for elem in temp ]

# 9.9
def ovais(n):
    if n == 1:
        return 2
    else:
        return 2* (n - 1) + ovais(n-1)

# 9.10
def figura_inc_lado_ang_var(lado,angulo,incl,inca): 
    "Desenha recursivamente com o incremento como parâmetro" 
    pd()
    if lado > 0:
	forward(lado)
	right(angulo)
	figura_inc_lado_ang(lado-incl,angulo-inca,0.8*incl,0.7*inca) 
	ht()
    return 0

# 9.11
from turtle import *

def arvore(lado, angulo,nivel):
    if nivel:
	pd()
	fd(lado)
	rt(angulo)
	arvore(lado/1.5,angulo,nivel-1)
	lt(2*angulo)
	arvore(lado/1.5,angulo,nivel-1)
	rt(angulo)
	bk(lado)

# 9.12
def arv_desigual(lado, angulo, nivel):
	if nivel:
		lt(angulo)
		arv_esq(lado,angulo, nivel-1)
		rt(2*angulo)
		arv_dir(lado, angulo, nivel -1)
		lt(angulo)
		
def arv_esq(lado, angulo,nivel):
	fd(2*lado)
	arv_desigual(lado, angulo, nivel)
	bk(2*lado)
	
def arv_dir(lado, angulo,nivel):
		fd(lado)
		arv_desigual(lado, angulo, nivel)
		bk(lado)
	
def main():
	setheading(90)
	arv_esq(25,30,7)
	ht()

# 9.13
def aplana(L):
    if L==[]:
	return L
    elif isinstance(L[0],list):
	return aplana(L[0]) + aplana(L[1:])
    else:
	return [L[0]] + aplana(L[1:])

# 9.14
def pat_match(pad,texto):
	if len(texto) < len(pad):
		return False
	elif pad == texto[:len(pad)]:
		return True
	else: 
		return pat_match(pad,texto[1:])
		
# - Variante: indica o índice do começo do padrão no texto
def pat_match_ind(pad,texto,indice):
	if len(texto) < len(pad):
		return False,-1
	elif pad == texto[:len(pad)]:
		return True, indice
	else: 
		return pat_match_ind(pad,texto[1:], indice +1)		

# 9.15
def prod_vectores(LV):
	if not LV:
		return [LV]
	else:
		res=[]
		for elem in LV[0]:
			for aux in prod_vectores(LV[1:]):
				res.append([elem] + aux)
		return res
# -- Variante		
def prod_vect_2(LV):
	if not LV:
		return [LV]
	else:
		return [[elem] + aux for elem in LV[0] for aux in prod_vect_2(LV[1:])]	



# 9.16
from random import *
from numpy import *

# Gerador de matrizes quadradas

def gera_mat(dim, val_max):
	return array([randint(1, val_max) for i in range(dim * dim)]).reshape(dim,dim)

# Strassen: caso de base	
def strassen_2(X2,Y2):
	# inicia matriz resultado
	Z2=zeros((2,2), dtype=int)
	# parâmetros
	p1=(X2[0,0] + X2[1,1]) * (Y2[0,0] + Y2[1,1])
	p2= (X2[1,0] + X2[1,1]) * Y2[0,0] 
	p3= X2[0,0] * (Y2[0,1] - Y2[1,1])
	p4=  X2[1,1] * (Y2[1,0] - Y2[0,0])	
	p5=(X2[0,0] + X2[0,1]) * Y2[1,1]
	p6=(X2[1,0] - X2[0,0]) * (Y2[0,0] + Y2[0,1])
	p7=(X2[0,1] - X2[1,1]) * (Y2[1,0] + Y2[1,1])
	# valores actualizados
	Z2[0,0]= p1 + p4 - p5 + p7
	Z2[0,1] = p3 + p5
	Z2[1,0] = p2 + p4
	Z2[1,1] = p1 + p3 + - p2 + p6
	
	return Z2
	
# Strassen: Geral
	
def strassen(X,Y):
	if (X.shape == (2,2)) and (Y.shape == (2,2)):
		return strassen_2(X,Y)
	else:
		n=X.shape[0]
		Z=gera_mat(n,1)
		m= n/2
		X11 = X[:m,:m]
		X12 = X[:m,m:]
		X21 = X[m:,:m]
		X22 = X[m:,m:]
		
		Y11 = Y[:m,:m]
		Y12 = Y[:m,m:]
		Y21 = Y[m:,:m]
		Y22 = Y[m:,m:]		
		
		P1= strassen((X11 + X22),(Y11 + Y22))
		P2= strassen((X21 + X22),Y11)
		P3= strassen(X11,(Y12 - Y22))
		P4= strassen( X22,(Y21 - Y11))
		P5= strassen((X11 + X12),Y22)
		P6= strassen((X21 - X11),(Y11 + Y12))
		P7= strassen((X12 - X22),(Y21 + Y22))
		
		Z11= P1 + P4 - P5 + P7
		Z12= P3 + P5
		Z21= P2 + P4
		Z22= P1 + P3 - P2 + P6
		
		Z[:m,:m] = Z11
		Z[:m,m:] = Z12
		Z[m:,:m] = Z21
		Z[m:,m:] = Z22
		return Z

# 9.17
"""Detector de paridade par."""
transit={'P':{'0':'P','1':'I'}, 'I':{'0':'I','1':'P'}}
inicial= 'P'
final= ['P']

def automato(estado,cad): 
    if cad == '':
	return (estado in final) 
    else:
	estado=transit[estado][cad[0]] 
	return automato(estado,cad[1:])

# 9.18
from turtle import *

def snowflake(size,level):
	for i in range(3):
		side(size,level)
		rt(120)
		
def side(size,level):
	if level == 0:
		fd(size)
		
	else:
		side(size/3, level-1)
		lt(60)
		side(size/3, level-1)
		rt(120)
		side(size/3,level-1)
		lt(60)
		side(size/3, level-1)

def main():
	speed(10)
	size,level=eval(input("Tamanho e Nível: "))
	snowflake(size,level)
	ht()
	exitonclick()

# 9.19
from turtle import *


def hilbert_esq(size,level):
	if level == 0 :
		return
	else:
		lt(90)
		hilbert_dir(size,level-1)
		fd(size)
		rt(90)
		hilbert_esq(size, level-1)
		fd(size)
		hilbert_esq(size, level-1)
		rt(90)
		fd(size)
		hilbert_dir(size,level-1)
		lt(90)
		
def hilbert_dir(size,level):
	if level == 0 :
		return
	else:
		rt(90)
		hilbert_esq(size,level-1)
		fd(size)
		lt(90)
		hilbert_dir(size, level-1)
		fd(size)
		hilbert_dir(size, level-1)
		lt(90)
		fd(size)
		hilbert_esq(size,level-1)
		rt(90)		
	



def main():
	tamanho = eval(input("Tamanho: "))
	nivel = eval(input('Nível: '))
	hilbert_esq(tamanho,nivel)
	exitonclick()




if __name__ == '__main__':
    print(ovais(5))
    c1 = [1,2,5]
    c2 = [5,3,4,1,2,6]
    print(incluido(c1,c2))

