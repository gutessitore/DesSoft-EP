# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:18:58 2018

@author: gugat
"""

# teste

#input
print('Controle de estoque')
print('0 - sair')
print('1 - adicionar item')
print('2 - remover item')
print('3 - alterar item')
print('4 - imprimir estoque')
escolha = int(input('Faça sua escolha: '))

#estoque

estoque = ['b']
quantidades = []

#opcao 0
if escolha == 0:
    print('Até mais')
    
#opcao 1

elif escolha == 1:

# adiciona o produto e verifica se ele ja esta contido na lista
    c = True
    while c == True:
        nome_do_produto = input('Nome do produto: ')
        for e in estoque:
            if nome_do_produto != e:
                estoque.append(nome_do_produto)
            elif e == nome_do_produto:
                print('Produto já cadastrado!')
                
    
#se a quantidade for negativa ela nao e salva e printa 'quantidade inicial 
#nao pode ser negativa'
    a = True
    while a == True:
        quantidade = int(input('Quantidade inicial: '))
        if quantidade < 0:
            print('A quantidade inicial não pode ser negativa.')
        elif quantidade > 0:
            quantidades.append(quantidade)
            a = False
            
#opcao 2
elif escolha == 2:
    nome_do_produto == input('Nome do produto: ')
    
    for e in range(len(estoque)):
        if estoque[e] == nome_do_produto:
            estoque.remove(e)
            
#opcao 3
            
elif escolha == 3:
        d = True
        while d:
            produto = input('Nome do Produto: ')
            Produto = produto.lower()
            if Produto in estoque:
                input('voce gostaria de alterar a q')
                print('Voce possui {0} unidade(s) desse produto'.format(estoque[Produto]['Quantidade']))
                um_dois = int(input('Voce gostaria de 1 - Adicionar ou 2 - remover? '))
                
                if um_dois == 1:
                    adicionar = int(input('Quanto gostaria de adicionar? '))
                    estoque[Produto]['Quantidade'] = estoque[Produto]['Quantidade'] + adicionar
                    d = False
                elif um_dois == 2:
                    remover = int(input('Quanto gostaria de remover? '))
                    estoque[Produto]['Quantidade'] = estoque[Produto]['Quantidade'] - remover
                    d = False
                else:
                    print('Escolha invalida, escolha novamente')
                    
#opcao 4
elif escolha == 4:
        for i in estoque:
            print(i)