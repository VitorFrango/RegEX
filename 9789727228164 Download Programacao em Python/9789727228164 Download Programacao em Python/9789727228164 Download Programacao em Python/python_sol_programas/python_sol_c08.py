"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 8: Visões (II)


import cImage
import random
import math


#  8.1
# Matriz triangular inferior
def mostra_tri_inf(matriz):
    """Matriz triangular superior.Indexação pela posição."""
    for pos_linha in range(len(matriz)):
        for pos_coluna in range(0,pos_linha+1):
            print("%4d" % matriz[pos_linha][pos_coluna],end='')
        print()

# 8.2
# sub-matriz
def sub_matriz(matriz, linha, coluna, dim_x, dim_y):
    """Extrai a sub-matriz a partir de (linha, coluna) com dimensão dimX X dimY."""
    sub = cria_mat(dim_x, dim_y,0)
    for x in range(dim_x):
        for y in range(dim_y):
            sub[x][y] = matriz[linha+x][coluna+y]
    return sub
# 8.3
def matriz_tuplos(altura, largura):
    """Cria uma matriz de tuplos RGB."""
    matriz = list()
    for lin in range(altura):
        linha = list()
        for col in range(largura):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            linha.append((r,g,b))
        matriz.append(linha)
    return matriz


# 8.4
# Desenha recta
def desenha_recta(janela, x1,y1,x2,y2):
    largura = janela.getWidth()
    altura = janela.getHeight()
    imagem = cImage.EmptyImage(largura,altura)
  
    pixel = cria_random_pixel()
    # desenha recta
    for x in range(x1,x2):
        y = int(((y2 - y1) / (x2 -x1)) * ( x - x1) + y1)
        imagem.setPixel(x,y,pixel)
    imagem.draw(janela)
    
# 8.5
def arco(x,y, raio, amplitude):
    """ 
    Desenha (um arco de circunferência) com centro em (x,y) e raio.
    """
    largura = 4 * raio
    altura = 4 * raio
    janela = cImage.ImageWin('Janela', largura, altura)
    imagem = cImage.EmptyImage(largura,largura)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
            
    #imagem.setPosition(x,y)
    pixel = cria_random_pixel()
    
    for angulo in range(amplitude):
        cordx = int((raio * math.cos((math.pi /float(180)) * angulo)) + x)
        cordy = int((raio * math.sin((math.pi /float(180)) * angulo))  + y)
        imagem.setPixel(cordx,cordy,pixel)
    imagem.draw(janela)
    janela.exitOnClick()
    
# 8.6
# Criar moldura

def cria_moldura(imagem,tamanho, cor):
    """Cria uma moldura à volta da imagem original de tamanho e cor."""
    img = cImage.FileImage(imagem)
    largura = img.getWidth()
    altura = img.getHeight()
    
    nova_imagem = cImage.EmptyImage(largura+2*tamanho, altura + 2*tamanho)
   
    janela = cImage.ImageWin('Moldura', largura+2*tamanho, altura + 2*tamanho)
    janela.setBackground('red')

    img.setPosition(tamanho, tamanho)
    img.draw(janela)
    janela.exitOnClick()
    
# 8.7    
# Corta imagem
def corta_imagem(img, pos_x, dim_x, pos_y, dim_y):
    """ Corta uma parte da imagem a partir da posição com as dimensões especificadas."""
    nova_imagem = cImage.EmptyImage(dim_x, dim_y)
    for coluna in range(pos_x, pos_x+dim_x):
        for linha in range(pos_y, pos_y+dim_y):
            pixel = img.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna - pos_x, linha - pos_y, pixel)
    return nova_imagem

def mostra_corta_imagem(imagem, pos_x, dim_x, pos_y, dim_y):
    img = cImage.FileImage(imagem)
    altura = img.getHeight()
    largura = img.getWidth()
    img_cortada = corta_imagem(img,pos_x, dim_x, pos_y, dim_y)
    
    janela = cImage.ImageWin('Corta Imagem', 2*largura, altura)
    img_cortada.setPosition(largura+pos_x, pos_y)
    img.draw(janela)
    img_cortada.draw(janela)
    
    janela.exitOnClick()
    

# 8.8 
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos tendo em atenção a diferença dos canais."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()    
    int_media = int(0.299*vermelho + 0.587*verde + 0.114*azul) // 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

def preto_branco_pixel(pixel_cinzento,limiar):
    preto = cImage.Pixel(0,0,0)
    branco = cImage.Pixel(255,255,255)
    if pixel_cinzento.getRed() < limiar :
        novo_pixel = preto
    else:
        novo_pixel = branco
    return novo_pixel

def imagem_preto_branco(imagem, limiar):
    """ 
    Transforma para escala de cinzentos e depois converte
    para preto e branco de acordo com o limiar.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem=cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = preto_branco_pixel(pixel_cinzento(pixel),limiar)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem

def mostra_preto_branco(imagem, limiar):
    """ Substitui na imagem as cores pelas mais próximas na palete."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = imagem_preto_branco(img, limiar)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Preto e Branco', 2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
    
    
# 8.9
# Manipula cores por canal
def manipula_cor(imagem_fich, val_r,val_g,val_b):
    """ Manipula cores. Altera de modo independente os
    três canais de cor."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Manipula cores', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel= imagem.getPixel(coluna,linha)
            r = pixel.getRed()
            g = pixel.getGreen()
            b = pixel.getBlue()
            novo_r = max(r, r + ((val_r * r) % 255))
            novo_g = max(g, g + ((val_g * g) % 255)) 
            novo_b = max(r, r + ((val_b * b) % 255)) 
            novo_pixel = cImage.Pixel(novo_r,novo_g, novo_b)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()   


# 8.10 
def distorcer_b(imagem, factor_x, factor_y):
    """ Encolhe uma imagem de acordo com os factores indicados."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = encolher(img, factor_x,factor_y)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()  
    nova_largura = largura//factor_x
    nova_altura = largura//factor_y
    janela = cImage.ImageWin('Distorce',  largura + nova_largura,  altura)
    # Coloca imagens
    img.draw(janela)
    nova_img.setPosition(largura + 1,0)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick()    
    
    
def encolher(imagem,factor_x, factor_y):
    """
    Encolhe a imagem de acordo com os factores.
    Estes devem ser inteiros.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_largura = largura // factor_x
    nova_altura =  altura // factor_y
    
    nova_imagem = cImage.EmptyImage(nova_largura,nova_altura)
    
    for coluna in range(nova_largura):
        for linha in range(nova_altura):
            pixel = imagem.getPixel(coluna * factor_x, linha * factor_y)
            nova_imagem.setPixel(coluna,linha, pixel)
    return nova_imagem


# 8.11

def espelho_h_s(imagem_fich):
    """Faz o espelho horizontal de uma imagem.
    Usa a parte superior."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Vertical Superior', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura//2):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(coluna,altura - linha - 1,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()

# 8.12
# Redução das cores
def mostra_reduz_cores(imagem, palete):
    """ Substitui na imagem as cores pelas mais próximas na palete."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = reduz_cores(img, palete)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Reduz Cores', 2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
    
def reduz_cores(imagem, palete):
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)
            novo_pixel = distancia_palete(pixel, palete)
            nova_imagem.setPixel(coluna, linha, novo_pixel)
    return nova_imagem


def distancia_cores(pixel_1, pixel_2):
    """Calcula a distância entre duas cores dada por uma fórmula de distância elclidiana."""
    r_1 = pixel_1.getRed()
    g_1 = pixel_1.getGreen()
    b_1 = pixel_1.getBlue()
    
    r_2 = pixel_2.getRed()
    g_2 = pixel_2.getGreen()
    b_2 = pixel_2.getBlue()
    
    r = (r_1 - r_2)**2
    g = (g_1 - g_2)**2
    b = (b_1 - b_2)**2
    
    return math.sqrt(r+g+b)


def distancia_palete(cor, palete):
    """Qual a cor mais próxima."""
    distancia_min = distancia_cores(cImage.Pixel(0,0,0), cImage.Pixel(255,255,255))
    cor_min = cor
    for pal_cor in palete:
        cor_pixel = cImage.Pixel(pal_cor[0],pal_cor[1], pal_cor[2])
        distancia = distancia_cores(cor,cor_pixel)
        if distancia < distancia_min:
            distancia_min = distancia
            cor_min = cor_pixel	    
    return cor_min

# 8.13

def colagem(lista_imagens, largura, altura):
    """ lista_imagens = [....,[imagem, (posx, poy)], ...]"""
    # cria janela principal inicialmente vazia
    janela = cImage.ImageWin('Colagem',largura,altura)
    for imagem in lista_imagens:
        img = cImage.FileImage(imagem[0])
        img.setPosition(imagem[1][0], imagem[1][1])
        img.draw(janela)
    janela.exitOnClick()
    
    


# 8.14
#   
def blur(imagem):
    """Suaviza uma imagem."""
    # Inicializa
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura)
    
    # Percorre a imagem e calcula
    for coluna in range(largura):
        for linha in range(altura):
            novo_pixel = media(coluna,linha,imagem)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem

def media(coluna, linha, imagem):
    """Calcula o valor médio dos pixeis na vizinhança do pixel (coluna,linha)."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    # Extrai pixeis
    vizinhos = []
    for c in [-1,0,1]:
        for l in [-1,0,1]:
            nova_coluna = coluna+c
            nova_linha = linha+l
            if (0 < nova_coluna < largura) and (0 < nova_linha < altura):
                vizinhos.append(imagem.getPixel(nova_coluna, nova_linha))                    
    # Calcula pixel "médio" por canal
    n_viz = len(vizinhos)
    r = sum([vizinhos[i].getRed() for i in range(n_viz)])//n_viz
    g = sum([vizinhos[i].getGreen() for i in range(n_viz)])//n_viz
    b = sum([vizinhos[i].getBlue() for i in range(n_viz)])//n_viz
    
    novo_pixel = cImage.Pixel(r,g,b)
    return novo_pixel
    
def mostra_blur(imagem):
    """ Procede à diminiuição da pixelização da imagem."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    img_ampliada = ampliar(img,3,2)
    nova_img = blur(img_ampliada)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Blur', 6 * largura, 2*altura )
    # Coloca imagens
    nova_img.setPosition(3*largura+1,0)
    img_ampliada.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
def ampliar(imagem,factor_x, factor_y):
    """
    Altera a imagem de acordo com os factores.
    Estes devem ser números inteiros positivos.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(factor_x * largura, factor_y * altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)
            # repete o pixel numa área definida pelos factores
            for i_x in range(factor_x):
                for i_y in range(factor_y):
                    nova_imagem.setPixel(factor_x * coluna + i_x, factor_y * linha + i_y, pixel)
    return nova_imagem  

# 8.15
""" Alguns filtros  """
masc_1 = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
sharpen = [[0,-1,0],[-1,5,-1],[0,1,0]]
sharpen_2 = [[0,0,0,0,0],[0,0,-1,0,0],[0,-1,5,-1,0],[0,0,1,0,0], [0,0,0,0,0]]
sharpen_3 = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
blur = [[1,1,1],[1,1,1],[1,1,1]]
edge_enhance = [[0,0,0],[-1,1,0],[0,0,0]]
edge_detect = [[0,1,0],[1,-4,1],[0,1,0]]
emboss = [[-2,-1,0],[-1,1,1],[0,1,2]]
sobel_v = [[-1,0,1],[-2,0,2],[-1,0,1]]
sobel_h = [[1,2,1],[0,0,0],[-1,-2,-1]]
gauss_1 = [[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]]


# Variante em relação ao texto do livro
def convolve_todos(imagem, pix_linha, pix_coluna, kernel):
    """ Calcula a convolução de um pixel."""
    kernel_coluna_base = pix_coluna - 1
    kernel_linha_base = pix_linha - 1
    
    soma_r = 0
    soma_g = 0
    soma_b = 0
    for linha in range(kernel_linha_base, kernel_linha_base + 3):
        for coluna in range(kernel_coluna_base,kernel_coluna_base + 3):
            k_coluna_indice = coluna - kernel_coluna_base
            k_linha_indice = linha - kernel_linha_base
            
            pixel = imagem.getPixel(coluna, linha)
            intensidade_r = pixel.getRed()
            intensidade_g = pixel.getGreen()
            intensidade_b = pixel.getBlue()
            
            soma_r = int(soma_r + intensidade_r * kernel[k_linha_indice][k_coluna_indice])
            soma_g = int(soma_g + intensidade_g * kernel[k_linha_indice][k_coluna_indice])
            soma_b = int(soma_b + intensidade_b * kernel[k_linha_indice][k_coluna_indice])
    return soma_r,soma_g,soma_b

def convolve_geral(imagem_fich, kernel):
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    for linha in range(1, altura - 1):
        for coluna in range(1, largura - 1):
            r,g,b = convolve_todos(imagem, linha, coluna, kernel)
            pixel_cor = cImage.Pixel(r,g,b)
            pixel_cinza = pixel_cinzento(pixel_cor)
            nova_imagem.setPixel(coluna, linha, pixel_cor)
    janela = cImage.ImageWin('Convolve',2*largura,altura)
    imagem.draw(janela)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()

    
    
# 8.16
# Elimina ruido
import cImage

def elimina_ruido(imagem):
    """ Elimina o ruido de uma imagem  calculando a mediana."""
    # Inicializa
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura) 
    # Percorre a imagem e calcula
    for coluna in range(1,largura-1):
        for linha in range(1,altura-1):
            novo_pixel = mediana(coluna,linha,imagem)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem


def mediana(coluna, linha, imagem):
    """Calcula a mediana dos pixeis na vizinhança do pixel (coluna,linha)."""
    r,g,b = [], [], []
    for c in [-1,0,1]:
        for l in [-1,0,1]:
            nova_coluna = coluna+c
            nova_linha = linha+l
            pixel = imagem.getPixel(nova_coluna, nova_linha)     
            # Actualiza pixel por canal
            r.append(pixel.getRed())
            g.append(pixel.getGreen())
            b.append(pixel.getBlue())
    r.sort()
    med_r = r[len(r)//2]
    med_g = g[len(g)//2]
    med_b = b[len(b)//2]
    novo_pixel = cImage.Pixel(med_r,med_g,med_b)
    return novo_pixel 
    
def mostra(imagem):
    """ Procede à diminiuição do ruído da imagem."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = elimina_ruido(img)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Elimina ruído', 2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 


# 8.17
# Fusão de imagens
def combina_pixel(pixel1, pixel2,function):
    """ Combina dois pixeis de acordo com a função."""
    r1 = pixel1.getRed()
    g1 = pixel1.getGreen()
    b1 = pixel1.getBlue()
    
    r2 = pixel2.getRed()
    g2 = pixel2.getGreen()
    b2 = pixel2.getBlue()
    
    r,g,b = function(r1,r2,g1,g2,b1,b2)
    return cImage.Pixel(r,g,b)

def media(r1,g1,b1, r2,g2,b2):
    """ Devolve tuplo formado pela média."""
    r = (r1 + r2) // 2
    g = (g1 + g2) //2
    b = (b1 + b2) // 2
    return r,g,b

def maior(r1,g1,b1, r2,g2,b2):
    """ Devolve tuplo formado pela pelo maior dos dois."""
    r = max(r1 , r2)
    g = max(g1 , g2)
    b = max(b1 , b2)
    return r,g,b

def menor(r1,g1,b1, r2,g2,b2):
    """ Devolve tuplo formado pela pelo maior dos dois."""
    r = min(r1 , r2)
    g = min(g1 , g2)
    b = min(b1 , b2)
    return r,g,b


def funde(imagem1, imagem2,  funcao):
    
    largura_1 = imagem1.getWidth()
    altura_1 = imagem1.getHeight()
    largura_2 = imagem2.getWidth()
    altura_2 = imagem2.getHeight()
    largura = min(largura_1,largura_2)
    altura = min(altura_1,altura_2)
    

    
    nova_imagem = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pix1= imagem1.getPixel(coluna, linha)
            pix2 = imagem2.getPixel(coluna,linha)
            
            novo_pixel = combina_pixel(pix1,pix2, funcao)
            
            nova_imagem.setPixel(coluna,linha,novo_pixel)
            
    return nova_imagem



def main17(imagem_fich_1, imagem_fich_2,funcao):
    imagem_1 = cImage.FileImage(imagem_fich_1)
    imagem_2 = cImage.FileImage(imagem_fich_2)
    
    largura_1 = imagem_1.getWidth()
    altura_1 = imagem_1.getHeight()
    largura_2 = imagem_2.getWidth()
    altura_2 = imagem_2.getHeight()
    largura = min(largura_1,largura_2)
    altura = min(altura_1,altura_2)
    
    janela = cImage.ImageWin('Fusão', largura, altura)
    
    nova_imagem = funde(imagem_1,imagem_2,funcao)
    
    nova_imagem.draw(janela)
    janela.exitOnClick()




# 8.18   
# roda 90
def roda_90(imagem):
    """ Roda uma imagem 90 graus para a direita."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_imagem = cImage.EmptyImage(altura,largura) # troca por causa da rotação
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            nova_imagem.setPixel(linha,coluna,pixel)
    return nova_imagem  

# 8.19
# Roda arbitráriamente
def roda_imagem(imagem, angulo):
    """
    Roda a imagem um valor igual a angulo. Com amputa��o.
    """
    ang_rad= math.radians(angulo)
    val1 = math.cos(ang_rad)
    val2 = math.sin(ang_rad)
    mat=[[val1, -val2],[val2, val1]]
    
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    
    # cria background branco
    pixel_branco = cImage.Pixel(255,255,255)
    
    nova_imagem = cImage.EmptyImage(largura, altura)
    for coluna in range(largura):
        for linha in range(altura):
            nova_imagem.setPixel(coluna,linha,pixel_branco)
            
    # roda num novo sistema de eixos
    
    for coluna in range((-largura//2)+1 , largura//2):
        for linha in range((-altura//2)+1 , altura//2):
            
            nova_coluna, nova_linha = [int(valor) for valor in prod_matriz_vector(mat,[coluna, linha])]

            nova_coluna = converte_x(nova_coluna, largura//2)
            nova_linha =  converte_y(nova_linha,altura//2)
            
            if dentro(nova_coluna,nova_linha, largura, altura):
                col = converte_x(coluna,largura//2)
                lin = converte_y(linha,altura//2)
                pixel = imagem.getPixel(col, lin)
                nova_imagem.setPixel(nova_coluna,nova_linha, pixel)
    return nova_imagem

def converte_x(px, referencia):
    return referencia + px


def converte_y(py, referencia):
    return referencia - py

def dentro(px1,py1,px2,py2):
    """
    Estou a considerar o canto superior esquerdo
    como tendo coordenadas (0,0).
    """
    res = (px1 > 0) and (py1 > 0) and (px1 < px2) and (py1 < py2)
    return res
            
    
def main19(imagem_fich, angulo):
    imagem = cImage.FileImage(imagem_fich)
    
    largura = imagem.getWidth()
    altura =  imagem.getHeight()
    
    janela = cImage.ImageWin('Roda', largura,altura)
    
    nova_imagem = roda_imagem(imagem, angulo)
    
    nova_imagem.draw(janela)
    
    janela.exitOnClick()
    
# 8.20
import cImage
import random

def encripta(imagem):
    """Encripta uma imagem mudando a ordem das linhas."""
    # Converte em lista de listas

    imagem_lista = imagem.toList()
    # Define permutação
    tamanho = len(imagem_lista)
    original = list(range(tamanho))
    permuta = original[:]
    random.shuffle(permuta)
    # Encripta
    nova_imagem_lista = mistura_imagem(imagem_lista, permuta)
    # Converte de volta
    nova_imagem = cImage.ListImage(nova_imagem_lista)
    return nova_imagem

def mistura_imagem(imagem, permuta):
    nova_imagem = []
    for i in range(len(imagem)):
        nova_imagem.append(imagem[permuta[i]])
    return nova_imagem

def mostra_encripta(imagem):
    img = cImage.FileImage(imagem)
    largura = img.getWidth()
    altura = img.getHeight()
    
    nova_imagem = encripta(img)
    
    janela = cImage.ImageWin('Encripta', 2*largura, altura)
    nova_imagem.setPosition(largura+1,0)
    
    img.draw(janela)
    nova_imagem.draw(janela)
    
    janela.exitOnClick()


if __name__ == '__main__':
    #mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    #mostra_tri_inf(mat)
    #print(sub_matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],1,1,2,2))
    #print(matriz_tuplos(3,4))
    #imagem = gera_imagem(2,3)     
    #fich = open('/Users/ernestojfcosta/imagem.txt','w')
    #fich.write(str(imagem))
    #fich.close()  
    colagem([['/images/calvin_leia_s.jpg', (100,500)], ['/images/duck_s.jpg',(50,250)],['/images/duck_s.jpg',(150,0)],['/images/dd.jpg',(400,200)],['/images/dd_60.jpg',(300,20)]], 1024, 768)
    #espelho_h_s('/images/calvin_leia.jpg')
    #palete_cores = [(255,0,0), (0,255,0), (0,0,255), (0,0,0), (255,255,255), (255,255,0), (0,255,255), (255,0,255)] 
    #mostra_preto_branco('/images/calvin_leia.jpg', 128)
    #convolve_geral('/images/calvin_leia_s.jpg', gauss_1)
    #mostra_reduz_cores('/images/calvin_leia.jpg', palete_cores)
    #mostra_reduz_cores('/images/d_duck.jpeg', palete_cores)
    #cria_moldura('/images/calvin_leia.jpg', 10,(255,0,0))
    #mostra_corta_imagem('/images/calvin_leia.jpg', 50,200, 100,250)