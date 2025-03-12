# iterando strings com while

nome = input('digite seu nome: ')
#strings sao iteraveis
#tamanho_nome = len(nome)

#print(nome[5])#pegar o indice de uma string

#objetivo : e antes de mostrar a string nome colocar 
# * antes e depois de cada letra '*g*u*i*'
nova = 0
novo = ''# -> string vazia
while nova < len(nome): #-> enquanto nova menor que qtd de caracteres
    letra = nome[nova] # -> variavel letra armazena o indice da string nome
    novo = novo + f'*{letra}' #-> variavel novo armazena e incrementa + 1 letra em novo 
    nova = nova + 1 # -> variavel incrementa + 1 

print(novo) # mostra na tela o resultado apos termino da condicao
