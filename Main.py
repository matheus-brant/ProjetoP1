# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:48:40 2018

@author: mrbn
"""

import Criptografia
import Pedidos
import datetime
import Elementos
#dicionario de usuários[e-mail] = (nome, senha, nível de acesso)

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
    print("n11 - Pesquisar usuario por nome")
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
                else:
                    print("Opção inválida, tente novamente")
        elif comando == 2:
            Elementos.exibirProdutos(pedido, cardapio)       
        elif comando == 3:
            cont = 1
            for produto in pedido:
                nome = produto[0]
                qtd = produto[1]
                valor = cardapio[nome][1]
                print("n{} - {}, R${}".format(cont, nome, qtd*valor))
                cont += 1
            print("n0 - Sair")
            opcao = int(input("Selecione o produto"))
            continuar = True
            while continuar == True:
                if opcao == 0:
                    continuar = False
                elif opcao >0 and opcao <= len(pedido):
                    aux = pedido.pop(opcao-1)
                else:
                    print("Produto inváildo, tente novamente.")
        elif comando == 4:
            pedido = []
            print("Seu pedido foi cancelado.")
        elif comando == 5:
            if usuarios[email][2] < 2:
                continue
            nome =  input ("Informe o nome do produto: ")
            desc = input ("Informe a descrição do produto: ")
            valor = float(input ("Informe o valor do produto: "))
            print("n0 - Petiscos, n1 - Entradas, n2 - Prato Principal, n3 - Sobremesas")
            tipo = int(input("Informe o tipo do Prato: n"))
            cardapio[nome] = (desc, valor, True, tipo)
            print("Produto cadastrado com sucesso!")
        elif comando == 6:
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
                elif produto >0 and produto >len(inativos):
                    nome = inativos[produto - 1]
                    cardapio[nome] = (cardapio[nome][0], cardapio[nome][1], True, cardapio[nome][3])
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
                elif produto >0 and produto >len(ativos):
                    nome = ativos[produto - 1]
                    cardapio[nome] = (cardapio[nome][0], cardapio[nome][1], False, cardapio[nome][3])
            elif opcao == 3:
                nome = input("Informe o produto: ")
                if not nome in cardapio:
                    print("Produto inválido, tente novamente.")
                else:
                    novaDescricao = input("Informe a nova descrição: ")
                    cardapio[nome] = (novaDescricao, cardapio[nome][1], cardapio[nome][2], cardapio[nome][3])
            elif opcao == 4:
                nome = input("Informe o produto: ")
                if not nome in cardapio:
                    print("Produto inválido, tente novamente.")
                else:
                    novoValor = input("Informe o novo valor: ")
                    cardapio[nome] = (cardapio[nome][0], novoValor, cardapio[nome][2], cardapio[nome][3])
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
        elif comando == 8:
            pass
        elif comando == 9:
            pass
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
        elif comando == 0:
            Criptografia.criptografarUsuarios(usuarios)
            Criptografia.criptografarElementos(cardapio)
            login = False 
        else:
            print("Erro! Tente novamente.")
        