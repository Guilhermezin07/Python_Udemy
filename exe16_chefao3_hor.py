#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#escrito, exiba a saudação apropriada



#sempre que voce quiser alguma coisa relacionada com numeros 
#voce tem que converter tudo para int ou float
horario = input('digite a hora em numeros inteiros:')

try: 
    hora = float(horario)

    if hora >= 0 and hora <= 12:
        print(f'bom dia, sao {horario}  ')

    elif hora >= 13 and hora <= 18:
        print(f'boa tarde sao {horario} ')

    elif hora >= 19 and hora <= 23:
        print(f'boa noite sao {horario} ')
    
    else:
        print('esse horario nao existe')

except:
    print('digite apenas numeros inteiros')