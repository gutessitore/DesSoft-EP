# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:16:22 2018

@author: gugat
"""

#import json
import unicodedata
import re

from firebase import firebase

firebase = firebase.FirebaseApplication('https://estoques-e-quantidades.firebaseio.com/estoques-e-quantidades', None)
result = firebase.get('https://estoques-e-quantidades.firebaseio.com/estoques-e-quantidades', None)


Lojas = result

#le o arquivo



#with open ('estoques_e_quantidades.txt','r') as arquivo:
#    conteudo = arquivo.read()
#    Lojas = json.loads(conteudo)


def pudim(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    Palavra = palavraSemAcento.lower()
    Word = Palavra.strip()
    
    
    
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', Word)
z = True
while z:
    
    print('Controle de loja')
    print('_' * 20)
    print('0 - Sair')
    print('1 - Cadastrar Loja')
    print('2 - Remover Loja')
    print('3 - Alterar Loja')
    print('4 - Imprimir Lojas') 
    print('_' * 20)
    escolha = (input('Faça sua escolha: '))
    
#Opção 0: Cadastrar Loja
    if escolha == '0':        
                
        print('Até mais!')
        z = False
                
    elif escolha == '1':
        y = True
        while y:
            loja = input('Nome da loja: ')
            Loja = pudim(loja)
            
            if Loja == 'menu':
                y = False
                    
            elif Loja not in Lojas:
                Lojas[loja] = {}   
                y = False
            else:
                print('Loja já cadastrado!')  
                y = False
                
        firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Lojas)
        #with open('estoques_e_quantidades.txt', 'w') as arquivo:
        #                    conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
        #                    arquivo.write(conteudo)
                
    elif escolha == '2':
        loja = input('Nome da loja: ')
        Loja = pudim(loja)
        
        if Loja in Lojas:
            del(Lojas[loja])
            
            firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Lojas)
            #with open('estoques_e_quantidades.txt', 'w') as arquivo:
            #                conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
            #                arquivo.write(conteudo)
            
    elif escolha == '4':
        for i in Lojas:
            print('-', i)
            y = False
    
            
    elif escolha == '3':
            loja = input('Nome da loja: ')
            Loja = pudim(loja)
            if Loja in Lojas:
                a = True
                
                while a:
                   
                        
                    print('Controle de Estoque')
                    print('_' * 20)
                    print('0 - voltar para as lojas')
                    print('1 - Cadastrar Item')
                    print('2 - Remover Item')
                    print('3 - Alterar Item')
                    print('4 - Imprimir Estoque')
                    print('_' * 20)
                    print('escreva "menu" para voltar a qualquer momento')
                    
                    Escolha = (input('Faça sua escolha: '))
                    
                
                    
                #Opção 0: Sair
                    if Escolha == '0':
                        print('=-' * 10)
                        a = False

                        
                        #with open('estoques_e_quantidades.txt', 'w') as arquivo:
                        #    conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
                        #    arquivo.write(conteudo)
                        
                        firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Lojas)
                    
                #Opção 1: Adicionar Item
                    elif Escolha == '1':
                        b = True
                        while b:
                            produto = input('Nome do Produto: ')
                            Produto = pudim(produto)
                            if Produto == 'menu':
                                b = False
                            else:
                                c = True
                                while c:
                                    if Produto not in Lojas[loja]:
                                        Valor_Unitário = (input('Valor do Item: '))
                                        Quantidade_Inicial = (input('Quantidade Inicial: '))
                                        
                                        if Quantidade_Inicial == '' or Valor_Unitário == '':
                                            print('Comando Inválido')
                                        
                                            
                                        elif float(Quantidade_Inicial) < 0 or float(Valor_Unitário) < 0:
                                            print('A Quantidade Inicial ou Valor do Item não pode ser negativa.')
                                            
                                        else:
                                            Lojas[loja][Produto] = {'Quantidade': float(Quantidade_Inicial), 'Valor': float(Valor_Unitário)}
                                            print('O produto {0} foi cadastrado no valor de R${1}'.format(Produto, Lojas[loja][Produto]['Valor']))
                                            b = False
                                            c = False
                                        
                                    else:
                                        print('Produto já Cadastrado')
                                        c = False
                                        
                        #with open('estoques_e_quantidades.txt', 'w') as arquivo:
                        #    conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
                        #    arquivo.write(conteudo)
                        
                        firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Loja)
                                    
                #Opção 2: Remover Item
                    elif Escolha == '2':
                        c = True
                        while c:
                            produto = input('Nome do Produto: ')
                            Produto = pudim(produto)
                            if Produto == 'menu':
                                c = False
                            else:
                            
                                if Produto in Lojas[loja]:
                                    del Lojas[loja][Produto]
                                    print('O produto {0} foi removido com sucesso'.format(Produto))
                                    c = False
                                else:
                                    print('Elemento não encontrado')
                        #with open('estoques_e_quantidades.txt', 'w') as arquivo:
                        #    conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
                        #    arquivo.write(conteudo)
                    
                        firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Loja)
                 
                #Opção 3: Alterar Item           
                    elif Escolha == '3':
                        d = True
                        while d:
                            produto = input('Nome do Produto: ')
                            Produto = pudim(produto)
                            if Produto == 'menu':
                                d = False
                            else:
                                if Produto in Lojas[loja]:
                                    Q_V = (input('Você gostaria de alterar a 1- Quantidade ou 2- Valor? '))
                                    
                                    if Q_V == '':
                                        print('Comando Inválido')
                                    
                                    elif Q_V == '1':
                                        print('Você possui {0} unidade(s) desse produto'.format(Lojas[loja][Produto]['Quantidade']))
                                        um_dois = (input('Você gostaria de 1 - Adicionar ou 2 - remover? '))
                                        
                                        if um_dois == '':
                                            print('Comando Inválido')
                                        
                                        elif um_dois == '1':
                                            adicionar = (input('Quanto gostaria de adicionar? '))
                                            if adicionar == '':
                                                print('Comando Inválido')
                                            
                                            else:
                                                Lojas[loja][Produto]['Quantidade'] = Lojas[loja][Produto]['Quantidade'] + float(adicionar)
                                                print('Foram adicionadas {0} unidade(s) do produto {1}'.format(adicionar, Produto))
                                                print('A Quantidade Final é de {0}'.format(Lojas[loja][Produto]['Quantidade']))
                                                d = False
                                            
                                        elif um_dois == '2':
                                            remover = (input('Quanto gostaria de remover? '))
                                            if remover == '':
                                                print('Comando Inválido')
                                            else:
                                                Lojas[loja][Produto]['Quantidade'] = Lojas[loja][Produto]['Quantidade'] - float(remover)
                                                print('Foram removidas {0} unidade(s) do produto {1}'.format(adicionar, Produto))
                                                print('A Quantidade Final é de {0}'.format(Lojas[loja][Produto]['Quantidade']))
                                                d = False
                                        else:
                                            print('Escolha invalida, escolha novamente')
                                            
                                    if Q_V == '2':
                                            print('Este pruduto tem um valor unitário de R${0}'.format(Lojas[loja][Produto]['Valor']))
                                            um_dois = (input('Você gostaria de 1 - Aumentar ou 2 - Diminuir o valor? '))
                                            
                                            if um_dois == '':
                                                print('Comando Inválido')
                                            
                                            elif um_dois == '1':
                                                adicionar = (input('Quanto gostaria de aumentar? '))
                                                if adicionar == '':
                                                    print('Comando Inválido')
                                                else:
                                                    Lojas[loja][Produto]['Valor'] = Lojas[loja][Produto]['Valor'] + float(adicionar)
                                                    print('Foi aumentado R${0} no valor do produto {1}'.format(adicionar, Produto))
                                                    print('O Valor Final é de R${0}'.format(Lojas[loja][Produto]['Valor']))
                                                    d = False
                                                
                                            elif um_dois == '2':
                                                e = True
                                                while e:
                                                    remover = (input('Quanto gostaria de diminuir? '))
                                                    if remover == '':
                                                        print('Comando Inválido')
                                                    else:
                                                        if float(remover) > Lojas[loja][Produto]['Valor']:
                                                            print('O valor diminuido não pode ser maior que o valor atual')
                                                        else:
                                                            Lojas[loja][Produto]['Valor'] = Lojas[loja][Produto]['Valor'] - float(remover)
                                                            print('Foi diminudo R${0} no valor do produto {1}'.format(remover, Produto))
                                                            print('O Valor Final é de R${0}'.format(Lojas[loja][Produto]['Valor']))
                                                            d = False
                                                            e = False
                                            else:
                                                print('Escolha inválida, escolha novamente')
                                else:
                                    print('Elemento não encontrado')
                                    
                        #with open('estoques_e_quantidades.txt', 'w') as arquivo:
                        #    conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
                        #    arquivo.write(conteudo)
                            
                        firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Loja)
                                
                                
                #Opção 4: Imprimir Estoque
                
                    elif Escolha == '4':
                        f = True
                        while f:
                            for i in Lojas[loja]:
                                print(i,'-', 'Quantidade', Lojas[loja][i]['Quantidade'],'-', 'Valor padrão', 'R${0}'.format(Lojas[loja][i]['Valor']))
                            escolha = (input('Você gostaria de 1- ver os produtos em estoque negativo, 2- ver o valor total do estoque ou 3- voltar? '))
                            
                            if escolha == '1':
                                negativos = []
                                for i in Lojas[loja]:
                                    if Lojas[loja][i]['Quantidade'] < 0:
                                        negativos.append(i)
                                print(negativos)
                                
                                
                            elif escolha == '2':
                                soma = 0
                                total = 0
                                for i in Lojas[loja]:
                                    soma = Lojas[loja][i]['Quantidade'] * Lojas[loja][i]['Valor']
                                    total += soma
                                print('R${0}'.format(total))
                                
                                
                            f = False       
                
                        #with open('estoques_e_quantidades.txt', 'w') as arquivo:
                        #    conteudo = json.dumps(Lojas, sort_keys=True, indent=4)
                        #    arquivo.write(conteudo)
                            
                        firebase.put('https://estoques-e-quantidades.firebaseio.com/', 'estoques-e-quantidades', Loja)                
                    else:
                        print('Escolha inválida, escolha novamente')
                
