# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:29:09 2018

@author: ienzo
"""

from firebase import firebase
firebase = firebase.FirebaseApplication("https://projeto-ep1.firebaseio.com/",None)
loja = firebase.get("",None)

import json

with open ('ep1.txt', 'r') as arquivo:
    todas_lojas = json.loads(arquivo.read())

while True:
    
    print('''Controle de loja
              0 - sair
              1 - adicionar loja
              2 - remover loja
              3 - alterar loja
              4 - imprimir lojas''')    
    y = int(input('Faça sua escolha: '))
    if y == 0:
            print('Até mais!')
            break
    elif y == 1:
        loja = input('Nome da loja: ')
        loja = loja.lower()
        
        if loja not in todas_lojas:
            todas_lojas[loja] = {}            
        else:
            print('Loja já cadastrado!')    
    if y == 2:
        loja = input('Nome do loja: ')
        loja = loja.lower()
        if loja in todas_lojas:
            del(todas_lojas[loja]) 
    elif y == 3:
        loja = input('Nome da loja: ')
        loja = loja.lower()
        if loja in todas_lojas:
            while True:
                print('''Controle de estoque
              0 - sair
              1 - adicionar item
              2 - remover item
              3 - alterar item
              4 - imprimir estoque
              5 - estoque negativo
              6 - imprimir preço total''')    
                x = int(input('Faça sua escolha: '))    
                if x == 0:
                    print('Até mais!')
                    break
                elif x == 1:
                    produto = input('Nome do produto: ')
                    produto = produto.lower()
                    if produto not in todas_lojas[loja]:        
                        quantidade = int(input('Quantidade inicial: '))      
                        while quantidade < 0:
                            print('A quantidade inicial não pode ser negativa.')
                            quantidade = int(input('Quantidade inicial: '))
                        while quantidade >= 0:
                            preco = float(input('Preço inicial: '))
                            if preco not in todas_lojas[loja]:
                                while preco < 0:
                                    print('O preço inicial não pode ser negativo.')
                                    preco = float(input('Preço inicial: '))
                                if preco >= 0:
                                    todas_lojas[loja][produto] = {'quantidade': quantidade, 'preco': preco}
                                    break
                    else:
                        print('Produto já cadastrado!')    
                    todas_lojas[loja][produto] = {'quantidade': quantidade, 'preco': preco} 
                    break                  
                elif x == 2:
                    produto = input('Nome do produto: ')
                    produto = produto.lower()
                    if produto in todas_lojas[loja]:
                        del(todas_lojas[loja][produto])           
                elif x == 3:
                    produto = input('Nome do produto: ')
                    produto = produto.lower()
                    if produto in todas_lojas[loja]:
                        opcao = str(input('Alterar quantidade ou preço?(q/p) '))
                        quantidade=todas_lojas[loja][produto]['quantidade']
                        preco=todas_lojas[loja][produto]['preco']
                        if opcao == 'q':
                            adicao = int(input('Quantidade: '))
                            quantidade_nova = adicao + quantidade            
                            print('Novo estoque de {0}: {1} '.format(produto, quantidade_nova))
                            del(quantidade)
                            todas_lojas[loja][produto] = {'quantidade': quantidade_nova, 'preco': preco}
                        else:
                            adicao2 = int(input('Preço: '))
                            preco_novo = adicao2 + preco            
                            print('Novo preço de {0}: {1} '.format(produto, preco_novo))
                            del(preco)
                            todas_lojas[loja][produto] = {'quantidade': quantidade, 'preco': preco_novo}
                elif x == 4:      
                    for i in todas_lojas[loja]:
                        print('{0} : {1}'.format(i, todas_lojas[loja][i]["quantidade"]))
                elif x == 5:
                    estoque_negativo = []
                    for e in todas_lojas[loja]:
                        if todas_lojas[loja][e]['quantidade'] < 0:
                            estoque_negativo.append(e)
                    for i in estoque_negativo:
                        print('{0} : {1}'.format(i,todas_lojas[loja][i]["quantidade"]))
                elif x == 6:
                    i = 0
                    for e in todas_lojas[loja]:
                        i += todas_lojas[loja][e]['quantidade'] * todas_lojas[loja][e]['preco']
                    print(i)
                else:
                    print("Loja não encontrada!")   
    elif y == 4:
        for i in todas_lojas:
                print(i)

with open ('ep1.txt', 'w') as arquivo:
    estoque_atualizado = json.dumps(todas_lojas)
    arquivo.write(estoque_atualizado)
    
firebase.patch(loja,todas_lojas[loja])