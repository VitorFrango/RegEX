"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 4: Instruções Destrutivas


# 4.1
""" correr no interpretador. os não válidos são:
5peso (começa por dígito)
with, class (palavras reservadas)
peso$, a(b), area-rect (caracteres não autorizados)
"""
 
# 4.2
"""
>>> chr(0x3B1)
'α'
>>> 
"""

# 4.3

"""
>>> x = 5
>>> y = 5
>>> id(x)
4446072256
>>> 4446072256

Trata-se do mesmo objecto com dois nomes diferentes. Os inteiros pequenos
estão internalizados.
"""

# 4.4

"""
Semelhante ao caso anterior.
"""

# 4.5
""" A identidade alterou-se. O nome é um atributo do objecto.
A instrução de atribuição tem à esquerda um nome e à direita uma expressão. A expressão é avaliada e o objecto
encontrado é associado com o nome 'x', desfazendo a ligação anterior.
"""

# 4.6
"""
Junta os dois casos anteriores.
"""

# 4.7
"""
Fazer o boneco...
"""


# 4.8
"""  
É feita uma cópia de superficie da cadeia 'a' com tamanho 3.
"""

# 4.9

"""
print(format('Bem vindo a IPRP', '20s'))
print(format('Bem vindo a IPRP', '<20s'))
print(format('Bem vindo a IPRP', '>20s'))
print(format('Bem vindo a IPRP e ao DEIUC', '>20s'))
"""

# 4.10

def imprime_tabela(numero):
    """ Tabela com os valores de numero, numero ^ 2."""
    print('Número\t\tQuadrado')
    for i in range(1,numero+1):
        print('%6d\t\t%8d' % (i, i**2))

# 4.11

def tabuada(n):
    """Imprime a tabela da tabuada do númeron."""
    print('Tabuada do número  %d' % n)
    print('-'*30)
    for i in range(1,11):
        print('%d\tx\t%4d\t=%4d' % (n,i,i*n))

# 4.12

def acronimo(cadeia):
    """Constrói o acrónimo a partir de uma frase representada por uma cadeia de caracteres."""
    acro = ''
    inicio = True
    for car in cadeia:
        if inicio == True:
            acro = acro + car.upper()
            inicio = False
        elif car == ' ':
            inicio = True
    return acro

# 4.13

def comprimento():
    """Calcula o tamanho da pista necessário para a descolagem."""
    vel = eval(input('Velocidade de descolagem (m/s): '))
    ace = eval(input('Aceleração para descolagem (m/s²): '))    
    comp = (vel**2) / (2*ace)
    print('Para a velocidade %3.2f e aceleração %3.2f o comprimento mínimo da pista é: %5.2f.' % (vel,ace,comp))

# 4.14

def energia():
    """Calcula o valor da energia necessária para variar a temperatura da água."""
    t_i = eval(input('Temperatura inicial  (Celcius): '))
    t_f = eval(input('Temperatura final (Celcius): '))  
    m = eval(input('Quantidade de água (Quilogramas): ')) 
    
    e = m * (t_f - t_i) * 4184
    
    print('Para a massa de água %3.2f, temperatura inicial %3.2f e temperatura final %3.2f a energia necessária é: %10.2f Joules.' % (m,t_i,t_f,e))  

# 4.15

def temperatura():
    """Calcula o valor da temperatura exterior em função do vento."""
    vel = eval(input('Velocidade do vento (milhas/hora): '))
    temp = eval(input('Temperatura (Fashrenheit [-58, 41]): '))    
    
    res = 35.74 + 0.6215 * temp - 35.75 * (vel**0.16) + 0.4275 * temp * (vel ** 0.16)
    
    print('Para a velocidade do vento %3.2f e temperatura exterior %3.2f a temperatura é sentida conmo: %5.2f.' % (vel,temp,res))  

# 4.16

def mostra_matriz(matriz):
    """imprime os elementos de uma matriz de modo organizado."""
    print()
    for j,linha in enumerate(matriz):
        for i,coluna in enumerate(linha):
            print('(%d,%d): %d\t' % (j,i,coluna), end='')
        print()

# 4.17

def estima(pop):
    """Ao fim de um ano qual o novo valor da população."""
    nasce = eval(input('Frequência de nascimentos (minutos): '))
    morre = eval(input('Frequência de falecimentos (minutos): '))
    emigra = eval(input('Frequência de emigração (minutos): '))
    
    total_minutos = 365 * 24 * 60
    
    nascimentos_ano = total_minutos // nasce
    mortes_ano = total_minutos // morre
    emigrantes_ano = total_minutos // emigra
    
    final_ano = pop + nascimentos_ano - mortes_ano - emigrantes_ano
    print('Resumo dos dados:')
    print('-----------------')
    print('Frequência de nascimentos: %d\nFrequência de mortes: %d\n\
    Frequência de emigrantes:%d\nPopulação Inicial:%d'%(nasce,morre, emigra, pop))
    print('Estimativa:')  
    print('-----------')
    print('A população ao fim de um ano: %d' %final_ano)

# 4.18

def add2me(x):
    return x + x

"""
>>> add2me(23.4)
46.8
>>> add2me('toto')
toto
O operador '+' está sobrecarregado funcionando no promeiro caso como soma
e no segundo como concatenação.
"""


# 4.19
def prod(x,y):
    return x * y

"""Os nomes x e y só existem durante a execução (e no interior) da função prod.
Daí que se obtenha um erro quando se procura saber o valor de x fora da execução de prod.
Por outro lado o valor associado a não é alterado pois a não foi associado a nenhum novo objecto.
"""


# repete impressão
def mensagem(texto):
    """ Imprime o texto cinco vezes."""
    for i in range(5):
        print(texto)


if __name__ == '__main__':
    #print(acronimo('Random Acess Memory'))
    #imprime_tabela(5)
    #comprimento()
    #temperatura()
    #energia()
    #tabuada(5)
    mat = ((1,2,3),(4,5,6),(7,8,9),(10,11,12))
    #mostra_matriz(mat)
    #estima(10e6)
    print(add2me(23.4))
    print(add2me('toto'))
    a = 5
    print(prod(a,3))