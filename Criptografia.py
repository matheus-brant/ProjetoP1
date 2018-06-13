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
Funcionalidade do Script: Esse scirpt contém as funções de criptografia e
descriptografia das informações dos usuários e elementos. 
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
    '''
    Percorre o arquivo passado como parâmetro na função lerChave, incrementando
    os caracteres diferentes de espaço nas variáveis indicadas com a fórmula de
    criptografia solicitada no detalhamento do projeto.
    '''
    e, n = lerChave('chavePublica.txt')
    cod = ''
    for x in string:
        if x!= '':
           cod += str((ord(x)**e)%n)+'?'
    return cod

def decifrarString(cod):
    '''
    Percorre o arquivo passado como parâmetro na função lerChave, incrementando
    os caracteres diferentes de '?' nas variáveis indicadas com a fórmula de
    descriptografia solicitada no detalhamento do projeto.
    '''
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
    '''
    Abre o arquivo txt no modo escrita e escreve cada elemento da tupla
    correspondente aos dados dos usuários (no dicionário usuários definido no 
    script principal) e usa a função de criptografarString para criptografar
    cada elemento de acordo com seu índice.
    '''
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
    '''
    Abre o arquivo txt no modo leitura e lê cada linha do arquivo, usando a
    função decifrar string em cada elemento definido.
    '''
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
    '''
    Abre o arquivo txt no modo escrita e escreve cada elemento da tupla
    correspondente aos dados dos elementos (no dicionário cardapio definido no 
    script principal) e usa a função de criptografarString para criptografar
    cada elemento de acordo com seu índice.
    '''
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
    '''
    Abre o arquivo txt no modo leitura e lê cada linha do arquivo, usando a
    função decifrar string em cada elemento definido.
    '''
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

