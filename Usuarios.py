# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:49:16 2018

@author: mrbn
"""
import datetime

def buscaUsuario(parametros):
    pass

def logAct(usuario, acao):
    arquivo = open('log.txt', 'a')
    agora = datetime.datetime.now()
    arquivo.write('{}: {} às {} {}\n.'.format(usuario, acao, str(agora.time()), str(agora.date())))
    arquivo.close()
    
def recuperaUsuario(linha):
    usuario = ''
    for c in linha:
        if c != ":":
            usuario += c
        else:
            return usuario

def recuperaData(linha):
    data = ''
    for c in linha:
        if c == ' ':
            data = ''
        elif c!= ' ' and c!= '.':
            data += c
    return data

def lerLogUsuario(usuario):
    arquivo = open('log.txt', 'r')
    acao = arquivo.readline()
    acoes = []
    while acao != '':
        if recuperaUsuario(acao) == usuario:
            acoes.append(acao)
        acao = arquivo.readline()
    return acoes

def lerLogData(data):
    arquivo = open('log.txt', 'r')
    acao = arquivo.readline()
    acoes = []
    while acao != '':
        if recuperaData(acao) == data:
            acoes.append(acao)
        acao = arquivo.readline()
    return acoes
