"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 7: Ficheiros


# 7.1 

# Solução Geral
def cria_ficheiro71(nome_fich, mensagem):
   """
   Cria um ficheiro com um texto. Versão simples.
   """
   conteudo = open(nome_fich,'w')
   conteudo.write(mensagem)
   conteudo.close()

def cria_ficheiro71b(nome_fich, mensagem):
   """
   Cria um ficheiro com um texto. Versão genérica.
   """
   conteudo = open(nome_fich,'w',encoding='utf-8')
   conteudo.write(mensagem)
   conteudo.close()
   
frase = "Acabei de criar o meu primeiro ficheiro em Python.\n"


# 7.2 

# Solução Geral
def ler_seleccao(nome_fich, pos_inicial, num_caract):
   """
   Ler num_caract caracteres  de um ficheiro a partir pos_inicial. Ficheiros ASCII.
   """
   conteudo = open(nome_fich,'r')
   conteudo.seek(pos_inicial)
   cont = conteudo.read(num_caract)
   conteudo.close()
   return cont


def ler_seleccao_b(nome_fich, pos_inicial, num_caract):
   """
   Ler num_caract caracteres  de um ficheiro a partir pos_inicial. Geral.
   """
   conteudo = open(nome_fich,'r', encoding='utf-8')
   conteudo.read(pos_inicial)
   cont = conteudo.read(num_caract)
   conteudo.close()
   return cont

# 7.3 

# Solução geral
def nova_linha(nome_fich, texto):
   """
   Adiciona uma linha no final ao ficheiro
   """
   conteudo = open(nome_fich,'r+')
   conteudo.seek(0,2)
   conteudo.write(texto)
   conteudo.close()
   
def nova_linha_b(nome_fich, texto):
   """
   Adiciona uma linha no final ao ficheiro
   """
   conteudo = open(nome_fich,'a')
   conteudo.write(texto)
   conteudo.close()
   
def nova_linha_c(nome_fich, texto):
   """
   Adiciona uma linha no final ao ficheiro. Geral
   """
   conteudo = open(nome_fich,'a', encoding='utf-8')
   conteudo.write(texto)
   conteudo.close()

# 7.4 

# Simples: só números separados são reconhecidos
def identifica_numeros(nome_fich):
   """
   Identifica se um ficheiro tem números, e retorna o resultado numa lista
   """
   f_in = open(nome_fich,'r')
   resultado =[]
   texto = f_in.read()
   texto_pal = texto.split()
   for pal in texto_pal:
      if pal.isdigit():
         resultado.append(int(pal))
   f_in.close()
   return resultado

# Básico
def identifica_numeros_b(nome_fich):
   """
   Identifica se um ficheiro tem digitos, e retorna o resultado numa lista
   """
   resultado =[]
   linhas = []
   conteudo = open(nome_fich,'r')
   linhas = conteudo.readlines()
   for i in range(len(linhas)):
      uma_linha = linhas[i].strip().split()
      for j in range(len(uma_linha)):
         if uma_linha[j].isdigit():
            resultado.append(int(uma_linha[j]))
   return resultado

# Mais geral
def identifica_numeros_c(ficheiro):
   """
   Identifica os números  num ficheiro e devolve-os numa lista.
   """
   lista_numeros = []
   f_in = open(ficheiro,'r')
   caracter = f_in.read(1)
   while caracter !='':
      num = ''
      while (not caracter.isdigit()) and (caracter != ''):
         caracter = f_in.read(1)
      if caracter != '':
         num = caracter
         caracter = f_in.read(1)
         while caracter.isdigit():
            num = num + caracter
            caracter = f_in.read(1)
         lista_numeros.append(int(num))
   f_in.close()
   return lista_numeros

# 7.5 
#import matplotlib.pyplot as plt

def temp_max_min(f_ent):
   """
   Lê temperaturas mensais de várias cidades, calcula valores máximos e mínimos.
   Mostra o resultado num gráfico.
   """
   # lê dados
   f_in = open(f_ent)
   dados = []
   cidade = f_in.readline()
   while cidade != '':
      dados.append([float(valor) for valor in cidade[:-1].split()])
      cidade = f_in.readline()
   # calcula máximo e mínimo
   lista_valores_mes = list(zip(*dados))
   maximos = [max(mes) for mes in lista_valores_mes]
   minimos = [min(mes) for mes in lista_valores_mes]
   # mostra resultados
   plt.figure(1)
   plt.plot(maximos)
   plt.plot(minimos)
   plt.show()

# Gráfico mais sofisticado...
def temp_max_min_b(f_ent):
   """
   Lê temperaturas mensais de várias cidades, calcula valores máximos e mínimos.
   Mostra o resultado num gráfico.
   """
   # lê dados
   f_in = open(f_ent)
   dados = []
   cidade = f_in.readline()
   while cidade != '':
      dados.append([float(valor) for valor in cidade[:-1].split()])
      cidade = f_in.readline()
   # calcula máximo e mínimo
   lista_valores_mes = list(zip(*dados))
   maximos = [max(mes) for mes in lista_valores_mes]
   minimos = [min(mes) for mes in lista_valores_mes]
   # mostra resultados
   plt.figure(1)
   absissa = range(len(maximos))
   plt.xlabel('Meses')
   plt.ylabel('Temperaturas')
   #plt.title(r'$\mathrm{M\acute aximo\,e\,M\acute inimo}$')
   plt.title('Máximo e Mínimo')
   plt.plot(absissa,maximos,'r-o', label='Máximos')
   plt.plot(absissa, minimos,'b-^', label='Mínimos')
   plt.legend(loc='best')
   plt.show()


def temp_max_min_c(f_ent):
   """
   Lê temperaturas mensais de várias cidades, calcula valores máximos e mínimos.
   Mostra o resultado num gráfico. Prevê linhas vazias!
   """
   # lê dados
   f_in = open(f_ent)
   dados = []
   for cidade in f_in:
      if len(cidade)== 1: #linha vazia...
         continue
      else:
         dados.append([float(valor) for valor in cidade[:-1].split()])
   # calcula máximo e mínimo
   lista_valores_mes = list(zip(*dados))
   maximos = [max(mes) for mes in lista_valores_mes]
   minimos = [min(mes) for mes in lista_valores_mes]
   # mostra resultados
   plt.figure(1)
   absissa = range(len(maximos))
   plt.xlabel('Meses')
   plt.ylabel('Temperaturas')
   #plt.title(r'$\mathrm{M\acute aximo\,e\,M\acute inimo}$')
   plt.title('Máximo e Mínimo')
   plt.plot(absissa,maximos,'r-o', label='Máximos')
   plt.plot(absissa, minimos,'b-^', label='Mínimos')
   plt.legend(loc='best')
   plt.show()
   
# 7.6 

def copia_ficheiros(fich_origem, fich_destino):
   """
   Copia ficheiros
   """
   conteudo_o = open(fich_origem,'r',encoding='utf-8')
   conteudo_d = open(fich_destino,'w',encoding='utf-8')

   linha = conteudo_o.readline()

   while (linha !=''):
      conteudo_d.write(linha)
      linha = conteudo_o.readline()

   conteudo_o.close()
   conteudo_d.close()
   
def copia_ficheiros_b(fich_origem, fich_destino):
   """
   Copia ficheiros
   """
   conteudo_o = open(fich_origem,'r',encoding='utf-8')
   conteudo_d = open(fich_destino,'w',encoding='utf-8')
   for linha in conteudo_o:
      conteudo_d.write(linha)
   conteudo_o.close()
   conteudo_d.close()
   
def copia_bin(fich_origem, fich_destino):
   """
   Copia ficheiros
   """
   conteudo_o = open(fich_origem,'rb')
   conteudo_d = open(fich_destino,'wb')
   dados = conteudo_o.read()
   conteudo_d.write(dados)
   conteudo_o.close()
   conteudo_d.close()   

# 7.7 
#import turtle
import random

def gera_pares(n):
   res = [(random.randint(1,6), random.randint(1,6)) for i in range(n)]
   return res

def cria_ficheiro(nome,dados):
   f_out = open(nome,'w')
   for par in dados:
      linha = str(par[0]) + '\t' + str(par[1]) + '\n'
      f_out.write(linha)
   f_out.close()
    
def le_ficheiro_77(nome):
   f_in = open(nome,'r')
   dados = []
   for linha in f_in:
      x,y = linha[:-1].split()
      dados.append([int(x), int(y)])     
   f_in.close()
   return dados


def visualiza(tartaruga,dados):
   tartaruga.up()
   tartaruga.goto(dados[0])
   tartaruga.down()
   for ponto in dados[1:]:
      tartaruga.goto(ponto)      
   turtle.hideturtle()
   
def main77(ficheiro, num_pontos):
   # Sistema de Coordenadas
   turtle.setworldcoordinates(0,0,7,7)
   # Formação dos dados
   pares = gera_pares(num_pontos)
   cria_ficheiro(ficheiro,pares)
   # Leitura dos dados
   pares_tartaruga = le_ficheiro_77(ficheiro)
   # Visualização
   tartaruga= turtle.Turtle()
   visualiza(tartaruga,pares_tartaruga)
   turtle.exitonclick()
   
   

# 7.8 

# --- comum às duas versões

def le_ficheiro_78(nome):
   """Lê e transforma os pares na soma."""
   f_in = open(nome,'r')
   dados = []
   linha =  f_in.readline()
   while linha !='' and linha != '\n':
      x,y = linha[:-1].split()
      dados.append((int(x),int(y)))
      linha = f_in.readline()        
   f_in.close()
   return dados


def analisa_frequencias_78(dados):
   """Constrói dicionário de frequências."""
   frequencias={}
   for valor in dados:
      frequencias[valor] = frequencias.get(valor,0)+1
   return frequencias

# ----- vesão matplotlib

import matplotlib.pyplot as plt

def visualiza_frequencias_plt_78(frequencias):
   """Recurso a matplotlib."""

   chaves = list(frequencias.keys())
   x = list(range(len(chaves)))
   etiquetas = [str(elem) for elem in chaves]        
   valores = list(frequencias.values())
   plt.xticks(x,etiquetas, rotation=45)
   plt.bar(x,valores)
   plt.title('Gráfico de Ocorrências')
   plt.xlabel('Números')
   plt.ylabel('Ocorrências')
   plt.show()
    

def main78_plt(ficheiro):
   # Leitura dos dados
   pares = le_ficheiro_78(ficheiro)
   # Análise de frequências
   frequencias = analisa_frequencias_78(pares)
   # Visualização de frequências
   visualiza_frequencias_plt_78(frequencias)
   
# ----- versão turtle
import turtle

def desenha_coluna(numero, altura):
   x=(numero*16) - 200 # para começar no inicio do eixo
   y=altura * 20
    
   # escrever número no eixo
   turtle.up()
   turtle.goto(x+5,-20)
   turtle.down()
   turtle.write(str(numero), move=False, align='left', font=('Arial', 10, 'bold'))
    
   #desenhar coluna
   turtle.up()
   turtle.goto(x+2,0)
   turtle.down()
   turtle.goto(x+2,y)
   turtle.goto(x+14,y)
   turtle.goto(x+14,0)
    
   # escrever número da frequência
   turtle.up()
   turtle.goto(x+5,y+5)
   turtle.down()
   turtle.write(str(altura), move=False, align='left', font=('Arial', 10, 'normal'))
    

def visualiza_frequencias_turtle_78(frequencias):
    # desenhar eixo dos x
   turtle.up()
   turtle.goto(-200,0)
   turtle.down()
   turtle.goto(10*len(frequencias),0)
   # desenhar frequências
   
   for i,ch in enumerate(frequencias):
      desenha_coluna(i,frequencias.get(ch,0))
      
   turtle.hideturtle()

def main78_turtle(ficheiro):
   # Leitura dos dados
   pares = le_ficheiro_78(ficheiro)
   # Análise de frequências
   frequencias = analisa_frequencias_78(pares)
   # Visualização de frequências
   visualiza_frequencias_turtle_78(frequencias)
   turtle.exitonclick()


# 7.9 

# --- comum às duas versões

def le_ficheiro_79(nome):
   """Lê e transforma os pares na soma."""
   f_in = open(nome,'r')
   dados = []
   linha =  f_in.readline()
   while linha !='' and linha != '\n':
      x,y = linha[:-1].split()
      total = int(x)+int(y)
      dados.append(total)
      linha = f_in.readline()        
   f_in.close()
   return dados


def analisa_frequencias_79(dados):
   """Constrói dicionário de frequências."""
   total_num = len(dados)
   frequencias={}
   for valor in dados:
      frequencias[valor] = frequencias.get(valor,0)+1
   for ch in frequencias:
      frequencias[ch] /= total_num
   return frequencias

# ----- versão matplotlib
#import matplotlib.pyplot as plt

def visualiza_frequencias_plt_79(frequencias):
   """Recurso a matplotlib."""
   for ch in frequencias:
      plt.bar(ch,frequencias[ch])
   plt.xticks(list(frequencias.keys()))
   plt.title('Gráfico de Frequências')
   plt.xlabel('Números')
   plt.ylabel('Frequência')
   plt.show()
    

      
def main79_plt(ficheiro):
   # Leitura dos dados
   pares = le_ficheiro_79(ficheiro)
   # Análise de frequências
   frequencias = analisa_frequencias_79(pares)
   # Visualização de frequências
   visualiza_frequencias_plt_79(frequencias)

# ----- versão  turtle
#import turtle

def desenha_coluna_79(tartaruga, numero, altura):
   x=(numero-1)*20 # para começar no inicio do eixo
   y=altura *500
    
   # escrever número no eixo
   tartaruga.up()
   tartaruga.goto(x+5,-20)
   tartaruga.down()
   tartaruga.write(str(numero), move=False, align='left', font=('Arial', 10, 'bold'))
    
   #desenhar coluna
   tartaruga.up()
   tartaruga.goto(x+2,0)
   tartaruga.down()
   tartaruga.goto(x+2,y)
   tartaruga.goto(x+18,y)
   tartaruga.goto(x+18,0)
    
   # escrever número da frequência
   tartaruga.up()
   tartaruga.goto(x+5,y+5)
   tartaruga.down()
   tartaruga.write(str(altura), move=False, align='left', font=('Arial', 10, 'normal'))
    

def visualiza_frequencias_turtle(tartaruga,frequencias):
    # desenhar eixo dos x
   tartaruga.up()
   tartaruga.goto(0,0)
   tartaruga.down()
   tartaruga.goto(20*12,0)
    
   # desenhar frequências
   for i in range(2,13):
      desenha_coluna_79(tartaruga,i,frequencias.get(i,0))      
   tartaruga.hideturtle()

def main79_turtle(ficheiro):
   # Leitura dos dados
   pares = le_ficheiro_79(ficheiro)
   # Análise de frequências
   frequencias=analisa_frequencias_79(pares)
   print(frequencias)
   # Visualização de frequências
   tartaruga= turtle.Turtle()
   visualiza_frequencias_turtle(tartaruga,frequencias)
   turtle.exitonclick()
   


# 7.10 

import matplotlib.pyplot as plt
    
def le_ficheiro710(nome):
   f_in = open(nome,'r', encoding='utf-8')
   dados = f_in.read()
   dados = dados.lower()
   f_in.close()
   return dados

def analisa_frequencias710(dados):
   sinais = [' ', '.', ',','!','?','\n','-','_','(',')','1','2','3','4','5','6','7','8','9','0']
   especiais = {'é':'e','á':'a','ç':'c','ó':'o','ã':'a', 'í':'i','ê':'e','ô':'o','ò':'o','õ':'o'}
   frequencias={}
   for caractere in dados:
      if caractere not in sinais:
         if caractere not in especiais:
            frequencias[caractere]=frequencias.get(caractere,0)+1
         else:
            frequencias[especiais[caractere]] = frequencias.get(especiais[caractere],0)+1   
   return frequencias
           

def visualiza_frequencias710(ocorrencias):
   """ A partir do dicionário das ocorrências produz o plot
   das percentagens.
   """
   lista_ocorrencias = list(ocorrencias.items())
   lista_ocorrencias.sort()
   total = sum(list(ocorrencias.values()))
   
   
   nomes = [valor[0] for valor in lista_ocorrencias]
   percentagem = [100* valor[1]/total for valor in lista_ocorrencias]
   plt.title('Frequência de Ocorrências')
   plt.ylabel('Percentagem')
   plt.xlabel('Caracteres')
   plt.grid(True)
   plt.xticks(range(len(nomes)), nomes)
   plt.plot(percentagem)
   plt.show()
    
    
    
def main710(ficheiro):
   # Leitura dos dados
   dados = le_ficheiro710(ficheiro)
   # Frequências
   frequencias = analisa_frequencias710(dados)
   # Visualização de frequências
   visualiza_frequencias710(frequencias)
   
# 7.11 

def main711(ficheiro,transacao,vendedor):
   """ Actualiza um ficheiro de vendas."""
   # Abre ficheiro  e posiciona-se
   with open(ficheiro,'a') as f_in:  
      # Actualiza
      nova_transac = '%d,%s,%d,%s,%.2f\n' % transacao
      f_in.write(nova_transac)
      f_in.close()
      # Mostra
      print('Venda a dinheiro nº %d   ' % transacao[0])
      print('*' * 30)
      dados = transacao[1:] + (vendedor,)
      print('Empresa: %s\nN.C.: %d\nData:  %s\nValor: %.2f Euros\nVendedor: %s' % dados)
   


 
# 7.12 


def freq_inteiros(ficheiro):
   """ Constrói um dicionário com a frequência dos inteiros."""
   f_in = open(ficheiro)
   dicio = dict()
   linha = f_in.readline()
   while linha != '':
      linha = linha[:-1].split()
      for i in range(len(linha)):
         dicio[int(linha[i])] = dicio.get(int(linha[i]), 0) + 1
      linha = f_in.readline()
   f_in.close()
   return dicio
   
   
# 7.13 

def main713(ficheiro, dicio_profs, dicio_estados):
   """ 
   A partir de  um ficheiro com dados pessoais codificados constrói um novo baseado
   num dicionário de códigos de profissões e num dicionário de códigos de estados civis.
   """
   with open(ficheiro, 'r',encoding='utf-8') as f_in:
      f_out = open(prefixo+'pessoas.txt','w', encoding='utf-8')
      linha = f_in.readline()
      while linha !='':
         linha = linha[:-1].split(',')
         nova_linha = linha[0]+','+linha[1]+','+str(dicio_profs[int(linha[2])])+','+ str(dicio_estados[int(linha[3])])+'\n'
         f_out.write(nova_linha)
         linha = f_in.readline()
      f_out.close()
      f_in.close()
   
                  
   
  
# 7.14

import math

def correlacao(fich_1, fich_2, numero):
   """ Calcula o coeficiente de correlação entre dados de duas acções."""
   dados_fich_1 = busca_dados(fich_1, numero)
   dados_fich_2 = busca_dados(fich_2, numero)   
   valor = pearson(dados_fich_1, dados_fich_2)
   return valor

def busca_dados(fich,numero):
   """Retira os dados da cotação de fecho para o formato dado."""
   fich_ficheiro = open(fich, 'r')
   dados_ficheiro = fich_ficheiro.readlines()[1:numero]
   fich_ficheiro.close()
   # retira dados
   dados_ficheiro_fecho = []
   for linha in dados_ficheiro:
      dados_ficheiro_fecho.append(float(linha.split(',')[4]))
   return dados_ficheiro_fecho

def pearson(lista_a, lista_b):
   """ Calcula o coeficiente de correlação entre duas listas de valores."""
   media_a = media(lista_a)
   media_b = media(lista_b)    
   desvio_a = desvio_padrao(lista_a)
   desvio_b = desvio_padrao(lista_b)
   n = len(lista_a) 
    
   soma = 0
   for indice in range(n):
      soma = soma + (lista_a[indice] - media_a) * (lista_b[indice] - media_b)
   correlacao = float(soma) / ((n - 1) * desvio_a * desvio_b) 
   
   return correlacao

def media(lista):
   """Calcula a média associada aos valores na lista."""
   return sum(lista)/float(len(lista))


def desvio_padrao(lista):
   """Calcula o desvio padrao dos elementos na lista."""
   a_media = media(lista)
   soma = 0.0
   for elem in lista:
      soma = soma + (elem - a_media) ** 2
   desvio = math.sqrt(float(soma)/ (len(lista) - 1))
   return desvio

# 7.15 

def gera_carta(carta,clientes):
   """
   carta = texto geral da carta, num ficheiro.
   clientes = dicionário com os dados dos clientes.
   nome, data de nascimento (dd/mm/aaaa), morada, telefone
   """
   PREFIXO = '/tempo/data/'
   # lê carta 
   f_in = open(carta,'r')
   texto_carta = f_in.read()
   f_in.close()
   # filtra clientes
   lista_clientes = [(nome_cliente(cliente),morada_cliente(cliente)) for cliente in clientes.values() if (ano_cliente(cliente) < 1974)]


   for numero in range(len(lista_clientes)):
      # processa
      saudacao = 'Caro(a)'
      nome = lista_clientes[numero][0]
      morada = lista_clientes[numero][1]
      preambulo = saudacao+' '+nome + '\n' + morada + '\n\n'
   
   f_out = open(PREFIXO+nome+str(numero)+'.txt','w')
   f_out.write(preambulo)
   f_out.write(texto_carta)
   f_out.close


 
def dados(cliente):
   nome,data,morada,telefone = cliente
   dia, ano, mes = data.split('/')
   return (nome, (int(dia),int(ano),int(mes)),morada, int(telefone))

def ano_cliente(cliente):
   dados_cliente = dados(cliente)
   ano = dados_cliente[1][2]
   return ano

def nome_cliente(cliente):
   dados_cliente = dados(cliente)
   nome = dados_cliente[0]
   return nome

def morada_cliente(cliente):
   dados_cliente = dados(cliente)
   morada = dados_cliente[2]
   return morada

def main716():
   clientes = {100:('Ernesto','15/06/1953','F 26','239790019'),101:('Joana','29/09/2001','A  15','239700400'),102: ('Lurdes','17/06/1913','G 30','808242424'),103:('Daniela','31/03/2002','F 16','239400400')}
   gera_carta('/tempo/data/carta.txt', clientes)
   
# 7.16 

def acrescenta_musica(ficheiro, musica):
   with open(ficheiro,'a',encoding='utf-8') as f_in:
      f_in.seek(0,2)
      musica = musica + ('Não',)
      nova_musica = '\n%s\t%s\t%s\t%s\t%s' % musica
      f_in.write(nova_musica)
      f_in.close()


def empresta_musica(ficheiro,nome_musica):
   """ Anota uma música existente como emprestada."""
   with open(ficheiro,'r+',encoding='utf-8') as f_in:
      # Procura Música
      linha = f_in.readline()
      while linha != '':
         comp = len(linha)
         linha = linha[:-1].strip().split()
         if linha[1] == nome_musica:
            break
         linha = f_in.readline()
      else:
         print('Música inexistente!')
         return 'Done'
      # Actualiza
      linha[-1] = 'Sim'
      f_in.seek(f_in.tell() - comp - 1)
      nova_linha = '\t'.join(linha) + '\n'
      f_in.write(nova_linha)
      f_in.close()
 
def mostra_musicas_tipo(ficheiro,tipo):
      with open(ficheiro,'r+',encoding='utf-8') as f_in:
         # Procura Música
         linha = f_in.readline()
         while linha != '' and linha != '\n':
            linha = linha[:-1].strip().split()
            if linha[2] == tipo:
               print(linha)
            linha = f_in.readline()
         f_in.close()


# 7.17 

def nomes(fich, dicio):
   """
   Usa um ficheiro para extrair nomes 
   e um dicionário para encontrar nome comleto.
   """
   
   ficheiro = open(fich)
   dados = ficheiro.readlines()
   ficheiro.close()

   lista = []
   
   for elem in dados:
      pos = elem.find('~')
      nome = elem[pos+1:-1]
      if nome in dicio:
         completo = dicio[nome][0]
         lista.append(completo)
   lista.sort()
   return lista

# 7.18 
import csv

def le_csv(nome_fich):
   """
   Lê  um ficheiro em formato csv.
   """
   fich = open(nome_fich)
   csv_reader = csv.reader(fich)
   dados = []
   for linha in csv_reader:
      dados.append(linha)   
   fich.close()
   return dados

def main718(nome_ficheiro):
   dados = le_csv(nome_ficheiro)
   dicio = dict()
   for elem in dados:
      classe = elem[-1]
      nome = elem[0]
      dicio[classe] = dicio.get(classe,[]) + [nome]
   return dicio

# 7.19 

import urllib.request

def extract(text, sub1, sub2):
   """ Retira o texto entre duas subcadeias."""
   return text.split(sub1, 1)[-1].split(sub2, 1)[0]

def main719(url): 
   fp = urllib.request.urlopen(url)
   mybytes = fp.read()
   encoding = extract(str(mybytes).lower(), 'charset=', '"')
   if encoding:
      #mystr = mybytes.decode(encoding)
      print('-'*50)
      print( "Encoding type = %s" % encoding )
      print('-'*50)
   else:
      print("Encoding type not found!")
   fp.close()




if __name__ == '__main__':
   prefixo = '/Users/ernestojfcosta/data/'
   #mensagem = 'Acabei de criar um programa são em Python\n'
   #rase = 'mais lixo para o ficheiro\n'
   #frase_uni = 'são tótós e pedem clemência\n'
   #cria_ficheiro71b(prefixo+'ex_71b.txt', mensagem)
   #print(ler_seleccao(prefixo+'numeros72.txt',5,8))
   #print(ler_seleccao(prefixo+'numeros72.txt',0,8))
   #print(ler_seleccao_b(prefixo+'ex_71b.txt',0,25))
   #nova_linha(prefixo+'ex_71.txt',frase)
   #nova_linha_b(prefixo+'ex_71.txt',frase)
   #nova_linha_c(prefixo+'ex_71b.txt',frase_uni)
   
   #temp_max_min(prefixo+'temperaturas.txt')
   #temp_max_min_b(prefixo+'temperaturas.txt')
   #temp_max_min_c(prefixo+'temperaturas.txt')
   
   #copia_bin(prefixo+'einstein.jpg', prefixo+'lingua.jpg')

   #main77('/Users/ernestojfcosta/exo_77.txt', 50)
   #main77(prefixo+'exo_77.txt',50)
   #main78_plt(prefixo+'exo_77.txt')
   #main78_turtle(prefixo+'exo_77.txt')
   #main78('/Users/ernestojfcosta/exo_77.txt')
   #main79_plt('/Users/ernestojfcosta/data/exo_77.txt')
   #main79_turtle('/Users/ernestojfcosta/data/exo_77.txt')
   #main710(prefixo+'texto.txt')
   #transa = (4,'Bom e Barato',789,'07/12/2015', 15)
   #vendedor = 'Ernesto Costa'
   #main711(prefixo+'vendas.txt',transa, vendedor)
   #print(freq_inteiros('/data/inteiros.txt'))
   #print(fich_dic_a('/data/ex_normal.txt'))
   #meu_dicio = {'ernesto':['Ernesto Costa', 'ernesto@dei.uc.pt'],  'zeze':['Bernardo Zeus','zeze@hotmail.com'],'toto': ['Artur Toto', 'toto@gmail.com']}
   #print(nomes('/data/url.txt',meu_dicio))
   prof = {102: 'Professor', 411: 'Advogado', 203:'Estudante', 112:'Desempregado'}
   estado= {1:'Casado', 2:'Solteiro', 3:'Viúvo'}
   main713(prefixo+'dados_pessoas.txt',prof,estado)
   #vendas('/data/vendas.txt', (4,'Ako',1357,'15/06/1953',123.45), 'Ernesto Costa')
   #acrescenta_musica('/data/musicas.txt',('Camané','Lisboa','Fado','3:24'))
   #empresta_musica('/data/musicas.txt','LAWoman')
   #mostra_musicas_tipo('/data/musicas.txt','Rock')
   #print(main718('/data/zoo.csv'))
   #main719('http://expresso.sapo.pt')