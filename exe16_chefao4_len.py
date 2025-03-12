primero_nome = input('digite o seu nome ')
nome = len(primero_nome)

if nome > 1:
    if nome <= 4:
        print(' seu nome e curto')    
    elif nome >= 5 and nome <= 6 :
        print('seu nome e medio')
    if nome > 6 :
        print('seu nome e grande')

else:
   print("digite pelo menos uma letra")