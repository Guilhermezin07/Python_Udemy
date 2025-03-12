#Formatação de Strings
# .2.f -> para ajustar casa decimal
#funcao .format()

nome = "guilherme"
altura = 18
peso = 77
imc = peso / ( altura ** 2)

linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha2 = f'pesa {peso} kg'
linha3 = f'seu imc = {imc:,.2f}'

print(linha_1)
print(linha2)
print(linha3)

a = 'Aaaaaa'
b = 'bbbbbbb'
c = 2.3
string = '\n a = {nome1} b = {nome2} c = {nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)

#parametro nomeado e quando voce da nome dentro da funcao
# ex ->   a, nome2 = b, c