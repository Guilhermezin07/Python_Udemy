import os

lista = []

while True:
    print(
        '\n1. Digite [I] para inserir itens na lista'
        '\n2. Digite [A] para apagar um item da lista'
        '\n3. Digite [M] para mostrar a lista completa'
        '\n4. Digite [S] para sair'
    )

    opcoes = input('\nSelecione uma das opções acima: ').strip().lower()

    if opcoes == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')  # Funciona no Windows/Linux
        item = input('Adicionar item: ').strip()
        if item:
            lista.append(item)
            print('\n✅ Seu item foi adicionado com sucesso à lista.')
        else:
            print('\n⚠️ O item não pode estar vazio!')

    elif opcoes == 'm':
        os.system('cls' if os.name == 'nt' else 'clear')
        if not lista:
            print('\n📌 A lista está vazia.')
        else:
            print('🛒 Itens na lista:')
            for indice, item in enumerate(lista):
                print(f'[{indice}] {item}')

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

    elif opcoes == 's':
        print('\n👋 Saindo do programa. Até logo!')
        break  # Sai do loop e finaliza o programa

    else:
        print('\n⚠️ Opção inválida. Tente novamente.\n')
