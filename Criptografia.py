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
        arquivo.write('\n')
        arquivo.write(criptografarString(str(int(dicionario[nome][3]))))
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
        sit = bool(int(decifrarString(linha)))
        linha = arquivo.readline()
        dicionario[email] = (nome, senha, acesso, sit)
        linha = arquivo.readline()
        
def criptografarElementos(cardapio):
    arquivo = open('elementos.txt', 'w')
    for nome in cardapio:
        arquivo.write(criptografarString(nome))
        arquivo.write('\n')
        arquivo.write(criptografarString(cardapio[nome][0]))
        arquivo.write('\n')
        arquivo.write(criptografarString(str(cardapio[nome][1])))
        arquivo.write('\n')
        arquivo.write(criptografarString(str(int(cardapio[nome][2]))))
        arquivo.write('\n')
        arquivo.write(criptografarString(str(cardapio[nome][3])))
        arquivo.write('\n\n')
    arquivo.close()
    
def decifrarElementos(cardapio):
    arquivo = open('elementos.txt', 'r')
    linha = arquivo.readline()
    while linha != '':
        nome = decifrarString(linha)
        linha = arquivo.readline()
        desc = decifrarString(linha)
        linha = arquivo.readline()
        valor = float(decifrarString(linha))
        linha = arquivo.readline()
        sit = bool(int(decifrarString(linha)))
        linha = arquivo.readline()
        tip = int(decifrarString(linha))
        cardapio[nome] = (desc, valor, sit, tip)
        linha = arquivo.readline()
        linha = arquivo.readline()

