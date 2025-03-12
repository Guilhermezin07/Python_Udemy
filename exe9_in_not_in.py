nome = input("digite seu nome: ")
encontrar = input("o que voce deseja encontrar em nome? ")

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')    