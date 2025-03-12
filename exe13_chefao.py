# digite seu nome:
nome = input("digite seu nome: ") or ' '
idade = input("digite sua idade: ") or ''

if nome and idade:
    print(f'seu nome e {nome}')
    print(f'seu nome invertido e', nome[::-1])
    
    if ' ' in nome:
        print(f'nome {nome} tem espaco')
    else:
        print(f'nome {nome} nao tem espaco')

    print("seu nome tem", len(nome), "letras")
    print('a primeira letra do seu nome e', nome[0])
    print('a ultima letra do seu nome e', nome[-1])
else:
    print('voce deixou os campo vazio')
