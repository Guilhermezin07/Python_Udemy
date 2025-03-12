# Criar uma calculadora utilizando while # 
# Pedir o primeiro numero ao usuairio, segundo numero e depois 
# pedir o operador matematico e efetuar o calculo

while True:
    num1 = input('digite o primeiro numero: ')
    num2 = input('digite o segundo numero: ')
    num3 = input('digite o operador que deseja usar: (+ * - /) ' )

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('um ou outros numeros digitados sao invalidos')
        continue

    operadores_permitidos = "+-/*"

    if num3 not in operadores_permitidos:
        print('operador invalido')
        continue

    if len(num3) > 1:
        print('digite apenas um operador')
        continue

    if num3 == '+':
        soma = num1_float + num2_float
        print(soma)
    
    elif num3 == '-':
        menos = num1_float - num2_float
        print(menos)
    
    elif num3 == '*':
        mult = num1_float * num2_float
        print(mult)
    
    elif num3 == '/':
        divis = num1_float / num2_float
        print(divis)

    else:
        print('nao deveria chegar aqui')


    sair = input('quer sair ? digite s para sair , senao continue:').lower().startswith('s')

    if sair is True:
        break

# .lower() -> deixa todas as letras em minusculas
# .startswith('d') -> serve para verificar com qual letra comeca
# .endswith('a') -> verifica com qual letra termina