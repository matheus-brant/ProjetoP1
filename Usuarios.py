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
Funcionalidade do Script: Esse scirpt contém as funções relacionadas aos
usuários e os dados de produtividade gerados por suas operações (busca,
usuários ativos e inativos, log de ações do usuário). 
"""

import datetime

def buscaUsuario(usuarios, nome):
    '''
    Percorre a lista que armazena os dados dos usuários e acrescenta ao final
    da lista resultados cada usuario que tenha o elemento de índice 0 igual ao
    nome informado pelo usuário, retornado essa lista ao final. Essa função é
    chamada no comando 11 do script principal.
    '''
    resultados = []
    for n in usuarios:
        if usuarios[n][0] == nome:
            resultados.append(n)
    resultados.sort()
    return resultados

def usuariosAtivos(dicionario):
    '''
    Percorre cada tupla do dicionario passado como parâmetro e atribui o
    valor booleano True ao elemento que esteja no índice 2 de cada tupla,
    adicionado ao final da lista ativos o elemento encontrado e retornando essa
    lista no final. Essa função é chamada no comando 8 do script principal.
    '''
    ativos = []
    for usuario in dicionario:
        if dicionario[usuario][3] == True:
            ativos.append(usuario)
    return ativos

def usuariosInativos(dicionario):
    '''
    Percorre cada tupla do dicionario passado como parâmetro e atribui o
    valor booleano False ao elemento que esteja no índice 2 de cada tupla,
    adicionado ao final da lista inativos o elemento encontrado e retornando
    essa lista no final. Essa função é chamada no comando 8 do script principal.
    '''
    inativos = []
    for usuario in dicionario:
        if dicionario[usuario][3] == False:
            inativos.append(usuario)
    return inativos

def logAct(usuario, acao):
    '''
    Abre o arquivo txt no modo de adição e acrescenta uma string que informa
    a hora, a data e a ação realizada pelo usuário conforme os parâmetros
    passados. Em seguida fecha o arquivo.
    '''
    arquivo = open('log.txt', 'a')
    agora = datetime.datetime.now()
    arquivo.write('{}: {} às {} {}\n.'.format(usuario, acao, str(agora.time()), str(agora.date())))
    arquivo.close()
    
def recuperaUsuario(linha):
    '''
    Recupera os caracteres de um arquivo que estejam antes da string ":" e
    armazenam o valor na variável usuário, retornando ela ao final.
    '''
    usuario = ''
    for c in linha:
        if c != ":":
            usuario += c
        else:
            return usuario

def recuperaData(linha):
    '''
    Recupera os caracteres de um arquivo que estejam antes da string "." e
    armazenam o valor na variável data, retornando ela ao final.
    '''
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
