# Variável global para armazenar o stock de um produto
stock_produto = 100

# Variável global para rastrear o total de vendas
total_vendas = 0


print(f"Stock inicial: {stock_produto}.")
print(f"Vendas iniciais: {total_vendas}")


# Função que tenta vender uma quantidade especificada do produto.
# Se o stock for suficiente, a venda é realizada e a quantidade vendida é retornada.
# Se o stock for insuficiente, nada é vendido e 0 é retornado.
def vender_normal(quantidade):
    global stock_produto, total_vendas
    if stock_produto >= quantidade:
        stock_produto -= quantidade
        total_vendas += quantidade
        return quantidade
    return 0


# Função que tenta vender uma quantidade especificada do produto.
# Se o stock for suficiente, a venda é realizada e a quantidade vendida é retornada.
# Se o stock for insuficiente, todo o stock é vendido e a quantidade vendida é retornada.
def vender_tudo(quantidade):
    global stock_produto, total_vendas
    vendido = min(stock_produto, quantidade)
    stock_produto -= vendido
    total_vendas += vendido
    return vendido


# Função que vende a quantidade especificada do produto independentemente do stock disponível.
# Se o stock for insuficiente, a venda é realizada e o stock torna-se negativo, refletindo uma entrega futura.
# A quantidade vendida é sempre retornada.
def vender_negativo(quantidade):
    global stock_produto, total_vendas
    stock_produto -= quantidade
    total_vendas += quantidade
    return quantidade


# Função que gera um relatório de vendas
def relatorio_vendas():
    global stock_produto, total_vendas
    stock_final = stock_produto - total_vendas
    if stock_final < 0:
        print("Erro: Stock negativo!")
    else:
        print(f"Total Vendido: {total_vendas}, Stock Final: {stock_final}")


# Correção do Bug: Separar stock final e entregas por realizar
entregas_por_realizar = 0
print(f"Entregas por realizar: {entregas_por_realizar}")


def relatorio_vendas_corrigido():
    global stock_produto, total_vendas, entregas_por_realizar
    stock_final = stock_produto - total_vendas
    if stock_final < 0:
        entregas_por_realizar = -stock_final
        stock_final = 0
    else:
        entregas_por_realizar = 0
    print(f"Total Vendido: {total_vendas}, Stock Final: {stock_final}, Entregas Por Realizar: {entregas_por_realizar}")


# Novo Bug: Funcionalidade de reabastecimento que não atualiza o total de vendas corretamente
def reabastecer(quantidade):
    global stock_produto, total_vendas
    stock_produto += quantidade
    # stock_produto agora inclui o reabastecimento mas esquece-se que pode ser negativo à partida


# Testes
# Variável global com o stock de um produto
print("Caso com bug")
vender_normal(150)
vender_tudo(150)
vender_negativo(150)
relatorio_vendas()  # Resultado incorreto devido ao stock negativo

# Reiniciar o stock e o total de vendas para demonstrar a correção do bug
print("Bug corrigido")
stock_produto = 100
total_vendas = 0
entregas_por_realizar = 0
print(f"Stock inicial: {stock_produto}.")
print(f"Vendas iniciais: {total_vendas}")
print(f"Entregas por realizar: {entregas_por_realizar}")
vender_normal(150)
vender_tudo(150)
vender_negativo(150)
relatorio_vendas_corrigido()  # Resultado correto

# Demonstração do novo bug
print("Novo bug")
stock_produto = 100
total_vendas = 0
entregas_por_realizar = 0
vender_normal(150)
vender_tudo(150)
vender_negativo(150)
reabastecer(300)
relatorio_vendas_corrigido()  # O resultado é incorreto, pois o reabastecimento não foi considerado no total de vendas
print("Deviam ter ido 300 para stock e ainda haver entregas por realizar")
