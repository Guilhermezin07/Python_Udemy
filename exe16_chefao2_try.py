# um programa que usuario digite um numero inteiro, informe se ele 
# e par ou impar, se o usuario nao digitar nada diga que nao e um 
# numero inteiro

numero = input('digite um numero inteiro  ')

try:
    numero_int = float(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
          par_impar_texto = 'par'
    print(f'o numero {numero_int} e {par_impar_texto}')

except:
    print('voce nao digitou numero inteiro')



