"""
texto = 'python'

i = 0
string_tamanho = len(texto)

while i < string_tamanho:
    print(texto[i], i)

    i += 1
"""
# while e usado para iterar sobre uma string 
# while justamente serve quando nao se sabe quantas repeticoes vai ter
# Ex: algoritmo de digitar senha ate acertar 

""" texto = "python"
novo_texto = ''

for letra in texto: # -> para cada letra em variavel exiba letra
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*') 

"""

# mesmo que voce usa no while, serve para for:

for i in range(10):
    if i == 2:
        print('i e 2, pulando')
        continue
    
    if i == 8:
        print('i e 8, seu else nao executara')
        break
    
    for j in range(1, 3):
        print(i, j)
else:
    print('for completo com sucesso')