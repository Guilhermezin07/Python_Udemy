# While (enquanto) -> executa algo quando condicao for verdadeira
# loop infinito = codigo sem fim
'''
condicao = True
while condicao:
    nome = input('qual seu nome ')
    print(f'seu nome e {nome}')
    
    if nome == 'sair':
        break
    
print('acabou o programa')

'''
contador = 0 
while contador <= 100:
    contador += 1 # ponto chave

    if contador == 6:
        print('continue')
        continue

    if contador >= 10 and contador <= 27:
        print('nao vou mostrar o', contador)
        continue    


    print(contador)

    if contador == 60:
     break
  
  

print('contagem acabou')