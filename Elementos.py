# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Projeto Programação 1
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Matheus Ribeiro Brant Nobre (mrbn)
Email: mrbn@cin.ufpe.br
Data: 2018-06-13
Copyright(c) 2018 Matheus Ribeiro Brant Nobre
"""

"""
Funcionalidade do Script: Esse scirpt contém as funções de busca e apresentação
dos produtos ao usuário. As operaões que chamam as funções abaixo estão
no script principal. 
"""

def exibirProdutos(produtos, cardapio):
    '''
    Percorre a lista que armazena os dados dos produtos e printa na tela
    a quantidade, nome e valor do pedido realizado pelo usuário. Essa função é
    chamada no comando 10 do script principal.
    '''
    for tupla in produtos:
        nome = tupla[0]
        qtd = tupla[1]
        valor = cardapio[nome][1]
        print("{} {} - R${}".format(qtd, nome, qtd*valor))

def buscaProdutos(cardapio, valor):
    '''
    Percorre a lista que armazena os dados dos produtos e acrescenta ao final
    da lista resultados cada elemento que tenha um valor menor ou igual ao
    valor informado pelo usuário, retornado essa lista ao final. Essa função é
    chamada no comando 12 do script principal.
    '''
    resultados = []
    for produto in cardapio:
        if cardapio[produto][1] <= valor:
            resultados.append(produto)
    resultados.sort()
    return resultados