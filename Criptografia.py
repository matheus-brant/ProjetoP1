# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:49:14 2018

@author: mrbn
"""

def lerChave(address):
    '''
    Recupera dois números inteiros separados por espaço na primeira linha de
    um arquivo cujo parametro é dado como endereço.
    '''
    arquivo = open(address, 'r')
    linha = arquivo.readline()
    aux = ''
    for c in linha:
        if c!= ' ':
            aux += c
        else:
            n1 = int(aux)
            aux = ''
    n2 = int(aux)
    return n1, n2

def criptografarString(string):
    e, n = lerChave('chavePublica.txt')
    cod = ''
    for x in string:
        if x!= '':
           cod += str((ord(x)**e)%n)+'?'
    return cod

def decifrarString(cod):
    d, n = lerChave('chavePrivada.txt')
    y = ''
    frase = ''
    for c in cod:
        if c!= '?':
            y += c
        else:
            frase += chr((int(y)**d)%n)
            y = ''
    return frase

def criptografarUsuarios(dicionario):
    arquivo = open('usuarios.txt', 'w')
    for nome in dicionario:
        arquivo.write(criptografarString(nome))
        arquivo.write('\n')
        arquivo.write(criptografarString(dicionario[nome][0]))
        arquivo.write('\n')
        arquivo.write(criptografarString(dicionario[nome][1]))
        arquivo.write('\n')
        arquivo.write(criptografarString(str(dicionario[nome][2])))
        arquivo.write('\n\n')
    arquivo.close()

def decifrarUsuarios(dicionario):
    arquivo = open('usuarios.txt', 'r')
    linha = arquivo.readline()
    while linha != '':
        email = decifrarString(linha)
        linha = arquivo.readline()
        nome = decifrarString(linha)
        linha = arquivo.readline()
        senha = decifrarString(linha)
        linha = arquivo.readline()
        acesso = int(decifrarString(linha))
        linha = arquivo.readline()
        dicionario[email] = (nome, senha, acesso)
        linha = arquivo.readline()