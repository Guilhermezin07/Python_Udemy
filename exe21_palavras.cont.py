#objetivo =  descobrir qual letra apareceu mais vezes

frase = ' python e uma linguagem de programacao multiparadigma foi criado por Guido van Rossum'

i = 0 
qtd_pareceu_mais = 0 
letra_apareceu_mais = ' '
palavras_letra = []

palavras = frase.split()

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    palavras_atual = []
    for palavra in palavras:
        if letra_atual in palavra:
            palavras_atual.append(palavra)   

    qts_vezes_letra_atual =  frase.count(letra_atual)

    if qtd_pareceu_mais < qts_vezes_letra_atual:
        qtd_pareceu_mais = qts_vezes_letra_atual
        letra_apareceu_mais = letra_atual
        palavras_letra = palavras_atual

    i += 1    

    
print(
    'a letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais}" que apareceu '
    f'{qtd_pareceu_mais}x nas palavras {palavras_letra}'
)
