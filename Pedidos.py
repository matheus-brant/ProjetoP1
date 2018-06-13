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
Funcionalidade do Script: Esse script contém as funções que definem a ativação 
e desativação de produtos cadastrados no programa, de acordo com sua
disponibilidade para consumo. Produtos desativados não aparecerão como opção
no pedido e pode, ser reativados quando estiverem disponíveis. 
"""

def produtosAtivos(dicionario):
    '''
    Percorre cada tupla do dicionario passado como parâmetro e atribui o
    valor booleano True ao elemento que esteja no índice 2 de cada tupla,
    adicionado ao final da lista ativos o elemento encontrado e retornando essa
    lista no final. Essa função é chamada no comando 6 do script principal.
    '''
    ativos = []
    for produto in dicionario:
        if dicionario[produto][2] == True:
            ativos.append(produto)
    return ativos

def produtosInativos(dicionario):
    '''
    Percorre cada tupla do dicionario passado como parâmetro e atribui o
    valor booleano False ao elemento que esteja no índice 2 de cada tupla,
    adicionado ao final da lista inativos o elemento encontrado e retornando
    essa lista no final. Essa função é chamada no comando 6 do script principal.
    '''
    inativos = []
    for produto in dicionario:
        if dicionario[produto][2] == False:
            inativos.append(produto)
    return inativos