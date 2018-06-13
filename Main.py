# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Projeto Programação 1
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Matheus Ribeiro Brant Nobre (mrbn)
Email: mrbn@cin.ufpe.br
Copyright(c) 2018 Matheus Ribeiro Brant Nobre
"""

"""
Funcionalidade do Script: Esse scirpt contém o código principal do programa, 
responsável pelas funcionalidades operacionais (Login e logout; Menu de 
operações; cadastro, remoção, alteração, nível de acesso, ativação e
desativação de informações). 
"""

import Criptografia
import Pedidos
import datetime
import Elementos
import Usuarios

#dicionario de usuários[e-mail] = (nome, senha, nível de acesso, atividade)

usuarios = dict()
usuarios['adm'] = ('Administrador', 'adm', 3, True)
Criptografia.decifrarUsuarios(usuarios)

#cardapio[nome] = (desc, valor, atividade, tipo)
cardapio = dict()
Criptografia.decifrarElementos(cardapio)

login = False
continua = True

while login == False and continua == True:
    opt = int(input('(1): Login\n(2): Cadastro\n(0): Sair\n\nAção: '))
    if opt == 1:
        email = input("Login (e-mail): ")
        if email in usuarios:
            senha = input("Senha: ")
            if usuarios[email][1] == senha:
                if usuarios[email][3] == True:
                    login = True
                    Usuarios.logAct(email, 'Login')
                else:
                    print("Usuário inativo. Entre em contato com o Administrador")
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
            usuarios[email] = (nome, senha, 1, True)
    elif opt == 0:
        continua = False
        Criptografia.criptografarUsuarios(usuarios)
    else:
        print("Comando inválido. Tente novamente.")

while login == True:
    print("Bem-vindo, {}\n".format(usuarios[email][0].split(' ')[0]))
    print("n1 - Montar meu cardápio")
    print("n2 - Ver meu pedido")
    print("n3 - Remover Produto do pedido")
    print("n4 - Cancelar meu pedido")
    print("n5 - Cadastrar novos produtos (2)")
    print("n6 - Atualizar ou desativar cadastro do produto (2)")
    print("n7 - Relatório de produtos")
    print("n8 - Atualizar ou desativar usuário (3)")
    print("n9 - Relatório de usuários")
    print("n10 - Confirmar Pedido")
    print("n11 - Pesquisar usuario por nome (2)")
    print("n12 - Pesquisar produto por preço")
    print("n0 - Sair")
    comando = 1
    pedido = []  
    while comando != 0:
        comando = int(input("Comando: "))
        if comando == 1:
            ativos = Pedidos.produtosAtivos(cardapio)
            contador = 1
            for produto in ativos:
                print("n{} - {}, R${}".format(contador, produto, cardapio[produto][1]))
                contador += 1
            print('n0 - Sair')
            continuar = True
            while continuar == True:
                opcao = int(input("Escolha o produto: "))
                if opcao == 0:
                    continuar = False
                elif opcao > 0 and opcao <= len(ativos):
                    quantidade = int(input("Quantos: "))
                    pedido.append((ativos[opcao-1], quantidade))
                    Usuarios.logAct(email, 'Adicionou um produto ao pedido')
                else:
                    print("Opção inválida, tente novamente")
        elif comando == 2:
            Elementos.exibirProdutos(pedido, cardapio)
            Usuarios.logAct(email, 'Visualizou seu pedido no programa')
        elif comando == 3:
            cont = 1
            for produto in pedido:
                nome = produto[0]
                qtd = produto[1]
                valor = cardapio[nome][1]
                print("n{} - {}, R${}".format(cont, nome, qtd*valor))
                cont += 1
            print("n0 - Sair")
            opcao = int(input("Selecione o produto: "))
            continuar = True
            while continuar == True:
                if opcao == 0:
                    continuar = False
                elif opcao >0 and opcao <= len(pedido):
                    aux = pedido.pop(opcao-1)
                    continuar = False
                    Usuarios.logAct(email, 'Removeu seu pedido')
                else:
                    print("Produto inváildo, tente novamente.")
                    continuar = False
        elif comando == 4:
            pedido = []
            print("Seu pedido foi cancelado.")
            Usuarios.logAct(email, 'Cancelou o pedido')
        elif comando == 5:
            if usuarios[email][2] < 2:
                print("Nível de acesso insuficiente, entre em contato com o Administrador.")
                continue
            nome =  input ("Informe o nome do produto: ")
            desc = input ("Informe a descrição do produto: ")
            valor = float(input ("Informe o valor do produto: "))
            print("n0 - Petiscos, n1 - Entradas, n2 - Prato Principal, n3 - Sobremesas")
            tipo = int(input("Informe o tipo do Prato: n"))
            cardapio[nome] = (desc, valor, True, tipo)
            print("Produto cadastrado com sucesso!")
            Usuarios.logAct(email, 'Cadastrou um novo produto')
        elif comando == 6:
            if usuarios[email][2] < 2:
                print("Nível de acesso insuficiente, entre em contato com o Administrador.")
                continue
            print("n1 - Ativar produto")
            print("n2 - Desativar produto")
            print("n3 - Alterar Descrição")
            print("n4 - Alterar Valor")
            print("n0 - Sair")
            opcao = int(input("Ação: "))
            if opcao == 1:
                inativos = Pedidos.produtosInativos(cardapio)
                cont = 1
                for nome in cardapio:
                    print("n{} - {}".format(cont, nome))
                    cont += 1
                print('n0 - sair')
                produto = int(input("Escolha o produto: "))
                if produto == 0:
                    continue
                elif produto >0 and produto <=len(inativos):
                    nome = inativos[produto - 1]
                    cardapio[nome] = (cardapio[nome][0], cardapio[nome][1], True, cardapio[nome][3])
                    Usuarios.logAct(email, 'Ativou um produto')
                else:
                    print("Prodtuo inválido, tente novamente.")
            elif opcao == 2:
                ativos = Pedidos.produtosAtivos(cardapio)
                cont = 1
                for nome in cardapio:
                    print("n{} - {}".format(cont, nome))
                    cont += 1
                print('n0 - sair')
                produto = int(input("Escolha o produto: "))
                if produto == 0:
                    continue
                elif produto >0 and produto <=len(ativos):
                    nome = ativos[produto - 1]
                    cardapio[nome] = (cardapio[nome][0], cardapio[nome][1], False, cardapio[nome][3])
                    Usuarios.logAct(email, 'Desativou um produto')
            elif opcao == 3:
                nome = input("Informe o produto: ")
                if not nome in cardapio:
                    print("Produto inválido, tente novamente.")
                else:
                    novaDescricao = input("Informe a nova descrição: ")
                    cardapio[nome] = (novaDescricao, cardapio[nome][1], cardapio[nome][2], cardapio[nome][3])
                    Usuarios.logAct(email, 'Atualizou a descrição do produto')
            elif opcao == 4:
                nome = input("Informe o produto: ")
                if not nome in cardapio:
                    print("Produto inválido, tente novamente.")
                else:
                    novoValor = input("Informe o novo valor: ")
                    cardapio[nome] = (cardapio[nome][0], novoValor, cardapio[nome][2], cardapio[nome][3])
                    Usuarios.logAct(email, 'Atualizou o valor do produto')
            elif opcao == 0:
                continue
        elif comando == 7:
            ativos = Pedidos.produtosAtivos(cardapio)
            ativos.sort()
            arquivo = open('Relatório - Produtos Ativos.txt', 'w')
            for nome in ativos:
                 arquivo.write('Produto: '+nome+' '+'R$'+str(valor)+'\n')
            arquivo.close()
            inativos = Pedidos.produtosInativos(cardapio)
            inativos.sort()
            arquivo = open('Relatório - Produtos Inativos.txt', 'w')
            for nome in inativos:
                arquivo.write('Produto: '+nome+' '+'R$'+str(valor)+'\n')
            arquivo.close()
            Usuarios.logAct(email, 'Imprimiu Relatórios de Produtos Ativos e Inativos')
        elif comando == 8:
            if usuarios[email][2] < 3:
                print("Nível de acesso insuficiente, entre em contato com o Administrador.")
                continue
            print("n1 - Ativar usuário")
            print("n2 - Desativar usuário")
            print("n3 - Alterar Nome")
            print("n4 - Alterar Senha")
            print("n5 - Alterar Nível de Acesso")
            print("n0 - Sair")
            opcao = int(input("Ação: "))
            if opcao == 1:
                inativos = Usuarios.usariosInativos(usuarios)
                cont = 1
                for nome in usuarios:
                    print("n{} - {}".format(cont, nome))
                    cont += 1
                print('n0 - sair')
                nome = int(input("Escolha o usuário: "))
                if nome == 0:
                    continue
                elif nome >0 and nome <= len(inativos):
                    usuarioInativo = inativos[nome - 1]
                    usuarios[usuarioInativo] = (usuarios[usuarioInativo][0], usuarios[usuarioInativo][1], usuarios[usuarioInativo][2], True)
                    Usuarios.logAct(email, 'Ativou um usuário')
                else:
                    print("Usuário inválido, tente novamente.")
            elif opcao == 2:
                ativos = Usuarios.usuariosAtivos(usuarios)
                cont = 1
                for nome in usuarios:
                    print("n{} - {}".format(cont, nome))
                    cont += 1
                print('n0 - sair')
                nome = int(input("Escolha o usuário: "))
                if nome == 0:
                    continue
                elif nome >0 and nome <= len(ativos):
                    usuarioAtivo = ativos[nome - 1]
                    usuarios[usuarioAtivo] = (usuarios[usuarioAtivo][0], usuarios[usuarioAtivo][1], usuarios[usuarioAtivo][2], False)
                    Usuarios.logAct(email, 'Desativou um usuário')
            elif opcao == 3:
                usr = input("Informe o e-mail do usuário: ")
                if not usr in usuarios:
                    print("Usuário inválido, tente novamente.")
                else:
                    novoNome = input("Informe o novo nome: ")
                    usuarios[usr] = (novoNome, usuarios[usr][1], usuarios[usr][2], usuarios[usr][3])
                    Usuarios.logAct(email, 'Atualizou o nome de um usuário')
            elif opcao == 4:
                usr = input("Informe o e-mail do usuário: ")
                if not usr in usuarios:
                    print("Usuário inválido, tente novamente.")
                else:
                    novaSenha = input("Informe a nova senha: ")
                    usuarios[usr] = (usuarios[usr][0], novaSenha, usuarios[usr][2], usuarios[usr][3])
                    Usuarios.logAct(email, 'Atualizou a senha de um usuário')
            elif opcao == 5:
                usr = input("Informe o e-mail do usuário: ")
                if not usr in usuarios:
                    print("Usuário inválido, tente novamente.")
                else:
                    novoNivelAcesso = input("Informe o novo nível de acesso: ")
                    usuarios[usr] = (usuarios[usr][0], usuarios[usr][1], novoNivelAcesso, usuarios[usr][3])
                    Usuarios.logAct(email, 'Atualizou o nível de acesso de um usuário')
            elif opcao == 0:
                continue
        elif comando == 9:
            ativos = Usuarios.usuariosAtivos(usuarios)
            ativos.sort()
            arquivo = open('Relatório - Usuários Ativos.txt', 'w')
            for nome in ativos:
                arquivo.write('Usuário: '+nome+' '+'Nível de Acesso: '+str(usuarios[nome][2])+'\n')
            arquivo.close()
            inativos = Usuarios.usuariosInativos(usuarios)
            inativos.sort()
            arquivo = open('Relatório - Usuários Inativos.txt', 'w')
            for nome in inativos:
                arquivo.write('Usuário: '+nome+' '+'Nível de Acesso: '+str(usuarios[nome][2])+'\n')
            arquivo.close()
            Usuarios.logAct(email, 'Imprimiu os Relatórios de Usuários Ativos e Inativos')
        elif comando == 10:
            if len(pedido) == 0:
                print("Quantidade de produtos insuficiente.")
                continue
            data = input("Digite o Prazo de Entrega [dd-mm-aaaa]: ")
            hora = input("Digite a hora da Entrega [hh]h[mm]m: ")
            agora = datetime.datetime.now()
            if agora.day == int(data[:2]) and agora.month == int(data[3:5]):
                if int(hora[:2]) < (agora.hour + 6):
                    print("Prazo muito curto!")
                    continue
            relatorio = '{}_{}_{}.txt'.format(email, data, hora)
            arquivo = open(relatorio, 'w')
            arquivo.write("Nome do cliente: {}\n".format(usuarios[email][0]))
            arquivo.write("{} {}\n".format(data, hora))
            total = 0
            for produto in pedido:
                nome = produto[0]
                qtd = produto[1]
                valor = cardapio[nome][1]
                arquivo.write("{} x {} = R$ {}\n".format(qtd, nome, valor*qtd))
                total += qtd*valor
            arquivo.write("\nTotal: R$ {}".format(total))
            arquivo.close()
            print("Pedido confimado com sucesso!")
            print("Salvo no arquivo {}".format(relatorio))
            Usuarios.logAct(email, 'Confirmou o pedido')
        elif comando == 11:
            if usuarios[email][2] < 2:
                print("Nível de acesso insuficiente, entre em contato com o Administrador.")
                continue
            pesquisa = input("Informe o nome do usuário desejado: ")
            buscaUsuario = Usuarios.buscaUsuario(usuarios, pesquisa)
            if len(buscaUsuario) == 0:
                print("Nenhum usuário encontrado, tente novamente.")
            else:
                print("Usuários encontrados:\n")
                for nome in buscaUsuario:
                    print(nome)
                    Usuarios.logAct(email, 'Pesquisou usuários por nome')
        elif comando == 12:
            precoMaximo = float(input("Informe o valor máximo do produto desejado: "))
            buscaProduto = Elementos.buscaProdutos(cardapio, precoMaximo)
            while len(buscaProduto) == 0:
                print("Nenhum produto encontrado, tente novamente.")
                precoMaximo = float(input("Informe o valor máximo do produto desejado: "))
                buscaProduto = Elementos.buscaProdutos(cardapio, precoMaximo)
            print("Produtos Disponíveis:\n", buscaProduto)
            Usuarios.logAct(email, 'Pesquisou produtos pelo preço máximo')
        elif comando == 0:
            Criptografia.criptografarUsuarios(usuarios)
            Criptografia.criptografarElementos(cardapio)
            login = False 
        else:
            print("Erro! Tente novamente.")
        