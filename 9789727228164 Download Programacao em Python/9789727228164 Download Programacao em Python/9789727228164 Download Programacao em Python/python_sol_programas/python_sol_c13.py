"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 13 : Programação Orientada aos Objectos

# 13.1

# 13.2
class Ponto:
    
    def __init__(self):
        self._x = 0
        self._y = 0
      
    def def_coordenadas(self, x, y):
        self._x = x
        self._y = y

# 13.3
class Ponto:
    
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

# 13.4

# 13.5

# 13.6

# 13.7

# 13.8

# 13.9

# 13.10

# 13.11

# 13.12

# 13.13

# 13.14
def move(self):
    from random import choice
    delta = [(-1,0),(1,0),(0,-1),(0,1)]
    x,y = self.obtem_posicao()
    d_x, d_y = choice(delta)
    n_x =  x + d_x
    n_y = y + d_y
    tamanho = self._mundo.obtem_tamanho()
    while not ((0 <= n_x < tamanho) and (0 <= n_y < tamanho) and self._mundo.celula_vazia(n_x,n_y)):
        d_x, d_y = choice(delta)
        n_x =  x + d_x
        n_y = y + d_y            
    
    self._mundo.limpa_registo(x,y)
    self.define_posicao(n_x,n_y)
    self._mundo.regista(self)  

# 13.15
def move(self):
    from random import choice
    delta = [(-1,0),(1,0),(0,-1),(0,1)]
    x,y = self.obtem_posicao()
    tamanho = self._mundo.obtem_tamanho()
    d_x, d_y = choice(delta)
    n_x =  (x + d_x) % tamanho
    n_y = (y + d_y) % tamanho

    if self._mundo.celula_vazia(n_x,n_y):
        self._mundo.limpa_registo(x,y)
        self.define_posicao(n_x,n_y)
        self._mundo.regista(self)   
    else:
        print('Célula Ocupada')
        

# 13.16
class Predador(Robot):
    
    def __init__(self, nome, mundo, pos_x=0, pos_y=0, energia=100):
        super().__init__(nome, mundo,pos_x, pos_y)
        self._energia = energia
        
    def move(self):
        from random import choice
        delta = [(-1,0),(1,0),(0,-1),(0,1)]
        x,y = self.obtem_posicao()
        tamanho = self.obtem_mundo().obtem_tamanho()        
        if self._energia <= 0: # morre??
            self._mundo.limpa_registo(x,y)          
            return
        # Procura uma presa
        for d_x, d_y in delta:
            n_x =  (x + d_x) % tamanho
            n_y =  (y + d_y) % tamanho
            conteudo = self._mundo.obtem_conteudo(n_x,n_y)
            if isinstance(conteudo,Presa):
                energia_mais = conteudo.obtem_energia()
                self._mundo.limpa_registo(x,y)
                self.define_posicao(n_x,n_y)
                self._mundo.regista(self)
                self._energia += energia_mais - 10
                break     
            else:
                continue
        else: # não encontrou presa
            # procura célula vazia
            for d_x,d_y in delta:
                n_x =  (x + d_x) % tamanho
                n_y =  (y + d_y) % tamanho               
                if self._mundo.celula_vazia(n_x,n_y):
                    self._mundo.limpa_registo(x,y)
                    self.define_posicao(n_x,n_y)
                    self._mundo.regista(self)
                    self._energia -= 10
                    break
                else:
                    continue
            # nem presa nem célula vazia
            else:
                print('movimento impossível')

            
                          
    
class Presa(Robot):
    def __init__(self, nome, mundo, pos_x=0, pos_y=0, energia=100):
        super().__init__(nome, mundo,pos_x, pos_y)
        self._energia = energia
           
        
    def move(self):
        vizinhos = [(0,-1),(1,0),(0,1),(-1,0)]
        tamanho = self.obtem_mundo().obtem_tamanho() 
        x,y = self.obtem_posicao()
        if self._energia <= 0: # morre??
            self._mundo.limpa_registo(x,y)
            return        
        for d_x, d_y in vizinhos:
            n_x =  (x + d_x) % tamanho
            n_y = (y + d_y) % tamanho
            tamanho = self._mundo.obtem_tamanho()
            conteudo = self._mundo.obtem_conteudo(n_x,n_y)
            if isinstance(conteudo,Predador):
                continue
            elif isinstance(conteudo,Presa):
                continue
            else:
                self._mundo.limpa_registo(x,y)
                self.define_posicao(n_x,n_y)
                self._mundo.regista(self)
                self._energia -= 10
                break     
        else:
            print('Movimento Impossível.')

# 13.17

# 13.18

# 13.19

# 13.20

