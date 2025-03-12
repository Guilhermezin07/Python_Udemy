# jogo de palavras secretas 

import os

palavra_secreta = 'caderno'
letras_acertos = ''
tentativas = 0

while True:

    letra = input('digite uma letra: ')
    tentativas += 1
    
# agora vai ter que ler que usuario digitou uma letra so
    if len(letra) > 1:
        print('digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        letras_acertos += letra
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertos:
            palavra_formada += letra_secreta
        else:
            palavra_formada += ' * '
    print(palavra_formada)

    if palavra_formada ==  palavra_secreta:
        os.system('cls')
        print('PARABENS, voce acertou!')
        print('A palavra era : ', palavra_secreta)
        print('tentativas:', tentativas)
        letras_acertos = ''
        tentativas = 0