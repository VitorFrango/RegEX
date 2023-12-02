"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 14: Interfaces Gráficas com o Utilizador
"""
from tkinter import *
# 14.1
raiz = Tk()
raiz.title('Exemplo Básico')



quadro = Frame(raiz)
quadro.grid()

etiqueta1 = Label(quadro,text='Primeiro')
etiqueta1.grid(row=0,column=0)

nome_entrada_1=StringVar()
nome_entrada_1.set('')

nome_p = Entry(quadro,textvariable=nome_entrada_1)
nome_p.grid(row=0,column=1)

nome_entrada_2=StringVar()
nome_entrada_2.set('')

nome_s = Entry(quadro,textvariable=nome_entrada_2)
nome_s.grid(row=1,column=0)

etiqueta2 = Label(quadro,text='Segundo')
etiqueta2.grid(row=1,column=1)

raiz.mainloop()

# 14.2

raiz = Tk()
raiz.title('Botões')
raiz.geometry('200x50')

quadro = Frame(raiz)
quadro.pack()

botao1 = Button(quadro,text='OK',width=10)
botao1.pack(side=LEFT)

botao2 = Button(quadro,text='KO',width=10)
botao2.pack()
raiz.mainloop()

# 14.3

class Calcula_velocidade:
    
    def __init__(self,janela):
             
        self.entrada1=Entry(janela,width=25, bg='yellow')
        self.entrada1.pack(fill=BOTH)
  
        self.entrada2=Entry(janela,width=25, bg='yellow')
        self.entrada2.bind("<Return>",self.__calcula)
        self.entrada2.pack(fill=BOTH)        
        
        self.formula=Label(janela)
        self.formula.pack()
        
        self.butao=Button(janela,text='Limpa', command=self.__limpa)
        self.butao.pack()
        
        
    def __calcula(self,evento):
        # Tem protecção de erros.
        while True:
            valor1 = self.entrada1.get()
            valor2 = self.entrada2.get()
            try:
                res = float(valor1)/float(valor2)
            except NameError:
                self.formula.configure(text="*** ERRO ***: Entre de novo a formula sff. ")
                self.__limpa()
            else:
                break
        self.formula.configure(text="Resultado = " + str(res))
        
    def __limpa(self):
        self.entrada1.delete(0,END)
        self.entrada2.delete(0,END)
        self.formula.configure(text="")

        

if __name__ == '__main__':
    janela=Tk()
    janela.title("Calcula Velocidade")
    calc=Calcula_velocidade(janela)
    mainloop()
# 14.4

raiz = Tk()
raiz.title('Botões')
raiz.geometry('200x50')

quadro = Frame(raiz)
quadro.pack()

etiqueta = Label(quadro)
etiqueta.pack()

def _ok_press():
    etiqueta['fg'] = 'green'
    etiqueta['text'] = 'Botão OK pressionado'
    
def _ko_press():
    etiqueta['fg'] = 'red'
    etiqueta['text'] = 'Botão KO pressionado'
    
botao1 = Button(quadro,text='OK',width=10, command=_ok_press)
botao1.pack(side=LEFT)

botao2 = Button(quadro,text='KO',width=10,command=_ko_press)
botao2.pack()


raiz.mainloop()
# 14.5

import sys

from tkinter import *

class Quadro:
	
	def __init__(self):
		self.raiz=Frame(width=100,height=100,bg='light gray')
		self.raiz.pack(expand=YES,fill=BOTH)

		self.can=Canvas(self.raiz,bg='green')
		self.can.pack(expand=YES,fill=BOTH)
		
		self.entrada=Entry(self.raiz,fg='white',bg='blue')
		self.entrada.pack(expand=YES,fill=BOTH)
		
		self.etiqueta=Label(self.raiz,text='Valor',bg='yellow', fg='magenta')
		self.etiqueta.pack(expand=YES,fill=BOTH)
		
		self.lista=Listbox(self.raiz,bg='light blue')
		self.lista.pack()
		
		# Problemas com a cor dos botoes...
		self.botao=Button(self.raiz,text='Ola')
		self.botao.pack(expand=YES,fill=BOTH)
		self.botao.configure(bg='red')
		
		self.botaoradial=Radiobutton(self.raiz,text='Escolha')
		self.botaoradial.pack(expand=YES,fill=BOTH)
		
		self.botaocheck=Checkbutton(self.raiz,text='On')
		self.botaocheck.pack(expand=YES,fill=BOTH)
		
		self.botao=Button(self.raiz,text='Sair', command=self.raiz.quit)
		self.botao.pack(expand=YES,fill=BOTH)
		
		def quit(self):
			sys.exit()



		self.raiz.mainloop()


if __name__ == '__main__':
	Quadro()
 
# 14.6


raiz = Tk()
raiz.title('Vencimento')


quadro1 = Frame(raiz)
quadro1.grid()

horas = Label(quadro1,text='Horas')
horas.grid(row=0,column=0)

horas_ent = Entry(quadro1)
horas_ent.grid(row=0,column=1)

sal_h = Label(quadro1,text='Sal. Hora')
sal_h.grid(row=1,column=0)

sal_h_ent = Entry(quadro1)
sal_h_ent.grid(row=1,column=1)


quadro2 = Frame(raiz)
quadro2.grid()

bruto = Label(quadro2,text='V. Bruto')
bruto.grid(row=0,column=0)

bruto_var = StringVar()
bruto_var.set('0')

bruto_ent = Entry(quadro2, textvariable=bruto_var)
bruto_ent.grid(row=0,column=1)

descontos_var = StringVar()
descontos_var.set('0')

descontos = Label(quadro2,text='Descontos')
descontos.grid(row=1,column=0)

desc_ent = Entry(quadro2, textvariable=descontos_var)
desc_ent.grid(row=1,column=1)

liquido = Label(quadro2,text='V. Líquido')
liquido.grid(row=2,column=0)

liquido_var = StringVar()
liquido_var.set('0')

liquido_ent = Entry(quadro2, textvariable=liquido_var)
liquido_ent.grid(row=2,column=1)


def _calcula():
    hr = horas_ent.get()
    vh = sal_h_ent.get()
    bruto_var.set(str(float(hr)*float(vh)))
    descontos_var.set(str(float(bruto_var.get()) * 0.2))
    liquido_var.set(str(float(bruto_var.get()) - float(descontos_var.get())))


botao1 = Button(quadro2,text='Calcula',command=_calcula)
botao1.grid(row=3,column=0)

def _limpa():
    horas_ent.delete(0,END)
    sal_h_ent.delete(0,END)
    
    bruto_var.set('0')
    descontos_var.set('0')
    liquido_var.set('0')
    

botao2 = Button(quadro2,text='Limpa',command=_limpa)
botao2.grid(row=3,column=1)



mainloop()
# 14.7

def grelha(n,m):
    for y in range(n):
        for x in range(m):
            botao = Button(quadro,text="(%d,%d)" % (x,y))
            botao.grid(row=y,column=x)

raiz = Tk()
raiz.title('Usar Grid')

quadro = Frame(raiz)
quadro.grid()

grelha(4,7)

raiz.mainloop()

# 14.8

janela=Tk()
janela.title('Ficha Pessoal')
janela['bg']='light yellow'

# Texto
texto1=Label(janela,text='Nome',bg='light yellow')
texto2=Label(janela,text='Morada',bg='light yellow')
texto3=Label(janela,text='Cargo',bg='light yellow')

# Entry
entrada1=Entry(janela)
entrada2=Entry(janela)
entrada3=Entry(janela)
    
# Imagem
can=Canvas(janela,width=150,height=180, bg='white')
foto=PhotoImage(file='espadas.gif')
item=can.create_image(73,97,image=foto)

# Posiciona os widgets
texto1.grid(row=0, sticky=W)
texto2.grid(row=1,sticky=W)
texto3.grid(row=2,sticky=W)

entrada1.grid(row=0,column=1)
entrada2.grid(row=1,column=1)
entrada3.grid(row=2,column=1)

can.grid(row=0,column=2,rowspan=3,padx=10,pady=10)
    
janela.mainloop()

#  14.9

from random import randint

def quadrado(x,y,lado,cor='black'):
    """Cria um quadrado."""
    can.create_rectangle(x,y,x+lado,y+lado,fill=cor)



janela = Tk()
janela.title('Tabuleiro')
can = Canvas(janela,width=160,height=160)
can.pack(side=TOP,padx=5,pady=5)

def tabuleiro():
    can.delete(ALL)
    for lin in range(8):
        # desenha linha
        for col in range(8):
            if (lin + col)% 2 == 0:
                quadrado(20*lin,20*col,20,'gray')
            else:
                quadrado(20*lin,20*col,20,'black')
            
botao_1 = Button(janela,text='Tabuleiro',command=tabuleiro)
botao_1.pack(fill=BOTH)    


janela.mainloop()

#  14.10

from random import randint

def quadrado(x,y,lado,cor='black'):
	"""Cria um quadrado."""
	can.create_rectangle(x,y,x+lado,y+lado,fill=cor)

	
def tabuleiro():
	"""Desenha o tabuleiro. Quadrado a quadrado"""
	can.delete(ALL)
	for lin in range(8):
		# desenha linha
		for col in range(8):
			if (lin + col)% 2 == 0:
				quadrado(20*lin,20*col,20,'gray')
			else:
				quadrado(20*lin,20*col,20,'black')

def piao():
	""" Desenha um pião num quadrado de um tabuleiro."""
	x = randint(0,7)
	y = randint(0,7)
	can.create_oval(x*20,y*20,(x+1)*20,(y+1)*20,fill='white')



if __name__ == '__main__':
	janela = Tk()
	janela.title('Tabuleiro com Piões')
	can = Canvas(janela,width=160,height=160)
	can.pack(side=TOP,padx=5,pady=5)

	butao_1 = Button(janela,text='Tabuleiro',command=tabuleiro)
	butao_1.pack(side=LEFT,padx=3,pady=3)
	
	butao_2 = Button(janela,text='Pião',command=piao)
	butao_2.pack(side=RIGHT,padx=3,pady=3)

	janela.mainloop()

#  14.11

raiz= Tk()
raiz.title('Cores')

quadro1 = Frame(raiz)
quadro1.pack()

etiqueta1 = Label(quadro1, text='Cor')
etiqueta1.pack(side=LEFT)

cor = StringVar()
cor.set('gray')

entrada = Entry(quadro1, textvariable=cor)
entrada.pack(side=LEFT)

def muda_cor(evento):
	tela.create_rectangle(0,0,200,200,fill=cor.get())

entrada.bind('<Return>', muda_cor)
quadro2 = Frame(raiz)
quadro2.pack()

tela = Canvas(quadro2, height=200,width=200, bg=cor.get())
tela.pack(side=LEFT)


raiz.mainloop()
# 14.12

raiz = Tk()
raiz.title('Texto que se move...')
  
tela = Canvas(raiz,width=300,height=50)
tela.pack(fill=BOTH)

sg = IntVar()
sg.set(1)

def stop_and_go():
    global sg
    if sg.get() == 1:
        sg.set(0)
    else:
        sg.set(1)
    
stop_go = Button(raiz,text='STOP/GO',command=stop_and_go)
stop_go.pack()

largura_tela = 300
delta_x = 3
x = 0
tela.create_text(x,25, text='Ernesto Costa', tags='text')

while True:
    if sg.get() == 1:
        tela.move('text',delta_x, 0)
        tela.after(100)
        tela.update()
        if x < largura_tela:
            x += delta_x
        else:
            x = 0
            tela.delete('text')
            tela.create_text(x,25, text='Ernesto Costa', tags='text')	
    else:
        raiz.wait_variable(sg)

raiz.mainloop()

# 14.13

raiz = Tk()
raiz.title('Conversor Temperaturas')
raiz.grid()

quadro = Frame(raiz)
quadro.grid()

etiqueta = Label(quadro,text='Entre temperatura')
etiqueta.grid(row=0, columnspan=2)

temp = StringVar()
temp.set('')

entrada = Entry(quadro,textvariable=temp)
entrada.grid(row=1, columnspan=2)

def f_to_c():
    f = eval(temp.get())
    c = round((f-32)*5/9,2)
    temp.set(str(c))

botao1 = Button(quadro,text='F -> C', command=f_to_c)
botao1.grid(row=2,column=0)


def c_to_f():
    c = eval(temp.get())
    f = round((9/5 * c ) +32,2)
    temp.set(str(f))

botao2 = Button(quadro,text='C -> F', command=c_to_f)
botao2.grid(row=2,column=1)

raiz.mainloop()
# 14.14

# 14.15

#  14.16

# 14.17

# 14.18

# 14.19

class Calculadora(Frame):
	

	def __init__(self):
		Frame.__init__(self)
		self.pack(expand=YES,fill=BOTH)
		self.master.title('Calculadora Simples')
		self.master.iconname('calc')
		
		display=StringVar()
		Entry(self.master,textvariable=display).pack(side=LEFT,expand=YES,fill=BOTH)
		
		for key in ('123','456','789','-0.'):
			keyF=self.frame(self,TOP)
			for char in key:
				self.button(keyF,LEFT,char,
				lambda w=display, s='%s'% char: w.set(w.get() + s))
		
		opsF=self.frame(self,TOP)
		for char in '+-*/=':
			if char =='=':
				btn=self.button(opsF,LEFT,char)
				btn.bind('<ButtonRelease-1>',
				lambda e, s=self,w=display: s.calc(w))
			else:
				btn=self.button(opsF,LEFT,char,
				lambda w=display, c=char: w.set(w.get()+c))
		clearF=self.frame(self,BOTTOM)
		self.button(clearF,LEFT,'Limpa',lambda w=display: w.set(''))
		
	def calc(self,display):
		try:
			display.set(eval(display.get()))
		except ValueError:
			display.set('ERRO')
			
	@staticmethod		
	def frame(root,side):
		w=Frame(root)
		w.pack(side=side,expand=YES,fill=BOTH)
		return w

	@staticmethod
	def button(root,side,text,command=None):
		w=Button(root,text=text,command=command)
		w.pack(side=side,expand=YES,fill=BOTH)
		return w
	


if __name__ == '__main__':
    Calculadora()
    mainloop()
    
# 14.20

# 14.21

# Solução de Paulo Marques

from tkinter import Canvas, Frame
import time
import sys

#-----------------------------------------------------------------------------

def hanoi(n, a, b, tmp, move=(lambda a, b: sys.stdout.write('Moving 1 disk from %s to %s\n' % (a, b)))):
    """Hanoi Tower algorithm. Moves <n> disks from <a> to <b> using <tmp> as auxiliary. 
       (It doesn't really matter what <a>, <b> and <tmp> are. It can be numbers, strings, etc.)
       <move> represents a callback funcion. Everytime a move is made this function is invoked as
       move(from, to). <from> and <to> correspond to either <a>, <b> or <tmp>. If no <move> is 
       provided, hanoi() prints out to the console the list of moves."""

    if n==0:
        return

    hanoi(n-1, a, tmp, b, move)
    move(a, b)
    hanoi(n-1, tmp, b, a, move)

#-----------------------------------------------------------------------------

class Hanoi(Frame):
    """Class that implements the programs GUI"""

    delay  = 0.8        # Delay between moves
    width  = 500       # Window width
    height = 200        # Window height
    sep    = 30         # Major separation among items
    dx     = 5          # Small separation among items

    #-------------------------------------------------------------------------
    def __init__(self, n_disks):
        """Class constructor. Receives number of disks as parameter."""

        Frame.__init__(self)
        self.n_disks = n_disks
        self.bars = [ [], [], [] ]

        self.createGUI()

    #-------------------------------------------------------------------------

    def createGUI(self):
        """Initializes the GUI, creating the floor, pegs and disks."""

        # Create main canvas
        self.master.title('Torres de Hanói')
        self.canvas = Canvas(self, width=Hanoi.width, height=Hanoi.height)
        self.canvas.pack()
        self.pack()

        # Object sizes        
        floor_size = Hanoi.width-2*Hanoi.dx
        self.disk_height = (Hanoi.height - 4*Hanoi.sep) / self.n_disks
        self.disk_width = (floor_size - 4*Hanoi.dx) / 3

        # Shorthand notation
        disk_w = self.disk_width
        disk_h = self.disk_height
        width = Hanoi.width
        height = Hanoi.height
        sep = Hanoi.sep
        dx = Hanoi.dx

        # Draw floor
        self.canvas.create_rectangle(dx, height-sep, width-dx, height,
                                     fill='brown', outline='brown')

        # draw bars
        bar_pos = [ 2*dx + disk_w/2 + (disk_w+dx)*i for i in range(0,3) ]
        for x in bar_pos:
            self.canvas.create_rectangle(x-dx, sep, x+dx, height-sep-1, fill='black')

        # create disks
        for i in range(self.n_disks):
            disk = self.canvas.create_rectangle(2*dx + 4*dx*i, height-sep-1-disk_h*i,
                                                2*dx + disk_w - 4*dx*i, height-sep-1-disk_h*(i+1),
                                                fill='blue')
            self.bars[0].append(disk)

        self.update()

    #-------------------------------------------------------------------------

    def moveDisk(self, origin, dest):
        """Moves a disk between an origin peg and a destination peg. Pegs are
           numbered from 0 to 2."""

        # Move the disk in terms of data structures
        disk = self.bars[origin].pop()
        self.bars[dest].append(disk)

        # Move the disk on the GUI
        dx = (dest-origin) * (self.disk_width + Hanoi.dx)
        dy = ( len(self.bars[origin])-len(self.bars[dest])+1 ) * self.disk_height

        self.canvas.move(disk, dx, dy)
        self.canvas.update()
        time.sleep(Hanoi.delay)

    def run(self):
        """Main method of the GUI, which starts the simulation."""

        hanoi(self.n_disks, 0, 2, 1, self.moveDisk)

#-----------------------------------------------------------------------------

if __name__ == "__main__":
    #hanoi(4,'A','B','C')
    gui = Hanoi(4)
    time.sleep(1)
    gui.run()
# 14.22

from random import *
from tkinter import *


class CA_1D:
	
	def __init__(self, rule,generations=75,grid_size=150):
		self._result = None
		self._decompose(rule)
		self._generations = generations
		self._grid_size = grid_size
	
	def run(self):
		g0 = [0]*(self._grid_size//2) + [1] + [0]*(self._grid_size//2)
		result = [g0]
		last = g0
		for i in range(self._generations):
			left_elem = self._apply_rule(last[self._grid_size], last[0], last[1])
			right_elem = self._apply_rule(last[self._grid_size - 1], last[self._grid_size], last[0])
			other_elem = [self._apply_rule(last[i-1], last[i], last[i+1]) for i in range(1, self._grid_size)]
			
			new= [left_elem] + other_elem + [right_elem]
			
			result.append(new)
			last = new
			
		self._result = result
		return result
	
	def _apply_rule(self, left, center, right):
		return self._rule_template[ left*4 + center*2 + right ]
		
		
	def _decompose(self, n):
		self._rule_template = []
		for i in range(8):
			r = n%2
			n = n//2
			self._rule_template.append(r)

class Display:
	def __init__(self,autocel):
		self._result = autocel._result
		self._grid_size = autocel._grid_size
		self._generations = autocel._generations
	
	
	def draw(self):
		if self._result == None:
			print("Ainda nada para ver...")
			return
		d = 2
		width  = d*(self._grid_size + 1)
		height = d*(self._generations + 1)
		canvas = Canvas(width=width, height=height, bg='white')
		canvas.master.title('Simulador de um Autómato Celular')
		canvas.pack(side=LEFT,expand=YES,fill=BOTH)		
		x = 2
		y = 2		
		for line in self._result:
			for block in line:
				if block==0:
					canvas.create_rectangle(x, y, x+d, y+d, fill='white', width=1)
				else:
					canvas.create_rectangle(x, y, x+d, y+d, fill='black', width=1)
				x =  x + d			
			y= y + d
			x = 2


class MyApp():
	def __init__(self,rule,generations,grid_size):
		self._ca = CA_1D(rule,generations,grid_size)
		self._ca.run()
		self._d = Display(self._ca)
		self._d.draw()
		

if __name__ == '__main__': 
	# Número da Regra, Gerações, Tamanho da Grelha
	app1=MyApp(30,75,150)
	#app2=MyApp(31,75,150)
	mainloop()

# 14.23

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:34:58 2015

@author: ernestojfcosta
"""

from tkinter import *
from math import *

# Sistema L
class SistemaL:
	"""Um sistema L tem um axioma, regras e uma forma sentencial."""
	# construtor
	def __init__(self,axioma,regras,frase=None):
		self._axioma=axioma
		self._regras = regras
		if frase:
			self._frase=frase
		else:
			self._frase=axioma
	
	# Selectores
	def obtem_axioma(self):
		return self._axioma
		
	def obtem_regras(self):
		return self._regras
		
	def obtem_frase(self):
		return self._frase
		
	# Modificadores
	def reescreve(self):
		self._frase= ''.join([self._regras.get(ch,ch) for ch in self._frase])
		
	# Auxiliares
	def show(self):
		print('Axioma: ', self._axioma)
		print('Regras: ', self._regras)
		print('Frase: ', self._frase)
		
		
		
class Tartaruga:
	
	def __init__(self,posx=300,posy=300,heading=-90,estado='up',tamanho=5,angulo=90):
		self._posx = posx
		self._posy = posy
		self._heading = heading
		self._estado = estado
		self._tamanho = tamanho
		self._angulo = angulo
		
		self._pilha = []
		
		self._dicio={'F':'self.tart_down();self.move(ecran);self.tart_up()',
		'B':'pass','f':'self.tart_up();self.move(ecran)',
		'+':'self.rodad()','-':'self.rodae()',
		'[':'self.guarda_estado()',']':'self.restaura_estado()' ,
		'D':'self.tart_down();self.move(ecran);self.rodad();self.move(ecran);self.tart_up()',
		'E':'self.tart_down();self.move(ecran);self.rodae();self.move(ecran);self.tart_up()'}

	# Comandos da tartaruga
	# Movimento	
	def move(self,ecran):
		posxx = self._posx + self._tamanho * cos(radians(self._heading))
		posyy = self._posy + self._tamanho * sin(radians(self._heading))
		if self._estado == 'up':
			self._posx = posxx
			self._posy = posyy
		else:
			ecran.create_line(self._posx,self._posy,posxx,posyy)	
			self._posx = posxx
			self._posy = posyy
			
	# roda a tartaruga
	def rodad(self):
		self._heading += self._angulo
		
	def rodae(self):
		self._heading -= self._angulo
	
	# controla caneta	
	def tart_up(self):
		self._estado='up'
		
	def tart_down(self):
		self._estado='down'
		
	# Gestao do estado da pilha
	def guarda_estado(self):
		posicx = self._posx
		posicy = self._posy
		heading =self._heading
		self._pilha=[[posicx,posicy,heading]] + self._pilha

	def restaura_estado(self):
		posicx,posicy,heading = self._pilha[0]
		self._posx = posicx
		self._posy = posicy
		self._heading = heading
		self._pilha = self._pilha[1:]
		
	def obtem_codigo(self,simbolo):
		return self._dicio[simbolo]
	
	def executa_codigo(self,codigo,ecran):
		exec(codigo)
	
		
class Ecran(Frame):

	def __init__(self):
		super().__init__()
		self.pack(expand=1,fill=BOTH)
		self.master.title('Simulador de Sistemas de Lindenmayer')
		
		self._ax = Label(self, text='Axioma')
		self._ax.pack()
		self._var_ax=StringVar()
		self._ax_ent = Entry(self,textvariable=self._var_ax)
		self._ax_ent.pack()
		
		self._regras = Label(self, text='Regras')
		self._regras.pack()
		self._var_regras=StringVar()
		self._regras_ent = Entry(self,textvariable=self._var_regras)
		self._regras_ent.pack()
		
		self._frase = Label(self, text='Frase')
		self._frase.pack()
		self._var_frase=StringVar()
		self._frase_ent = Entry(self,textvariable=self._var_frase, width=50)
		self._frase_ent.pack()
		

		self._tela = Canvas(self,width=600,height=600,bg='light yellow')
		self._tela.pack(expand=YES,fill=BOTH)
		
	def mostra_axioma(self,axioma):
		self._var_ax.set(axioma)
		
	def mostra_regras(self, regras):
		self._var_regras.set(regras)
		
	def mostra_frase(self, frase):
		self._var_frase.set(frase)
			
	def create_line(self, x1,y1,x2,y2):
		self._tela.create_line(x1,y1,x2,y2)
	
	
class Aplicacao:
	
	def __init__(self,axioma,regras,frase, passos):
		self._sl = SistemaL(axioma,regras,frase)
		self._ecran = Ecran()
		self._tartaruga = Tartaruga()
		self._passos = passos
		
		self._ecran.mostra_axioma(self._sl.obtem_axioma())
		self._ecran.mostra_regras(self._sl.obtem_regras())
		
	def run(self):
		# Passo 1: Executa o sistema L
		for i in range(self._passos):
			self._sl.reescreve()
		self._frase = self._sl.obtem_frase()
		self._ecran.mostra_frase(self._sl.obtem_frase())
		
		for simbolo in self._frase:
			# Passo 2: traduz comando em codigo
			self._codigo = self._tartaruga.obtem_codigo(simbolo)
			# Passo 3: Executa codigo
			self._tartaruga.executa_codigo(self._codigo,self._ecran)
		mainloop()
				
if __name__ == '__main__':
     axioma ='E'
     regras = {'E':'E+D+','D':'-E-D'}
     frase = None
     passos = 10
     aplica = Aplicacao(axioma, regras,frase, passos)
     aplica.run()

