"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 5: Instruções de Controlo


# 5.1

def ordena_3(x,y,z):
    """Ordena os três números por ordem crescente."""
    if (x <= y) and (x <= z):
        if y <= z:
            return (x,y,z)
        else:
            return (x,z,y)
    if (y <= x) and (y <= z):
        if x <= z:
            return (y,x,z)
        else:
            return (y,z,x)    
    if (z <= x) and (z <= y):
        if x <= y:
            return (z,x,y)
        else:
            return (z,y,x)  

# 5.2

def custo_percurso(quil, alternativa):
    if alternativa == 'A1':
        return 0.15 * quil + 6.52
    elif alternativa == 'A20':
        return 0.12 * quil + 15.2
    elif alternativa == 'A21':
        return 0.1 * quil + 5.75
    

# 5.3

def vencimento(bruto, ss, cga,irs):
    """Calcula o vencimento ilíquido."""
    descontos = (ss+cdg+irs) * bruto
    return bruto - descontos
    

# 5.4

def nota(e,t1,t2,t3,t4):
    """Calcula nota final."""
    nota = 0.075 * (t1 + t2 + t3 + t4) + 0.7 * e
    print(nota)
    if nota >= 14 :
        return "Aprovado"
    elif nota < 7:
        return "Reprovado"
    else:
        return "Oral"

# 5.5

def ciclo_alternativo(n):
    for i in range(20,-1,-2):
        print("i= ",i)

# 5.6

"""
i      j    i/j
________________
0      1    0.0
0      2    0.0
----------------
1      1    1.0
1      2    0.5
----------------
2      1    2.0
2      2    1.0
"""


# 5.7

def amigas(cad_1, cad_2):
    """palavras que diferem em menos de 10% dizem-se amigas. Assume igual comprimento"""
    # Calcula distancia
    diferem = 0 
    for i in range(len(cad_1)):
        if cad_1[i] != cad_2[i]:
            diferem += 1
    percentagem = diferem / len(cad_1)
    return percentagem < 0.1


# 5.8

def min_div(num):
    """Calcula o menor divisor de um número inteiro > 1."""
    for i in range(2,num//2 + 1):
        if num % i == 0:
            return i
    return 1

def primo(num):
    return min_div(num) == 1


# 5.9
import random 

def dados(tentativas):
    """Determina a percentagem de lançamentos que deram um número par."""
    conta = 0
    for i in range(tentativas):
        numero = random.randint(0,6)
        if numero % 2 == 0:
            conta = conta + 1
    return conta/tentativas   

# 5.10

import random

def probab(num_dardos):
    """Probabilidade de acertar nas áreas ímpares."""
    conta = 0
    for i in range(num_dardos):
        x = random.uniform(0,2)
        y = random.uniform(0,2)   
        if ((x <= 1) and (y >= 1)) or ((x > 1) and (y <= 1)) or ((x > 1) and (y >= 1) and (y < x)):
            conta += 1
    return 100*conta/num_dardos

# 5.11

def fact(n):
    """Calcula o factorial de n."""
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res


# 5.12

def seno(x,prec):
    """ Calcula o seno de x com uma dada precisão."""
    ordem = 0
    res = 0
    dif = x
    while dif> prec:
        termo= (pow(-1,ordem) * pow(x,2*ordem +1)) / fact(2*ordem+1)
        res,ant = res + termo,res
        dif = abs(res-ant)
        ordem = ordem + 1
    return res

# 5.13
def harmonico(n):
    """ Calcula H_n."""
    h_n = 0
    for k in range(1,n+1):
        h_n += (1/k)
    return h_n


def harmonia(n):
    """Calcula uma sequência de números harmónicos."""
    serie = ()
    for i in range(1,n+1):
        serie += (harmonico(i),)
    return serie

def main(num):
    valores = harmonia(num)
    plt.xlabel('n')
    plt.ylabel('$H_n$')
    plt.title('Números Harmónicos')
    plt.plot(valores, label='Fórmula Usual')
    plt.legend(loc=0)
    plt.show()    

# 5.14
import math
import matplotlib.pyplot as plt

def harmonico(n):
    """ Calcula H_n."""
    h_n = 0
    for k in range(1,n+1):
        h_n += (1/k)
    return h_n

def harmonico_b(n):
    return math.log(n) + 0.5772156649

def harmonia(n):
    """Calcula uma sequência de números harmónicos."""
    serie = ()
    for i in range(1,n+1):
        serie += (harmonico(i),)
    return serie

def harmonia_b(n):
    """Calcula uma sequência de números harmónicos usando fórmula aproximada."""
    serie = ()
    for i in range(1,n+1):
        serie += (harmonico_b(i),)
    return serie

def main(num):
    valores = harmonia(num)
    valores_b = harmonia_b(num)
    plt.xlabel('n')
    plt.ylabel('$H_n$')
    plt.title('Números Harmónicos')
    plt.plot(valores, label='Fórmula Usual')
    plt.plot(valores_b, label='Fórmula Aproximada')
    plt.legend(loc=0)
    plt.show()  



# 5.15

def exponencial(prec):
    """ Calcula o valor de 'e' com uma dada precisão. Assume precisão inferior a 1."""
    ordem = 0
    res = 0
    dif = 1
    while dif> prec:
        termo= 1 / fact(ordem)
        res,ant = res + termo,res
        dif = abs(res-ant)
        ordem = ordem + 1
    return res

# 5.16

def perfeito(n):
    return n == soma_div(n)

def soma_div(n):
    """Calcula a soma dos dividores de um número excluindo ele próprio."""
    soma = 0
    for i in range(2,n):
        if n % i == 0:
            soma += i
    return soma + 1

# 5.17

def padrao_1(n):
    """ Imprime linhas de números entre 1 e n. Crescente alinhado à esquerda."""
    comp = len(str(n))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=comp*' ')
        print()

def padrao_2(n):
    """ Imprime linhas de números entre 1 e n. Decrescente alinhado à esquerda.."""
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
 
def padrao_3(n):
    """ Imprime linhas de números entre 1 e n. Crescente alinhado à direita."""
    for i in range(1,n+1):
        print(end=(n-i)*'  ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print() 
"""O primeiro padrão não tem problemas com os números."""

# 5.18
import turtle

def grelha(dim,lado):
    """Desenha uma grelha dim x dim em que cada célula tem de lado lado."""
    turtle.color("gray")
    tam = (dim*lado)
    x = -tam//2
    y = tam//2
    turtle.penup()
    turtle.goto(x,y)
    for lin in range(dim):  
        # Desenha linha de quadrados
        for col in range(dim):
            turtle.pendown()
            quadrado(lado)            
            turtle.penup()
            turtle.setx(turtle.xcor() + lado)
        # reposiciona
        turtle.penup()
        turtle.setposition(x, turtle.ycor()-lado)        
    turtle.hideturtle()

def quadrado(lado):
    for i in range(4):
        turtle.fd(lado)
        turtle.rt(90)
        
# 5.19

import turtle

def grelha(dim,lado):
    """Desenha uma grelha dim x dim em que cada célula tem de lado lado."""
    turtle.color("gray")
    tam = (dim*lado)
    x = -tam//2
    y = tam//2
    turtle.penup()
    turtle.goto(x,y)
    for lin in range(dim):  
        # Desenha linha de quadrados
        for col in range(dim):
            turtle.pendown()
            quadrado(lado)            
            turtle.penup()
            turtle.setx(turtle.xcor() + lado)
        # reposiciona
        turtle.penup()
        turtle.setposition(x, turtle.ycor()-lado)        
    turtle.hideturtle()

def quadrado(lado):
    for i in range(4):
        turtle.fd(lado)
        turtle.rt(90)
        
def passeio(dim, lado, passos):    
    # Prepara grelha
    turtle.speed(0)
    grelha(dim,lado)
    turtle.color('red')
    turtle.home()
    turtle.pendown()
    # Passeio
    turtle.speed(6)
    turtle.dot()
    turtle.showturtle()
    lim_x = lim_y = (dim*lado)//2
    cor_x = 0
    cor_y = 0
    for i in range(passos):
        vai_para = random.choice(['N','E','S','W'])
        if (vai_para == 'N') and (cor_y < lim_y):
            cor_y += lado
            turtle.setheading(90)
            turtle.fd(lado)
        elif (vai_para == 'E') and (cor_x < lim_x):
            cor_x += lado
            turtle.setheading(0)
            turtle.fd(lado)
        elif (vai_para == 'S') and (cor_y > -lim_y):
            cor_y -= lado
            turtle.setheading(270)
            turtle.fd(lado)
        elif (vai_para == 'W') and (cor_x > -lim_x):
            cor_x -= lado
            turtle.setheading(180)
            turtle.fd(lado) 
        else:
            print((vai_para,turtle.xcor(),turtle.ycor()))
            continue

# 5.20

def is_fib(n):
    """Determina se n é um número da sequência de fibonacci."""
    fib_ant = 0
    fib = 1
    while fib < n: 
        # next fib
        fib_ant, fib = fib, fib_ant + fib
    return fib == n

# 5.21

def novo_index(cadeia,elemento):
    try:
        indice = cadeia.index(elemento)
        return indice
    except ValueError:
        return -1
    
    
if __name__ == '__main__':
    #print(seno(2.4,0.001))
    #tabela_conv(10,100,1.609)
    #print(amigas('abcdefghijabcdefghij', 'abcdemghijabcdefghij'))
    #print(primo(101))
    #main(50)
    print(probab(50000))
    #print(exponencial(0.001))
    #print(perfeito(15))
    #grelha(5,20)
    #passeio(8,20,50)
    #turtle.exitonclick()
    cadeia ='abcdefghi'
    print(novo_index(cadeia,'z'))