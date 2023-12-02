"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 10: Complementos


# 10.1
"""
>>> nome = 'ernesto'
>>> def toto():
...	nome='costa'
...	return None
...
>>> toto()
>>> nome
'ernesto' # <-- Resultado
"""

# 10.2
"""
>>> ultima_resposta = 60
>>> def ultima_maquina():
...     global ultima_resposta
...     ultima_resposta = 'Nope!'
...     return ultima_resposta
... 
>>>
>>> ultima_maquina()
'Nope!' # <--- resultado
>>> ultima_resposta
'Nope!'
"""

# 10.3
"""
>>> def f(t=0):
...       def g(t=0):
...           def h():
...               nonlocal t
...               t += 1
...          return h, lambda:t
...      h, gt = g()
...      return h,gt,lambda:t
...
>>> h,gt,ft = f()
>>> h
<function f.<locals>.g.<locals>.h at 0x101677f28>
>>> gt
<function f.<locals>.g.<locals>.<lambda> at 0x101776048>
>>> ft
<function f.<locals>.<lambda> at 0x1017760d0>
>>> ft(),g()
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
builtins.NameError: name 'g' is not defined
>>> h()
>>> ft(),gt()
(0, 1)
"""

# 10.4 
def gere_depositos_2(saldo):
    def movimento(montante):
        nonlocal saldo
        if (montante < 0) and abs(montante) > saldo:
            return 'Saldo insuficiente'
        saldo += montante
        return saldo
    return movimento

# 10.5
def gere_contador(inicio):
    def actualiza(accao):
        nonlocal inicio
        if accao == 'conta':
            inicio += 1
            return inicio
        elif accao == 'reiniciar':
            inicio = 0
            return inicio
        else:
            return 'Accção desconhecida'
    return actualiza 

# 10.6
def eco_atrasado():
    velha = ''
    while True:
        nova = get_frase()
        yield velha
        velha = nova
        
def get_frase():
    f = input('Frase: ')
    return f


eco = eco_atrasado()
for i in range(3):
    print(next(eco))

# 10.7

# 10.8
def trace(f):
    """Como fazer o trace da execução de funções."""
    f.indent = 0
    def aux(x):
        print('|  ' * f.indent + '|__',f.__name__,x)
        f.indent += 1
        resultado = f(x)
        print('|  ' * f.indent + '|__','return', repr(resultado))
        f.indent -= 1
        return resultado
    return aux

def trace_b(f):
    def aux(x):
        print(f.__name__,x)
        res = f(x)
        print('return ', repr(res))
        return res
    return aux

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
        
fib = trace(fib)
print(fib(5))

# 10.9
def range_iter(inicio,fim,step):
    while inicio < fim:
        yield inicio
        inicio += step
for i in range_iter(2.4, 6,2, 0.5):
    print(i)

# 10.10
def pares():
    num = 0
    while True:
        yield num
        num += 2
num_par = pares()
for i in range(5):
    print(next(num_par))
    
# 10.11
def gera_valores(func,gera_ent):
    val = func(next(gera_ent))
    while True:
        yield val
        val = func(next(gera_ent))
        
def gera_ent(val,novo_val):
    while True:
        yield val
        val = novo_val(val)
        
def transforma(x):
    return 2*x

def funcao(x):
    return x**2


g_x = gera_ent(1,transforma)
g_val = gera_valores(funcao,g_x)
for i in range(10):
    print(next(g_val))

# 10.12
def letras(inicial='a'):
    actual = inicial
    while 1:
        yield actual
        actual = chr(ord(actual) + 1)
        
gera_letras = letras('c')
for i in range(5):
    print(next(gera_letras))

# 10.13
from math import factorial

def exponencial(x):
    val = 1
    n = 0
    while True:
        yield val
        n += 1
        val += pow(x,n)/factorial(n)

exp = exponencial(2)       
for i in range(10):
    print(next(exp))

# 10.14
def gera_par(seq):
    index = 0
    while True:
        yield (seq[index],seq[index+1])
        index += 1
        
def ordenada(seq):
    par = gera_par(seq)
    return all([compara(next(par)) for i in range(len(seq)-1)])
        
    
def ordenada_b(seq):
    return all([compara((seq[i],seq[i+1])) for i in range(len(seq)-1)])

def compara(par):
    return par[0] <= par[1]

# 10.15
def filtra(func,seq):
    return list(filter(func,seq))

def criterio(x):
    return (x % 3 != 0) and (x % 5 != 0)


lista = [1,2,3,4,5,6,7,8,9,10]
print(filtra(criterio,lista))

# 10.16
import functools

def meu_min(sequencia):
    return functools.reduce(lambda x,y: x if x<y else y,sequencia)


lista = [3,6,2,8,1,-9,10]
print(meu_min(lista))

# 10.17
import functools
import operator

def factorial(n):
    if n == 0:
        return 1
    else:
        return functools.reduce(operator.mul,range(1,n+1))
    
print(factorial(4))

# 10.18
def cadeia_f(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g


my_pow = cadeia_f(pow)
print(my_pow(2)(3))

# 10.19
import operator

def prod_escalar(vec_1, vec_2):
    return sum(map(operator.mul,vec_1,vec_2))

# 10.20





