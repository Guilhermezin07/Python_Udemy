# fazer uma lista de compras com listas
# nao quebrar com indices inexistentes

# dados de entrada 

import os

lista = []
condicao = True
while condicao:
   
    print('selecione opcao:')
    indic = input('[i]nserir, [a]pagar ou [l]istar : ')

    if indic == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)
             

    elif indic == 'a':
        apag = input('apagar item da lista: ')
        apaga_indice = int(apag)
        del lista[apaga_indice]

 
    elif indic == 'l':
        for indice, nome in enumerate(lista):
            print(indice, nome)
            

    else:
        print('digite denovo porfavor')




#for item in enumerate(lista):
#   print('for tupla')
#   for valor in item:
#      print(f'\t{valor}')



