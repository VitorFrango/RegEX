# Dicionários para armazenar dados
livros = {1: {"titulo": "Os Escolhidos", "autor": "Ricardo Pinto", "disponivel": True},
          2: {"titulo": "O Nome do Vento", "autor": "Patrick Rothfuss", "disponivel": True}}

utilizadores = {1: {"nome": "João", "livros_emprestados": []},
                2: {"nome": "Maria", "livros_emprestados": []}}


print(f"Livros disponíveis: {livros}")
print(f"Utilizadores registados: {utilizadores}")


# Função para emprestar um livro
def emprestar_livro(id_livro, id_utilizador):
    if livros[id_livro]["disponivel"]:
        livros[id_livro]["disponivel"] = False
        utilizadores[id_utilizador]["livros_emprestados"].append(id_livro)
        return f"Confirmo: o livro '{livros[id_livro]['titulo']}' foi emprestado."
    return "Não foi possível efetuar o empréstimo."


# Função para devolver um livro
def devolver_livro(id_livro, id_utilizador):
    if id_livro in utilizadores[id_utilizador]["livros_emprestados"]:
        utilizadores[id_utilizador]["livros_emprestados"].remove(id_livro)
        return f"Confirmo: o livro '{livros[id_livro]['titulo']}' foi devolvido."
    return "Não foi possível efetuar a devolução."


# Demonstração do bug: um livro pode ser devolvido, mas permanece indisponível na biblioteca
print(emprestar_livro(1, 1))  # O João leva emprestado o livro 1
print(devolver_livro(1, 1))  # João devolve o livro 1, mas o livro permanece indisponível
print(emprestar_livro(1, 1))  # João não consegue pedi-lo outra vez porque ficou indisponível


# Correção do bug: atualizar o estado de disponibilidade do livro ao devolvê-lo
def devolver_livro_corrigido(id_livro, id_utilizador):
    if id_livro in utilizadores[id_utilizador]["livros_emprestados"]:
        livros[id_livro]["disponivel"] = True
        utilizadores[id_utilizador]["livros_emprestados"].remove(id_livro)
        return f"Confirmo: o livro '{livros[id_livro]['titulo']}' foi devolvido."
    return "Não foi possível efetuar a devolução."


# Demonstração da correção, reinicializando as estruturas de dados
livros = {1: {"titulo": "Os Escolhidos", "autor": "Ricardo Pinto", "disponivel": True},
          2: {"titulo": "O Nome do Vento", "autor": "Patrick Rothfuss", "disponivel": True}}

utilizadores = {1: {"nome": "João", "livros_emprestados": []},
                2: {"nome": "Maria", "livros_emprestados": []}}


print(emprestar_livro(1, 1))  # O João leva emprestado o livro 1
print(devolver_livro_corrigido(1, 1))  # O João devolve o livro 1, já fica disponível
print(emprestar_livro(1, 1))  # João agora consegue pedi-lo outra vez porque ficou disponível
print(devolver_livro_corrigido(1, 1))  # E repoe-se na biblioteca novamente, para o próximo exemplo.


# Nova função com bug: devolução de um livro perdido que foi achado
def devolucao_de_perdido_e_achado(id_livro):
    if not livros[id_livro]["disponivel"]:
        livros[id_livro]["disponivel"] = True
        return f"O livro '{livros[id_livro]['titulo']}' foi encontrado e devolvido por alguém e agora está disponível."
    return (
        "Não foi possível efetuar devolução porque o livro já estava disponível. "
        "O achado não deve ser da biblioteca."
    )


# Demonstração da situação com bug
print(emprestar_livro(2, 1))  # O João leva emprestado o livro 2
print(devolucao_de_perdido_e_achado(2))  # O livro 2 é devolvido por um terceiro e fica disponível
print(emprestar_livro(2, 2))  # A Maria leva emprestado o livro 2

# A lista de livros emprestados ao João ainda inclui o livro 2, embora o livro agora esteja disponível.
titulos_joao = [livros[id_livro]['titulo'] for id_livro in utilizadores[1]["livros_emprestados"]]
print(f'Livros emprestados ao João: {", ".join(titulos_joao)}')

# A lista de livros emprestados à Maria também inclui o livro 2, agora está emprestado aos dois!
titulos_maria = [livros[id_livro]['titulo'] for id_livro in utilizadores[2]["livros_emprestados"]]
print(f'Livros emprestados à Maria: {", ".join(titulos_maria)}')
