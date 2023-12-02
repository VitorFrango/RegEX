"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 6: Objectos (II)

# 6.1

def num_id(lista_idades):
    return len(lista_idades)

def idades(lista_idades):
    return lista_idades

def idades_inv(lista_idades):
    return lista_idades[::-1]

def min_max(lista_idades):
    return min(lista_idades), max(lista_idades)

def soma_idades(lista_idades):
    return sum(lista_idades)

def abaixo_de(referencia, lista_idades):
    for elem in lista_idades:
        if elem < referencia:
            print(elem)
            
def tem_17(lista_idades):
    return 17 in lista_idades


# 6.2 
def pares_impares(lista):
    """ Devolve a soma dsos pares e a soma dos impares."""
    pares = 0
    impares = 0
    for elem in lista:
        if elem % 2 == 0:
            pares = pares + elem
        else:
            impares = impares + elem
    return pares, impares

# 6.3

def alterna(lista_1, lista_2):
    """ Nova lista com elementos alternados. Assume mesmo comprimento."""
    nova_lista = []
    for i in range(len(lista_1)):
        nova_lista = nova_lista + [lista_1[i]] + [lista_2[i]]
    return nova_lista

# 6.4
def conta_menores(referencia, lista):
    """ Conta o número de elementos da lista menores do que o de referência."""
    conta = 0
    for elem in lista:
        if elem < referencia:
            conta = conta + 1
    return conta

# 6.5

import random

def lanca_dados(numero):
	"""
	Lança dois dados um número de vezes. Guarda resultados e determina
	a percentagem de somas pares.
	"""
	resultados = list()
	conta = 0
	for i in range(numero):
		primo = random.randint(1,6)
		segundo = random.randint(1,6)
		resultados.append([primo,segundo])
		if ((primo + segundo) % 2) == 0:
			conta = conta + 1
	return conta/numero, resultados

# 6.6

# Versão básica
def soma_cumulativa(lista):
	lista_1 = []
	for i in range(len(lista)):
		soma = 0
		for y in range(i+1):
			soma += lista[y]
		lista_1.append(soma)
	return lista_1

# Versão Pitónica
def soma_cumulativa_b(lista):
	lista_aux = list()
	for i in range(len(lista)):
		lista_aux.append(sum(lista[:i+1]))
	return lista_aux
    
# Versão ainda mais Pitónica...
def soma_cumulativa_c(lista):
    res = [sum(lista[:i+1]) for i in range(len(lista))]
    return res

# 6.7

""" Atenção à mutabilidade!!! Usar deepcopy pois cópia de superfície não serve!!!."""
import copy

# Versão básica
def negativo(imagem):
    copia = copy.deepcopy(imagem)
    for linha in range(len(imagem)):
        for coluna in range(len(imagem[0])):
            if copia[linha][coluna] == 0:
                copia[linha][coluna] = 1
            else:
                copia[linha][coluna] = 0
    return copia

# Versão Pitónica 
def negativo_b(imagem):
    copia = copy.deepcopy(imagem) 
    for linha in range(len(imagem)):
        for coluna in range(len(imagem[0])):
            #print('antes: ',copia[linha][coluna], end=' ')
            copia[linha][coluna] = (copia[linha][coluna] + 1) %  2
            #print('depois: ',copia[linha][coluna])
    return copia
    
# Versão ainda mais Pitónica   
def negativo_c(imagem):
    copia = copy.deepcopy(imagem) 
    for linha in range(len(imagem)):
        for coluna in range(len(imagem[0])):
            copia[linha][coluna] ^= 1
    return copia

# 6.8

# Versão Básica
def roda_90(imagem):
    """Baseia-se na construção da transposta da imagem vista como uma matriz."""
    copia_imagem = copy.deepcopy(imagem)
    imagem_aux = list()
    # transpõe
    for coluna in range(len(copia_imagem[0])):
        nova_linha = list()
        for linha in copia_imagem:
            nova_linha += [linha[coluna]]
        imagem_aux += [nova_linha]
    # inverte dentro das linhas
    for linha in range(len(imagem_aux)):
        imagem_aux[linha] = imagem_aux[linha][::-1]

    return imagem_aux

# Versão super pitónica
def roda_90_b(imagem):
    copia = copy.deepcopy(imagem)
    transposta = zip(*copia)
    final = [list(linha[::-1]) for linha in transposta]
    return final

# 6.9
import turtle
import random

def navega(comandos, tartaruga):
    """Simula o caminhar dde uma tartaruga numa cidade geométrica."""
    tartaruga.color('green')
    tartaruga.dot(10)
    tartaruga.color('black')
    for comando in comandos:
        if comando == 'A':
            tartaruga.fd(30)
        elif comando == 'R':
            tartaruga.bk(30)
        elif comando =='E':
            tartaruga.left(90)
        elif comando == 'D':
            tartaruga.right(90)
        else:
            print('comando desconhecido. Foi Ignorado!')
    tartaruga.color('red')
    tartaruga.dot(10)
    tartaruga.ht()

def gera_comandos(n):
    """Gera n comandos aleatoriamente. Alguns movimentos são mais prováveis do que outros."""
    comandos = ''
    for i in range(n):
        if random.choice([0,0,0,1]) == 0:
            comandos += random.choice(['A','A', 'A','A','R'])
        else:
            comandos += random.choice(['E', 'D'])
    return comandos
    
def main_tarta(n):
    tartaruga = turtle.Turtle()
    comandos = gera_comandos(n)
    navega(comandos,tartaruga)
    turtle.exitonclick()
    
# 6.10

def posicoes_vogais(texto):
    """Constrói um dicionário em que as chaves são vogais e os valores são listas das posições onde ocorrem."""
    dicio = dict()
    for i,car in enumerate(texto):
        if car in 'aeiouAEIOU':
            dicio[car] = dicio.get(car,[]) + [i]
    return dicio


# 6.11
"""
# Criar
autor = {"php":"Rasmus Lerdorf","perl":"Larry Wall","tcl":"John Ousterhout","awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens","python":"GuidovanRossum","xpto":"zxcv"}
print(autor)
{'tcl': 'John Ousterhout', 'awk': 'Brian Kernighan', 'parrot': 'Simon Cozens', 'python': 'GuidovanRossum', 'java': 'James Gosling', 'php': 'Rasmus Lerdorf', 'xpto': 'zxcv', 'perl': 'Larry Wall'}
#  a) Acrescentar
autor["c++"]="stroustrup"
print(autor)
{'tcl': 'John Ousterhout', 'awk': 'Brian Kernighan', 'c++': 'stroustrup', 'parrot': 'Simon Cozens', 'python': 'GuidovanRossum', 'java': 'James Gosling', 'php': 'Rasmus Lerdorf', 'xpto': 'zxcv', 'perl': 'Larry Wall'}
# b) Alterar
autor["python"]="Guido van Rossum"
print(autor)
{'tcl': 'John Ousterhout', 'awk': 'Brian Kernighan', 'c++': 'stroustrup', 'parrot': 'Simon Cozens', 'python': 'Guido van Rossum', 'java': 'James Gosling', 'php': 'Rasmus Lerdorf', 'xpto': 'zxcv', 'perl': 'Larry Wall'}
# c) Remover
del autor["xpto"]
print(autor)
# d) Contar
len(autor)
8
{'tcl': 'John Ousterhout', 'awk': 'Brian Kernighan', 'c++': 'stroustrup', 'parrot': 'Simon Cozens', 'python': 'Guido van Rossum', 'java': 'James Gosling', 'php': 'Rasmus Lerdorf', 'perl': 'Larry Wall'}
# e) Consultar
print(autor["c++"])
'stroustrup'
"""

# 6.12

# Versão básica
def dicio_fruta(fruta, peso):
    """Constrói um dicionário a partir de duas listas. São supostas ter o mesmo comprimento e sem repetições na fruta."""
    base_dados = dict()
    for i in range(len(fruta)):
        base_dados[fruta[i]] = peso[i]
    return base_dados

# Versão pitónica
def dicio_fruta_b(fruta, peso):
    """Constrói um dicionário a partir de duas listas. São supostas ter o mesmo comprimento e em repetições na fruta."""
    return dict(zip(fruta,peso))

# 6.13

def lucro(dicio):
    """ Dicionário organizado como pares (fruta, {compra: c, venda:v, peso:p,stock:s})."""
    lucro = 0
    for valor in dicio.values():
        lucro += (valor['peso'] - valor['stock']) * (valor['venda'] - valor['compra'])
    return lucro

def mais_cara(dicio):
    """Qual a fruta mais cara?"""
    lista = list()
    for fruta,dados in dicio.items():
        lista.append([dados['venda'],fruta])
    fruta_cara = max(lista)
    return fruta_cara[::-1]
    




# 6.14

def data(data,dicio_s,dicio_m):
    """ 
    Dada uma data no formato DS/DM/M/A, e um dicionário para dias da semana e outro para os meses
    converte a data um formato mais compreensível.
    """
    lista = data.split("/")
    return dicio_s[int(lista[0])]+", "+lista[1]+" de "+dicio_m[int(lista[2])]+" de "+lista[3]

# 6.15
import copy

def metabolismo(dicio):
    novo_dicio = copy.deepcopy(dicio)
    for chave,valor in dicio.items():
        if 'Masculino' in valor:
            metabola = 66 + 6.3 * valor[3] + 12.9 * valor[2] - 6.8 * valor[1]
        else:
            metabola = 65.5 + 4.3 * valor[3] + 4.7 * valor[2] - 4.7 * valor[1]
        novo_dicio[chave].append(metabola)
    return novo_dicio

# 6.16

def imc(dicio):
    for chave,valor in dicio.items():
        imc= valor[1] / (valor[0] ** 2)
        dicio[chave].append(imc)
    return dicio

# 6.17

# Versão Básica
def inverte(dicio):  
    """ Inverte um dicionário. Admite chaves diferentes com o mesmo valor."""
    novo_dicio = dict()
    for chave, valor in dicio.items():
        novo_dicio[valor] = novo_dicio.get(valor, []) + [chave]
    return novo_dicio

# Versão Pitónica
def inverte_dicio(dicio):
    """ Inverte dicionário no pressuposto de que chaves diferentes têm valores diferentes."""
    return dict([(valor, chave) for chave,valor in dicio.items()])


# 6.18
""" Árvores genealógicas organizadas como dicionário com pares (pai: [filho1, filho2,...])."""
def irmaos(dic,nome1,nome2):
    """ Têm o mesmo progenitor?"""
    prog1 = progenitor(dic, nome1)
    prog2 = progenitor (dic,nome2)
    return prog1 == prog2

# 6.19

# Versão básica
def netos(dicio,progenitor):
    """ Lista netos. Filhos dos filhos"""
    desc1 = filhos(dicio,progenitor)
    if desc1:
        net = []
        for elem in desc1:
            desc2 = filhos(dicio,elem)
            if desc2:
                net = net + desc2
    else:
        return []
    return net
            
def filhos(dicio,progenitor):
    """ lista dos filhos."""
    res= dicio.get(progenitor,None)
    return res

# Versão funcional
def netos_b(dicio ,progenitor):
    """ Lista dos netos. Os filhos dos filhos"""
    netos = filhos_b(dicio,filhos_b(dicio,[progenitor]))
    return netos

def filhos_b(dicio,lista_progenitores):
    lista_filhos = []
    for filho in lista_progenitores:
        lista_filhos.extend(dicio.get(filho,[]))
    return lista_filhos

# 6.20

def avo(dic,nome):
    """ Quem é o avô/avó do nome."""
    prog = progenitor(dic,nome)
    if prog:
        return progenitor(dic,prog)
    return None

if __name__ == '__main__':
    #print(lanca_dados(10))
    #print(soma_cumulativa(range(1,11)))
    #print(soma_cumulativa_b(range(1,11)))
    #print(soma_cumulativa_c(range(1,11)))
    #minha_imagem = [[0,1,0],[1,0,1],[0,0,0],[1,1,1]]
    #print('Original: ', minha_imagem)
    #print(negativo(minha_imagem))
    #print(negativo_b(minha_imagem))
    #print(negativo_c(minha_imagem))
    #outra_imagem = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #print(roda_90(outra_imagem))
    #print(roda_90_b(outra_imagem))
    #main_tarta(50)
    #fruta = ['peras','banana', 'abacate','uvas', 'laranja']
    #peso = [10,6,3,8,15]
    #print(dicio_fruta(fruta,peso))
    #print(dicio_fruta_b(fruta,peso))
    #texto = 'agora e que vao ser elas, Ai, Ai!'
    #print(posicoes_vogais(texto))
    # ----
    #fruta = ['pera','banana', 'abacate','uvas', 'laranja']
    #compra = [1.5,2.3,2.7,2.1,0.8]
    #venda = [1.7,2.6,3.1,2.4,1.0]
    #peso = [10,6,3,8,15] 
    #stock = [5,1,1,0,4]
    #d_1 = dict(zip(['compra', 'venda', 'peso','stock'], [compra, venda, peso, stock]))
    #print(d_1)
    #meu_dicio = {'pera':{'compra': 1.5, 'venda':1.7, 'peso':10,'stock':4}, 'banana':{'compra':2.1, 'venda':2.5, 'peso':8,'stock':0},'laranja':{'compra':0.8, 'venda':1.0, 'peso':15,'stock':2}}
    #print(meu_dicio)
    #print(lucro(meu_dicio))
    #print(mais_cara(meu_dicio))
    #outro_dicio = {123:['Masculino', 60, 1.80, 72],124:['Feminino', 41,1.67,47],125:['Masculino',25,1.83,70], 126:['Feminino',11,1.27,30]}
    #print(metabolismo(outro_dicio))
    #dicio_2 = {123:[1.80,72],124:[1.67,41],125:[1.83,70], 126:[1.27,30]}
    #print(imc(dicio_2))
    dicio_3 = {'joao':10,'pedro':18, 'tiago':13, 'luis':18}
    print(inverte(dicio_3))
    
    
