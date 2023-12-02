# Variável global para armazenar o stock de um produto
stock_produto = 100


# Função para verificar se há stock suficiente para a venda
def verificar_stock(quantidade):
    global stock_produto
    return stock_produto >= quantidade


# Função para vender um produto normalmente
def vender_normal(quantidade):
    global stock_produto
    stock_produto -= quantidade
    if stock_produto < 0:
        print("Alerta, venda não concretizada na totalidade, stock insuficiente")
    return quantidade


# Função para vender um produto com a promoção "Pague 2, Leve 3"
def vender_promocao(quantidade):
    global stock_produto
    stock_produto -= quantidade + (quantidade // 2)  # Adiciona 50% mais produtos como promoção
    if stock_produto < 0:
        print("Alerta, venda não concretizada na totalidade, stock insuficiente")
    return quantidade + (quantidade // 2)


# Demonstração do bug: a função vender_promocao deixa o stock num estado que faz a função vender_normal falhar
print("Caso com bug")
if verificar_stock(20) and verificar_stock(80):  # Verificação de stock
    vender_promocao(20)  # Vende 20, oferece 10, total 30
    print(vender_normal(80))  # Resultado incorreto: o stock é insuficiente devido à promoção anterior
else:
    print("Stock insuficiente para realizar as vendas")

# Correção: a função de promoção regista ter provocado uma atualização excecional de stock
alerta_de_atualizacao_excecional = False


def vender_promocao_corrigida(quantidade):
    global stock_produto, alerta_de_atualizacao_excecional
    stock_produto -= quantidade + (quantidade // 2)  # Adiciona 50% mais produtos como promoção
    if stock_produto < 0:
        print("Alerta, venda não concretizada na totalidade, stock insuficiente")
    alerta_de_atualizacao_excecional = True
    return quantidade + (quantidade // 2)


# Reiniciar o stock para demonstrar a correção do bug
stock_produto = 100
print("Bug corrigido")

# Lista de ordens de venda (funções e quantidades)
posso_vender = True
vendas = [(vender_promocao_corrigida, 20), (vender_normal, 80)]

# Itera sobre a lista de vendas
total = 0
for venda_func, qtd in vendas:
    # Verifica o stock antes de cada venda
    if not verificar_stock(total+qtd):
        print("Stock insuficiente para realizar a venda de ", qtd)
        posso_vender = False
    else:
        total += qtd

if posso_vender:
    for venda_func, qtd in vendas:
        # Verifica o alerta de atualização excecional antes de cada venda
        if alerta_de_atualizacao_excecional:
            # Se o alerta estiver ativo, verifica o stock novamente
            if not verificar_stock(qtd):
                print("Stock insuficiente para realizar a venda de ", qtd)
                break  # Sai do loop se não houver stock suficiente
            # Limpar o alerta após a verificação
            alerta_de_atualizacao_excecional = False
        # Realiza a venda
        print(venda_func(qtd))
else:
    print("Stock insuficiente para realizar as vendas todas")


# Novo bug: função que vende e doa um produto para o banco alimentar a cada 10 produtos vendidos
def vender_com_doacao_para_banco_alimentar(quantidade):
    global stock_produto
    stock_produto -= quantidade + (quantidade // 10)  # Doa um produto a cada 10 vendidos
    if stock_produto < 0:
        print("Alerta, venda não concretizada na totalidade, stock insuficiente")
    return quantidade + (quantidade // 10)


# Reiniciar o stock para demonstrar o novo bug
stock_produto = 100
alerta_de_atualizacao_excecional = False
print("Novo bug")

# Lista de ordens de venda (funções e quantidades)
posso_vender = True
vendas = [(vender_promocao_corrigida, 20), (vender_com_doacao_para_banco_alimentar, 60), (vender_normal, 10)]

# Itera sobre a lista de vendas verificando o stock
total = 0
for venda_func, qtd in vendas:
    # Verifica o stock antes de cada venda
    if not verificar_stock(total+qtd):
        print("Stock insuficiente para realizar a venda de ", qtd)
        posso_vender = False
    else:
        total += qtd

if posso_vender:
    for venda_func, qtd in vendas:
        print(f"stock {stock_produto}")
        # Verifica o alerta de atualização excecional antes de cada venda
        if alerta_de_atualizacao_excecional:
            # Se o alerta estiver ativo, verifica o stock novamente
            if verificar_stock(qtd):
                print(venda_func(qtd))
            else:
                print(f"Stock insuficiente para realizar a venda de {qtd}")
                break  # Sai do loop se não houver stock suficiente
            # Limpar o alerta após a verificação
            alerta_de_atualizacao_excecional = False
        else:
            # Realiza a venda normal em caso de não alerta
            print(venda_func(qtd))  # Vai falhar no final porque a função do banco alimentar não ligou o alerta
else:
    print("Stock insuficiente para realizar as vendas todas")
