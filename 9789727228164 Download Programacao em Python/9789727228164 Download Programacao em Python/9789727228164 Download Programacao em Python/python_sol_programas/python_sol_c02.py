"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 2: Visões (I)


import turtle

# 2.1 -------------------------------------------------------------------------

def formas(num_lados, comp_lado, angulo_viragem):
    """
    Desenha formas regulares, fazendo variar os três parâmetros.
    >>> formas(4,100,144)
    desenha uma estrela.
    """
    for i in range(num_lados):
        turtle.forward(comp_lado)
        turtle.right(angulo_viragem)
    turtle.hideturtle()
    

# 2.2 -------------------------------------------------------------------------

import turtle

def estrela_espiral(tarta,repete,incremento):
    """
    Desenha uma estrela em espiral.
    """
    for i in range(repete):
        tarta.forward(i * incremento)
        tarta.right(144)
        
if __name__ == '__main__':
    tarta = turtle.Turtle()
    estrela_espiral(tarta,30,8)
    turtle.exitonclick()

# 2.3 -------------------------------------------------------------------------

import random 

def random_walk(num_lados,comp_lado):
    """
    Simula um passeio aleatório.Muda a cor em cada etapa.
    """
    # Define modo de cor
    turtle.colormode(255)
    for i in range(num_lados):
        # define cor
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        turtle.pencolor((r,g,b))
        # Avança
        turtle.forward(comp_lado)
        # Vira
        turtle.setheading(random.randint(0,360))
    turtle.hideturtle()
    
def random_walk_2(num_lados,comp_lado):
    """
    Simula um passeio aleatório.Muda a cor em cada etapa.
    """
    for i in range(num_lados):
        # define cor
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor((r,g,b))
        # Avança
        turtle.forward(comp_lado)
        # Vira
        turtle.setheading(random.randint(0,360))
    turtle.hideturtle()    

# variante

def random_walk_var(num_lados,comp_lado):
    """
    Simula um passeio aleatório. Só três direcções: esquerda, direita, frente.
    """
    for i in range(num_lados):
        # Avança
        turtle.forward(comp_lado)
        # Vira
        dir = random.randint(0,2)
        if dir == 1:
            turtle.setheading(turtle.heading() + 90)
        elif dir == 2:
            turtle.setheading(turtle.heading() - 90)   
    turtle.hideturtle() 
    
# 2.4 -------------------------------------------------------------------------

def poligono_regular(comp_lado,num_lados): 
    """
    Desenha um polígono regular.
    """
    angulo_viragem = 360 / num_lados
    # Desenha
    for i in range(num_lados): 
        turtle.forward(comp_lado) 
        turtle.right(angulo_viragem)
    turtle.hideturtle()

import math
def circunferencia(raio):
    """
    Desenha uma circunferência conhecido o raio.
    """
    perimetro = 2 * math.pi * raio
    tam_lado = perimetro / 360
    poligono_regular(tam_lado,360)

 
 
def circunferencia_var(raio, x_cor, y_cor):
    """
    Desenha uma circunferência conhecido o raio. Centro numa posição definida.
    """
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.pendown()
    perimetro = 2 * math.pi * raio
    tam_lado = perimetro / 360
    poligono_regular(tam_lado,360)  
    
# 2.5 -------------------------------------------------------------------------
 
def forma(nome,pontos):
    nova_forma = turtle.Shape('polygon',pontos)
    turtle.register_shape(nome,nova_forma)
    
if __name__ == '__main__':
    nome = 'oops'
    forma(nome,((0,0),(10,20),(5,20),(0,30),(-5,20), (-10,20)))
    turtle.shape(nome)
    turtle.fillcolor('red')
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(50)
    turtle.exitonclick()

# 2.6 -------------------------------------------------------------------------

def poly_circle(num_lados, comp_lado):
    """
    Desenha um polígono regular usando o comando circle.
    """
    turtle.circle(comp_lado,360,num_lados)
    turtle.hideturtle()

def poly_circle_var(num_lados, comp_lado):
    """
    Desenha um polígono regular usando o comando circle.
    """
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.width(3)
    turtle.circle(comp_lado,360,num_lados)
    turtle.end_fill()
    turtle.hideturtle()
    
# 2.7 -------------------------------------------------------------------------
def smiley(size):
    pass

def circunferencia(pos_x, pos_y,raio,cor,angulo=360):
    """pos_xz e pos_y são o centro!"""
    turtle.penup()
    turtle.goto(pos_x ,pos_y)
    turtle.fillcolor(cor)
    turtle.pendown()
    turtle.showturtle()
    turtle.begin_fill()
    turtle.circle(raio,angulo)
    turtle.end_fill()
    
    print(turtle.position())
    turtle.hideturtle()
    
    
if __name__ == '__main__':
    circunferencia(0,0,100,'white')
    circunferencia(-40,125,15,'black')
    circunferencia(40,125,15,'black')
    turtle.right(30)
    circunferencia(-55,50,100,'white',65)
    turtle.exitonclick()
# 2.8 -------------------------------------------------------------------------

import turtle

def avanca(tarta,dist, raio):
    """
    Mantém a tartaruga prisioneira num raio da origem.
    """
    x_cor = tarta.xcor()
    y_cor = tarta.ycor()
    for i in range(dist):
        if tarta.distance(x_cor,y_cor) > raio:
            angulo = tarta.towards(x_cor,y_cor)
            tarta.setheading(angulo)
        tarta.forward(1)
 
 
import random 

def avanca_2(tarta,dist, raio):
    """
    Mantém a tartaruga prisioneira num raio da origem.
    """
    x_cor = tarta.xcor()
    y_cor = tarta.ycor()
    for i in range(dist):
        if tarta.distance(x_cor,y_cor) > raio:
            angulo = tarta.towards(x_cor + random.randint(-25,25),x_cor + random.randint(-5,5))
            tarta.setheading(angulo)
        tarta.forward(1) 
 

       
tarta = turtle.Turtle()
avanca_2(tarta,10000,150)
turtle.exitonclick()
        
# 2.9 -------------------------------------------------------------------------
import turtle

def rasto(tarta, tamanho, passo, angulo, repete,cor_1, cor_2):
    janela = turtle.Screen()
    janela.bgcolor(cor_1)

    tarta.color(cor_2)
   
    tarta.penup()               
    for i in range(repete):
	tarta.stamp()             
	tamanho = tamanho + passo          
	tarta.forward(tamanho)       
	tarta.right(angulo)           
   
	janela.mainloop()
   
if __name__ == '__main__':
    tarta = turtle.Turtle()
    tarta.shape("turtle")   
    rasto(tarta,20,3,24,30,'blue','red')
    turtle.exitonclick()
    
# 2.10 -------------------------------------------------------------------------
def relogio(tarta, raio,cor_1, cor_2):
    janela = turtle.Screen()
    janela.bgcolor(cor_1)
    janela.title('Relógio')
    tarta.color(cor_2)
    tarta.penup() 
    tarta.setheading(60)
    for i in range(12):                     
	tarta.forward(raio)
	tarta.pendown()
	tarta.forward(30)
	tarta.penup()
	tarta.forward(30)
	tarta.pendown()
	tarta.write(i + 1, align='center', font=('Arial',20,'bold'))
	tarta.penup()
	tarta.goto(0,0)
	tarta.right(30)
    tarta.hideturtle()

   
    janela.mainloop()
   
if __name__ == '__main__':
    tarta = turtle.Turtle()  
    relogio(tarta,150,'lightgreen','red')
    turtle.exitonclick()
    
# 2.11 -------------------------------------------------------------------------

def triangulo(posx,posy,lado, orientacao):
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()
    turtle.setheading(orientacao)
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
        
def main(posx,posy,lado, orientacao):
    
    for i in range(6):
        triangulo(posx,posy,lado,orientacao)
        orientacao = orientacao + 60
        
if __name__ == '__main__':
    main(0,0,100,60)
    turtle.hideturtle()
    turtle.exitonclick()
    
# 2.12 -------------------------------------------------------------------------

def triangulo(posx,posy,lado, orientacao):
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()
    turtle.setheading(orientacao)
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
        
def rectangulo(posx,posy,lado1, lado2, orientacao):
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()
    turtle.setheading(orientacao)
    for i in range(2):
        turtle.forward(lado1)
        turtle.left(90)
        turtle.forward(lado2)
        turtle.left(90)        
        
if __name__ == '__main__':
    lado1 = 100
    lado2 = 30
    turtle.fillcolor('green')
    turtle.begin_fill()    
    rectangulo(0,0, lado1,lado1,0)
    turtle.end_fill()
    turtle.fillcolor('black')
    turtle.begin_fill()     
    rectangulo(1.9*lado1/3, 6*lado1/4,lado2/4,lado1/4,0)
    turtle.end_fill()
    turtle.fillcolor('red')
    turtle.begin_fill()
    triangulo(0,lado1,lado1,0)
    turtle.end_fill()
    
    turtle.hideturtle()
    turtle.exitonclick()
    
# 2.13 -------------------------------------------------------------------------

def esse(raio):
    turtle.setheading(270)
    turtle.circle(raio,180)
    turtle.setheading(270)
    turtle.circle(raio,-180)
    turtle.hideturtle()
    
    
if __name__ == '__main__':
    esse(30)
    turtle.exitonclick()
    
# 2.14 -------------------------------------------------------------------------

def quadrados_concentricos(num,comp_lado,distancia):
    """
    Desenha num quadrados concentricos.
    """
    x = turtle.xcor()
    y = turtle.ycor()
    for i in range(num):
	# Define cor
        r = random.random()
        g = random.random()
        b = random.random()
	# Desenha quadrado
        quadrado_cor(comp_lado+i*2*distancia, x - i*distancia, y + i*distancia,0,(r,g,b))

	
def quadrado_cor(lado,xcor,ycor,orient, cor):
    """
    Desenha um quadrado em que o lado, a posição inicial, a orientação inicial e a cor podem variar.
    """
    turtle.penup()
    turtle.goto(xcor,ycor)
    turtle.setheading(orient)
    turtle.pencolor(cor)
    turtle.pendown()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.hideturtle()
    
def quadrado(lado,xcor,ycor,orient):
    """
    Desenha um quadrado em que o lado, a posição inicial e a orientação inicial podem variar.
    """
    turtle.penup()
    turtle.goto(xcor,ycor)
    turtle.setheading(orient)    
    turtle.pendown()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.hideturtle()
    
# variante

def quadrados_concentricos_var(num,comp_lado,distancia, orienta):
    """
    Desenha num quadrados concentricos.
    """
    x = turtle.xcor()
    y = turtle.ycor()
    for i in range(num):
	# Define cor
        r = random.random()
        g = random.random()
        b = random.random()
	# Desenha quadrado
        quadrado_cor(comp_lado+i*2*distancia, x - i*distancia, y + i*distancia,orienta * i,(r,g,b))

# 2.15 -------------------------------------------------------------------------

def nautilus(n, lado, xcor,ycor, angulo):
    """
    Desenha n quadrados com lados e orientações variáveis.
    Desenha uma forma semelhante a um Nautilus.
    
    """
    for conta in range(n):
        quadrado(lado,xcor,ycor,angulo)
        lado = lado + 10
        angulo = angulo + 15
    turtle.hideturtle()
    


# 2.16 -------------------------------------------------------------------------
def circunferencia_cor(x,y,raio,cor):
    """
    Desenha circunferência colorida.
    """
    turtle.penup()
    turtle.setpos(x,y-raio)
    turtle.pendown()
    turtle.color(cor)
    turtle.circle(raio)
    turtle.penup()

def figura(raio,delta):
    """
    O símbolo dos jogos olímpicos, colorido.
    """
    turtle.width(5)
    turtle.colormode(255)
    circunferencia_cor(0,0,raio,'black')
    circunferencia_cor(2*raio+delta,0,raio,'red')
    circunferencia_cor(-2*raio-delta,0,raio,'blue')
    circunferencia_cor(raio+delta/2,-raio,raio,'green')
    circunferencia_cor(-raio-delta/2,-raio,raio,'orange')
    turtle.hideturtle()
    
# 2.17 -----------------------------------------------------------------------
def radioactividade(lado,x_cor,y_cor):
    fundo(lado,x_cor,y_cor,'yellow')
    vai_para(x_cor, y_cor)
    tres_sectores(0.8*lado/2)
    raio_2 = 0.2*lado/2
    circulo(raio_2,x_cor,y_cor,'black','yellow')
    turtle.hideturtle()

def vai_para(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def quad(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
	
def sector(raio, angulo,cor, orient):
    # Define orientação
    turtle.setheading(orient)
    # define cor 
    turtle.fillcolor(cor)
    turtle.pencolor(cor)
    # Desenha
    turtle.begin_fill()
    turtle.forward(raio)
    turtle.left(90)
    turtle.circle(raio, angulo)
    turtle.left(90)
    turtle.forward(raio)
    turtle.left(180-angulo)
    turtle.end_fill()
    
def tres_sectores(raio):
    """ 
    Desenha três sectores de círculo igualmente espaçados e com fundo preto.
    """
    sector(raio,60,'black',0)
    sector(raio,60,'black',120)
    sector(raio,60,'black',240)

def fundo(lado,x_cor,y_cor,cor):
    # Popsiciona
    turtle.penup()
    turtle.goto(x_cor - lado/2,y_cor - lado/2)
    turtle.pendown()
    # Prepara
    turtle.width(3)
    turtle.fillcolor(cor)
    turtle.begin_fill()
    # Desenha
    quad(lado)
    # Termina
    turtle.end_fill()
    
def circulo(raio,x_cor,y_cor,cor_1,cor_2):
    # Prepara
    vai_para(x_cor,y_cor+raio)
    turtle.right(60)
    turtle.fillcolor(cor_1)
    turtle.pencolor(cor_2)
    turtle.width(3)
    turtle.begin_fill()
    # Desenha
    turtle.circle(raio)
    turtle.end_fill()


# 2.18 -------------------------------------------------------------------------

def zen(raio,x_cor,y_cor,orient, cor_1,cor_2):
    """
    Desenha parte do símbolo zen.
    """
    vai_para(x_cor,y_cor)
    turtle.setheading(orient)
    turtle.pencolor(cor_1)
    turtle.fillcolor(cor_2)
    turtle.begin_fill()
    turtle.circle(raio,180)
    turtle.circle(raio/2,-180)
    turtle.setheading(orient + 180)
    turtle.circle(raio/2,180)    
    turtle.end_fill()

def yin_yang(raio):
    zen(raio,0,0,90,'black','white')
    zen(raio,-200,0,270,'black','black')
    circulo(raio/10,-55,0,'black','black')
    circulo(raio/10,-145,0,'white','white')
    turtle.hideturtle()    
    
    
# -- import turtle

def rasto(tarta, tamanho, passo, angulo, repete,cor_1, cor_2):
    janela = turtle.Screen()
    janela.bgcolor(cor_1)

    tarta.color(cor_2)
   
    tarta.penup()               
    for i in range(repete):
	tarta.stamp()             
	tamanho = tamanho + passo          
	tarta.forward(tamanho)       
	tarta.right(angulo)           
   
	janela.mainloop()
   
if __name__ == '__main__':
    tarta = turtle.Turtle()
    tarta.shape("turtle")   
    rasto(tarta,20,3,24,30,'blue','red')
    turtle.exitonclick()
    
if __name__ == '__main__':
    # 2.1
    #formas(16,100,164)
    # 2.2
    #random_walk_2(20,100)
    #random_walk_var(20,20)
    # 2.3
    #circunferencia(150)
    #circunferencia_var(50, 100,-50)
    # 2.4
    #poly_circle(8,50)
    #poly_circle_var(8,50)
    # 2.5
    #quadrados_concentricos(10,30,5)
    #quadrados_concentricos_var(10,30,5,4)
    # 2.6
    #nautilus(10, 20,0,0,10)
    # 2.c.1
    #figura(50,10)
    # 2.c.2
    #sector(150,60, 'red',45)
    #tres_sectores(150)
    #print(turtle.heading())
    #fundo(400, 0,0,'yellow')
    #radioactividade(400,0,0)
    #circulo(100,40,20,'black','yellow')
    # 2.c.3
    yin_yang(100)
    turtle.exitonclick()
        

