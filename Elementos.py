# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:49:16 2018

@author: mrbn
"""

def exibirProdutos(produtos, cardapio):
    for tupla in produtos:
        nome = tupla[0]
        qtd = tupla[1]
        valor = cardapio[nome][1]
        print("{} {} - R${}".format(qtd, nome, qtd*valor))

def buscaProdutos(cardapio, valor):
    resultados = []
    for produto in cardapio:
        if cardapio[produto][1] <= valor:
            resultados.append(produto)
    resultados.sort()
    return resultados