# método split serve dividir strings e retornar listas
frase = "  olha que legal, isso é show  "
lista_palavras = frase.split(',')

lista_corrigida = []
for i, frase in enumerate(lista_palavras):
# método strip serve para remover os espaços right, left ou ambos
    lista_corrigida.append(lista_palavras[i].strip())

print(lista_palavras)
print(lista_corrigida)

# método join para unir novamente as strings em uma frase só
frases_unidas = ", ".join(lista_corrigida)
print(frases_unidas)