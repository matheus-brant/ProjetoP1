# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:48:40 2018

@author: mrbn
"""

import Criptografia

#dicionario de usuários[e-mail] = (nome, senha, nível de acesso)

usuarios = dict()
usuarios['adm'] = ('Administrador', 'adm', 3)
Criptografia.decifrarUsuarios(usuarios)

##dicionário de pedidos[cliente] = (prazo, (produto, quantidade), (produto, quantidade))
elementos = dict()
login = False
continua = True
while login == False and continua == True:
    opt = int(input('(1): Login\n(2): Cadastro\n(0): Sair\n\nAção: '))
    if opt == 1:
        email = input("Login (e-mail): ")
        if email in usuarios:
            senha = input("Senha: ")
            if usuarios[email][1] == senha:
                login = True
            else:
                print("Senha inválida!")
        else:
            print("E-mail não cadastrado!")
    elif opt == 2:
        email = input("Digite seu e-mail: ")
        if email in usuarios:
            print("E-mail já cadastrado.")
        else:
            nome = input("Digite seu nome completo: ")
            senha = input("Digite sua senha: ")
            confirmacao = input("Confirme sua senha: ")
            while confirmacao != senha:
                print("Senha inválida, digite novamente.")
                senha = input("Digite sua senha: ")
                confirmacao = input("Confirme sua senha: ")
            usuarios[email] = (nome, senha, 1)
    elif opt == 0:
        continua = False
    else:
        print("Comando inválido. Tente novamente.")

while login == True:
    print("Bem-vindo, {}".format(usuarios[email][0].split(' ')[0]))
    break
Criptografia.criptografarUsuarios(usuarios)