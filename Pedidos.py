# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:28:23 2018

@author: mrbn
"""

def produtosAtivos(dicionario):
    ativos = []
    for produto in dicionario:
        if dicionario[produto][2] == True:
            ativos.append(produto)
    return ativos

def produtosInativos(dicionario):
    inativos = []
    for produto in dicionario:
        if dicionario[produto][2] == False:
            inativos.append(produto)
    return inativos