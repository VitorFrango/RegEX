"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 1 : Introdução


# 1.1
"""
 Windows: executar o IDLE (python gui) ou executar cmd; ir para o directório \texttt{c:\textbackslash Python34} e executar o ficheiro python.exe\\
 Linux e Mac OS: na linha de comandos executar o comando python3
 """
# 1.2

def computacoes():
    """ Efectua diversas computações simples. """
    print("2+4 =",2+4)
    print("40*300 =",40*300)
    print("1/2 =",1/2)
    print("1.0/2 =",1.0/2)
    print("1.0//2 =",1.0//2)
    print("20e30*4 =",20e30*4)
    print("20e50*20e50 =",20e50*20e50)
    print("7%5 =",7%5)
    print("(5+2j)+(3+4j) =",(5+2j)+(3+4j))
    print("(5+2j)*(3+4j) =",(5+2j)*(3+4j))
    print("(5+2j)/(3+4j) =",(5+2j)/(3+4j))

# 1.3
""" Se usar em modo interactivo não necessita do print."""
print((9459 * 10**12) * (2.9 * 10**6))

# 1.4
""" Se usar em modo interactivo não necessita do print."""
print (365 * 24 * 60 * 60)

# 1.5
""" Se usar em modo interactivo não necessita do print."""
print ((8*6) // (2*2))

# 1.6

def atributos_objectos():
    """ Mostra os atributos de três tipos numéricos diferentes. """
    int = 5
    print("Atributos de",int,":",id(int),type(int),int)
    float = 5.0
    print("Atributos de",float,":",id(float),type(float),float)
    imag = 2+5j
    print("Atributos de",imag,":",id(imag),type(imag),imag)
    
# 1.7

base = 5
altura = 7

area = base * altura / 2
print(area)

# Variante

def area(base, altura):
    return base * altura / 2

print(area(5,7))

# 1.8

nova_area = 7.62 ** 2

velha_area = 3.1459 * (8.89/2)**2

print('nova= ', nova_area, 'velha= ', velha_area)

# 1.9

def imc(peso, altura):
    return peso/altura**2

# 1.10

def converte_c_to_f(celcius):
    return 9/5 * celcius + 32

# 1.11

def volume_cone(raio, altura):
    return 3.1459 * (raio**2) * altura / 3
# 1.12

def valor_poli(x):
    return x**4 + x**3 + 2*x**2 - x

print(valor_poli(1.1))

# 1.13

import math

print (math.sqrt(-4))
"""
Traceback (most recent call last):
  File "/Volumes/Work/LIVRO_PYTHON_2012/IPRP_LIVRO_2013_07/introd/programas/intro_sol.py", line 72, in <module>
builtins.ValueError: math domain error
"""

# 1.14

def cambio_1(valor, taxa):
    return valor * taxa
    

# 1.15
def garrafas(litros):
    g5,r5 = int(litros/5), int(litros%5)
    g15,r15 = int(r5/1.5), int(r5%1.5)
    g05,r05 = int(r15/0.5), int(r15%0.5)
    g025, r025 = int(r05/0.25), int(r05%0.25)
    return (g5,g15,g05,g025,r025)

# 1.16

import random

def jogar():
    tentativas = 3
    print("Bem vindo ao jogo da adivinha.")
    print("Tem %d tentativas para adivinhar um número inteiro entre 0 e 100" % tentativas)
    print("Eu ajudo...")
    jogar = eval(input("Vamos jogar? Entre 1 para Sim, e 0 para Não:  "))
    acertou = 0
    total_tentativas = 0 
    jogos = 0
    while jogar:
        tent, acer = adivinha(tentativas)
        total_tentativas = total_tentativas + tent
        acertou = acertou + acer
        jogos = jogos + 1
        jogar = eval(input("Vamos jogar mais? Entre 1 para Sim, e 0 para Não:  "))
    if jogos == 0:
        print("Então não quer jogar???")
        print("Até à próxima!")
    else:
        print("Até à próxima!")
        print("Número de jogos: %d" % jogos)
        print("Percentagem de acerto: %3.2f." % (acertou/jogos))
        print("Número médio de tentativas: %3.2f." % (total_tentativas/jogos))

# 1.17

def cartesianas2polares(x,y):
    """ Converte coordenadas cartesianas em polares. """
    r = math.sqrt(x**2+y**2)
    theta = math.atan(y/x)
    return (r,theta)

# 1.18

def periodo_orbital_planeta(distancia_sol):
    """ Calcula o período, em anos, da órbita de um planeta, dada
    a sua distância ao Sol em Unidades Astronómicas (AU). """
    p = math.sqrt(distancia_sol**3)
    return p

# 1.19

def periodo_orbital_geral(distancia, M1, M2):
    """ Calcula o período orbital (em dias) de qualquer corpo que orbita
    em volta de qualquer estrela, a partir da distância (AUs) entre os
    corpos e a massa solar de cada um deles (M1 e M2). """
    G = 6.67e-11 # m^3 kg^(-1) s^(-2)
    p = math.sqrt(4*math.pi**2*distancia**3/(G*(M1+M2))) # segundos
    return p/(24*60*60) # dias

if __name__ == '__main__':
    pass
