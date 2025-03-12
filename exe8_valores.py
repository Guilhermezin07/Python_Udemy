primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} e maior que o {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} e maior que o {primeiro_valor=}')    
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} e igual ao {segundo_valor=}')


