# Desempacotamento e Empacotamento : 

nomes = ['maria', 'helena', 'joao']



nome1, oo, pp = ['maria', 'helena', 'joao'] # pegar so mente o primeiro valor
print(nome1, oo, pp)

# _ = utilizado para dizer que variavel existe mas nao sera utilizada
# * resto = uma outra lista com o restante dos valores nao usados

_, nome, _, *resto = nomes
print(nome, resto)