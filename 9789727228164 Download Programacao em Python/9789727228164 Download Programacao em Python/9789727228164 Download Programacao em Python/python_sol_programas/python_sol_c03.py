"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 3: Objectos (I)



# 3.1
"""
Python 3.2.3 (default, Sep  5 2012, 20:52:27) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.1.00)]
Type "help", "copyright", "credits" or "license" for more information.
a = 5
help(a)
Help on int object:

class int(object)
 |  int(x[, base]) -> integer
 |  
 |  Convert a string or number to an integer, if possible.  A floating
 |  point argument will be truncated towards zero (this does not include a
 |  string representation of a floating point number!)  When converting a
 |  string, use the optional base.  It is an error to supply a base when
 |  converting a non-string.
 |  
 |  Methods defined here:
 |  
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __and__(...)
 |      x.__and__(y) <==> x&y
 |  
 |  __bool__(...)
 |      x.__bool__() <==> x != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(...)
 |      x.__divmod__(y) <==> divmod(x, y)
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __float__(...)
 |      x.__float__() <==> float(x)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |  
 |  __format__(...)
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __index__(...)
 |      x[y:z] <==> x[y.__index__():z.__index__()]
 |  
 |  __int__(...)
 |      x.__int__() <==> int(x)
 |  
 |  __invert__(...)
 |      x.__invert__() <==> ~x
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __lshift__(...)
 |      x.__lshift__(y) <==> x<<y
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |  
 |  __or__(...)
 |      x.__or__(y) <==> x|y
 |  
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |  
 |  __pow__(...)
 |      x.__pow__(y[, z]) <==> pow(x, y[, z])
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __rand__(...)
 |      x.__rand__(y) <==> y&x
 |  
 |  __rdivmod__(...)
 |      x.__rdivmod__(y) <==> divmod(y, x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |  
 |  __rlshift__(...)
 |      x.__rlshift__(y) <==> y<<x
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |  
 |  __ror__(...)
 |      x.__ror__(y) <==> y|x
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(...)
 |      y.__rpow__(x[, z]) <==> pow(x, y[, z])
 |  
 |  __rrshift__(...)
 |      x.__rrshift__(y) <==> y>>x
 |  
 |  __rshift__(...)
 |      x.__rshift__(y) <==> x>>y
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __rtruediv__(...)
 |      x.__rtruediv__(y) <==> y/x
 |  
 |  __rxor__(...)
 |      x.__rxor__(y) <==> y^x
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  __truediv__(...)
 |      x.__truediv__(y) <==> x/y
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(...)
 |      x.__xor__(y) <==> x^y
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...)
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must either support the buffer protocol or be an
 |      iterable object producing bytes.  Bytes and bytearray are examples of
 |      built-in objects that support the buffer protocol.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

Descreve as operações do tipo inteiro.
"""

# 3.2
import math

def area_tri(a,b,c):
    """Area do triangulo: método de Heron."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
# 3.3
import math

def escada(altura, angulo):
    """ 
    Tamanho de uma escada para ser encostada a um parede com uma dada altura
    e fazendo um certoangulo.
    """
    return altura / math.sin(angulo)

def escada_graus(altura, angulo):
    """ 
    Tamanho de uma escada para ser encostada a um parede com uma dada altura
    e fazendo um certo angulo dado em graus.
    """
    radianos = math.pi/ 180 * angulo
    return altura / math.sin(radianos)
    
# 3.4

def bate_card_max(idade):
    """O batimento cardíaco aproximado em função da idade."""
    return 163 + 1.16 * idade - 0.018 * (idade **2)    

# 3.5

def ganhos(inicial, taxa_juro, tempo):
    """
    Taxa de juro composto. Um período de capitalazição.
    """
    return inicial * (1 + taxa_juro)** tempo
# 3.6

def ganhos_per(inicial, taxa_juro, tempo,per):
    """
    Taxa de hjuto composto. Vários períodos de capitalização
    """
    return inicial * (1 + taxa_juro/per)** (tempo*per)

# 3.7

import math

def entropia(n,m):
    if (n == 0) or (m == 0):
        return 0
    p_1 = n / (n+m)
    p_2 = m / (n+m)
    return - p_1 * math.log2(p_1) - p_2 * math.log2(p_2)


# 3.8 

def biseccao(func,a,b,n):
    """
    raízes de um polinómio pelo método da bisecção.
    função contínua em [a,b]
    a < b
    f(a) * f(b) < 0
    """
    for i in range(n):
        x = (a + b)/ 2
        res = func(x)
        print(x)
        if res * func(b) < 0:
            a = x
        else:
            b = x
            
def biseccao_b(func,a,b,eps):
    """
    raízes de um polinómio pelo método da bisecção.
    função contínua em [a,b]
    a < b
    f(a) * f(b) < 0
    """
    while True:
        x = (a + b)/ 2
        res = func(x)
        print(x)
        if abs(res) < eps:
            break
        if res < 0:
            a = x
        else:
            b = x
            
def poli_3(x):
    return x**3 - x - 1

if __name__ == '__main__':
    biseccao(poli_3,0,2,20)
    biseccao_b(poli_3,0,2,0.003)

            
# 3.9

def encripta(texto_normal):
    """Encriptação por separação dos caracteres nas posições pares
    e nas posições ímpares."""
    comp = len(texto_normal)
    # pares
    car_pares = texto_normal[0:comp:2]
    # impares
    car_impares = texto_normal[1:comp:2]
    # junta
    texto_encriptado = car_impares + car_pares
    return texto_encriptado

def desencripta(texto_encriptado):
    """Desencriptação por separação dos caracteres nas posições pares
    e nas posições ímpares. As posições ímpares foram colocadas primeiro!"""
    comp = len(texto_encriptado)
    meio = comp // 2
    # pares
    car_pares = texto_encriptado[meio:]
    # impares
    car_impares = texto_encriptado[:meio]
    # junta
    texto_normal = ''
    for i in range(meio):
        texto_normal = texto_normal + car_pares[i] + car_impares[i]
    if comp % 2 != 0:
        texto_normal = texto_normal + car_pares[-1]# tamanho ímpar
    return texto_normal

# 3.10

def descodifica_1(texto_encriptado,chave):
    """Descodifica um texto pelo método de substituição. A chave é 
    dada por uma correspondência um a um entre caracteres. Supõe que
    os caracteres são as 26 letras (minúsculas) do alfabeto mais o espaço em branco"""   
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    texto_normal = ''
    for car in texto_encriptado:
        indice = chave.find(car) 
        texto_normal = texto_normal + alfabeto[indice]
    return texto_normal

# 3.11

def complemento(adn):
    """Calcula o complemento de uma cadeia de ADN usando condicionais."""
    comp = ''
    for i in range(len(adn)):
        if adn[i] == 'A':
            comp = comp + 'T'
        elif adn[i] == 'T':
            comp = comp + 'A'
        elif adn[i] == 'C':
            comp = comp + 'G'
        elif adn[i] == 'G':
            comp = comp + 'C'
        else:
            print('ERRO: símbolo desconhecido!')
            return False
    return comp

# 3.12

def gera_adn_b(tam):
    """Gera uma cadeia de ADN de tamanho tam. Padrão ciclo-acumulador"""
    arn =''
    for i in range(tam):
        base = random.choice('TACG')
        arn = arn + base
    return arn

def gera_adn(tam):
    """Gera uma cadeia de ADN de tamanho tam."""
    return ''.join([random.choice('TACG') for i in range(tam)])

# 3.13

def tira_vogais(cadeia):
    """Retira as vogais e substitui por um espaço em branco.
    """
    vogais ='aeiou'
    nova_cadeia =''
    for conta in range(len(cadeia)):
        if cadeia[conta] in vogais:
            nova_cadeia = nova_cadeia + ' '
        else:    
            nova_cadeia = nova_cadeia + cadeia[conta]
    return nova_cadeia

def tira_vogais_b(cadeia):
    """Retira as vogais e substitui por um espaço em branco.
    """
    vogais ='aeiou'
    nova_cadeia =''
    for car in cadeia:
        if car in vogais:
            nova_cadeia = nova_cadeia + ' '
        else:    
            nova_cadeia = nova_cadeia + car
    return nova_cadeia  

# 3.14

def sub_cadeias(pal, n):
    """
    Todas as subcadeias de comprimento n.
    """
    for i in range(len(pal) - n + 1):
        print(pal[i:i + n])
# 3.15

def monty_pre():
    nome = 'Monty Python'
    for i in range(len(nome)):
        print(nome[:i+1])

# versão geral...
def prefixos(pal):
    """
    Mostra os prefixos da palavra.
    """
    for i in range(len(pal)):
        print(pal[:i+1])
        
# 3.16
def monty_suf():
    nome = 'Monty Python'
    for i in range(len(nome),-1,-1):
        print(nome[i:])
        
# Versão geral
def sufixos(pal):
    """
    Mostra os sufixos da palavra.
    """
    for i in range(len(pal),-1,-1):
        print(pal[i:])

# 3.17
import turtle

def adn_tartaruga(tartaruga, adn):
    """ Simula o comportamento da tartaruga ditado pelo seu ADN."""
    for car in adn:
        if car == 'f':
            tartaruga.fd(50)
        elif car == 't':
            tartaruga.bk(50)
        elif car == 'd':
            tartaruga.rt(45)
        else:
            tartaruga.lt(45)
            
            
# 3.18

import random

def adn_tartaruga_alea(tartaruga, adn):
    """ Simula o comportamento da tartaruga ditado pelo seu ADN."""
    for car in adn:
        lado = random.randint(20,100)
        angulo = random.randint(10,180)
        if car == 'f':
            tartaruga.fd(lado)
        elif car == 't':
            tartaruga.bk(lado)
        elif car == 'd':
            tartaruga.rt(angulo)
        else:
            tartaruga.lt(angulo)
            
            

# 3.19

def adn_tartaruga_total(tartaruga, passos):
    """ Simula o comportamento da tartaruga em função do seu ADN. O dito
    ADN é gerado aleatoriamente."""
    adn =''
    for i in range(passos):
        adn = adn + random.choice('fted')
    adn_tartaruga_alea(tartaruga,adn)

# 3.20

def codifica(texto_normal,chave):
    """Codifica um texto pelo método de substituição. A chave é a distância
    para codificar. Exemplo: 'a' passa a 'c' se chave for 2. Supõe que
    os caracteres são as 26 letras (minúsculas) do alfabeto  e o branco."""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    texto_encriptado = ''
    for car in texto_normal:
        novo_codigo = (alfabeto.index(car) + chave) % len(alfabeto)
        novo_car = alfabeto[novo_codigo]
        texto_encriptado = texto_encriptado + novo_car
    return texto_encriptado


def descodifica(texto_encriptado,chave):
    """Descodifica um texto pelo método de substituição. A chave é 
    dada por uma correspondência um a um entre caracteres. Supõe que
    os caracteres são as 26 letras (minúsculas) do alfabeto mais o espaço em branco"""   
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    texto_normal = ''
    for car in texto_encriptado:
        indice = alfabeto.find(car) 
        texto_normal = texto_normal + alfabeto[(indice - chave)%len(alfabeto)]
    return texto_normal

if __name__ == '__main__':
    #print(area_tri(2,3,4))
    #print(complemento('AATCGTAC'))
    #print(ganhos_dec(1000,0.02,5,12))
    #print(ganhos_dec(1000,0.02,5,1))
    texto = 'ernesto jorge fernandes costa'
    texto_2 ='anicomicoze '
    #encrip = encripta(texto)
    #print(encrip)
    #print(desencripta(encrip))
    #sub_cadeias('Monthy Python',4)
    #monty_pre()
    #prefixos('Monty Python')
    #print()
    #monty_suf()
    #sufixos('Monty Python')
    code = codifica(texto_2,-3)
    print(code)
    print(descodifica(code,-3))
    print(entropia(2,0))
    
    