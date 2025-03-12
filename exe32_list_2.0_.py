# criar uma nova lista de compras utilizando o try e except
# reforçar esse conteudo e exercicio aprendido
# amanha / hoje 18/02 as 16 da tarde

import os

lista = []

while True:
    print(
        '\n1. Digite i para inserir itens na lista \n2. Digite a para apagar item da lista \n3. Digite m para mostrar a lista completa' 
        )
  
    opcoes = input('\nSelecione uma das opcoes acima: ')


    if opcoes == 'i':
        os.system('cls')
        item = input('Adicionar item: ')
        lista.append(item)
        print('\nSeu item foi adicionado com sucesso a lista.')

    elif opcoes == 'm':
        os.system('cls')
        print('Itens adicionados na lista: ')
        for indice_lista, item_lista in enumerate(lista):
            print(indice_lista, item_lista)
            
        while True:
            apagar = input('\nDeseja apagar algum item: ? Digite sim ou nao:  ')

            if apagar == "sim":
                try:
                    indice = input('digite o indice a ser apagado: ')
                    apagar_lista = int(indice)
                    del lista [apagar_lista]
                    print('Item foi apagado')
                    break

                except IndexError:
                    print('Voce tentou apagar um indice que nao existe. Tente de novo')
                
                
            elif apagar == "nao":
                voltar = input('\ndigite v para voltar a tela inicial: ')
                break

            else:
                print('digite apenas sim ou nao: ')

      
    elif opcoes == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        if not lista:
            print('\n📌 A lista está vazia. Nada para apagar.')
        else:
            print('🛒 Itens na lista:')
            for indice, item in enumerate(lista):
                print(f'[{indice}] {item}')

            try:
                indice_apagar = int(input('\nDigite o índice do item que deseja apagar: '))
                if 0 <= indice_apagar < len(lista):
                    item_removido = lista.pop(indice_apagar)
                    print(f'\n✅ Item "{item_removido}" foi removido da lista.')
                else:
                    print('\n⚠️ Índice inválido. Tente novamente.')

            except ValueError:
                print('\n⚠️ Digite apenas números inteiros.')

           
    
    else:
         print('\ndigite novamente, comando nao reconhecido\n')
       